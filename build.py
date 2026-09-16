from pathlib import Path
import json, html, re
ROOT=Path(__file__).parent
OUT=ROOT/'dist'
OUT.mkdir(exist_ok=True)
E=html.escape
projects=[{'slug':'information-structure','name':'정보구조와 디자인 문법','en':'UNFOLD Information Structure Lab','desc':'정보의 의미와 사용자 목적은 어떻게 구획, 비교, 위계와 레이아웃이 되는가?','status':'탐구 중','question':'AI가 익숙한 스타일을 재현하는 데서 나아가, 무엇을 묶고 비교할지 결정하게 할 수 있을까?','next':'같은 비교 관계가 서로 다른 레이아웃으로 표현되는 조건을 살핀다.'},{'slug':'zero-waste','name':'제로웨이스트에서 주의의 리듬으로','en':'Reading into practice','desc':'재료를 살피고 부엌의 리듬을 찾듯, 아이디어와 하루를 돌보는 방법.','status':'관찰 시작','question':'아이디어의 특성과 내 생활 리듬을 함께 살피면, 저장한 생각을 실제 활동으로 이어갈 수 있을까?','next':'책을 대출받아 전시문에서 얻은 인상과 본문을 대조한다.'},{'slug':'gyguide','name':'갭이어 멘토링 서류 안내','en':'A guide in use','desc':'흩어진 멘토링 비용·서류 처리 정보를 실행할 수 있는 안내로 정리했다.','status':'산출물 있음','question':'안내문을 읽은 사람이 다음에 해야 할 일을 명확히 알게 하려면?','next':'실제 사용 중 헷갈리는 용어와 단계들을 관찰한다.'}]
posts=json.loads((ROOT/'content'/'글목록.json').read_text())
# Read the authored Markdown on each subsequent build.
for p in posts:p['body']=(ROOT/'content'/p['file']).read_text()
# Fact-checking projects: content/factchecks/<slug>/{meta.json,03-evidence-log.json,05-sample.en.md,06-process-notes.md}
# Each subfolder is one independent case; missing folder just means no fact-checks yet (site still builds).
FC=ROOT/'content'/'factchecks'
factchecks=[]
if FC.exists():
 for d in sorted(FC.iterdir()):
  if not d.is_dir():continue
  m=json.loads((d/'meta.json').read_text())
  m['slug']=d.name
  m['sample']=(d/'05-sample.en.md').read_text()
  m['evidence']=json.loads((d/'03-evidence-log.json').read_text())
  m['process']=(d/'06-process-notes.md').read_text()
  factchecks.append(m)
def bold(s):
 return re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
def md2(s):
 # Slightly richer renderer for fact-check prose: ##/### headings, - lists, > quotes, **bold**.
 out=[];lines=s.strip().split('\n');i=0
 while i<len(lines):
  line=lines[i]
  if line.startswith('### '):out.append('<h3>'+bold(E(line[4:]))+'</h3>');i+=1
  elif line.startswith('## '):out.append('<h2>'+bold(E(line[3:]))+'</h2>');i+=1
  elif line.startswith('> '):out.append('<blockquote>'+bold(E(line[2:]))+'</blockquote>');i+=1
  elif line.startswith('- '):
   items=[]
   while i<len(lines) and lines[i].startswith('- '):items.append('<li>'+bold(E(lines[i][2:]))+'</li>');i+=1
   out.append('<ul>'+''.join(items)+'</ul>')
  elif line.strip()=='':
   i+=1
  else:
   para=[]
   while i<len(lines) and lines[i].strip()!='' and not lines[i].startswith(('## ','### ','- ','> ')):para.append(lines[i]);i+=1
   out.append('<p>'+bold(E(' '.join(para)))+'</p>')
 return '\n'.join(out)
