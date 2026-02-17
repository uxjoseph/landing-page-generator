# 🎯 상세페이지 생성 스킬 (PNG 이어붙이기 방식)

## 핵심 구조: Gemini 이미지 생성 + 섹션별 PNG 조립

---

## 1️⃣ 전체 플로우

```
[입력] 제품/서비스 정보
         ↓
[오케스트레이터] SKILL.md
         ↓
    ┌────┴────┬────────┬────────┐
    ↓         ↓        ↓        ↓
[리서치]  [카피]    [디자인]   [프롬프트]
 에이전트  에이전트   에이전트   생성 에이전트
    └────┬────┴────────┴────────┘
         ↓
[13개 섹션별 Gemini 이미지 프롬프트]
         ↓
[Gemini 3 Pro] → 섹션별 PNG 13장
         ↓
[이미지 스티칭] → 최종 상세페이지 PNG/PDF
```

---

## 2️⃣ 스킬 폴더 구조 (클로드 공식 가이드 준수)

```
landing-page-generator/
├── SKILL.md                          # 메인 오케스트레이터 (<500줄)
│
├── agents/                           # 서브에이전트 (나노바나나 @호출용)
│   ├── 01-intake.md                  # 입력 수집 & 검증
│   ├── 02-research.md                # 타겟/페인포인트 리서치
│   ├── 03-copy.md                    # 13섹션 카피라이팅
│   ├── 04-design-direction.md        # 디자인 방향 설정
│   └── 05-prompt-generator.md        # Gemini 이미지 프롬프트 생성
│
├── references/
│   ├── 13-section-guide.md           # 13단 구조 상세 설명
│   ├── copy-patterns.md              # 고전환 카피 패턴
│   ├── gemini-prompt-patterns.md     # Gemini 이미지 프롬프트 베스트 프랙티스
│   └── design-specs.md               # 이미지 사이즈/스타일 스펙
│
├── scripts/
│   ├── stitch_images.py              # PNG 이어붙이기 스크립트
│   └── export_pdf.py                 # PDF 변환 스크립트
│
└── assets/
    └── style-presets/                # 스타일 프리셋 레퍼런스 이미지
        ├── minimal-example.png
        ├── sales-example.png
        └── premium-example.png
```

---

## 3️⃣ 서브에이전트 상세 설계

### 01-intake.md (입력 수집)
```
역할: 상세페이지 생성에 필요한 정보 수집

필수 입력:
- product_name: 제품/서비스명
- one_liner: 한 줄 정의
- target_audience: 핵심 타겟 (구체적으로)
- main_problem: 해결하는 핵심 문제
- key_benefit: 핵심 혜택/결과
- price: 가격 (원가/할인가)
- urgency: 한정 요소 (기간/수량/보너스)

선택 입력:
- testimonials: 후기 (텍스트/캡처)
- creator_bio: 제작자 소개
- bonus_items: 보너스 구성
- guarantee: 환불/보장 정책
- faq: FAQ 항목들
- brand_color: 브랜드 컬러 (없으면 자동 제안)

출력: structured_brief.json
```

### 02-research.md (리서치)
```
역할: 타겟 심층 분석 & 메시지 프레임 설계

분석 항목:
1. 페인포인트 5개 (공감 섹션용)
   - 감정적 고통
   - 반복 실패 경험
   - 시간/돈 낭비 경험

2. 실패 원인 3개 (문제 정의용)
   - 기존 방법의 한계
   - 숨겨진 진짜 원인
   - "내 탓이 아닌 구조 문제"

3. After 이미지 (변화 스토리용)
   - 구체적 결과 상태
   - 감정적 해방감
   - 시간/돈 절약 수치

4. 반대 의견/우려 (FAQ/리스크 제거용)
   - 예상 반론
   - 불안 요소

출력: research_output.json
```

### 03-copy.md (카피라이팅)
```
역할: 13개 섹션별 카피 생성

출력 형식 (각 섹션별):
{
  "section_01_hero": {
    "headline_options": ["옵션1", "옵션2", "옵션3"],
    "subheadline": "...",
    "urgency_text": "...",
    "cta_text": "..."
  },
  "section_02_pain": {
    "intro": "이런 고민 하시죠?",
    "pain_points": ["...", "...", "..."],
    "emotional_hook": "..."
  },
  // ... 13개 섹션 모두
}

카피 원칙:
- 한국어 자연스러운 구어체
- 감정 → 논리 흐름
- 구체적 숫자 사용
- 2인칭 "당신/여러분" 활용
```

### 04-design-direction.md (디자인 방향)
```
역할: 전체 비주얼 톤 & 스타일 결정

결정 사항:
1. 스타일 프리셋
   - minimal: 깔끔, 여백, 신뢰감
   - sales: 긴급성, 강조, 에너지
   - premium: 고급, 절제, 품격
   - community: 친근, 따뜻, 소속감

2. 컬러 팔레트
   - primary: 메인 컬러
   - secondary: 보조 컬러
   - accent: 강조 컬러 (CTA 등)
   - background: 배경
   - text: 본문

3. 타이포그래피 방향
   - 헤드라인 스타일
   - 본문 스타일

4. 레이아웃 원칙
   - 섹션 간격
   - 정렬 방식
   - 강조 패턴

출력: design_direction.json
```

