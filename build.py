# coloring.html(아티팩트용 본문) → index.html(어디서나 열리는 완성 페이지 · 깃허브 페이지용)
from pathlib import Path
body=Path('coloring.html').read_text(encoding='utf-8')
head=('<!doctype html><html lang="ko"><head><meta charset="utf-8">'
      '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
      '<meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes"><meta name="theme-color" content="#dff3f6">'
      '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
      '<link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="icon-192-v2.png"><link rel="icon" href="icon-192-v2.png">'
      '<style>[hidden]{display:none!important}html,body{margin:0}:root{padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}</style>'
      '</head><body>\n')
# 새 판(sw)이 깔리면 한 번 새로고침해서 바로 새 그림 · 새 화면을 보여 준다 (다운 2026-10-22 「업데이트가 안 되는 거 같은데」) · 칠하던 그림은 먼저 저장
sw=('<script>if("serviceWorker" in navigator){const had=!!navigator.serviceWorker.controller;let done=false;'
    'navigator.serviceWorker.addEventListener("controllerchange",()=>{if(!had||done)return;done=true;try{if(typeof saveNow==="function")saveNow()}catch(e){}location.reload()});'
    'navigator.serviceWorker.register("sw.js").catch(()=>{})}</script>')
Path('index.html').write_text(head+body+'\n'+sw+'\n</body></html>\n',encoding='utf-8'); print('index.html 만듦')

# 앱(서비스 워커) 저장본 판 번호를 빌드할 때마다 바꾼다 → 설치한 앱이 다음에 열릴 때 옛 저장본을 지우고 새 파일을 받는다
import re, datetime
sw=Path('sw.js'); t=sw.read_text(encoding='utf-8')
sw.write_text(re.sub(r"const V='kk-[^']*';", "const V='kk-"+datetime.datetime.now().strftime('%Y%m%d%H%M%S')+"';", t),encoding='utf-8'); print('sw 판 갱신')