def evidence_table(items):
 rows=''.join(f'''<tr><td><strong>{E(e["title"])}</strong><br><span class="ev-meta">{E(e.get("org",""))} · {E(e.get("date",""))} · {E(e.get("type",""))} · {E(e.get("primacy",""))}</span></td><td>{E(e.get("passage",""))}</td><td class="stance-{E(e.get("stance","context"))}">{E(e.get("stance_label",e.get("stance","")))}</td><td>{E(e.get("reliability",""))}</td><td>{f'<a class="external" href="{E(e["url"])}" target="_blank" rel="noopener">source ↗</a>' if e.get("url") else '—'}</td></tr>''' for e in items)
 return f'<div class="table-wrap"><table class="evidence-table"><thead><tr><th>Source</th><th>Relevant passage</th><th>Stance</th><th>Reliability</th><th>Link</th></tr></thead><tbody>{rows}</tbody></table></div>'
def md(s):
 result=[]
 for para in s.strip().split('\n\n'):
  if para.startswith('## '):result.append('<h2>'+E(para[3:])+'</h2>')
  elif para.startswith('> '):result.append('<blockquote>'+E(para[2:])+'</blockquote>')
  else:result.append('<p>'+E(para)+'</p>')
 return '\n'.join(result)
def page(path,title,body,active=''):
 depth=len(Path(path).parts)-1
 pre='../'*depth
 nav=''.join(f'<a {"aria-current=page" if label==active else ""} href="{pre}{url}">{label}</a>' for label,url in [('글','writing.html'),('프로젝트','projects.html'),('주제','topics.html')])
 markup=f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{E(title)} · Cartosheaf</title><meta name="description" content="아이디어를 실험하고 글로 남깁니다. 정보구조, 주의집중, 접근성을 탐구하는 개인 블로그."><link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23faf7ef'/%3E%3Cg stroke='%23a6812c' stroke-width='2.5' stroke-linecap='round'%3E%3Cline x1='16' y1='3' x2='16' y2='7'/%3E%3Cline x1='16' y1='25' x2='16' y2='29'/%3E%3Cline x1='3' y1='16' x2='7' y2='16'/%3E%3Cline x1='25' y1='16' x2='29' y2='16'/%3E%3Cline x1='6.5' y1='6.5' x2='9.2' y2='9.2'/%3E%3Cline x1='22.8' y1='22.8' x2='25.5' y2='25.5'/%3E%3Cline x1='6.5' y1='25.5' x2='9.2' y2='22.8'/%3E%3Cline x1='22.8' y1='9.2' x2='25.5' y2='6.5'/%3E%3C/g%3E%3Ccircle cx='16' cy='16' r='6.5' fill='%23a6812c'/%3E%3C/svg%3E"><link rel="stylesheet" href="{pre}style.css"></head><body><a class="skip" href="#main">본문으로 건너뛰기</a><div class="shell"><header><a class="brand" href="{pre}index.html">cartosheaf<span class="brandmark">*</span></a><nav aria-label="주 메뉴">{nav}</nav></header><main id="main">{body}</main><footer><a href="{pre}index.html">Cartosheaf</a><span>생각을 펼치고, 실험을 남기는 곳.</span><a href="{pre}projects/gyguide.html">갭이어 안내 프로젝트 ↗</a></footer></div></body></html>'''
 target=OUT/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(markup)
def eyebrow_for(p):
 m=next((x['name'] for x in projects if x['slug']==p['project']),None)
 if m:return m
 m=next((x['title_kr'] for x in factchecks if x['slug']==p['project']),None)
 return m or '프로젝트를 잇는 생각'
def rows(items,pre=''):
 return ''.join(f'''<article class="post-row"><div class="date">{p['date']}<br><span>{p['kind']}</span></div><div><div class="eyebrow">{eyebrow_for(p)}</div><h3><a href="{pre}posts/{p['slug']}.html">{p['title']}</a></h3><p>{p['desc']}</p><div class="tags">{''.join(f'<a href="{pre}topics.html#{t}">{t}</a>' for t in p['tags'])}</div></div><a class="read" aria-label="{p['title']} 읽기" href="{pre}posts/{p['slug']}.html">↗</a></article>''' for p in items)