### 05-prompt-generator.md (Gemini 프롬프트 생성) ⭐핵심
```
역할: 13개 섹션별 Gemini 이미지 생성 프롬프트 작성

입력:
- copy (03-copy 결과)
- design_direction (04 결과)
- image_spec (너비: 1200px 고정, 높이: 섹션별 가변)

출력 형식:
{
  "section_01_hero": {
    "prompt": "Create a landing page hero section image...",
    "width": 1200,
    "height": 800,
    "key_elements": ["headline", "subheadline", "cta_button", "urgency_badge"]
  },
  // ... 13개 섹션
}

프롬프트 원칙:
- 정확한 텍스트 포함 지시
- 레이아웃 구체적 명시
- 스타일 일관성 유지
- 한글 렌더링 주의사항
```

---

## 4️⃣ 13개 섹션 이미지 스펙

| # | 섹션명 | 권장 높이 | 핵심 요소 |
|---|--------|-----------|-----------|
| 01 | Hero (긴급성 헤더) | 800px | 헤드라인, 서브헤드, CTA, 긴급성 배지 |
| 02 | Pain (공감) | 600px | 페인포인트 3-4개, 감정 훅 |
| 03 | Problem (문제 정의) | 500px | 진짜 원인, 구조적 문제 |
| 04 | Story (Before→After) | 700px | 변화 스토리, 희망 메시지 |
| 05 | Solution Intro | 400px | 제품 한 줄 정의, 타겟 명시 |
| 06 | How It Works | 600px | 단계별 프로세스, 결과물 |
| 07 | Social Proof | 800px | 후기, 수치, 캡처 |
| 08 | Authority | 500px | 제작자 소개, 이력, 실적 |
| 09 | Benefits + Bonus | 700px | 혜택 요약, 보너스 구성 |
| 10 | Risk Removal | 500px | 환불 정책, FAQ, 보장 |
| 11 | Before/After Final | 400px | 최종 대비, 선택 압박 |
| 12 | Target Filter | 400px | 추천/비추천 대상 |
| 13 | Final CTA | 600px | 긴급성, CTA 버튼, 마지막 문구 |

**총 높이: ~7,000px (가변)**

---

## 5️⃣ 스티칭 스크립트 (scripts/stitch_images.py)

```python
from PIL import Image
import os

def stitch_sections(image_paths: list, output_path: str):
    """
    섹션별 PNG를 세로로 이어붙여 최종 상세페이지 생성
    
    Args:
        image_paths: 섹션 이미지 경로 리스트 (순서대로)
        output_path: 출력 파일 경로 (.png 또는 .pdf)
    """
    images = [Image.open(p) for p in image_paths]
    
    # 전체 높이 계산
    total_height = sum(img.height for img in images)
    max_width = max(img.width for img in images)
    
    # 새 캔버스 생성
    result = Image.new('RGB', (max_width, total_height), 'white')
    
    # 이미지 이어붙이기
    y_offset = 0
    for img in images:
        # 중앙 정렬
        x_offset = (max_width - img.width) // 2
        result.paste(img, (x_offset, y_offset))
        y_offset += img.height
    
    # 저장
    if output_path.endswith('.pdf'):
        result.save(output_path, 'PDF', resolution=150)
    else:
        result.save(output_path, 'PNG', optimize=True)
    
    return output_path
```

---

## 6️⃣ 실행 흐름 (나노바나나 프로 기준)

```
사용자: "ASC 상세페이지 만들어줘"

Step 1: @01-intake.md 호출
→ 필수 정보 수집 대화

Step 2: @02-research.md 호출  
→ 페인포인트/After 분석

Step 3: @03-copy.md 호출
→ 13섹션 카피 생성

Step 4: @04-design-direction.md 호출
→ 스타일/컬러 결정

Step 5: @05-prompt-generator.md 호출
→ Gemini 프롬프트 13개 생성

Step 6: Gemini 이미지 생성 (수동 또는 API)
→ 섹션별 PNG 13장

Step 7: stitch_images.py 실행
→ 최종 상세페이지 PNG/PDF
```

---

## 7️⃣ 핵심 고려사항

### Gemini 이미지 생성 한계
- **한글 렌더링**: 텍스트가 깨질 수 있음 → 핵심 텍스트만 포함하거나 후보정 필요
- **일관성**: 13장 스타일 통일 어려움 → 프롬프트에 스타일 앵커 강하게 명시
- **해상도**: 1200px 너비 기준, Gemini 출력 해상도 확인 필요

### 대안 옵션
1. **텍스트 오버레이 방식**: Gemini로 배경만 생성 → Python으로 텍스트 오버레이
2. **하이브리드**: 핵심 섹션만 Gemini, 나머지는 HTML→PNG 변환
3. **Figma 연동**: Gemini 결과를 Figma 템플릿에 삽입

---

## ❓ 확인 사항

1. **Gemini 호출 방식**: 
   - 나노바나나 내 Gemini API 연동?
   - 수동으로 프롬프트 복붙 후 이미지 업로드?

2. **한글 텍스트 처리**:
   - Gemini에서 직접 렌더링 시도?
   - 배경만 생성 후 텍스트 오버레이?

3. **섹션 수 조정**:
   - 13개 풀버전?
   - 핵심 7-8개 간소화 버전?

4. **최종 출력 포맷**:
   - PNG (웹 업로드용)
   - PDF (인쇄/다운로드용)
   - 둘 다?

이거 확정되면 바로 스킬 파일 생성 시작할게요!