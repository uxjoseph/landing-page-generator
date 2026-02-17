# 상세페이지 자동 생성기 (Landing Page Generator)

AI 에이전트 팀이 제품/서비스 정보를 기반으로 **13개 섹션의 고전환 상세페이지**를 자동 생성합니다.

## 특징

- **5개 AI 에이전트** 협업 시스템
- **Gemini API**로 섹션별 이미지 생성
- **1200px 고정 너비**, 총 ~7,000px 높이
- **PNG/PDF** 출력 지원

## 파이프라인

```
[입력] 제품 정보
    ↓
[기획팀] 입력수집 → 리서치
    ↓
[카피팀] 13섹션 카피 생성
    ↓
[디자인팀] 스타일/컬러 결정
    ↓
[개발팀] Gemini 프롬프트 → 이미지 생성 → 스티칭
    ↓
[출력] 상세페이지 PNG/PDF
```

## 에이전트 구성

| 에이전트 | 모델 | 역할 |
|----------|------|------|
| `01-intake` | haiku | 필수 정보 수집 |
| `02-research` | sonnet | 타겟/페인포인트 분석 |
| `03-copy` | sonnet | 13섹션 카피라이팅 |
| `04-design-direction` | haiku | 스타일 프리셋 결정 |
| `05-prompt-generator` | sonnet | Gemini 이미지 프롬프트 |

## 13개 섹션 구조

| # | 섹션 | 높이 | 목적 |
|---|------|------|------|
| 01 | Hero | 800px | 첫인상, CTA |
| 02 | Pain | 600px | 공감 유발 |
| 03 | Problem | 500px | 원인 제시 |
| 04 | Story | 700px | Before→After |
| 05 | Solution | 400px | 제품 소개 |
| 06 | How It Works | 600px | 프로세스 |
| 07 | Social Proof | 800px | 후기/증거 |
| 08 | Authority | 500px | 신뢰 구축 |
| 09 | Benefits | 700px | 혜택/보너스 |
| 10 | Risk Removal | 500px | 환불/FAQ |
| 11 | Comparison | 400px | 최종 대비 |
| 12 | Target Filter | 400px | 적합성 체크 |
| 13 | Final CTA | 600px | 행동 유도 |

## 설치

```bash
# 의존성 설치
pip install -r requirements.txt

# 환경변수 설정
cp .env.example .env
# .env 파일에 GEMINI_API_KEY 입력
```

## 사용법

### Claude Code에서 실행
```
사용자: 상세페이지 만들어줘
→ 에이전트가 필수 정보 질문
→ 자동으로 13섹션 생성
```

### 스크립트 직접 실행
```bash
# 전체 파이프라인
python scripts/generate_page.py

# 이미지 스티칭만
python scripts/stitch_images.py output/sections output/final_page.png
```

## 파일 구조

```
detail_page/
├── SKILL.md                 # 메인 오케스트레이터
├── prompt.md                # 전체 설계 문서
├── agents/                  # AI 에이전트 정의
│   ├── 01-intake.md
│   ├── 02-research.md
│   ├── 03-copy.md
│   ├── 04-design-direction.md
│   └── 05-prompt-generator.md
├── scripts/                 # Python 스크립트
│   ├── generate_page.py     # 전체 파이프라인
│   ├── gemini_api.py        # Gemini API 호출
│   └── stitch_images.py     # 이미지 스티칭
├── references/              # 참조 문서
└── output/                  # 생성 결과물 (gitignore)
```

## 기술 스펙

- **이미지 너비**: 1200px (고정)
- **총 높이**: ~7,000px
- **API**: Gemini 2.0 Flash
- **스타일**: 실사 사진 (일러스트 금지)

## 라이선스

MIT License
