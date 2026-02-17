# 다이어그램 스타일 프리셋

## 색상 팔레트

| 역할 | 배경색 | 테두리색 | 용도 |
|------|--------|----------|------|
| 메인/오케스트레이터 | `#fff59d` | `#f9a825` | 🟡 노란색 - 전체 조율 |
| 기획팀/서브에이전트 | `#bbdefb` | `#1976d2` | 🔵 파란색 - 분석/리서치 |
| 카피팀/스킬 | `#c8e6c9` | `#388e3c` | 🟢 초록색 - 콘텐츠 생성 |
| 디자인팀/스킬 | `#ffe0b2` | `#f57c00` | 🟠 주황색 - 비주얼 |
| 개발팀/스킬+코드 | `#e1bee7` | `#8e24aa` | 🟣 보라색 - 기술 구현 |
| 스크립트/자동화 | `#d1c4e9` | `#512da8` | 🟣 연보라 - 실행 |
| 결과물/출력 | `#ffcdd2` | `#c62828` | 🔴 빨간색 - 최종 산출물 |

---

## Mermaid 기본 템플릿

```mermaid
flowchart TB
    %% 메인 노드
    MAIN["🎯 제목<br/>부제목"]

    %% 팀 노드 (병렬)
    MAIN --> TEAM1["📋 팀1<br/>역할<br/>───<br/>상세 내용"]
    MAIN --> TEAM2["✍️ 팀2<br/>역할<br/>───<br/>상세 내용"]

    %% 합류 노드
    TEAM1 --> MERGE["🤖 합류 지점<br/>───<br/>통합 작업"]
    TEAM2 --> MERGE

    %% 결과 노드
    MERGE --> OUTPUT["🖼️ 결과물<br/>───<br/>출력 스펙"]

    %% 스타일 적용
    style MAIN fill:#fff59d,stroke:#f9a825
    style TEAM1 fill:#bbdefb,stroke:#1976d2
    style TEAM2 fill:#c8e6c9,stroke:#388e3c
    style MERGE fill:#e1bee7,stroke:#8e24aa
    style OUTPUT fill:#ffcdd2,stroke:#c62828
```

---

## 상세페이지 생성기 전체 구조

```mermaid
flowchart TB
    A["🎯 상세페이지 자동 생성기<br/>클로드 코드 오케스트레이터"]

    A --> B["📋 기획팀<br/>서브에이전트<br/>───<br/>01-intake.md 입력수집<br/>02-research.md 리서치"]

    B --> C["✍️ 카피팀<br/>클로드 스킬<br/>───<br/>03-copy.md<br/>13섹션 카피 생성"]

    B --> D["🎨 디자인팀<br/>클로드 스킬<br/>───<br/>04-design.md<br/>스타일/컬러 결정"]

    C --> E["🤖 개발팀<br/>클로드 스킬 + 파이썬<br/>───<br/>05-prompt.md<br/>Gemini 프롬프트 13개"]

    D --> E

    E --> F["🐍 스크립트 실행<br/>───<br/>gemini_api.py<br/>stitch_images.py"]

    F --> G["🖼️ 최종 결과물<br/>───<br/>상세페이지 PNG/PDF<br/>1200px × 7000px"]

    style A fill:#fff59d,stroke:#f9a825
    style B fill:#bbdefb,stroke:#1976d2
    style C fill:#c8e6c9,stroke:#388e3c
    style D fill:#ffe0b2,stroke:#f57c00
    style E fill:#e1bee7,stroke:#8e24aa
    style F fill:#d1c4e9,stroke:#512da8
    style G fill:#ffcdd2,stroke:#c62828
```

---

## 노드 작성 규칙

### 1. 노드 내용 구조
```
["이모지 제목<br/>부제목<br/>───<br/>상세1<br/>상세2"]
```

### 2. 병렬 처리 표현
```mermaid
A --> B
A --> C
B --> D
C --> D
```
→ B와 C가 같은 줄에 배치되고 D에서 합류

### 3. 이모지 가이드
| 역할 | 이모지 |
|------|--------|
| 메인/시작 | 🎯 |
| 기획/분석 | 📋 📊 🔍 |
| 카피/콘텐츠 | ✍️ ✏️ 📝 |
| 디자인 | 🎨 🖌️ |
| 개발/기술 | 🤖 ⚙️ 💻 |
| 스크립트 | 🐍 🔧 |
| 결과물 | 🖼️ 📤 ✅ |

---

## 사용법

1. 이 파일의 템플릿 복사
2. 노드 내용 수정
3. Whimsical MCP로 생성:
```
mcp__whimsical__create_whimsical_diagram 호출
- title: 다이어그램 제목
- mermaid_markup: 위 코드 붙여넣기
```

---

## Whimsical 링크

- 최종 버전: https://whimsical.com/EHpEe9G1Fvk4CVeSqQqU55
