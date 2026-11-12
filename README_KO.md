# All Mapmodes Selector (EU5 Mod)

[English](README.md) | [Deutsch](README_DE.md) | [Español](README_ES.md) | [Français](README_FR.md) | [日本語](README_JA.md) | **한국어** | [Polski](README_PL.md) | [Português (Brasil)](README_PT.md) | [Русский](README_RU.md) | [Türkçe](README_TR.md) | [简体中文](README_ZH.md)

유로파 유니버셜리스 5(Europa Universalis V / Project Caesar)용 맵 모드 확장 모드입니다.  
화면 우하단 HUD의 카테고리별 메뉴를 통해 일반 플레이에 필요한 **총 119종의 맵 모드**를 마우스 원클릭으로 빠르게 전환할 수 있는 UI를 제공합니다.

---

## 주요 특징 및 개선 사항

1. **플레이 가능한 119종 전 맵 모드 완벽 지원 (바닐라 누락 해결)**
   - 바닐라 UI에서 선택할 수 없거나 누락되었던 맵 모드를 모두 복구 및 등록:
     - `government`: `timeline_ownership` (영유권 타임라인/연대기 - Group 99)
     - `geography`: `expeditions` (탐험 원정 - Group 4)
     - `geography`: `rivers` (하천 전용 맵 모드 버튼)
2. **2열(2컬럼) 그리드 레이아웃 (스크롤 피로감 해소)**
   - 항목 수가 많은 카테고리(경제 26종, 인구 통계 19종, 계층/인구 17종, 외교 16종, 지리 16종)를 **좌우 2열 컬럼 레이아웃**으로 최적화.
   - 메뉴가 너무 길어져 화면 아래로 잘리는 문제를 해결하여, **화면을 가리지 않고 모든 항목을 한눈에 확인하고 클릭**할 수 있습니다.
3. **바닐라 고유 디자인 및 다국어 완벽 호환**
   - 바닐라의 양피지 질감, 금색 테두리 배너, 공식 아이콘 및 폰트 스타일을 충실하게 계승.
   - 맵 모드 명칭 및 툴팁은 게임의 공식 현지화(한국어, 영어 등 모든 언어)가 자동으로 적용됩니다.

---

## 수록 맵 모드 목록 (총 119종)

| 카테고리 | 개수 | 구성 | 주요 수록 맵 모드 |
|---|---|---|---|
| **Economy (경제)** | **26** | 2열 | 과세 기반, 개발도, 번영도, 도시, 원자재, 식량, 통제력, 접근성, 도로, 시장, 시장 접근 등 |
| **Demography (인구통계/문화·종교)** | **19** | 2열 | 국가 문화, 지역 문화, 언어, 전례 언어, 국교, 지역 종교, 성지, 문해율, 제도(Institution) 등 |
| **Population (계층/인구)** | **17** | 2열 | 만족도, 총인구, POP 유형, 계층별 비율·분포(귀족/시민/노동자/농민/군인), 이주, 불안 등 |
| **Diplomacy (외교)** | **16** | 2列 | 외교 관계, 태도, AI 성향, 열강, 전쟁, 대프랑스/대동맹, 휴전, AI 정복 욕망 등 |
| **Geography (지리/지형)** | **16** | 2열 | 로케이션, 프로빈스, 에어리어, 리전, 대륙, 지형, 식생, 기후, 겨울, 하천, 탐험 등 |
| **Government (국가/통치)** | **13** | 1열 | 정치, 정부 형태, 국가 등급, 왕조, 궁정 언어, 통합도, 안정도, 진보, 영유권 타임라인 등 |
| **Geopolitics (지정학/해양)** | **7** | 1열 | 전염병, 해양, 천연 양항 적합도, 항만 수용력, 항속 거리, 사략, 식민지 |
| **Military (군사)** | **5** | 1열 | 전술, 요새, 보급, 군사 통행권, 승점 |

*참고: 디버그 전용 5종 및 엔진 내부 처리 전용 51종(`category = hidden`)은 제외되었습니다.*

---

## 디렉토리 구조

```text
all-mapmodes-selector/
├── metadata.json              # 모드 메타데이터 파일 (Interface 태그 / v1.*)
├── README.md                  # 모드 설명서 (영어)
├── README_JA.md               # 모드 설명서 (일본어)
├── README_ZH.md               # 모드 설명서 (간체 중국어)
├── README_KO.md               # 모드 설명서 (한국어)
├── in_game/
│   ├── gui/
│   │   └── hud_bot.gui        # 최적화된 맵 모드 셀렉터 GUI
│   └── localization/
│       ├── english/           # 영어 텍스트
│       └── japanese/          # 일본어 텍스트
└── tools/
    ├── extract_mapmodes.py    # 맵 모드 추출 스크립트
    └── playable_mapmodes.json # 추출 데이터 (119건)
```

---

## 설치 방법 (로컬 모드)

본 모드 폴더 `all-mapmodes-selector`의 바로가기(심볼릭 링크) 또는 복사본을 EU5 모드 경로(통상 `~/Documents/Paradox Interactive/Europa Universalis V/mod/` 또는 `~/Library/Application Support/Paradox Interactive/Europa Universalis V/mod/`)에 배치하세요.

```bash
# 예시: Documents 경로에 심볼릭 링크 생성
mkdir -p "$HOME/Documents/Paradox Interactive/Europa Universalis V/mod"
ln -s "/Users/lencon/games/EU5mod/all-mapmodes-selector" "$HOME/Documents/Paradox Interactive/Europa Universalis V/mod/all-mapmodes-selector"
```

이후 Paradox Launcher의 플레이셋(Playset)에서 **All Mapmodes Selector**를 활성화하고 게임을 실행하면 됩니다.
