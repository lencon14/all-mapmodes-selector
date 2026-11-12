# All Mapmodes Selector (EU5 Mod)

**English** | [Deutsch](README_DE.md) | [Español](README_ES.md) | [Français](README_FR.md) | [日本語](README_JA.md) | [한국어](README_KO.md) | [Polski](README_PL.md) | [Português (Brasil)](README_PT.md) | [Русский](README_RU.md) | [Türkçe](README_TR.md) | [简体中文](README_ZH.md)

An interface enhancement mod for Europa Universalis V (EU5 / Project Caesar).  
Provides fast, one-click mouse access to all **119 playable mapmodes** through organized categorized menus in the bottom-right HUD.

---

## Key Features

1. **Complete Coverage of All 119 Playable Mapmodes (Fixing Vanilla Omissions)**
   - Unlocks and restores mapmodes that were previously missing or inaccessible in vanilla:
     - `government`: `timeline_ownership` (Timeline Ownership / Chronicle - Group 99)
     - `geography`: `expeditions` (Expeditions - Group 4)
     - `geography`: `rivers` (Dedicated river mapmode button)
2. **2-Column Layout (Eliminating Scroll Fatigue)**
   - High-density categories (Economy: 26, Demography: 19, Population: 17, Diplomacy: 16, Geography: 16) are rendered in a clean **two-column layout**.
   - Solves the vertical cutoff issue without blocking screen space, allowing you to see and pick any mapmode at a glance.
3. **Faithful Vanilla Aesthetic & Full Multi-Language Support**
   - Seamlessly matches the vanilla style: parchment texture, gold framing, official icons, and native typography.
   - Mapmode names and tooltips automatically use the official in-game localizations for all supported languages (English, Japanese, etc.).

---

## Included Mapmodes (119 Total)

| Category | Count | Layout | Key Mapmodes Included |
|---|---|---|---|
| **Economy** | **26** | 2 Columns | Tax Base, Development, Prosperity, Cities, Raw Materials, Food, Control, Proximity, Roads, Markets, Market Access, etc. |
| **Demography** | **19** | 2 Columns | Country Culture, Local Culture, Language, Liturgical Language, State Religion, Local Religion, Holy Sites, Literacy, Institutions, etc. |
| **Population** | **17** | 2 Columns | Satisfaction, Population, POP Types, POP Ratios (Nobles, Burghers, Laborers, Peasants, Soldiers), Migration, Unrest, etc. |
| **Diplomacy** | **16** | 2 Columns | Diplomatic Relations, Attitude, AI Stance, Great Powers, Wars, Coalitions, Truces, AI Conquest Desires, etc. |
| **Geography** | **16** | 2 Columns | Locations, Provinces, Areas, Regions, Continents, Topography, Vegetation, Climate, Winter, Rivers, Expeditions, etc. |
| **Government** | **13** | 1 Column | Politics, Government Type, Country Rank, Dynasties, Court Language, Integration, Stability, Progress, Timeline Ownership, etc. |
| **Geopolitics** | **7** | 1 Column | Epidemics, Maritime, Natural Harbors, Harbor Capacity, Naval Range, Privateering, Colonies |
| **Military** | **5** | 1 Column | Tactics, Forts, Supply, Military Access, War Score |

*Note: 5 debug-only mapmodes and 51 internal engine mapmodes (`category = hidden`) are excluded.*

---

## Directory Structure

```text
all-mapmodes-selector/
├── metadata.json              # Mod descriptor file (Interface tag / v1.*)
├── README.md                  # Mod documentation (English)
├── README_JA.md               # Mod documentation (Japanese)
├── in_game/
│   ├── gui/
│   │   └── hud_bot.gui        # Optimized mapmode selector GUI
│   └── localization/
│       ├── english/           # English localization
│       └── japanese/          # Japanese localization
└── tools/
    ├── extract_mapmodes.py    # Mapmode extraction script
    └── playable_mapmodes.json # Extracted data (119 entries)
```

---

## Installation (Local Mod)

Place a symbolic link or copy the `all-mapmodes-selector` folder into your EU5 user mod directory (typically `~/Documents/Paradox Interactive/Europa Universalis V/mod/` or `~/Library/Application Support/Paradox Interactive/Europa Universalis V/mod/`).

```bash
# Example: Create a symlink under Documents
mkdir -p "$HOME/Documents/Paradox Interactive/Europa Universalis V/mod"
ln -s "/Users/lencon/games/EU5mod/all-mapmodes-selector" "$HOME/Documents/Paradox Interactive/Europa Universalis V/mod/all-mapmodes-selector"
```

Then, enable **All Mapmodes Selector** in your playset via the Paradox Launcher and launch the game.
