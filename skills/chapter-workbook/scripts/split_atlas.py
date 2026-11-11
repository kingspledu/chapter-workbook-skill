"""Split a regular generated atlas at native resolution without retouching."""
from pathlib import Path
import argparse,json
from PIL import Image

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('image',type=Path)
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--columns',type=int,default=4)
    parser.add_argument('--rows',type=int,default=4)
    parser.add_argument('--inset',type=int,default=0,help='Uniform pixels removed inside each cell; inspect first')
    args=parser.parse_args()
    if args.columns<1 or args.rows<1 or args.inset<0:parser.error('Positive grid dimensions and nonnegative inset required')
    args.output.mkdir(parents=True,exist_ok=True)
    records=[]
    with Image.open(args.image) as im:
        for i in range(args.columns*args.rows):
            col,row=i%args.columns,i//args.columns
            box=(round(col*im.width/args.columns)+args.inset,round(row*im.height/args.rows)+args.inset,round((col+1)*im.width/args.columns)-args.inset,round((row+1)*im.height/args.rows)-args.inset)
            if box[2]<=box[0] or box[3]<=box[1]:parser.error('Grid/inset produces empty cells')
            target=args.output/f'element-{i+1:02d}.png'
            im.crop(box).save(target)
            records.append({'index':i+1,'row':row+1,'column':col+1,'file':target.name,'bounds':box})
    (args.output/'atlas-manifest.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
    print(f'Saved {len(records)} elements to {args.output}')

if __name__=='__main__':main()
