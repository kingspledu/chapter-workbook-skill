"""Measure PDF text against explicitly supplied safe text rooms (points, top-left)."""
import argparse,json,sys
from pathlib import Path
import fitz

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('pdf',type=Path)
    p.add_argument('--regions',type=Path,required=True,help='JSON list: page (1-based), text (exact span), safe_rect [x0,y0,x1,y1], optional occupancy [min,max], center_tolerance')
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();specs=json.loads(a.regions.read_text(encoding='utf-8'));results=[]
    with fitz.open(a.pdf) as doc:
        for s in specs:
            page=doc[s['page']-1];safe=fitz.Rect(s['safe_rect'])
            if safe.is_empty:raise ValueError('safe_rect must have positive area')
            spans=[z for b in page.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for z in l['spans'] if z['text']==s['text']]
            record={'page':s['page'],'text':s['text'],'safe_rect':list(safe),'matches':len(spans),'passed':False}
            if len(spans)==1:
                box=fitz.Rect(spans[0]['bbox']);occupancy=box.width/safe.width
                dx=(box.x0+box.x1-safe.x0-safe.x1)/2;dy=(box.y0+box.y1-safe.y0-safe.y1)/2
                contained=safe.contains(box);ran=s.get('occupancy',[0,1]);tol=s.get('center_tolerance')
                record.update(text_rect=list(box),width_occupancy=occupancy,center_offset_points=[dx,dy],contained=contained,font=spans[0]['font'],font_size=spans[0]['size'],passed=contained and ran[0]<=occupancy<=ran[1] and (tol is None or (abs(dx)<=tol and abs(dy)<=tol)))
            results.append(record)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
    failures=sum(not x['passed'] for x in results)
    print(f'Audited {len(results)} text rooms; failures: {failures}. Report: {a.output}')
    sys.exit(bool(failures))

if __name__=='__main__':main()
