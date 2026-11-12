# All Mapmodes Selector (EU5 Mod)

[English](README.md) | [Deutsch](README_DE.md) | [Español](README_ES.md) | [Français](README_FR.md) | [日本語](README_JA.md) | [한국어](README_KO.md) | **Polski** | [Português (Brasil)](README_PT.md) | [Русский](README_RU.md) | [Türkçe](README_TR.md) | [简体中文](README_ZH.md)

Mod ulepszający interfejs dla gry Europa Universalis V (EU5 / Project Caesar).  
Zapewnia szybki dostęp za jednym kliknięciem myszy do wszystkich **119 grywalnych trybów mapy** za pośrednictwem skategoryzowanego menu w prawym dolnym rogu HUD.

---

## Główne cechy i usprawnienia

1. **Pełne pokrycie wszystkich 119 trybów mapy (Naprawa braków z wersji podstawowej)**
   - Odblokowuje i przywraca tryby mapy, które były pominięte lub niedostępne w interfejsie podstawowym:
     - `government`: `timeline_ownership` (Oś czasu własności / Kronika - Grupa 99)
     - `geography`: `expeditions` (Ekspedycje - Grupa 4)
     - `geography`: `rivers` (Dedykowany przycisk trybu mapy rzek)
2. **Układ 2-kolumnowy (Koniec z uciążliwym przewijaniem)**
   - Kategorie o dużej liczbie pozycji (Ekonomia 26, Demografia 19, Populacja 17, Dyplomacja 16, Geografia 16) zostały zoptymalizowane w **przejrzyste układy 2-kolumnowe**.
   - Eliminuje problem ucinania menu na dole ekranu, umożliwiając natychmiastowy podgląd i wybór bez zasłaniania widoku gry.
3. **Zgodność ze stylem podstawowym i obsługa wielu języków**
   - Wierne zachowanie oryginalnego stylu: faktury pergaminu, złote obramowania, oficjalne ikony oraz czcionki.
   - Nazwy trybów mapy i podpowiedzi (tooltips) automatycznie dopasowują się do oficjalnego języka gry.

---

## Lista trybów mapy (Łącznie 119)

| Kategoria | Liczba | Układ | Główne tryby mapy |
|---|---|---|---|
| **Economy (Ekonomia)** | **26** | 2 kolumny | Baza podatkowa, Rozwój, Dobrobyt, Miasta, Surowce, Żywność, Kontrola, Bliskość, Drogi, Rynki, Dostęp do rynku itp. |
| **Demography (Demografia)** | **19** | 2 kolumny | Kultura państwowa, Kultura lokalna, Język, Język liturgiczny, Religia państwowa, Religia lokalna, Miejsca święte, Piśmienność, Instytucje itp. |
| **Population (Populacja/Stany)** | **17** | 2 kolumny | Zadowolenie, Łączna populacja, Typy POP, Proporcje stanów (Szlachta, Mieszczanie, Robotnicy, Chłopi, Żołnierze), Migracja, Niepokoje itp. |
| **Diplomacy (Dyplomacja)** | **16** | 2 kolumny | Relacje dyplomatyczne, Nastawienie, Postawa AI, Wielkie mocarstwa, Wojny, Koalicje, Rozejmy, Cele podbojów AI itp. |
| **Geography (Geografia/Ukształtowanie)** | **16** | 2 kolumny | Lokacje, Prowincje, Obszary, Regiony, Kontynenty, Topografia, Roślinność, Klimat, Zima, Rzeki, Ekspedycje itp. |
| **Government (Rząd/Władza)** | **13** | 1 kolumna | Polityka, Forma rządu, Ranga państwa, Dynastie, Język dworski, Integracja, Stabilność, Postęp, Oś czasu posiadania itp. |
| **Geopolitics (Geopolityka/Morze)** | **7** | 1 kolumna | Epidemie, Strefy morskie, Naturalne przystanie, Przepustowość portów, Zasięg morski, Kaperstwo, Kolonie |
| **Military (Wojskowość)** | **5** | 1 kolumna | Taktyka, Twierdze, Zaopatrzenie, Dostęp wojskowy, Wynik wojenny |

*Uwaga: Wykluczono 5 trybów czysto debugowych oraz 51 trybów silnikowych (`category = hidden`).*

---

## Struktura katalogów

```text
all-mapmodes-selector/
├── metadata.json              # Plik deskryptora moda (Tag Interface / v1.*)
├── README.md                  # Dokumentacja (Angielski)
├── README_JA.md               # Dokumentacja (Japoński)
├── README_PL.md               # Dokumentacja (Polski)
├── in_game/
│   ├── gui/
│   │   └── hud_bot.gui        # Zoptymalizowane GUI wyboru trybów mapy
│   └── localization/
│       ├── english/           # Angielska lokalizacja
│       └── japanese/          # Japońska lokalizacja
└── tools/
    ├── extract_mapmodes.py    # Skrypt do ekstrakcji trybów mapy
    └── playable_mapmodes.json # Wyodrębnione dane (119 wpisów)
```

---

## Instalacja (Mod lokalny)

Utwórz dowiązanie symboliczne lub skopiuj folder `all-mapmodes-selector` do katalogu modów EU5 (zazwyczaj `~/Documents/Paradox Interactive/Europa Universalis V/mod/` lub `~/Library/Application Support/Paradox Interactive/Europa Universalis V/mod/`).

```bash
# Przykład: Utworzenie dowiązania w katalogu Documents
mkdir -p "$HOME/Documents/Paradox Interactive/Europa Universalis V/mod"
ln -s "/Users/lencon/games/EU5mod/all-mapmodes-selector" "$HOME/Documents/Paradox Interactive/Europa Universalis V/mod/all-mapmodes-selector"
```

Następnie aktywuj **All Mapmodes Selector** w swoim zestawie (Playset) w Paradox Launcher i uruchom grę.
