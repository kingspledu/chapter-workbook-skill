"""Check edition parity and neutral black-and-white print output; not semantic QA."""
import argparse
from collections import Counter
import json,re
from pathlib import Path
import fitz
from PIL import Image,ImageChops

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('color',type=Path)
    p.add_argument('coloring',type=Path)
    p.add_argument('--flattened',type=Path)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();records=[]
    inventory=lambda text:Counter(re.sub(r'\s','',text))
    with fitz.open(a.color) as color,fitz.open(a.coloring) as coloring:
        if len(color)!=len(coloring):raise ValueError('Edition page counts differ')
        for i,(source,page) in enumerate(zip(color,coloring),1):
            spans=[s for b in page.get_text('dict')['blocks'] if 'lines' in b for line in b['lines'] for s in line['spans']]
            pix=page.get_pixmap(matrix=fitz.Matrix(.5,.5),colorspace=fitz.csRGB,alpha=False)
            r,g,b=Image.frombytes('RGB',(pix.width,pix.height),pix.samples).split()
            chroma=max(ImageChops.difference(r,g).getextrema()[1],ImageChops.difference(g,b).getextrema()[1])
            records.append(dict(page=i,same_character_inventory=inventory(source.get_text())==inventory(page.get_text()),same_page_size=abs(source.rect.width-page.rect.width)<.1 and abs(source.rect.height-page.rect.height)<.1,black_text=bool(spans) and all(s['color']==0 for s in spans),neutral_raster=chroma==0))
    if a.flattened:
        with fitz.open(a.flattened) as flat,fitz.open(a.coloring) as vector:
            if len(flat)!=len(vector):raise ValueError('Flattened page count differs')
            for rec,page,original in zip(records,flat,vector):
                rec['flattened_image_only']=not page.get_text().strip() and bool(page.get_images()) and not list(page.widgets() or [])
                rec['flattened_same_size']=abs(page.rect.width-original.rect.width)<.1 and abs(page.rect.height-original.rect.height)<.1
    passed=all(all(v for k,v in row.items() if k!='page') for row in records)
    report=dict(passed=passed,pages=records,limits='Character inventory ignores whitespace and order. Verify wording, sentence order, answer semantics, asset provenance and visual layout against the reviewed model separately.')
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(f'Edition checks: {len(records)} pages; passed={passed}. {a.output}')
    raise SystemExit(0 if passed else 1)

if __name__=='__main__':main()