def cards():return ''.join(f'<a class="project-card" href="projects/{p["slug"]}.html"><span class="eyebrow">{p["status"]}</span><h3>{p["name"]}</h3><p>{p["desc"]}</p><span class="card-end">프로젝트 보기 ↗</span></a>' for p in projects)+''.join(f'<a class="project-card" href="projects/{f["slug"]}.html"><span class="eyebrow">{f["status"]}</span><h3>{f["title_kr"]}</h3><p>{f["desc"]}</p><span class="card-end">Fact-Checking Sample 보기 ↗</span></a>' for f in factchecks)
page('index.html','생각과 실험',f'''<section class="intro"><div><div class="eyebrow accent">NOTES & EXPERIMENTS</div><h1>생각을 펼치고,<br>쓰면서 알아갑니다<span class="accent">.</span></h1></div><p>정보를 어떻게 구조화할까.<br>아이디어를 어떻게 돌볼까.<br>질문에서 시작해 실험과 글로 이어가는 기록.</p></section><div class="home-grid"><section><div class="section-title"><h2>최근 글</h2><a href="writing.html">모든 글 ↗</a></div>{rows(posts)}</section><aside><div class="section-title"><h2>탐구 중인 프로젝트</h2></div><a class="side-project" href="projects/information-structure.html"><span class="number">01</span><h3>정보구조와<br>디자인 문법</h3><p>의미가 레이아웃이 되기까지</p><span>탐구 중 ↗</span></a><a class="side-project" href="projects/zero-waste.html"><span class="number">02</span><h3>제로웨이스트에서<br>주의의 리듬으로</h3><p>저장한 생각을 일상으로</p><span>관찰 시작 ↗</span></a><a class="artifact" href="projects/gyguide.html"><span class="eyebrow">산출물</span><h3>갭이어 멘토링<br>서류 안내 ↗</h3><p>절차를 따라갈 수 있는 HTML 안내</p></a>'''+(''.join(f'<a class="artifact" href="projects/{f["slug"]}.html"><span class="eyebrow">Fact-Checking Sample</span><h3>{f["title_kr"]} ↗</h3><p>{f["desc"]}</p></a>' for f in factchecks[:1]))+'''</aside></div>''')
page('writing.html','모든 글','<section class="page-heading"><div class="eyebrow">WRITING</div><h1>글</h1><p>관찰, 실험, 그리고 생각의 변화.</p></section>'+rows(posts),'글')
page('projects.html','프로젝트','<section class="page-heading"><div class="eyebrow">PROJECTS</div><h1>프로젝트</h1><p>각자의 질문으로 시작해, 서로의 생각으로 이어집니다.</p></section><div class="cards">'+cards()+'</div>','프로젝트')
for proj in projects:
 related=[p for p in posts if p['project']==proj['slug']]
 output='<a class="external" href="https://gyguide.cartosheaf.com">갭이어 멘토링 서류 안내 열기 ↗</a>' if proj['slug']=='gyguide' else '<p>현재 산출물은 아래의 관찰·실험 기록입니다.</p>'
 page(f'projects/{proj["slug"]}.html',proj['name'],f'<a class="back" href="../projects.html">← 프로젝트 목록</a><section class="page-heading"><div class="eyebrow">{proj["en"]} / {proj["status"]}</div><h1>{proj["name"]}</h1><p>{proj["desc"]}</p></section><div class="project-summary"><section><h2>현재 질문</h2><p>{proj["question"]}</p></section><section><h2>다음 단계</h2><p>{proj["next"]}</p></section></div><section class="outputs"><h2>산출물</h2>{output}</section><div class="section-title"><h2>진행 기록</h2></div>'+ (rows(related,'../') if related else '<p class="empty">서류 안내를 만들며 내린 판단과 수정 과정을 이곳에 이어서 기록합니다.</p>'),'프로젝트')
