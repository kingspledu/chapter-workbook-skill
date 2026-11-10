from pathlib import Path
import json, re, math, textwrap, zipfile, shutil, hashlib, os, argparse
from xml.sax.saxutils import escape
import fitz
from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image, ImageOps, ImageDraw
from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'output'
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'assets').mkdir(exist_ok=True)
W,H=595.276,841.89
INK='#30466B'; PINK='#ED6796'; BLUE='#69B9DD'; GOLD='#E8C653'; LIGHT='#F0F8FC'
FONTDIR=Path(os.environ.get('WORKBOOK_FONT_DIR','C:/Windows/Fonts'))
for name,file in [('Body','trebuc.ttf'),('Bold','trebucbd.ttf'),('Korean','malgun.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(FONTDIR/file)))

class Page:
    def __init__(self,title,sub,number,teacher=False):
        self.ops=[]; self.number=number
        self.rect(0,0,W,H,'#FFFFFF',None)
        self.image('sky',15,12,W-30,55)
        self.rect(23,70,W-46,43,PINK,None,12)
        self.text(title,35,80,23,'Bold','#FFFFFF')
        self.text(BRAND,26,17,10,'Bold','#FFFFFF')
        self.text(BOOK_LABEL,395,18,9,'Bold','#FFFFFF')
        self.text(sub,28,124,11,'Bold')
        if not teacher:
            self.text('Name: _______________________     Date: ______________',28,146,10)
        self.line(28,794,W-28,794,'#C6DDE8')
        self.text(BRAND+'  |  '+('Teacher edition' if teacher else 'Grade 2 reading workbook'),28,804,8)
        self.text(f'{number:02d} / 13',516,803,9,'Bold')
        for i in range(57): self.rect(i*10.5,H-9,7,9,[PINK,BLUE,GOLD,'#96D7AA'][i%4],None,0)
    def rect(self,x,y,w,h,fill=LIGHT,stroke='#BDDBEA',radius=8): self.ops.append(dict(kind='rect',x=x,y=y,w=w,h=h,fill=fill,stroke=stroke,radius=radius))
    def text(self,text,x,y,size=12,font='Body',color=INK):
        if any('\uac00'<=c<='\ud7a3' for c in text): font='Korean'
        self.ops.append(dict(kind='text',text=text,x=x,y=y,size=size,font=font,color=color))
    def line(self,x,y,x2,y2,color='#A8BBCB'): self.ops.append(dict(kind='line',x=x,y=y,x2=x2,y2=y2,color=color))
    def image(self,name,x,y,w,h):
        if name!='sky':
            with Image.open(OUT/'assets'/(name+'.png')) as im: iw,ih=im.size
            ratio=min(w/iw,h/ih); nw,nh=iw*ratio,ih*ratio
            x+=(w-nw)/2;y+=(h-nh)/2;w,h=nw,nh
        self.ops.append(dict(kind='image',name=name,x=x,y=y,w=w,h=h))
    def wrap(self,text,x,y,width,size=12,font='Body',leading=None,color=INK):
        leading=leading or size*1.48
        line=''
        for word in text.split():
            test=(line+' '+word).strip()
            if pdfmetrics.stringWidth(test,font,size)>width and line:
                self.text(line,x,y,size,font,color); y+=leading; line=word
            else: line=test
        if line: self.text(line,x,y,size,font,color); y+=leading
        return y
    def badge(self,n,x,y):
        self.rect(x,y,22,22,PINK,None,11); self.text(str(n),x+6 if n<10 else x+3,y+3,12,'Bold','#FFFFFF')
    def check(self,items,y=713):
        self.rect(28,y,539,65,'#FFFBEA','#E8D78E',12)
        self.text('Check!',41,y+8,14,'Bold',PINK)
        for i,t in enumerate(items):
            self.rect(112,y+11+i*20,10,10,'#FFFFFF',GOLD,1); self.text(t,131,y+8+i*20,10)

def compose(d):
    pages=[]
    def new(t,s,teacher=False):
        p=Page(t,s,len(pages)+1,teacher); pages.append(p); return p
    p=new('1  /  '+d['title'],'Read the story. Then find the spelling words.')
    p.rect(28,176,539,362,LIGHT)
    y=191
    # Paragraph boundaries reflect HTML rather than design-sample narrative.
    for txt in d['story_paragraphs']:
        y=p.wrap(txt,43,y,509,12,leading=17)+7
    p.text('Find It!',31,553,19,'Bold',PINK)
    p.text('Check off the words you can find in the story.',31,580,11)
    for i,w in enumerate(d['words']):
        x=36+(i%3)*179; y=611+(i//3)*34
        p.rect(x,y+3,13,13,'#FFFFFF',GOLD,2); p.text(w,x+23,y,14,'Bold')
    p=new('2  /  Spelling Practice','Read each word. Copy it twice.')
    for x,label,c in [(28,'Read and Spell','#FCE8EF'),(210,'Copy and Spell',LIGHT),(392,'Spell It Again!','#FFF7D8')]:
        p.rect(x,181,175,32,c,None); p.text(label,x+12,188,13,'Bold')
    for i,w in enumerate(d['words']):
        y=229+i*34; p.badge(i+1,30,y); p.text(w,60,y+2,14,'Bold'); p.line(222,y+23,370,y+23); p.line(403,y+23,551,y+23)
    p.check(['I copied each word carefully.','I can read my spelling words.'])
    for k in range(2):
        p=new(f'3  /  Find the Words (Part {k+1})','Write the missing spelling words.')
        p.rect(28,181,539,74,'#FFF9DF',GOLD)
        p.text('WORD BANK',43,190,10,'Bold',PINK)
        for i,w in enumerate(d['words'][k*6:k*6+6]):p.text(w,45+(i%3)*175,213+(i//3)*22,14,'Bold')
        for i,t in enumerate(d['clues'][k]):
            y=287+i*54;p.badge(i+1,29,y);p.wrap(t,63,y+2,490,13,leading=21)
        p.image('bed',260,632,293,78)
        p.check(['I used every word once.','I checked the spelling.'])
    p=new('4  /  Scrambled Words','Unscramble each word and write it on the line.')
    for i,t in enumerate(d['scrambles']):
        x=29+(i%2)*278;y=199+(i//2)*76;p.badge(i+1,x,y);p.text(t,x+32,y+1,15,'Bold');p.line(x+32,y+49,x+250,y+49)
    p.check(['I checked every letter.','I can read the words aloud.'])
    p=new('5  /  Match the Meanings','Write the letter of the definition next to the word.')
    p.rect(28,180,185,478,'#FFF4F8',None);p.rect(228,180,339,478,LIGHT,None)
    for i,w in enumerate(d['words']):
        y=194+i*37;p.line(38,y+23,63,y+23);p.text(f'{i+1}. {w}',73,y+2,13,'Bold')
    for i,t in enumerate(d['definitions']):p.wrap(t,241,194+i*37,311,11.5,leading=15)
    p.check(['I matched words and meanings.','I know what the words mean.'])
    p=new('6  /  Comprehension Check','Find the correct answer. Fill in the bubble.')
    for i,q in enumerate(d['questions']):
        y=181+i*127;p.rect(28,y,539,116,['#EDF8FE','#FFF9E5','#FDF0F6','#F0FAF3'][i],None)
        p.wrap(f'{i+1}. '+q['question'],40,y+9,512,12,'Bold',16,color=INK)
        for j,opt in enumerate(q['options']):
            p.rect(44,y+37+j*24,12,12,'#FFFFFF',BLUE,6);p.text(opt,67,y+33+j*24,11.7)
    p.check(['I found the answers in the story.','I understand what happened.'])
    p=new("7  /  Let's Speak!",'Read the song out loud 3 times!')
    for i,t in enumerate(d['song']):
        y=187+i*80;p.rect(28+(i%2)*24,y,515,66,['#EAF6FD','#FCECF3','#FFF8DC','#EDF8EE'][i],None,16);p.wrap('"'+t+'"',47+(i%2)*24,y+18,477,18,'Bold',24)
    p.image('bed',95,508,405,140)
    p.rect(28,654,539,119,'#FFFBEA',GOLD,16);p.text('Did you read it 3 times?',55,675,18,'Bold')
    for i in range(3):p.rect(99+i*144,716,22,22,'#FFFFFF',GOLD,3);p.text(f'Read {i+1}',130+i*144,716,12)
    p=new('8  /  Complete the Sentences','Fill in the blanks from the song.')
    p.rect(28,181,539,76,'#FFF9DF',GOLD);p.text('WORD BANK',43,191,10,'Bold',PINK)
    p.text('   '.join(d['sentence_bank']),43,220,14,'Bold')
    sentences=d['sentence_prompts']
    for i,t in enumerate(sentences):
        y=295+i*77;p.badge(i+1,29,y);p.wrap(t,65,y+2,486,15,leading=25)
    p.image('bed',280,626,270,72);p.check(['I completed the song.','I can read the sentences aloud.'])
    p=new('9  /  My Spelling Test','Ask someone to test you on the spelling words.')
    for i in range(12):
        y=190+i*35;p.badge(i+1,36,y);p.line(78,y+24,551,y+24)
    p.image('bed',280,627,270,72)
    p.rect(28,713,539,65,'#FFFBEA',GOLD)
    p.text("For teachers & parents",41,722,12,'Bold',PINK)
    p.wrap('1번부터 12번까지 단어를 불러 주세요. 단어가 포함된 짧은 문장으로 받아쓰기를 진행해도 좋습니다.',41,744,509,10,'Korean',15)
    for part in range(2):
        p=new(f"Teacher's Guide (Part {part+1})",BOOK_LABEL+'  /  문장별 해석',True)
        y=161
        for i,pair in enumerate(d['guides'][part]):
            en,ko=pair
            # Calculate box height from actual wrapped text before drawing the card.
            begin=len(p.ops); ey=p.wrap(en,44,y+11,507,11.5,'Body',16); ky=p.wrap(ko,44,ey+5,507,10,'Korean',15,color='#397AA3')
            texts=p.ops[begin:];p.ops=p.ops[:begin];p.rect(28,y,539,ky-y+11,LIGHT,'#D2E4ED');p.ops.extend(texts);y=ky+22
        p.text(d.get('teaching_focus','Discuss evidence from the chapter.'),30,751,10,'Bold')
    p=new('Answer Key',BOOK_LABEL+'  /  Check your answers!',True)
    def card(x,y,w,h,title,lines,color):
        p.rect(x,y,w,h,color,None);p.text(title,x+12,y+10,14,'Bold',PINK)
        for i,t in enumerate(lines):p.wrap(t,x+12,y+38+i*16,w-24,10.5,leading=14)
    card(28,160,263,275,'Find the Words',['Part 1']+[f'{i+1}. {w}' for i,w in enumerate(d['clue_answers'][0])]+['Part 2']+[f'{i+1}. {w}' for i,w in enumerate(d['clue_answers'][1])],LIGHT)
    card(306,160,261,275,'Comprehension Check',[f'{i+1}. '+a for i,a in enumerate(d['comprehension_answers'])],'#F4EFFA')
    card(28,449,263,268,'Scrambled Words',[f'{i+1}. {w}' for i,w in enumerate(d['words'])],'#EFF8EF')
    card(306,449,261,268,'Match the Meanings',[f'{i+1}. {w} - {a}' for i,(w,a) in enumerate(zip(d['words'],d['match_answers']))],'#FFF8E5')
    card(28,730,539,51,'Complete the Sentences',[],'#FDEEF4')
    p.wrap('    '.join(f'{i+1}. {a}' for i,a in enumerate(d['sentence_answers'])),41,759,510,10.5,leading=13)
    return pages

def pdf(pages):
    target=OUT/'workbook-publishing.pdf'; c=canvas.Canvas(str(target),pagesize=(W,H))
    c.setTitle("Chapter workbook | Publishing mockup")
    for p in pages:
        for o in p.ops:
            k=o['kind'];x=o.get('x',0);y=o.get('y',0)
            if k=='rect':
                c.setFillColor(o['fill']);c.setStrokeColor(o['stroke'] or o['fill']);c.setLineWidth(.8)
                c.roundRect(x,H-y-o['h'],o['w'],o['h'],o['radius'],fill=1,stroke=bool(o['stroke']))
            elif k=='text':
                c.setFillColor(o['color']);c.setFont(o['font'],o['size']);c.drawString(x,H-y-o['size'],o['text'])
            elif k=='line':
                c.setStrokeColor(o['color']);c.setLineWidth(.7);c.line(x,H-y,o['x2'],H-o['y2'])
            elif k=='image':c.drawImage(str(OUT/'assets'/(o['name']+'.png')),x,H-y-o['h'],o['w'],o['h'])
        c.showPage()
    c.save()
    doc=fitz.open(target);flat=fitz.open();thumbs=[]
    for i,p in enumerate(doc):
        pix=p.get_pixmap(dpi=300,alpha=False); data=pix.tobytes('png');(OUT/'canva-pages').mkdir(exist_ok=True)
        (OUT/'canva-pages'/f'page-{i+1:02d}.png').write_bytes(data)
        fp=flat.new_page(width=W,height=H);fp.insert_image(fp.rect,stream=data)
        im=Image.open(__import__('io').BytesIO(data));thumbs.append(ImageOps.contain(im,(224,317)))
    flat.set_metadata({'title':"Chapter workbook - A4 flattened 300 dpi"});flat.save(OUT/'workbook-a4-flattened.pdf',deflate=True)
    contact=Image.new('RGB',(960,4*355),'#E8EEF3')
    for i,im in enumerate(thumbs):
        x=(i%4)*240+8;y=(i//4)*355+8;contact.paste(im,(x,y));ImageDraw.Draw(contact).text((x+5,y+322),f'PAGE {i+1:02d}',fill='#30466B')
    contact.save(OUT/'preview.jpg',quality=92)
    with zipfile.ZipFile(OUT/'canva-a4-pages.zip','w',zipfile.ZIP_DEFLATED) as z:
        for f in (OUT/'canva-pages').glob('*.png'):z.write(f,f.name)

def rgb(s):return RGBColor.from_string(s.lstrip('#'))
def pptx(pages):
    prs=Presentation();prs.slide_width=Pt(W);prs.slide_height=Pt(H)
    for p in pages:
        s=prs.slides.add_slide(prs.slide_layouts[6])
        for o in p.ops:
            k=o['kind'];x=o.get('x',0);y=o.get('y',0)
            if k=='image':s.shapes.add_picture(str(OUT/'assets'/(o['name']+'.png')),Pt(x),Pt(y),Pt(o['w']),Pt(o['h']))
            elif k=='rect':
                sh=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if o['radius'] else MSO_SHAPE.RECTANGLE,Pt(x),Pt(y),Pt(o['w']),Pt(o['h']))
                if o['radius'] and min(o['w'],o['h'])>0:sh.adjustments[0]=min(.5,o['radius']/min(o['w'],o['h']))
                sh.fill.solid();sh.fill.fore_color.rgb=rgb(o['fill'])
                if o['stroke']:sh.line.color.rgb=rgb(o['stroke']);sh.line.width=Pt(.8)
                else:sh.line.fill.background()
            elif k=='line':
                sh=s.shapes.add_connector(1,Pt(x),Pt(y),Pt(o['x2']),Pt(o['y2']));sh.line.color.rgb=rgb(o['color']);sh.line.width=Pt(.7)
            elif k=='text':
                sh=s.shapes.add_textbox(Pt(x),Pt(y-1),Pt(W-x-15),Pt(o['size']*1.65));tf=sh.text_frame;tf.word_wrap=False
                tf.margin_left=tf.margin_right=tf.margin_top=tf.margin_bottom=0
                run=tf.paragraphs[0].add_run();run.text=o['text'];run.font.size=Pt(o['size']);run.font.name='맑은 고딕' if o['font']=='Korean' else 'Trebuchet MS';run.font.bold=o['font']=='Bold';run.font.color.rgb=rgb(o['color'])
    prs.save(OUT/'workbook-canva-editable.pptx')

def indesign(pages):
    data=json.dumps([p.ops for p in pages],ensure_ascii=False)
    jsx='''#target indesign
(function(){
var base=File($.fileName).parent;
var data=DATA;
var doc=app.documents.add();doc.documentPreferences.facingPages=false;doc.documentPreferences.pageWidth="210mm";doc.documentPreferences.pageHeight="297mm";
doc.viewPreferences.horizontalMeasurementUnits=MeasurementUnits.POINTS;doc.viewPreferences.verticalMeasurementUnits=MeasurementUnits.POINTS;
doc.documentPreferences.documentBleedTopOffset="3mm";doc.documentPreferences.documentBleedBottomOffset="3mm";doc.documentPreferences.documentBleedInsideOrLeftOffset="3mm";doc.documentPreferences.documentBleedOutsideOrRightOffset="3mm";
var shapes=doc.layers.add({name:"Boxes and rules"}), art=doc.layers.add({name:"Illustrations"}), text=doc.layers.add({name:"Editable text"});
function col(hex){var n=hex.substring(1);var c=doc.colors.itemByName(n);if(!c.isValid)c=doc.colors.add({name:n,model:ColorModel.PROCESS,space:ColorSpace.RGB,colorValue:[parseInt(n.substr(0,2),16),parseInt(n.substr(2,2),16),parseInt(n.substr(4,2),16)]});return c;}
for(var i=0;i<data.length;i++){var page=i?doc.pages.add():doc.pages[0];page.marginPreferences.properties={top:28,bottom:28,left:28,right:28};
for(var j=0;j<data[i].length;j++){var o=data[i][j],s;
if(o.kind=="text"){s=page.textFrames.add(text);s.geometricBounds=[o.y-2,o.x,o.y+o.size*1.65,580];s.contents=o.text;s.textFramePreferences.insetSpacing=0;var t=s.parentStory.texts[0];t.pointSize=o.size;t.leading=o.size*1.2;t.fillColor=col(o.color);try{t.appliedFont=o.font=="Korean"?"Malgun Gothic":(o.font=="Bold"?"Trebuchet MS\\tBold":"Trebuchet MS\\tRegular");}catch(e){} }
else if(o.kind=="image"){s=page.rectangles.add(art);s.geometricBounds=[o.y,o.x,o.y+o.h,o.x+o.w];s.strokeWeight=0;s.place(File(base+"/assets/"+o.name+".png"));s.fit(FitOptions.CONTENT_TO_FRAME);}
else if(o.kind=="rect"){s=page.rectangles.add(shapes);s.geometricBounds=[o.y,o.x,o.y+o.h,o.x+o.w];s.fillColor=col(o.fill);s.strokeWeight=o.stroke ? 0.8 : 0;if(o.stroke)s.strokeColor=col(o.stroke);if(o.radius){s.topLeftCornerOption=s.topRightCornerOption=s.bottomLeftCornerOption=s.bottomRightCornerOption=CornerOptions.ROUNDED_CORNER;s.topLeftCornerRadius=s.topRightCornerRadius=s.bottomLeftCornerRadius=s.bottomRightCornerRadius=o.radius;}}
else if(o.kind=="line"){s=page.graphicLines.add(shapes);s.paths[0].entirePath=[[o.x,o.y],[o.x2,o.y2]];s.strokeColor=col(o.color);s.strokeWeight=.7;}
}}
doc.save(File(base+"/workbook.indd"));doc.exportFile(ExportFormat.INDESIGN_MARKUP,File(base+"/workbook.idml"));alert("13 editable pages created. Check fonts and overset text before press mastering.");
})();'''.replace('DATA',data)
    (OUT/'open-in-indesign.jsx').write_text(jsx,encoding='utf-8')

def html(pages):
    parts=['<!doctype html><html lang="en"><meta charset="utf-8"><title>Chapter workbook preview</title><style>body{margin:0;background:#e8eef3;font-family:Arial}nav{padding:16px;text-align:center}section{width:210mm;height:297mm;margin:20px auto;position:relative;background:white;box-shadow:0 8px 30px #bbc}svg{width:100%;height:100%}@page{size:A4;margin:0}@media print{nav{display:none}section{margin:0;box-shadow:none;break-after:page}}</style><nav>Chapter workbook · 13 pages <button onclick="print()">Print / Save PDF</button></nav>']
    for p in pages:
        parts.append(f'<section><svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">')
        for o in p.ops:
            k=o['kind'];x=o.get('x',0);y=o.get('y',0)
            if k=='rect':parts.append(f'<rect x="{x}" y="{y}" width="{o["w"]}" height="{o["h"]}" rx="{o["radius"]}" fill="{o["fill"]}" stroke="{o["stroke"] or "none"}"/>')
            elif k=='line':parts.append(f'<path d="M{x} {y} L{o["x2"]} {o["y2"]}" stroke="{o["color"]}"/>')
            elif k=='image':parts.append(f'<image href="assets/{o["name"]}.png" x="{x}" y="{y}" width="{o["w"]}" height="{o["h"]}" preserveAspectRatio="none"/>')
            elif k=='text':parts.append(f'<text x="{x}" y="{y+o["size"]}" fill="{o["color"]}" font-family="Trebuchet MS,Malgun Gothic,sans-serif" font-size="{o["size"]}" font-weight="{"bold" if o["font"]=="Bold" else "normal"}">{escape(o["text"])}</text>')
        parts.append('</svg></section>')
    (OUT/'preview.html').write_text('\n'.join(parts),encoding='utf-8')

def validate(d,pages):
    assert len(pages)==13
    assert len(d['definitions'])==12 and len(d['questions'])==4
    for a,b in zip(d['words'],d['scrambles']):assert sorted(a)==sorted(b),(a,b)
    for bank,answers in zip([d['words'][:6],d['words'][6:]],d['clue_answers']):assert sorted(bank)==sorted(answers)
    assert len(d['match_answers'])==12 and set(d['match_answers'])==set('abcdefghijkl')
    issues=[]
    for p in pages:
        for o in p.ops:
            if o['kind']=='text':
                right=o['x']+pdfmetrics.stringWidth(o['text'],o['font'],o['size'])
                if right>W-12 or o['y']+o['size']>H-12:issues.append([p.number,o['text'],right])
    assert not issues,issues
    report={'pages':13,'student_pages':10,'teacher_pages':3,'size':'A4 210 × 297 mm','flattened_dpi':300,'source_html_words':len(d['words']),'checks':['scrambles preserve exact letters','cloze word banks match answer sets','matching answers follow question order','text within page bounds'],'corrections':d.get('corrections',[]),'limitations':['InDesign JSX is supplied; INDD/IDML are generated when run in InDesign and have not been verified in that application.','Canva PPTX import requires visual inspection in Canva.','Publishing PDF is an RGB mockup, not a certified PDF/X press file.','Use only artwork supplied or authorized for this chapter.']}
    (OUT/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Render a reviewed 13-page chapter workbook model.')
    parser.add_argument('--chapter',required=True,type=Path)
    parser.add_argument('--assets',required=True,type=Path,help='Directory with authorized sky.png and bed.png artwork')
    parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args()
    OUT=args.output.resolve(); OUT.mkdir(parents=True,exist_ok=True);(OUT/'assets').mkdir(exist_ok=True)
    d=json.loads(args.chapter.read_text(encoding='utf-8'))
    BRAND=d.get('brand','READING ADVENTURE');BOOK_LABEL=f"BOOK {d['book']:02d}  /  CHAPTER {d['chapter']:02d}"
    assert len(d['words'])==12 and len(set(d['words']))==12
    assert len(d['song'])==4 and len(d['sentence_answers'])==4
    assert len(d['clues'])==2 and all(len(x)==6 for x in d['clues'])
    assert len(d['questions'])==len(d['comprehension_answers'])==4
    assert all(len(q['options'])==3 and len(set(q['options']))==3 and a in q['options'] for q,a in zip(d['questions'],d['comprehension_answers']))
    assert len(d['sentence_bank'])==6 and len(d['sentence_prompts'])==4
    assert sum(x.count('________') for x in d['sentence_prompts'])==6
    assert len(d['scrambles'])==12 and all(a!=b for a,b in zip(d['words'],d['scrambles']))
    assert len(d['guides'])==2 and all(len(x)==2 for group in d['guides'] for x in group)
    for asset in ['sky.png','bed.png']:
        assert (args.assets/asset).is_file(),asset
        if (args.assets/asset).resolve()!=(OUT/'assets'/asset).resolve():shutil.copy2(args.assets/asset,OUT/'assets'/asset)
    (OUT/'chapter.json').write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
    pages=compose(d);validate(d,pages);pdf(pages);pptx(pages);indesign(pages);html(pages)
    print(f'Created {len(pages)} pages in {OUT}')
