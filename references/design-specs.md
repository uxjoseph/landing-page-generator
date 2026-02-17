# 디자인 스펙 가이드

## ⚠️ 필수 준수 사항 (CRITICAL REQUIREMENTS)

### 크기 고정 (DIMENSION LOCK)
- **너비: 정확히 1200px (절대 변경 금지)**
- 모든 섹션이 동일한 1200px 너비를 가져야 함
- 좌우 마진 없이 전체 너비를 콘텐츠로 채움 (FULL BLEED)

### 실사 사진 스타일 (PHOTOGRAPHY STYLE)
- **일러스트/만화/카툰 스타일 절대 금지**
- 사람 등장 시: 실제 인물 사진 스타일 (리얼리스틱)
- 피부 질감, 조명이 자연스러운 프로 사진 품질
- 참조: 설화수, 이니스프리, 라네즈 광고 스타일

---

## 이미지 사이즈

### 기본 스펙
| 항목 | 값 |
|------|-----|
| 기본 너비 | **1200px (절대 고정)** |
| DPI | 72 (웹용) / 150 (PDF용) |
| 포맷 | PNG (투명도 필요시), JPG (사진) |
| 색상 모드 | sRGB |

### 섹션별 높이
| 섹션 | 높이 | 비고 |
|------|------|------|
| 01. Hero | 800px | 풀스크린 느낌 |
| 02. Pain | 600px | 3-4개 포인트 |
| 03. Problem | 500px | 3개 원인 |
| 04. Story | 700px | Before/After |
| 05. Solution | 400px | 심플 소개 |
| 06. How It Works | 600px | 3-4 단계 |
| 07. Social Proof | 800px | 후기 + 숫자 |
| 08. Authority | 500px | 프로필 |
| 09. Benefits | 700px | 혜택 + 보너스 |
| 10. Risk Removal | 500px | FAQ |
| 11. Comparison | 400px | 2컬럼 |
| 12. Target Filter | 400px | 2컬럼 |
| 13. Final CTA | 600px | 마무리 |

**총 높이: ~7,000px**

---

## 스타일 프리셋

### Minimal (미니멀)
```
특징: 깔끔, 여백, 신뢰감
적합: SaaS, 전문 서비스, B2B

컬러:
- Primary: #2563EB (Blue)
- Secondary: #60A5FA
- Accent: #F59E0B (Amber)
- Background: #FFFFFF
- Text: #1F2937

타이포:
- 헤드라인: Bold, 크게
- 본문: Regular, 여유로운 행간
- 여백 많이 사용

버튼:
- Border-radius: 8px
- 깔끔한 그림자
```

### Sales (세일즈)
```
특징: 긴급성, 강조, 에너지
적합: 이벤트, 한정 판매, 프로모션

컬러:
- Primary: #DC2626 (Red)
- Secondary: #F97316 (Orange)
- Accent: #FBBF24 (Yellow)
- Background: #FEF3C7 또는 #FFFBEB
- Text: #1F2937

타이포:
- 헤드라인: Black, 아주 크게
- 강조: 형광 하이라이트
- 뱃지 많이 사용

버튼:
- Border-radius: 0-4px
- 강한 그림자
- 펄스 애니메이션 (CSS시)
```

### Premium (프리미엄)
```
특징: 고급, 절제, 품격
적합: 고가 상품, 럭셔리, 하이엔드 서비스

컬러:
- Primary: #1F2937 (Dark Gray)
- Secondary: #374151
- Accent: #D4AF37 (Gold)
- Background: #F9FAFB 또는 #FFFFFF
- Text: #111827

타이포:
- 헤드라인: Medium/SemiBold
- Serif 폰트 고려
- 넉넉한 자간

버튼:
- Border-radius: 0-4px
- 미묘한 그림자
- 골드 액센트
```

