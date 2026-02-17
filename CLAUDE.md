# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**상세페이지 자동 생성기** - 제품/서비스 정보를 입력받아 13개 섹션의 고전환 한국어 상세페이지(랜딩페이지)를 Gemini API로 자동 생성합니다.

## Development Commands

```bash
# 의존성 설치
pip install -r requirements.txt

# 상세페이지 생성 (샘플 데이터)
python3 scripts/generate_page.py

# API 연결 테스트
python3 scripts/gemini_api.py

# 섹션 이미지 스티칭만
python3 scripts/stitch_images.py output/sections output/final_page.png
```

## Architecture

### Pipeline Flow
```
Product Brief → Gemini Prompts → 13 Section Images → Stitched PNG/PDF
```

### Key Files
```
detail_page/
├── SKILL.md                    # 메인 오케스트레이터 (스킬 정의)
├── agents/                     # 서브에이전트 (단계별 처리)
│   ├── 01-intake.md           # 입력 수집 & 검증
│   ├── 02-research.md         # 타겟/페인포인트 리서치
│   ├── 03-copy.md             # 13섹션 카피라이팅
│   ├── 04-design-direction.md # 디자인 방향 설정
│   └── 05-prompt-generator.md # Gemini 이미지 프롬프트 생성
├── scripts/
│   ├── generate_page.py       # 전체 파이프라인 실행
│   ├── gemini_api.py          # Gemini API 호출
│   └── stitch_images.py       # 이미지 스티칭
├── references/                 # 참조 문서
└── output/                     # 생성 결과물
    ├── sections/              # 섹션별 PNG 13장
    ├── final_page.png         # 최종 상세페이지
    └── final_page.pdf         # PDF 버전
```

## Technical Specs

| 항목 | 값 |
|------|-----|
| 이미지 너비 | 1200px (고정) |
| 총 높이 | ~7,000px (13개 섹션) |
| API | Gemini 3 Pro Image Preview (Nano Banana Pro) |
| 출력 | PNG, PDF |

## 13 Section Structure

1. **Hero** (800px) - 헤드라인, CTA, 긴급성 배지
2. **Pain** (600px) - 페인포인트 3-4개
3. **Problem** (500px) - 진짜 원인, 구조적 문제
4. **Story** (700px) - Before→After 변화
5. **Solution** (400px) - 제품 한 줄 정의
6. **How It Works** (600px) - 단계별 프로세스
7. **Social Proof** (800px) - 후기, 수치
8. **Authority** (500px) - 제작자 소개
9. **Benefits** (700px) - 혜택, 보너스
10. **Risk Removal** (500px) - 환불 정책, FAQ
11. **Comparison** (400px) - Before/After 대비
12. **Target Filter** (400px) - 추천/비추천 대상
13. **Final CTA** (600px) - 최종 CTA

## Environment Variables

`.env` 파일에 Gemini API 키 설정:
```
GEMINI_API_KEY=your_api_key_here
```

## Customization

1. `scripts/generate_page.py`의 `create_sample_brief()` 함수에서 제품 정보 수정
2. `agents/*.md` 파일에서 카피/디자인 방향 커스터마이징
3. `references/` 폴더의 가이드 참조하여 스타일 프리셋 변경

## Important Notes

- **한글 텍스트 렌더링**: Gemini가 한글을 잘 렌더링하지만, 복잡한 텍스트는 후보정 필요할 수 있음
- **API 레이트 리밋**: 섹션 간 3초 딜레이 적용됨
- **스타일 일관성**: 프롬프트에 동일한 스타일 앵커 포함하여 13장 일관성 유지

## ⚠️ 필수 준수 사항 (Critical Requirements)

### 1. 이미지 크기 고정 (Dimension Lock)
- **너비: 정확히 1200px (절대 변경 금지)**
- Gemini API가 정확한 픽셀 크기를 보장하지 않으므로, `stitch_images.py`에서 자동으로 1200px로 리사이즈
- 모든 섹션이 동일한 너비를 가져야 좌우 마진이 일관됨

### 2. 실사 사진 스타일 (Photography Style)
- **일러스트/만화/카툰 스타일 절대 금지**
- 사람 등장 시: 실제 인물 사진 스타일 (리얼리스틱)
- 참조 스타일: 설화수, 이니스프리, 라네즈 광고
- 모든 프롬프트에 `PHOTOGRAPHY STYLE (MANDATORY)` 섹션 포함

### 3. 풀 블리드 (Full Bleed)
- 좌우 마진 없이 전체 너비 사용
- 콘텐츠가 이미지 가장자리까지 채움
