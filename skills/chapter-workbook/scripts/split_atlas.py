"""Split a user-requested, model-generated 4x4 asset atlas without retouching."""
from pathlib import Path
import argparse,json
from PIL import Image

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('image',type=Path)
    parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    records=[]
    with Image.open(args.image) as im:
        for i in range(16):
            col,row=i%4,i//4
            box=(round(col*im.width/4),round(row*im.height/4),round((col+1)*im.width/4),round((row+1)*im.height/4))
            target=args.output/f'element-{i+1:02d}.png'
            im.crop(box).save(target)
            records.append({'index':i+1,'row':row+1,'column':col+1,'file':target.name,'bounds':box})
    (args.output/'atlas-manifest.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
    print(f'Saved {len(records)} elements to {args.output}')

if __name__=='__main__':main()
