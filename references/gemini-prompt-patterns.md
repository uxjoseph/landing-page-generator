# Gemini 이미지 프롬프트 베스트 프랙티스

## ⚠️ 필수 준수 사항 (CRITICAL - 모든 프롬프트에 적용)

### 1. 크기 고정 (DIMENSION LOCK)
```
=== CRITICAL REQUIREMENTS ===
1. EXACT DIMENSIONS: 1200x[HEIGHT] pixels - MUST be exactly 1200px wide
2. FULL BLEED: Content fills ENTIRE 1200px width with NO margins or borders
3. WIDTH LOCK: Image width MUST be exactly 1200 pixels, no deviation
```

### 2. 실사 사진 스타일 (PHOTOGRAPHY STYLE)
```
=== PHOTOGRAPHY STYLE (MANDATORY) ===
- Use REALISTIC PHOTOGRAPHY style, NOT illustrations or cartoons
- When showing people: Use REAL HUMAN MODELS with natural skin texture
- Professional photography lighting and composition
- Photo-realistic quality like high-end Korean beauty advertisements
- Style reference: Sulwhasoo, Innisfree, Laneige advertising quality
```

### 3. 체크리스트 (모든 프롬프트 끝에 추가)
```
=== FINAL CHECKLIST ===
✓ Image is EXACTLY 1200x[HEIGHT] pixels
✓ Content fills full width with NO side margins
✓ People shown are realistic photos, NOT illustrations
✓ Korean text is clear and readable
✓ Professional advertising quality
```

---

## 기본 구조

### 프롬프트 템플릿
```
[CRITICAL REQUIREMENTS] + [PHOTOGRAPHY STYLE] + [LAYOUT] + [CONTENT] + [CHECKLIST]
```

### 예시
```
Create a professional landing page hero section.

=== CRITICAL REQUIREMENTS ===
1. EXACT DIMENSIONS: 1200x800 pixels - MUST be exactly 1200px wide
2. FULL BLEED: Content fills ENTIRE 1200px width with NO margins or borders
3. WIDTH LOCK: Image width MUST be exactly 1200 pixels, no deviation

=== PHOTOGRAPHY STYLE (MANDATORY) ===
- Use REALISTIC PHOTOGRAPHY style, NOT illustrations or cartoons
- When showing people: Use REAL HUMAN MODELS with natural skin texture
- Professional photography lighting and composition
- Style reference: Sulwhasoo, Innisfree, Laneige advertising quality

Style: Minimal, clean, professional.
Background: Gradient from #2563EB to #1E40AF.
Layout: Centered content with headline at top, subtext middle, CTA button bottom.
Text (Korean): "월 1000만원 매출의 비밀" (headline), "지금 시작하기" (button).
Include: Subtle geometric shapes, soft shadows, professional atmosphere.

=== FINAL CHECKLIST ===
✓ Image is EXACTLY 1200x800 pixels
✓ Content fills full width with NO side margins
✓ People shown are realistic photos, NOT illustrations
✓ Korean text is clear and readable
✓ Professional advertising quality
```

---

## 스타일 지시어

### 전체적인 느낌
```
Modern, Contemporary, Clean
Professional, Corporate, Business
Minimal, Sleek, Sophisticated
Warm, Friendly, Inviting
Bold, Dynamic, Energetic
Premium, Luxury, High-end
```

### 디자인 스타일
```
Flat design with subtle shadows
Glassmorphism with blur effects
Neumorphism with soft shadows
Gradient mesh backgrounds
Geometric patterns
Abstract shapes
```

---

## 컬러 지시

### 방법 1: Hex 코드 직접 지정
```
Background color: #2563EB (blue)
Accent color: #F59E0B (amber)
Text color: #1F2937 (dark gray)
```

### 방법 2: 컬러 팔레트 설명
```
Use a blue and white color scheme with amber accents.
Color palette: Corporate blue (#2563EB) as primary,
white background, amber (#F59E0B) for CTAs.
```

### 방법 3: 감성적 표현
```
Professional blue tones conveying trust
Warm orange accents for energy and action
Clean white space for clarity
```

---

## 레이아웃 지시

### 위치 표현
```
Top-left, Top-center, Top-right
Center-left, Center, Center-right
Bottom-left, Bottom-center, Bottom-right
```

### 정렬
```
Centered layout
Left-aligned content
Right-aligned sidebar
Symmetrical composition
Asymmetrical dynamic layout
```

### 구역 분할
```
Split layout: left side for text, right side for image
Three-column grid layout
Stacked vertical sections
Overlapping elements
```

---

## 텍스트 렌더링 (한글)

### 주의사항
Gemini는 한글 텍스트 렌더링이 불안정할 수 있음.

