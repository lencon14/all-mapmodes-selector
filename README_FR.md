# All Mapmodes Selector (EU5 Mod)

[English](README.md) | [日本語](README_JA.md) | [简体中文](README_ZH.md) | [한국어](README_KO.md) | **Français** | [Deutsch](README_DE.md) | [Español](README_ES.md) | [Português](README_PT.md) | [Русский](README_RU.md) | [Polski](README_PL.md) | [Türkçe](README_TR.md)

Un mod d'amélioration de l'interface pour Europa Universalis V (EU5 / Project Caesar).  
Offre un accès rapide en un clic à l'ensemble des **119 modes de carte jouables** via des menus organisés par catégorie dans le HUD en bas à droite.

---

## Fonctionnalités principales

1. **Prise en charge intégrale des 119 modes de carte (Correction des omissions vanilla)**
   - Débloque et réintègre les modes de carte manquants ou inaccessibles dans l'interface vanilla :
     - `government` : `timeline_ownership` (Chronologie des possessions / Historique - Groupe 99)
     - `geography` : `expeditions` (Expéditions - Groupe 4)
     - `geography` : `rivers` (Bouton dédié au mode de carte des fleuves)
2. **Disposition en 2 colonnes (Finis les défilements interminables)**
   - Les catégories denses (Économie 26, Démographie 19, Population 17, Diplomatie 16, Géographie 16) sont organisées en **grilles de 2 colonnes**.
   - Évite les menus trop hauts qui dépassent de l'écran, vous permettant de voir et sélectionner n'importe quel mode de carte d'un simple clic sans masquer votre vue de jeu.
3. **Harmonie esthétique vanilla et support multilingue**
   - Respecte fidèlement le style graphique vanilla : textures de parchemin, bordures dorées, icônes officielles et typographie originale.
   - Les noms des modes de carte et infobulles s'adaptent automatiquement à la langue officielle configurée dans votre jeu (français, anglais, etc.).

---

## Liste des modes de carte inclus (119 au total)

| Catégorie | Nombre | Disposition | Principaux modes de carte |
|---|---|---|---|
| **Economy (Économie)** | **26** | 2 colonnes | Base fiscale, Développement, Prospérité, Cités, Matières premières, Nourriture, Contrôle, Proximité, Routes, Marchés, Accès aux marchés, etc. |
| **Demography (Démographie)** | **19** | 2 colonnes | Culture nationale, Culture locale, Langue, Langue liturgique, Religion d'État, Religion locale, Lieux saints, Alphabétisation, Institutions, etc. |
| **Population (Classes/Populations)** | **17** | 2 colonnes | Satisfaction, Population totale, Types de POP, Ratios de classes (Nobles, Bourgeois, Ouvriers, Paysans, Soldats), Migration, Agitation, etc. |
| **Diplomacy (Diplomatie)** | **16** | 2 colonnes | Relations diplomatiques, Attitude, Posture IA, Grandes Puissances, Guerres, Coalitions, Trêves, Désirs de conquête IA, etc. |
| **Geography (Géographie/Relief)** | **16** | 2 colonnes | Localisations, Provinces, Zones, Régions, Continents, Topographie, Végétation, Climat, Hiver, Fleuves, Expéditions, etc. |
| **Government (Gouvernement/État)** | **13** | 1 colonne | Politique, Forme de gouvernement, Rang du pays, Dynasties, Langue de cour, Intégration, Stabilité, Progrès, Chronologie, etc. |
| **Geopolitics (Géopolitique/Mer)** | **7** | 1 colonne | Épidémies, Zones maritimes, Ports naturels, Capacité portuaire, Portée navale, Course, Colonies |
| **Military (Militaire)** | **5** | 1 colonne | Tactiques, Forts, Ravitaillement, Accès militaire, Score de guerre |

*Note : 5 modes de carte réservés au débogage et 51 modes internes (`category = hidden`) sont exclus.*

---

## Structure des dossiers

```text
all-mapmodes-selector/
├── metadata.json              # Fichier descripteur de mod (Tag Interface / v1.0.0)
├── README.md                  # Documentation (Anglais)
├── README_JA.md               # Documentation (Japonais)
├── README_FR.md               # Documentation (Français)
├── in_game/
│   ├── gui/
│   │   └── hud_bot.gui        # GUI optimisée du sélecteur de modes de carte
│   └── localization/
│       ├── english/           # Localisation anglaise
│       └── japanese/          # Localisation japonaise
└── tools/
    ├── extract_mapmodes.py    # Script d'extraction des modes de carte
    └── playable_mapmodes.json # Données extraites (119 entrées)
```

---

## Installation (Mod local)

Créez un lien symbolique ou copiez le dossier `all-mapmodes-selector` dans le répertoire des mods de votre jeu EU5 (généralement `~/Documents/Paradox Interactive/Europa Universalis V/mod/` ou `~/Library/Application Support/Paradox Interactive/Europa Universalis V/mod/`).

```bash
# Exemple : Création d'un lien symbolique dans Documents
mkdir -p "$HOME/Documents/Paradox Interactive/Europa Universalis V/mod"
ln -s "/Users/lencon/games/EU5mod/all-mapmodes-selector" "$HOME/Documents/Paradox Interactive/Europa Universalis V/mod/all-mapmodes-selector"
```

Activez ensuite **All Mapmodes Selector** dans votre ensemble de mods (Playset) sur le Paradox Launcher et lancez le jeu.
