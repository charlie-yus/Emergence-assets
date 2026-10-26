#!/usr/bin/env python3
"""Compile this local thesis project without writing generated files into its source."""
import argparse, hashlib, json, os, pathlib, shutil, subprocess, time

def build(source, out, engine=None):
    source=source.resolve(); out=out.resolve()
    if not source.is_file():raise FileNotFoundError(source)
    if out==source.parent:raise ValueError('Build output must be separate from the source directory')
    out.mkdir(parents=True,exist_ok=True)
    default=pathlib.Path.home()/'texlive/2026/bin/universal-darwin/xelatex'
    exe=engine or shutil.which('xelatex') or (str(default) if default.exists() else None)
    if not exe:raise RuntimeError('XeLaTeX is unavailable; preserve sources and install a TeX runtime first')
    env=dict(os.environ);env['PATH']=str(pathlib.Path(exe).parent)+os.pathsep+env.get('PATH','')
    (out/'build-record.json').unlink(missing_ok=True)
    stamp=time.time();runs=[];last=None;stable=0
    for i in range(1,7):
        r=subprocess.run([exe,'-interaction=nonstopmode','-halt-on-error','-file-line-error','-no-shell-escape','-output-directory='+str(out),source.name],cwd=source.parent,env=env,capture_output=True,text=True,timeout=180)
        log=out/f'compile-{i}.txt';log.write_text(r.stdout+r.stderr)
        runs.append({'pass':i,'exit_code':r.returncode,'log':log.name})
        if r.returncode:raise RuntimeError(f'XeLaTeX failed on pass {i}; inspect {log}')
        auxiliary=b''.join(p.read_bytes() for p in sorted(out.glob(source.stem+'.*')) if p.suffix in {'.aux','.toc','.out'})
        digest=hashlib.sha256(auxiliary).hexdigest()
        stable=stable+1 if digest==last else 0;last=digest
        if i>=3 and stable>=1:break
    else:raise RuntimeError('Auxiliary files did not stabilize after six passes; do not deliver unresolved pagination')
    pdf=out/(source.stem+'.pdf')
    if not pdf.is_file() or pdf.stat().st_size<1000:raise RuntimeError('Compiler did not produce a valid-size PDF')
    final=(out/(source.stem+'.log')).read_text(errors='replace')
    critical=[line for line in final.splitlines() if any(k in line for k in ['Overfull \\hbox','Overfull \\vbox','Missing character:','undefined references','There were undefined','Font shape','Rerun to get','Label(s) may have changed'])]
    inputs={str(p.relative_to(source.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in source.parent.rglob('*') if p.is_file() and p.suffix in {'.tex','.cls','.png','.pdf','.jpg','.jpeg'} and out not in p.parents}
    result={'source':source.name,'output':pdf.name,'seconds':round(time.time()-stamp,3),'runs':runs,'inputs_sha256':inputs,'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'warnings_requiring_review':critical,'acceptance':'Compilation and log checks only; inspect PDF and font mapping separately.'}
    (out/'build-record.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'pdf':str(pdf),'passes':len(runs),'warnings':critical},ensure_ascii=False))
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('source',nargs='?',type=pathlib.Path,default=pathlib.Path(__file__).with_name('main.tex'));ap.add_argument('--out',type=pathlib.Path);ap.add_argument('--engine');a=ap.parse_args()
    build(a.source,a.out or a.source.parent/'build',a.engine)
