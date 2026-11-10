from pathlib import Path
import argparse,json,fitz
p=argparse.ArgumentParser();p.add_argument('folder',type=Path);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
a.output.mkdir(parents=True,exist_ok=True);result=[]
for f in sorted(a.folder.glob('*.pdf')):
 d=fitz.open(f);pages=[{'pdf_page':i+1,'text':page.get_text().strip()} for i,page in enumerate(d)]
 name=f.stem;scan=sum(not x['text'] for x in pages)>len(pages)*.8
 (a.output/(name+'.json')).write_text(json.dumps(pages,ensure_ascii=False,indent=2),encoding='utf-8')
 result.append({'file':f.name,'pages':len(d),'image_only':scan,'chapter_boundaries':'unverified'})
(a.output/'inventory.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