for fc in factchecks:
 verdict_cls='verdict-'+re.sub(r'[^a-z]+','-',fc['verdict'].lower()).strip('-')
 deliverable=f'''<a class="back" href="../projects.html">← 프로젝트 목록</a><section class="page-heading"><div class="eyebrow">FACT-CHECKING SAMPLE · {E(fc["status"])}</div><h1>{E(fc["title_kr"])}</h1><p>{E(fc["desc"])}</p></section><div class="verdict-badge {verdict_cls}">Verdict: {E(fc["verdict"])}</div><div class="prose">{md2(fc["sample"])}</div><section class="outputs"><h2>관련 자료</h2><p><a href="{fc["slug"]}-evidence.html">Evidence Log 전체 보기 ↗</a> · <a href="{fc["slug"]}-process.html">조사 과정 기록 보기 ↗</a></p></section>'''
 page(f'projects/{fc["slug"]}.html',fc['title_kr'],deliverable,'프로젝트')
 ev=f'<a class="back" href="{fc["slug"]}.html">← Fact-Checking Sample</a><section class="page-heading"><div class="eyebrow">EVIDENCE LOG</div><h1>{E(fc["title_kr"])} — Evidence Log</h1><p>수집한 근거와 신뢰도 평가, 결론에 이르지 못한 검색까지 포함한 전체 기록입니다.</p></section>'+evidence_table(fc['evidence'])
 page(f'projects/{fc["slug"]}-evidence.html',fc['title_kr']+' Evidence Log',ev,'프로젝트')
 pr=f'<a class="back" href="{fc["slug"]}.html">← Fact-Checking Sample</a><section class="page-heading"><div class="eyebrow">PROCESS NOTES</div><h1>{E(fc["title_kr"])} — 조사 과정</h1></section><div class="prose">{md2(fc["process"])}</div>'
 page(f'projects/{fc["slug"]}-process.html',fc['title_kr']+' 조사 과정',pr,'프로젝트')
for p in posts:
 proj=next((x for x in projects if x['slug']==p['project']),None)
 fcm=next((x for x in factchecks if x['slug']==p['project']),None) if not proj else None
 if proj:context=f'<a href="../projects/{proj["slug"]}.html">{proj["name"]} ↗</a>'
 elif fcm:context=f'<a href="../projects/{fcm["slug"]}.html">{fcm["title_kr"]} ↗</a>'
 else:context='<a href="../projects.html">프로젝트를 잇는 생각 ↗</a>'
 page(f'posts/{p["slug"]}.html',p['title'],f'<a class="back" href="../writing.html">← 모든 글</a><article class="reading"><div class="eyebrow">{p["kind"]} · {p["date"]}</div><h1>{p["title"]}</h1><p class="dek">{p["desc"]}</p><div class="article-context">{context}</div><div class="prose">{md(p["body"])}</div><div class="article-end"><h2>이어지는 주제</h2><div class="tags">'+''.join(f'<a href="../topics.html#{t}">{t}</a>' for t in p['tags'])+'</div></div></article>','글')
page('topics.html','주제','<section class="page-heading"><div class="eyebrow">CONNECTIONS</div><h1>주제로 이어 읽기</h1><p>하나의 질문이 여러 프로젝트를 만나는 자리.</p></section>'+''.join(f'<section class="topic" id="{t}"><h2>{t}</h2>{rows([p for p in posts if t in p["tags"]])}</section>' for t in ['정보구조','주의집중','글쓰기','디자인','접근성']),'주제')
page('404.html','페이지를 찾을 수 없습니다','<section class="page-heading"><h1>페이지를 찾을 수 없습니다.</h1><p>주소가 바뀌었거나 아직 없는 기록입니다.</p><a href="index.html">홈으로 돌아가기 →</a></section>')
(OUT/'.nojekyll').touch()
print('Built',len(list(OUT.rglob('*.html'))),'pages')