### 방법 1: 명확한 지시
```
Text content in Korean:
- Headline: "월 1000만원 매출의 비밀"
  (Render this Korean text clearly and accurately)
- Subtext: "지금 시작하기"
  (Ensure Korean characters are properly rendered)
```

### 방법 2: 텍스트 플레이스홀더
```
Include placeholder areas for text:
- Large headline area (center-top)
- Subheadline area (below headline)
- CTA button area (bottom-center)
(Text will be added separately in post-processing)
```

### 방법 3: 최소 텍스트
```
Minimal text approach:
Only include the CTA button text: "시작하기"
Other text areas should be clean spaces for overlay
```

---

## 섹션별 프롬프트 예시

### Hero Section
```
Create a landing page hero section image.
Dimensions: 1200x800 pixels.

Style:
- Modern, professional design
- Gradient background from #2563EB to #1E40AF
- Clean, minimal aesthetic

Layout:
- Top-right corner: Small urgency badge
- Center: Large headline (Korean text area)
- Below center: Subheadline area
- Bottom-center: Large CTA button with arrow icon

Elements:
- Subtle floating geometric shapes (circles, lines)
- Soft glow effects
- Professional atmosphere

Text to render (Korean):
- Badge: "선착순 100명"
- CTA Button: "지금 시작하기"

Keep other text areas clean for later overlay.
```

### Pain Points Section
```
Create a pain points section for landing page.
Dimensions: 1200x600 pixels.

Style:
- Empathetic, relatable design
- Light gray background (#F3F4F6)
- Card-based layout

Layout:
- Top: Section header area
- Center: 3-4 pain point cards in horizontal row
- Each card: Icon placeholder + text area + emotional hook

Elements:
- Worry/stress related icons (clock, money, stress symbols)
- Soft card shadows
- Muted color tones conveying difficulty

Visual mood:
- Slightly darker, problem-focused
- Reader should feel "this describes me"
```

### Social Proof Section
```
Create a testimonials/social proof section.
Dimensions: 1200x800 pixels.

Style:
- Trust-building, credible design
- White background with subtle texture
- Professional testimonial cards

Layout:
- Top: Statistics bar (3 large numbers with labels)
- Center: 3 testimonial cards
- Each card: Avatar circle + quote marks + text area + name/result

Elements:
- Star ratings (5 stars)
- Quote mark decorations
- Checkmark icons for verified
- Number highlights

Stats format:
- "2,847명" (large number)
- "누적 수강생" (label below)
```

### Final CTA Section
```
Create a final call-to-action section.
Dimensions: 1200x600 pixels.

Style:
- High-contrast, attention-grabbing
- Gradient background (primary color)
- Urgent but professional

Layout:
- Center-top: Compelling headline area
- Center: Price display (original strikethrough, discounted highlighted)
- Center-bottom: Large CTA button
- Bottom: Urgency reminder + closing text area

Elements:
- Glowing or pulsing effect on CTA button
- Strikethrough on original price
- Highlight/badge on discounted price
- Timer or countdown indicator placeholder

Color emphasis:
- Dark background or vibrant gradient
- White/light text for contrast
- Accent color (yellow/orange) for CTA button
```

---

## 품질 향상 키워드

### 해상도/선명도
```
High resolution, sharp details
Crystal clear, crisp edges
4K quality, detailed
```

### 전문성
```
Professional design, corporate quality
Magazine-quality layout
Agency-level design
Award-winning aesthetic
```

### 일관성
```
Consistent with brand guidelines
Matching style with other sections
Cohesive visual language
Unified color scheme throughout
```

---

## 피해야 할 것

### 부정 지시어 사용
```
❌ "Don't include people"
✅ "Abstract shapes only, no human figures"

❌ "No cluttered design"
✅ "Clean, minimal layout with ample whitespace"
```

### 모호한 표현
```
❌ "Make it look good"
✅ "Modern, professional design with blue gradient background"

❌ "Add some text"
✅ "Include headline area (48px height) at center-top"
```

### 너무 많은 요소
```
❌ "Include headline, subheadline, 5 bullet points,
    3 images, testimonials, pricing, FAQ..."

✅ Focus on 3-4 key elements per section
```

---

## 스타일 일관성 유지 팁

### 앵커 문구 사용
모든 섹션 프롬프트에 동일한 스타일 앵커 포함:

```
STYLE ANCHOR (use in all sections):
"Consistent with landing page style:
- Color palette: Primary #2563EB, Accent #F59E0B
- Typography: Bold headlines, clean body text
- Visual style: Minimal, professional, modern
- Mood: Trustworthy, confident, action-oriented"
```

### 시리즈 명시
```
"This is section 3 of 13 in a landing page series.
Maintain visual consistency with previous sections."
```
