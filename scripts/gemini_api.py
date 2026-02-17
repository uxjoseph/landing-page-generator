"""
Gemini API를 사용하여 상세페이지 섹션 이미지를 생성하는 모듈
Gemini 3 Pro Image Preview 모델 사용
"""

import os
import json
import base64
import time
from pathlib import Path
from typing import Optional
import requests
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini 3 Pro Image Preview 모델 (Nano Banana Pro)
MODEL_NAME = "gemini-3-pro-image-preview"
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent"


def generate_image(
    prompt: str,
    output_path: str,
    width: int = 1200,
    height: int = 1200
) -> Optional[str]:
    """
    Gemini API를 사용하여 이미지를 생성합니다.

    Args:
        prompt: 이미지 생성 프롬프트
        output_path: 저장할 파일 경로
        width: 이미지 너비
        height: 이미지 높이

    Returns:
        저장된 파일 경로 또는 None (실패시)
    """
    if not GEMINI_API_KEY:
        print("Error: GEMINI_API_KEY not found in .env")
        return None

    # 프롬프트에 크기 정보 및 울트라 리얼리스틱 스타일 강제 추가
    full_prompt = f"""Generate a PHOTOREALISTIC professional image.

=== ABSOLUTE DIMENSION REQUIREMENTS ===
1. EXACT SIZE: {width}x{height} pixels - NO EXCEPTIONS
2. FULL BLEED: Content fills ENTIRE {width}x{height} canvas with NO margins
3. DIMENSION LOCK: Output MUST be exactly {width}x{height} pixels

=== ULTRA-REALISTIC PHOTOGRAPHY STYLE (CRITICAL - MUST FOLLOW) ===

CAMERA QUALITY:
- Shot on professional DSLR (Canon 5D Mark IV / Sony A7R IV quality)
- High resolution, sharp details, professional color grading
- Natural depth of field with beautiful bokeh where appropriate

HUMAN MODELS (when showing people):
- REAL Korean models with NATURAL skin texture
- Visible pores, subtle skin details - NOT airbrushed plastic look
- Professional makeup with glass-skin/dewy finish
- Natural expressions, NOT AI-generated uncanny valley faces
- Individual hair strands visible, professionally styled

PRODUCT PHOTOGRAPHY:
- Luxury cosmetic brand quality
- Realistic reflections, refractions, material textures
- Touchable cream/gel textures
- Accurate glass/plastic light behavior

LIGHTING:
- Professional studio lighting with soft diffusion
- Natural shadows and highlights
- Rim lighting for skin glow effects

STYLE REFERENCE:
- Amorepacific, Sulwhasoo, Laneige flagship advertising
- Vogue Korea beauty editorial
- High-end department store imagery

ABSOLUTELY AVOID:
- Cartoon, illustration, vector art, or graphic design style
- Flat colors or digital art look
- Overly smooth, plastic-looking skin
- Generic stock photo feel
- AI-generated artifacts

=== CONTENT ===
{prompt}

=== FINAL QUALITY CHECKLIST ===
✓ Image is EXACTLY {width}x{height} pixels
✓ Looks like a REAL photograph, not digital art
✓ Skin has realistic texture with visible pores
✓ Lighting creates natural shadows and highlights
✓ Could be mistaken for actual brand advertisement
✓ Korean text is elegant and perfectly readable"""

    headers = {
        "Content-Type": "application/json"
    }

    # Gemini 이미지 생성 API 형식
    payload = {
        "contents": [{
            "parts": [{
                "text": full_prompt
            }]
        }],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"]
        }
    }

    try:
        print(f"Calling API: {MODEL_NAME}")
        response = requests.post(
            f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
            headers=headers,
            json=payload,
            timeout=180  # 3분 타임아웃
        )

        if response.status_code != 200:
            print(f"Error: API returned status {response.status_code}")
            error_text = response.text[:500] if len(response.text) > 500 else response.text
            print(f"Response: {error_text}")
            return None

        result = response.json()

        # 응답에서 이미지 데이터 추출
        candidates = result.get("candidates", [])
        if not candidates:
            print("Error: No candidates in response")
            print(f"Full response: {json.dumps(result, indent=2)[:1000]}")
            return None

        parts = candidates[0].get("content", {}).get("parts", [])

        for part in parts:
            if "inlineData" in part:
                image_data = part["inlineData"]["data"]
                mime_type = part["inlineData"].get("mimeType", "image/png")
                image_bytes = base64.b64decode(image_data)

                # 디렉토리 생성
                Path(output_path).parent.mkdir(parents=True, exist_ok=True)

                with open(output_path, "wb") as f:
                    f.write(image_bytes)

                print(f"Image saved: {output_path} ({mime_type})")
                return output_path

        # 이미지가 없으면 텍스트 응답 확인
        for part in parts:
            if "text" in part:
                print(f"Text response: {part['text'][:200]}")

        print("Error: No image data in response")
        return None

    except requests.exceptions.Timeout:
        print("Error: Request timed out (180s)")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: Request failed - {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return None


def generate_all_sections(
    prompts_file: str,
    output_dir: str,
    delay_between: float = 2.0
) -> list:
    """
    모든 섹션 이미지를 순차적으로 생성합니다.

    Args:
        prompts_file: gemini_prompts.json 파일 경로
        output_dir: 출력 디렉토리
        delay_between: API 호출 간 대기 시간 (초)

    Returns:
        생성된 이미지 경로 리스트
    """
    with open(prompts_file, "r", encoding="utf-8") as f:
        prompts_data = json.load(f)

    generated_images = []
    total_sections = len(prompts_data)

    for i, (section_key, section_data) in enumerate(prompts_data.items(), 1):
        print(f"\n[{i}/{total_sections}] Generating {section_key}...")

        prompt = section_data["prompt"]
        width = section_data.get("width", 1200)
        height = section_data.get("height", 600)
        filename = section_data.get("filename", f"{section_key}.png")

        output_path = os.path.join(output_dir, filename)

        result = generate_image(prompt, output_path, width, height)

        if result:
            generated_images.append(result)
        else:
            print(f"Warning: Failed to generate {section_key}")

        # API 레이트 리밋 방지를 위한 대기
        if i < total_sections:
            print(f"Waiting {delay_between}s before next request...")
            time.sleep(delay_between)

    print(f"\nGeneration complete: {len(generated_images)}/{total_sections} images")
    return generated_images


def test_api_connection() -> bool:
    """
    API 연결을 테스트합니다.
    """
    if not GEMINI_API_KEY:
        print("Error: GEMINI_API_KEY not found")
        return False

    print(f"API Key found: {GEMINI_API_KEY[:10]}...")

    # 간단한 텍스트 생성으로 연결 테스트
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{
            "parts": [{"text": "Say 'API connection successful' in Korean."}]
        }]
    }

    try:
        response = requests.post(
            f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
            headers=headers,
            json=payload,
            timeout=30
        )

        if response.status_code == 200:
            print("API connection successful!")
            return True
        else:
            print(f"API test failed: {response.status_code}")
            print(response.text)
            return False

    except Exception as e:
        print(f"API test error: {e}")
        return False


if __name__ == "__main__":
    # API 연결 테스트
    print("Testing Gemini API connection...")
    test_api_connection()
