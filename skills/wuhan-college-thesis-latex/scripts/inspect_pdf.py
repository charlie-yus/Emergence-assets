#!/usr/bin/env python3
"""Create 16-page contact sheets and limited geometry checks; not visual acceptance."""
import argparse,json,pathlib,re,hashlib
import fitz
from PIL import Image,ImageDraw
p=argparse.ArgumentParser(description=__doc__);p.add_argument('pdf',type=pathlib.Path);p.add_argument('--out',required=True,type=pathlib.Path);a=p.parse_args()
src=a.pdf.resolve();out=a.out.resolve()
if out.exists():p.error('Output already exists; choose a new review directory')
doc=fitz.open(src);out.mkdir(parents=True);rows=[];thumbs=[]
for n,page in enumerate(doc,1):
 spans=[s for b in page.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans'] if s['text'].strip()]
 bad=[s['text'] for s in spans if s['bbox'][0]<-1 or s['bbox'][1]<-1 or s['bbox'][2]>page.rect.width+1 or s['bbox'][3]>page.rect.height+1]
 small=[{'text':s['text'][:60],'size':round(s['size'],2)} for s in spans if s['size']<7]
 footer=''.join(s['text'].strip() for s in spans if s['bbox'][1]>page.rect.height-65 and s['text'].strip().isdigit())
 flags=[]
 if abs(page.rect.width-595.276)>0.6 or abs(page.rect.height-841.89)>0.6:flags.append('non_A4')
 if bad:flags.append('outside_paper')
 if small:flags.append('small_text_review')
 text=page.get_text()
 if len(text.strip())<50:flags.append('sparse_page_review')
 if '\ufffd' in text or '\x00' in text:flags.append('replacement_or_null_character')
 rows.append({'physical_page':n,'size_bp':[round(page.rect.width,3),round(page.rect.height,3)],'footer':footer,'flags':flags,'outside_paper':bad,'small_spans':small,'links':len(page.get_links())})
 pix=page.get_pixmap(matrix=fitz.Matrix(.5,.5),alpha=False)
 im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples);im.thumbnail((200,283))
 thumbs.append((im,n,flags))
 if flags:page.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(out/f'review-{n:03}.png')
for start in range(0,len(thumbs),16):
 canvas=Image.new('RGB',(880,1280),'#ddd');d=ImageDraw.Draw(canvas)
 for idx,(im,n,flags) in enumerate(thumbs[start:start+16]):
  x=8+(idx%4)*220;y=8+(idx//4)*320
  d.text((x,y),f'Page {n}'+(' REVIEW' if flags else ''),fill='red' if flags else 'black');canvas.paste(im,(x,y+16))
 canvas.save(out/f'overview-{start//16+1:02}.jpg',quality=90)
report={'pdf':src.name,'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'pages':len(doc),'page_checks':rows,'scope':'Geometry, extracted text and thumbnail generation only. Review every overview, enlarge marked pages and inspect representative complex components.'}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'pages':len(doc),'flagged':[r['physical_page'] for r in rows if r['flags']],'out':str(out)},ensure_ascii=False))
