# All Mapmodes Selector (EU5 Mod)

[English](README.md) | [日本語](README_JA.md) | [简体中文](README_ZH.md) | [한국어](README_KO.md) | [Français](README_FR.md) | **Deutsch** | [Español](README_ES.md) | [Português](README_PT.md) | [Русский](README_RU.md) | [Polski](README_PL.md) | [Türkçe](README_TR.md)

Eine Interface-Erweiterungs-Mod für Europa Universalis V (EU5 / Project Caesar).  
Ermöglicht schnellen Ein-Klick-Zugriff auf alle **119 spielbaren Kartenmodi** über übersichtliche Kategorienmenüs in der HUD-Leiste unten rechts.

---

## Hauptmerkmale & Verbesserungen

1. **Vollständige Abdeckung aller 119 spielbaren Kartenmodi (Vanilla-Lücken behoben)**
   - Schaltet zuvor unzugängliche oder vergessene Kartenmodi frei:
     - `government`: `timeline_ownership` (Besitzchronik / Zeitleiste - Gruppe 99)
     - `geography`: `expeditions` (Expeditionen - Gruppe 4)
     - `geography`: `rivers` (Eigene Schaltfläche für Fluss-Kartenmodus)
2. **2-Spalten-Layout (Kein endloses Scrollen mehr)**
   - Umfangreiche Kategorien (Wirtschaft 26, Demografie 19, Bevölkerung 17, Diplomatie 16, Geografie 16) werden in **übersichtlichen 2-Spalten-Gittern** dargestellt.
   - Verhindert übermäßig lange Menüs, die über den Bildschirmrand hinausgehen. Alle Modi sind auf einen Blick sichtbar, ohne das Spielfeld zu verdecken.
3. **Stimmiges Vanilla-Design & Mehrsprachigkeit**
   - Treu dem originalen Look: Pergamenttexturen, goldene Rahmen, offizielle Symbole und Originalschriften.
   - Namen und Tooltips der Kartenmodi passen sich automatisch der offiziellen Spracheinstellung Ihres Spiels an.

---

## Enthaltene Kartenmodi (119 gesamt)

| Kategorie | Anzahl | Layout | Wichtige enthaltene Kartenmodi |
|---|---|---|---|
| **Economy (Wirtschaft)** | **26** | 2 Spalten | Steuerbasis, Entwicklung, Wohlstand, Städte, Rohstoffe, Nahrung, Kontrolle, Nähe, Straßen, Märkte, Marktzugang etc. |
| **Demography (Demografie)** | **19** | 2 Spalten | Staatskultur, Lokale Kultur, Sprache, Liturgiesprache, Staatsreligion, Lokale Religion, Heilige Stätten, Alphabetisierung, Institutionen etc. |
| **Population (Bevölkerung)** | **17** | 2 Spalten | Zufriedenheit, Gesamtbevölkerung, POP-Typen, Ständeverteilung (Adel, Bürger, Arbeiter, Bauern, Soldaten), Migration, Unruhe etc. |
| **Diplomacy (Diplomatie)** | **16** | 2 Spalten | Diplomatische Beziehungen, Einstellung, KI-Haltung, Großmächte, Kriege, Koalitionen, Waffenstillstände, KI-Eroberungslust etc. |
| **Geography (Geografie)** | **16** | 2 Spalten | Standorte, Provinzen, Gebiete, Regionen, Kontinente, Topografie, Vegetation, Klima, Winter, Flüsse, Expeditionen etc. |
| **Government (Regierung)** | **13** | 1 Spalte | Politik, Regierungsform, Rang, Dynastien, Hofsprache, Integration, Stabilität, Fortschritt, Besitz-Zeitleiste etc. |
| **Geopolitics (Geopolitik/Meer)** | **7** | 1 Spalte | Seuchen, Meeresgebiete, Naturhäfen, Hafenkapazität, Reichweite, Kaperfahrt, Kolonien |
| **Military (Militär)** | **5** | 1 Spalte | Taktik, Festungen, Nachschub, Militärischer Zugang, Kriegspunkte |

*Hinweis: 5 reine Debug-Kartenmodi und 51 spielinterne Modi (`category = hidden`) wurden ausgeschlossen.*

---

## Verzeichnisstruktur

```text
all-mapmodes-selector/
├── metadata.json              # Mod-Beschreibungsdatei (Interface-Tag / v1.0.0)
├── README.md                  # Dokumentation (Englisch)
├── README_JA.md               # Dokumentation (Japanisch)
├── README_DE.md               # Dokumentation (Deutsch)
├── in_game/
│   ├── gui/
│   │   └── hud_bot.gui        # Optimierte Kartenmodus-Auswahl-GUI
│   └── localization/
│       ├── english/           # Englische Lokalisierung
│       └── japanese/          # Japanische Lokalisierung
└── tools/
    ├── extract_mapmodes.py    # Skript zur Extraktion der Kartenmodi
    └── playable_mapmodes.json # Extrahierte Daten (119 Einträge)
```

---

## Installation (Lokale Mod)

Erstellen Sie einen symbolischen Link oder kopieren Sie den Ordner `all-mapmodes-selector` in das Mod-Verzeichnis von EU5 (üblicherweise `~/Documents/Paradox Interactive/Europa Universalis V/mod/` oder `~/Library/Application Support/Paradox Interactive/Europa Universalis V/mod/`).

```bash
# Beispiel: Symlink im Documents-Ordner erstellen
mkdir -p "$HOME/Documents/Paradox Interactive/Europa Universalis V/mod"
ln -s "/Users/lencon/games/EU5mod/all-mapmodes-selector" "$HOME/Documents/Paradox Interactive/Europa Universalis V/mod/all-mapmodes-selector"
```

Aktivieren Sie anschließend **All Mapmodes Selector** im Playset des Paradox Launchers und starten Sie das Spiel.
