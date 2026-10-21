# coloring.html(아티팩트용 본문) → index.html(어디서나 열리는 완성 페이지 · 깃허브 페이지용)
from pathlib import Path
body=Path('coloring.html').read_text(encoding='utf-8')
head=('<!doctype html><html lang="ko"><head><meta charset="utf-8">'
      '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
      '<meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes"><meta name="theme-color" content="#dff3f6">'
      '<link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="icon-192.png"><link rel="icon" href="icon-192.png">'
      '<style>[hidden]{display:none!important}html,body{margin:0}:root{padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}</style>'
      '</head><body>\n')
sw='<script>if("serviceWorker" in navigator)navigator.serviceWorker.register("sw.js").catch(()=>{})</script>'
Path('index.html').write_text(head+body+'\n'+sw+'\n</body></html>\n',encoding='utf-8'); print('index.html 만듦')

# 앱(서비스 워커) 저장본 판 번호를 빌드할 때마다 바꾼다 → 설치한 앱이 다음에 열릴 때 옛 저장본을 지우고 새 파일을 받는다
import re, datetime
sw=Path('sw.js'); t=sw.read_text(encoding='utf-8')
sw.write_text(re.sub(r"const V='kk-[^']*';", "const V='kk-"+datetime.datetime.now().strftime('%Y%m%d%H%M%S')+"';", t),encoding='utf-8'); print('sw 판 갱신')
