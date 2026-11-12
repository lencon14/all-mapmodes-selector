# All Mapmodes Selector (EU5 Mod)

[English](README.md) | [Deutsch](README_DE.md) | **Español** | [Français](README_FR.md) | [日本語](README_JA.md) | [한국어](README_KO.md) | [Polski](README_PL.md) | [Português (Brasil)](README_PT.md) | [Русский](README_RU.md) | [Türkçe](README_TR.md) | [简体中文](README_ZH.md)

Un mod de mejora de interfaz para Europa Universalis V (EU5 / Project Caesar).  
Ofrece acceso rápido y con un solo clic a los **119 modos de mapa jugables** a través de menús clasificados en el HUD inferior derecho.

---

## Características principales y mejoras

1. **Cobertura total de los 119 modos de mapa (Corrige omisiones del juego base)**
   - Desbloquea y recupera los modos de mapa no seleccionables en la interfaz original:
     - `government`: `timeline_ownership` (Cronología de posesiones / Historial - Grupo 99)
     - `geography`: `expeditions` (Expediciones - Grupo 4)
     - `geography`: `rivers` (Botón dedicado para el modo de mapa de ríos)
2. **Diseño en 2 columnas (Adiós a los desplazamientos interminables)**
   - Las categorías con muchas opciones (Economía 26, Demografía 19, Población 17, Diplomacia 16, Geografía 16) se han optimizado en **cuadrículas de 2 columnas**.
   - Evita menús verticales excesivamente largos que sobresalen de la pantalla, permitiendo ver y seleccionar todo de un vistazo sin obstaculizar la vista de juego.
3. **Estilo original de Paradox y compatibilidad multilingüe**
   - Fiel al diseño original: textura de pergamino, bordes dorados, iconos oficiales y tipografía nativa.
   - Los nombres y descripciones emergentes (tooltips) adoptan automáticamente las traducciones oficiales del juego.

---

## Modos de mapa incluidos (119 en total)

| Categoría | Total | Formato | Modos de mapa destacados |
|---|---|---|---|
| **Economy (Economía)** | **26** | 2 columnas | Base fiscal, Desarrollo, Prosperidad, Ciudades, Materias primas, Alimentos, Control, Proximidad, Caminos, Mercados, Acceso a mercados, etc. |
| **Demography (Demografía)** | **19** | 2 columnas | Cultura nacional, Cultura local, Idioma, Lengua litúrgica, Religión de estado, Religión local, Sitios sagrados, Alfabetización, Instituciones, etc. |
| **Population (Población/Clases)** | **17** | 2 columnas | Satisfacción, Población total, Tipos de POP, Proporciones de clases (Nobles, Burgueses, Obreros, Campesinos, Soldados), Migración, Malestar, etc. |
| **Diplomacy (Diplomacia)** | **16** | 2 columnas | Relaciones diplomáticas, Actitud, Postura de la IA, Grandes potencias, Guerras, Coaliciones, Treguas, Deseos de conquista de la IA, etc. |
| **Geography (Geografía/Relieve)** | **16** | 2 columnas | Localizaciones, Provincias, Áreas, Regiones, Continentes, Topografía, Vegetación, Clima, Invierno, Ríos, Expediciones, etc. |
| **Government (Gobierno/Estado)** | **13** | 1 columna | Política, Forma de gobierno, Rango de país, Dinastías, Idioma de la corte, Integración, Estabilidad, Progreso, Cronología, etc. |
| **Geopolitics (Geopolítica/Mar)** | **7** | 1 columna | Epidemias, Zonas marítimas, Puertos naturales, Capacidad portuaria, Alcance naval, Corso, Colonias |
| **Military (Militar)** | **5** | 1 columna | Tácticas, Fuertes, Suministros, Acceso militar, Puntuación de guerra |

*Nota: Se excluyen 5 modos de mapa exclusivos de depuración y 51 modos internos (`category = hidden`).*

---

## Estructura de carpetas

```text
all-mapmodes-selector/
├── metadata.json              # Descriptor del mod (Etiqueta Interface / v1.0.0)
├── README.md                  # Documentación (Inglés)
├── README_JA.md               # Documentación (Japonés)
├── README_ES.md               # Documentación (Español)
├── in_game/
│   ├── gui/
│   │   └── hud_bot.gui        # Interfaz optimizada del selector de modos de mapa
│   └── localization/
│       ├── english/           # Textos en inglés
│       └── japanese/          # Textos en japonés
└── tools/
    ├── extract_mapmodes.py    # Script de extracción de modos de mapa
    └── playable_mapmodes.json # Datos extraídos (119 registros)
```

---

## Instalación (Mod local)

Coloca un enlace simbólico o copia la carpeta `all-mapmodes-selector` en el directorio de mods de EU5 (generalmente `~/Documents/Paradox Interactive/Europa Universalis V/mod/` o `~/Library/Application Support/Paradox Interactive/Europa Universalis V/mod/`).

```bash
# Ejemplo: Crear enlace simbólico en Documents
mkdir -p "$HOME/Documents/Paradox Interactive/Europa Universalis V/mod"
ln -s "/Users/lencon/games/EU5mod/all-mapmodes-selector" "$HOME/Documents/Paradox Interactive/Europa Universalis V/mod/all-mapmodes-selector"
```

Activa **All Mapmodes Selector** en el conjunto de mods (Playset) del Paradox Launcher y ejecuta el juego.
