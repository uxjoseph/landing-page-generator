"""
상세페이지 전체 생성 파이프라인
입력 정보를 받아 최종 PNG/PDF까지 생성합니다.
"""

import os
import json
import sys
from pathlib import Path
from typing import Dict, Any, Optional

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.gemini_api import generate_image, test_api_connection
from scripts.stitch_images import stitch_from_directory, create_preview


# 섹션별 기본 높이
SECTION_HEIGHTS = {
    "01_hero": 800,
    "02_pain": 600,
    "03_problem": 500,
    "04_story": 700,
    "05_solution": 400,
    "06_how_it_works": 600,
    "07_social_proof": 800,
    "08_authority": 500,
    "09_benefits": 700,
    "10_risk_removal": 500,
    "11_comparison": 400,
    "12_target_filter": 400,
    "13_final_cta": 600
}


def create_sample_brief() -> Dict[str, Any]:
    """
    샘플 제품 정보 Brief를 생성합니다.
    """
    return {
        "product_name": "AI 마케팅 자동화",
        "one_liner": "광고비 50% 절감하는 AI 기반 마케팅 최적화 시스템",
        "target_audience": "월 광고비 100만원 이상 쓰는 스마트스토어 셀러",
        "main_problem": "광고 최적화에 하루 2시간 소비하면서도 ROAS는 제자리",
        "key_benefit": "AI가 24시간 자동으로 광고 최적화, 평균 광고비 50% 절감",
        "price": {
            "original": "199,000원",
            "discounted": "99,000원",
            "period": "월"
        },
        "urgency": {
            "type": "quantity",
            "value": "선착순 100명",
            "bonus": "1:1 셋업 컨설팅 무료"
        },
        "style_preset": "minimal",
        "brand_colors": {
            "primary": "#2563EB",
            "secondary": "#60A5FA",
            "accent": "#F59E0B"
        }
    }


