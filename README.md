# Cartosheaf 블로그

글·프로젝트·주제를 연결하는 한국어 정적 블로그. 별도 패키지 설치 없이 Python 3로 생성합니다.

## GitHub Pages에 올리기

1. GitHub에 새 저장소를 만들고 기본 브랜치를 `main`으로 둡니다.
2. ZIP을 풀어 파일과 폴더를 저장소 최상위에 올립니다. `.github/workflows/pages.yml`도 반드시 포함하세요.
3. 저장소 Settings → Pages → Build and deployment → Source에서 **GitHub Actions**를 선택합니다.
4. Actions에서 Deploy blog to GitHub Pages를 실행하거나 main에 변경을 저장합니다.
5. 배포가 끝나면 Settings → Pages에서 주소를 확인합니다.

일반 프로젝트 저장소의 `/저장소명/` 주소와 개인 도메인 모두에 대응하도록 상대경로를 사용합니다.

## cartosheaf.com 연결

사이트 확인 후 Settings → Pages의 Custom domain에 `cartosheaf.com`을 입력하고, 도메인 DNS에 GitHub Pages가 안내하는 레코드를 설정하세요. 기존 `gyguide.cartosheaf.com` 레코드는 유지하세요. DNS는 이 코드에서 변경하지 않습니다.

자동 배포에서도 도메인 설정이 명확히 남도록 `dist/CNAME`에 `cartosheaf.com` 한 줄을 작성해 커밋할 수 있습니다. 먼저 GitHub 기본 주소에서 확인할 수 있도록 현재 ZIP에는 CNAME을 넣지 않았습니다.

## 글 수정·추가

- `content/`의 내용이 드러나는 한글 파일명으로 된 Markdown을 수정하세요.
- `content/글목록.json`이 제목·날짜·프로젝트·주제·요약·글 파일명을 관리합니다. 배열 순서대로 표시되므로 최신 글을 앞에 추가합니다.
- 새 글: Markdown 파일을 만들고 글목록에 항목을 추가하세요. `slug`는 영문 소문자와 하이픈으로 고유하게 지정합니다.
- `project`: `information-structure`, `zero-waste`, `gyguide` 중 하나. 프로젝트 공통 글은 빈 문자열입니다.
- 지원하는 본문 문법은 문단, `## 제목`, `> 인용`입니다. 목록·이미지·표·링크 등 전체 Markdown 문법을 지원하는 구현은 아닙니다.
- `build.py`를 실행하면 HTML이 갱신됩니다. GitHub에 올리면 같은 작업이 자동으로 실행됩니다.
- 프로젝트 소개와 첫 화면 구성은 `build.py`, 디자인은 `dist/style.css`에서 수정합니다.
- 홈페이지와 글에 표시된 콘텐츠는 현재 대화를 토대로 작성한 초안입니다. 공개 전 본인 표현과 사실관계를 확인하세요.

## 내 컴퓨터에서 보기

```sh
python build.py
python -m http.server 8000 --directory dist
```

브라우저에서 http://localhost:8000 을 엽니다. 간단히 `dist/index.html`을 열어도 페이지 간 이동이 가능합니다.

## 포함된 화면

홈, 전체 글, 프로젝트 목록과 세 프로젝트 상세, 주제별 글, 세 개의 글 본문, 404 페이지. 실제 산출물 링크는 https://gyguide.cartosheaf.com 입니다.

회원가입·서버·데이터베이스·유료 서비스가 필요하지 않습니다. 모바일 대응, 키보드 포커스, 본문 건너뛰기, 한국어 문서 구조를 포함합니다.
