# 타입캐스트로 voice/<건우|루리>/<이름>.mp3 를 만든다 (1배속 · 크레딧 아님). 있는 건 건너뛴다.
import sys, base64, subprocess, json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, r'C:/Users/momop/dev/aiClaude/엔진/자동화')
sys.path.insert(0, str(Path(__file__).parent))
from tc공통 import 클라이언트
from typecast.models import Output, PresetPrompt, TTSRequestWithTimestamps
from lines import all_lines
from tale_lines import tale_lines
VOICES={'gunwoo':'tc_624cccbcadcd568510764d65','ruri':'tc_65a8c82a7e7bded32947497e'}
c=클라이언트(); L={**all_lines(),**tale_lines()}; out=Path(__file__).parent
def one(job):
    v,k,t=job; mp3=out/v/f'{k}.mp3'
    if mp3.exists(): return 'skip'
    for tryn in range(3):
        try:
            req=TTSRequestWithTimestamps(text=t,model='ssfm-v30',voice_id=VOICES[v],language='kor',
                prompt=PresetPrompt(emotion_type='preset',emotion_preset='happy',emotion_intensity=1.0),
                output=Output(audio_format='wav',target_lufs=-16,remove_silence_ms=250,audio_tempo=1.0))
            res=c.text_to_speech_with_timestamps(req,granularity='word')
            wav=mp3.with_suffix('.wav'); wav.write_bytes(base64.b64decode(res.audio))
            subprocess.run(['ffmpeg','-v','error','-y','-i',str(wav),'-ac','1','-ar','24000','-b:a','40k',str(mp3)],check=True); wav.unlink()
            return 'ok'
        except Exception as e:
            err=str(e)[:120]
    return 'FAIL '+k+' '+err
for v in VOICES: (out/v).mkdir(exist_ok=True)
jobs=[(v,k,t) for v in VOICES for k,t in L.items() if len(sys.argv)<2 or k in sys.argv[1:]]
print('줄',len(L),'× 목소리',len(VOICES),'=',len(jobs),flush=True)
with ThreadPoolExecutor(4) as ex:
    res=list(ex.map(one,jobs))
print({r.split()[0]:sum(1 for x in res if x.split()[0]==r.split()[0]) for r in res}); [print(r) for r in res if r.startswith('FAIL')]