def generate_section_prompts(brief: Dict[str, Any]) -> Dict[str, Dict]:
    """
    Brief 정보를 바탕으로 13개 섹션의 Gemini 프롬프트를 생성합니다.
    """
    style = brief.get("style_preset", "minimal")
    colors = brief.get("brand_colors", {})
    primary = colors.get("primary", "#2563EB")
    accent = colors.get("accent", "#F59E0B")

    product_name = brief.get("product_name", "제품명")
    one_liner = brief.get("one_liner", "제품 설명")
    target = brief.get("target_audience", "타겟 고객")
    problem = brief.get("main_problem", "해결하는 문제")
    benefit = brief.get("key_benefit", "핵심 혜택")
    price = brief.get("price", {})
    urgency = brief.get("urgency", {})

    # 공통 스타일 앵커 (크기 고정 + 실사 스타일 필수)
    style_anchor = f"""
=== CRITICAL REQUIREMENTS ===
1. EXACT DIMENSIONS: Image must be EXACTLY 1200px wide
2. FULL BLEED: Content fills ENTIRE 1200px width with NO margins or borders
3. WIDTH LOCK: Width MUST be exactly 1200 pixels, no deviation allowed

=== PHOTOGRAPHY STYLE (MANDATORY) ===
- Use REALISTIC PHOTOGRAPHY style, NOT illustrations or cartoons
- When showing people: Use REAL HUMAN MODELS with natural skin texture
- Professional photography lighting and composition
- Photo-realistic quality like high-end Korean beauty advertisements
- Style reference: Sulwhasoo, Innisfree, Laneige advertising quality

=== DESIGN STYLE ===
Style: {style}, modern, professional Korean landing page design.
Color palette: Primary {primary}, Accent {accent}, clean white/gray backgrounds.
Typography: Bold Korean headlines, clean body text, professional atmosphere.

=== FINAL CHECKLIST ===
✓ Image is EXACTLY 1200 pixels wide
✓ Content fills full width with NO side margins
✓ People shown are realistic photos, NOT illustrations
✓ Korean text is clear and readable
"""

    prompts = {
        "01_hero": {
            "prompt": f"""Create a hero section for a Korean landing page.
Dimensions: 1200x800 pixels.
{style_anchor}

Layout:
- Top-right: Small urgency badge with text "{urgency.get('value', '한정 특가')}"
- Center: Large headline area for Korean text
- Below: Subheadline area
- Bottom-center: Large CTA button with text "지금 시작하기"

Background: Gradient from {primary} to darker shade.
Include: Subtle geometric shapes, professional glow effects.
Mood: Trustworthy, action-oriented, premium feel.

Key message concept: "{benefit}"
""",
            "width": 1200,
            "height": 800,
            "filename": "01_hero.png"
        },

        "02_pain": {
            "prompt": f"""Create a pain points section for Korean landing page.
Dimensions: 1200x600 pixels.
{style_anchor}

Background: Light gray (#F3F4F6)

Layout:
- Top: Section intro "이런 고민 하고 계신가요?"
- Center: 3 pain point cards in horizontal layout
- Each card: Worry icon + text area

Pain point concepts related to: "{problem}"

Visual mood: Empathetic, the reader should feel "이거 내 얘기다"
Include: Stress/worry related icons, soft card shadows.
""",
            "width": 1200,
            "height": 600,
            "filename": "02_pain.png"
        },

        "03_problem": {
            "prompt": f"""Create a problem definition section.
Dimensions: 1200x500 pixels.
{style_anchor}

Background: White

Layout:
- Top: Hook text "당신 탓이 아닙니다"
- Center: 3 reason cards explaining the real problem
- Visual flow connecting the reasons

Concept: Reframing the problem - it's not their fault, the system is broken.
Include: Connecting arrows, numbered points, highlight effects.
""",
            "width": 1200,
            "height": 500,
            "filename": "03_problem.png"
        },

        "04_story": {
            "prompt": f"""Create a before/after transformation section.
Dimensions: 1200x700 pixels.
{style_anchor}

Layout:
- Left side or top: "Before" state (muted colors, stressed imagery)
- Center: Transformation arrow or timeline
- Right side or bottom: "After" state (vibrant, successful imagery)

Before concept: Struggling with "{problem}"
After concept: Achieving "{benefit}"

Include: Contrast between struggle and success, upward graphs, checkmarks.
""",
            "width": 1200,
            "height": 700,
            "filename": "04_story.png"
        },

        "05_solution": {
            "prompt": f"""Create a solution introduction section.
Dimensions: 1200x400 pixels.
{style_anchor}

Background: White with subtle accent

Layout:
- Center: Product name "{product_name}" prominently displayed
- Below: One-liner "{one_liner}"
- Subtle: Target audience indicator

Simple, clean, impactful introduction.
Include: Product logo placeholder, clean typography, subtle brand colors.
""",
            "width": 1200,
            "height": 400,
            "filename": "05_solution.png"
        },

        "06_how_it_works": {
            "prompt": f"""Create a "how it works" process section.
Dimensions: 1200x600 pixels.
{style_anchor}

Background: Light gray (#F3F4F6)

Layout:
- Header: "이렇게 작동합니다"
- Center: 3-step horizontal process
- Each step: Number circle + Icon + Title + Brief description

Steps should show simple progression to results.
Include: Connecting lines between steps, clean icons, progress indication.
""",
            "width": 1200,
            "height": 600,
            "filename": "06_how_it_works.png"
        },

        "07_social_proof": {
            "prompt": f"""Create a social proof/testimonials section.
Dimensions: 1200x800 pixels.
{style_anchor}

Background: White

Layout:
- Top: Stats bar with 3 large numbers (users, satisfaction, results)
- Center: 3 testimonial cards
- Each card: Avatar circle + Quote + Name + Result achieved

Include: Star ratings, quote marks, verified badges, result highlights.
Mood: Trust-building, credible, impressive numbers.
""",
            "width": 1200,
            "height": 800,
            "filename": "07_social_proof.png"
        },

        "08_authority": {
            "prompt": f"""Create an authority/about section.
Dimensions: 1200x500 pixels.
{style_anchor}

Background: Light gray (#F3F4F6)

Layout:
- Left: Professional headshot placeholder (circle frame)
- Right: Bio area, credentials list, personal message

Include: Credential badges/icons, professional atmosphere, trust indicators.
Mood: Expert, trustworthy, relatable.
""",
            "width": 1200,
            "height": 500,
            "filename": "08_authority.png"
        },

        "09_benefits": {
            "prompt": f"""Create a benefits and bonus section.
Dimensions: 1200x700 pixels.
{style_anchor}

Background: Subtle {primary} tint

Layout:
- Top: "What you get" header
- Center-left: Benefits list with checkmarks (5-6 items)
- Center-right: Bonus items with gift icons
- Bottom: Total value calculation

Include: Checkmark icons, gift/star icons, value strikethrough, highlight on savings.
""",
            "width": 1200,
            "height": 700,
            "filename": "09_benefits.png"
        },

        "10_risk_removal": {
            "prompt": f"""Create a risk removal/guarantee section.
Dimensions: 1200x500 pixels.
{style_anchor}

Background: White

Layout:
- Top-center: Guarantee badge/seal
- Center: Guarantee text area
- Bottom: FAQ preview (2-3 questions)

Include: Trust seal, shield icon, money-back imagery, accordion-style FAQ.
Mood: Safe, secure, no-risk.
""",
            "width": 1200,
            "height": 500,
            "filename": "10_risk_removal.png"
        },

        "11_comparison": {
            "prompt": f"""Create a before/after comparison section.
Dimensions: 1200x400 pixels.
{style_anchor}

Background: Light gray (#F3F4F6)

Layout:
- Two columns side by side
- Left column: "Without" (red X marks, negative items)
- Right column: "With" (green checkmarks, positive items)
- Bottom: "Which do you choose?" prompt

Clear visual contrast between the two paths.
""",
            "width": 1200,
            "height": 400,
            "filename": "11_comparison.png"
        },

        "12_target_filter": {
            "prompt": f"""Create a target audience filter section.
Dimensions: 1200x400 pixels.
{style_anchor}

Background: White

Layout:
- Two columns
- Left: "이런 분께 추천" (green theme, checkmarks)
- Right: "이런 분은 비추천" (gray theme, X marks)

Include: Clear icons, honest filtering, professional layout.
Target concept: "{target}"
""",
            "width": 1200,
            "height": 400,
            "filename": "12_target_filter.png"
        },

        "13_final_cta": {
            "prompt": f"""Create a final call-to-action section.
Dimensions: 1200x600 pixels.
{style_anchor}

Background: Gradient {primary} (darker, more urgent)

Layout:
- Top: Final compelling headline
- Center: Price display
  - Original: {price.get('original', '199,000원')} (strikethrough)
  - Discounted: {price.get('discounted', '99,000원')} (highlighted, large)
- Large CTA button: "지금 시작하기" with {accent} color
- Bottom: Urgency reminder "{urgency.get('value', '한정 수량')}"

High contrast, attention-grabbing, final push to action.
Include: Glowing CTA button effect, urgency indicators, professional close.
""",
            "width": 1200,
            "height": 600,
            "filename": "13_final_cta.png"
        }
    }

    return prompts


