import json
from pathlib import Path
def tale_lines():
    d=json.load(open(Path(__file__).parent.parent/'tales'/'tales.json',encoding='utf-8')); L={}
    for t in d['tales']:
        for i,pg in enumerate(t['pages'],1):
            for k in ('tell','after','book'): L[f'tale_{t["id"]}_{i}_{k}']=pg[k]
    return L
