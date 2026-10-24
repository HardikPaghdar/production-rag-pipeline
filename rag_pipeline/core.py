from pathlib import Path
from collections import Counter
import re

def load(root):
    base=Path(root).resolve()
    if not base.is_dir(): raise ValueError('Knowledge base directory not found')
    return [(p.relative_to(base).as_posix(),p.read_text(encoding='utf-8')) for p in sorted(base.rglob('*')) if p.is_file() and p.suffix.lower() in {'.md','.txt'} and p.stat().st_size<2000000]
def query(root, question, limit=5):
    if len(question.strip())<3: raise ValueError('Question too short')
    q=Counter(re.findall(r'[a-z0-9_]{2,}',question.lower())); ranked=[]
    for source,text in load(root):
        for start in range(0,len(text),600):
            chunk=text[start:start+600]; d=Counter(re.findall(r'[a-z0-9_]{2,}',chunk.lower())); score=sum(min(v,d[k]) for k,v in q.items())
            if score: ranked.append((score,source,start,chunk))
    ranked.sort(key=lambda x:(-x[0],x[1],x[2]))
    evidence=[{'score':score,'source':src,'start_char':start,'text':text} for score,src,start,text in ranked[:limit]]
    return {'question':question,'answer':'Review the cited evidence; this baseline does not synthesize unsupported claims.' if evidence else 'No matching evidence found.','evidence':evidence}
