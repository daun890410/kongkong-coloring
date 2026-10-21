# 목소리 조각들을 묶음 mp3 로 합친다 → voice/<누구>/pk_<묶음>.mp3 + voice/<누구>/map.json {이름:[묶음,시작초,길이초]}
import json, subprocess, re
from pathlib import Path
import numpy as np
SR=24000; GAP=int(SR*0.35)
root=Path(__file__).parent
def pcm(f):
    r=subprocess.run(['ffmpeg','-v','error','-i',str(f),'-f','s16le','-ac','1','-ar',str(SR),'-'],capture_output=True,check=True)
    return np.frombuffer(r.stdout,dtype=np.int16)
def group(k):
    m=re.match(r'tale_(t\d\d)_',k)
    if m: return m.group(1)
    m=re.match(r'done_(s\d\d)_',k)
    if m: return 'd'+m.group(1)
    return 'base'
for v in ('gunwoo','ruri'):
    d=root/v; files=sorted(d.glob('*.mp3')); files=[f for f in files if not f.name.startswith('pk_')]
    groups={}
    for f in files: groups.setdefault(group(f.stem),[]).append(f)
    M={}
    for g,fs in groups.items():
        parts=[np.zeros(GAP//2,np.int16)]; pos=GAP//2
        for f in fs:
            a=pcm(f); M[f.stem]=[g,round(pos/SR,3),round(len(a)/SR,3)]; parts+= [a,np.zeros(GAP,np.int16)]; pos+=len(a)+GAP
        wav=d/f'pk_{g}.wav'
        import wave
        with wave.open(str(wav),'wb') as w: w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes(np.concatenate(parts).tobytes())
        subprocess.run(['ffmpeg','-v','error','-y','-i',str(wav),'-c:a','libmp3lame','-b:a','40k',str(d/f'pk_{g}.mp3')],check=True); wav.unlink()
    json.dump(M,open(d/'map.json','w',encoding='utf-8'),separators=(',',':'))
    print(v,len(files),'조각 →',len(groups),'묶음')
