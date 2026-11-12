#!/usr/bin/env python3
import json
import re

GAME_PATH = "/Users/lencon/games/EU5/pipeline/game/game"
MAP_MODES_FILE = f"{GAME_PATH}/in_game/gfx/map/map_modes/map_modes.txt"
OUTPUT_JSON = "/Users/lencon/games/EU5mod/all-mapmodes-selector/tools/playable_mapmodes.json"

def main():
    with open(MAP_MODES_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    lines = text.split("\n")
    entries = []
    current_key = None
    current_body = []
    brace_count = 0

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if brace_count == 0:
            m = re.match(r"^([a-zA-Z0-9_]+)\s*=\s*\{", stripped)
            if m:
                current_key = m.group(1)
                brace_count += stripped.count("{") - stripped.count("}")
                current_body = [line]
                if brace_count == 0:
                    entries.append((current_key, "\n".join(current_body)))
                    current_key = None
            continue
        else:
            brace_count += stripped.count("{") - stripped.count("}")
            current_body.append(line)
            if brace_count == 0:
                entries.append((current_key, "\n".join(current_body)))
                current_key = None

    valid_categories = [
        "economy",
        "demography",
        "population",
        "diplomacy",
        "geography",
        "government",
        "geopolitics",
        "military"
    ]

    playable_modes = []

    for key, body in entries:
        cat_match = re.search(r"category\s*=\s*([a-zA-Z0-9_]+)", body)
        cat = cat_match.group(1) if cat_match else "NONE"
        if cat in valid_categories:
            # find icon or other attributes if present
            icon_match = re.search(r"icon\s*=\s*\"([^\"]+)\"", body)
            icon = icon_match.group(1) if icon_match else None
            playable_modes.append({
                "key": key,
                "category": cat,
                "icon": icon
            })

    print(f"Extracted {len(playable_modes)} playable mapmodes across {len(valid_categories)} categories.")
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(playable_modes, f, indent=2, ensure_ascii=False)
    print(f"Saved to {OUTPUT_JSON}")

if __name__ == "__main__":
    main()