def save_prompts(prompts: Dict, output_path: str):
    """프롬프트를 JSON 파일로 저장"""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=2)
    print(f"Prompts saved: {output_path}")


def generate_landing_page(
    brief: Optional[Dict[str, Any]] = None,
    output_dir: str = "output",
    skip_generation: bool = False
) -> Optional[str]:
    """
    전체 상세페이지 생성 파이프라인을 실행합니다.

    Args:
        brief: 제품 정보 (없으면 샘플 사용)
        output_dir: 출력 디렉토리
        skip_generation: True면 이미지 생성 스킵 (스티칭만)

    Returns:
        최종 페이지 경로
    """
    output_dir = str(PROJECT_ROOT / output_dir)
    sections_dir = os.path.join(output_dir, "sections")

    # 디렉토리 생성
    Path(sections_dir).mkdir(parents=True, exist_ok=True)

    if brief is None:
        print("Using sample brief...")
        brief = create_sample_brief()

    # Brief 저장
    brief_path = os.path.join(output_dir, "structured_brief.json")
    with open(brief_path, "w", encoding="utf-8") as f:
        json.dump(brief, f, ensure_ascii=False, indent=2)
    print(f"Brief saved: {brief_path}")

    # 프롬프트 생성
    print("\nGenerating prompts...")
    prompts = generate_section_prompts(brief)
    prompts_path = os.path.join(output_dir, "gemini_prompts.json")
    save_prompts(prompts, prompts_path)

    if not skip_generation:
        # API 연결 테스트
        print("\nTesting API connection...")
        if not test_api_connection():
            print("API connection failed. Check your GEMINI_API_KEY.")
            return None

        # 섹션별 이미지 생성
        print("\nGenerating section images...")
        for section_key, section_data in prompts.items():
            print(f"\n{'='*50}")
            print(f"Generating: {section_key}")
            print(f"{'='*50}")

            output_path = os.path.join(sections_dir, section_data["filename"])

            result = generate_image(
                prompt=section_data["prompt"],
                output_path=output_path,
                width=section_data["width"],
                height=section_data["height"]
            )

            if not result:
                print(f"Warning: Failed to generate {section_key}")

            # API 레이트 리밋 방지
            import time
            time.sleep(3)

    # 이미지 스티칭
    print("\n" + "="*50)
    print("Stitching final page...")
    print("="*50)

    final_png = os.path.join(output_dir, "final_page.png")
    final_pdf = os.path.join(output_dir, "final_page.pdf")

    # PNG 생성
    result = stitch_from_directory(sections_dir, final_png)

    if result:
        # PDF도 생성
        stitch_from_directory(sections_dir, final_pdf)

        # 미리보기 생성
        preview_path = os.path.join(output_dir, "preview.png")
        create_preview(final_png, preview_path, max_height=2000)

        print("\n" + "="*50)
        print("COMPLETE!")
        print("="*50)
        print(f"Final PNG: {final_png}")
        print(f"Final PDF: {final_pdf}")
        print(f"Preview: {preview_path}")

        return final_png

    return None


if __name__ == "__main__":
    # 샘플 상세페이지 생성
    result = generate_landing_page(
        brief=None,  # 샘플 사용
        output_dir="output",
        skip_generation=False  # 실제 생성
    )

    if result:
        print(f"\nSuccess! Check: {result}")
    else:
        print("\nFailed to generate landing page")