### Community (커뮤니티)
```
특징: 친근, 따뜻, 소속감
적합: 커뮤니티, 교육, 코칭

컬러:
- Primary: #7C3AED (Purple)
- Secondary: #A78BFA
- Accent: #EC4899 (Pink)
- Background: #FAF5FF
- Text: #374151

타이포:
- 헤드라인: SemiBold
- 둥근 느낌의 폰트
- 친근한 톤

버튼:
- Border-radius: 12-16px
- 부드러운 그림자
```

---

## 타이포그래피

### 크기 체계
```
Desktop:
- Hero Headline: 56-72px
- Section Headline: 36-48px
- Subheadline: 24-28px
- Body Large: 20px
- Body: 18px
- Caption: 14px

Mobile (0.75x):
- Hero Headline: 36-48px
- Section Headline: 28-36px
- Subheadline: 20-22px
- Body: 16px
```

### 행간 (Line Height)
```
- 헤드라인: 1.2 (타이트)
- 서브헤드: 1.4
- 본문: 1.6-1.8 (여유)
```

### 자간 (Letter Spacing)
```
- 헤드라인: -0.02em (약간 좁게)
- 본문: 0 (기본)
- 캡션: 0.02em (약간 넓게)
```

---

## 컴포넌트 스펙

### CTA 버튼
```
Large:
- 높이: 56-64px
- 패딩: 16px 48px
- 폰트: 20px Bold
- Border-radius: 프리셋별 (0-16px)

Medium:
- 높이: 48px
- 패딩: 12px 32px
- 폰트: 16px Bold

Small:
- 높이: 40px
- 패딩: 8px 24px
- 폰트: 14px Bold
```

### 카드
```
- 패딩: 24-32px
- Border-radius: 12-16px
- Border: 1px solid #E5E7EB
- Shadow: 0 4px 6px rgba(0,0,0,0.05)
```

### 뱃지
```
- 패딩: 4px 12px
- Border-radius: 4px (각진) 또는 9999px (둥근)
- 폰트: 12-14px SemiBold
```

### 아이콘
```
- 크기: 24px (인라인), 32-48px (독립)
- 스트로크: 2px
- 스타일: 프리셋별 (line/filled/outline)
```

---

## 레이아웃

### 그리드
```
- 최대 너비: 1200px
- 컬럼: 12 그리드
- 거터: 24px
- 마진: 48px (데스크탑), 24px (모바일)
```

### 섹션 간격
```
- 섹션 간: 80-120px
- 내부 패딩: 48-64px (상하), 48px (좌우)
```

### 정렬
```
- 기본: 중앙 정렬
- 텍스트: 좌측 정렬 (가독성)
- 버튼/CTA: 중앙 정렬
```

---

## 컬러 사용 가이드

### 배경색 패턴
```
밝음/어두움 교차로 섹션 구분:

01. Hero: Primary 그라데이션
02. Pain: 연한 회색 (#F3F4F6)
03. Problem: 흰색
04. Story: 연한 회색
05. Solution: 흰색
06. How: 연한 회색
07. Proof: 흰색
08. Authority: 연한 회색
09. Benefits: Primary + 투명도
10. Risk: 흰색
11. Compare: 연한 회색
12. Target: 흰색
13. CTA: Primary 그라데이션
```

### 강조색 사용
```
- CTA 버튼: Accent 컬러
- 뱃지/태그: Accent 또는 Primary
- 하이라이트: Accent 배경 + 어두운 텍스트
- 아이콘: Primary 또는 Accent
```

### 텍스트 컬러
```
- 헤드라인: Text Primary (#1F2937)
- 본문: Text Primary
- 보조 텍스트: Text Secondary (#6B7280)
- 흰 배경 위: 어두운 텍스트
- 어두운 배경 위: 흰색/밝은 텍스트
```

---

## 파일 명명 규칙

```
섹션 이미지:
01_hero.png
02_pain.png
03_problem.png
...
13_final_cta.png

최종 출력:
final_page.png
final_page.pdf

작업 파일:
{project_name}_v1.png
{project_name}_v2.png
```
