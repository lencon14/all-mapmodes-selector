# All Mapmodes Selector (EU5 Mod)

[English](README.md) | [日本語](README_JA.md) | [简体中文](README_ZH.md) | [한국어](README_KO.md) | [Français](README_FR.md) | [Deutsch](README_DE.md) | [Español](README_ES.md) | **Português** | [Русский](README_RU.md) | [Polski](README_PL.md) | [Türkçe](README_TR.md)

Mod de aprimoramento de interface para Europa Universalis V (EU5 / Project Caesar).  
Fornece acesso rápido por clique do mouse a todos os **119 modos de mapa jogáveis** através de menus categorizados no HUD inferior direito.

---

## Principais Recursos e Melhorias

1. **Cobertura Completa de Todos os 119 Modos de Mapa Jogáveis (Correção de Omissões do Jogo Base)**
   - Desbloqueia e restaura modos de mapa que estavam inacessíveis na interface vanilla:
     - `government`: `timeline_ownership` (Cronologia de Posse / Linha do Tempo - Grupo 99)
     - `geography`: `expeditions` (Expedições - Grupo 4)
     - `geography`: `rivers` (Botão exclusivo para o modo de mapa fluvial)
2. **Layout em 2 Colunas (Sem Rolagens Intermináveis)**
   - Categorias com muitos itens (Economia 26, Demografia 19, População 17, Diplomacia 16, Geografia 16) são organizadas em **grades elegantes de 2 colunas**.
   - Evita menus excessivamente longos que ultrapassam a tela, permitindo visualizar e selecionar qualquer opção sem bloquear o campo de visão do jogo.
3. **Harmonia com o Design Original e Suporte Multilíngue**
   - Segue fielmente a estética original: textura de pergaminho, bordas douradas, ícones oficiais e fontes nativas.
   - Os nomes dos modos de mapa e tooltips utilizam automaticamente a localização oficial do seu jogo.

---

## Modos de Mapa Incluídos (119 no Total)

| Categoria | Total | Formato | Principais Modos de Mapa |
|---|---|---|---|
| **Economy (Economia)** | **26** | 2 colunas | Base Tributária, Desenvolvimento, Prosperidade, Cidades, Matérias-primas, Alimentos, Controle, Proximidade, Estradas, Mercados, Acesso a Mercados etc. |
| **Demography (Demografia)** | **19** | 2 colunas | Cultura Nacional, Cultura Local, Idioma, Língua Litúrgica, Religião de Estado, Religião Local, Locais Sagrados, Alfabetização, Instituições etc. |
| **Population (População/Classes)** | **17** | 2 colunas | Satisfação, População Total, Tipos de POP, Proporções de Classes (Nobres, Burgueses, Operários, Camponeses, Soldados), Migração, Agitação etc. |
| **Diplomacy (Diplomacia)** | **16** | 2 colunas | Relações Diplomáticas, Atitude, Postura da IA, Grandes Potências, Guerras, Coalizões, Tréguas, Desejos de Conquista da IA etc. |
| **Geography (Geografia/Relevo)** | **16** | 2 colunas | Localizações, Províncias, Áreas, Regiões, Continentes, Topografia, Vegetação, Clima, Inverno, Rios, Expedições etc. |
| **Government (Governo/Estado)** | **13** | 1 coluna | Política, Forma de Governo, Grau do País, Dinastias, Língua da Corte, Integração, Estabilidade, Progresso, Linha do Tempo etc. |
| **Geopolitics (Geopolítica/Mar)** | **7** | 1 coluna | Epidemias, Zonas Marítimas, Portos Naturais, Capacidade Portuária, Alcance Naval, Corso, Colônias |
| **Military (Militar)** | **5** | 1 coluna | Táticas, Fortalezas, Suprimento, Acesso Militar, Pontuação de Guerra |

*Nota: 5 modos de mapa exclusivos de depuração e 51 modos internos (`category = hidden`) foram excluídos.*

---

## Estrutura de Diretórios

```text
all-mapmodes-selector/
├── metadata.json              # Descritor do mod (Tag Interface / v1.0.0)
├── README.md                  # Documentação (Inglês)
├── README_JA.md               # Documentação (Japonês)
├── README_PT.md               # Documentação (Português)
├── in_game/
│   ├── gui/
│   │   └── hud_bot.gui        # Interface otimizada do seletor de mapas
│   └── localization/
│       ├── english/           # Localização em inglês
│       └── japanese/          # Localização em japonês
└── tools/
    ├── extract_mapmodes.py    # Script de extração de modos de mapa
    └── playable_mapmodes.json # Dados extraídos (119 registros)
```

---

## Instalação (Mod Local)

Crie um link simbólico ou copie a pasta `all-mapmodes-selector` para o diretório de mods do EU5 (normalmente `~/Documents/Paradox Interactive/Europa Universalis V/mod/` ou `~/Library/Application Support/Paradox Interactive/Europa Universalis V/mod/`).

```bash
# Exemplo: Criar symlink em Documents
mkdir -p "$HOME/Documents/Paradox Interactive/Europa Universalis V/mod"
ln -s "/Users/lencon/games/EU5mod/all-mapmodes-selector" "$HOME/Documents/Paradox Interactive/Europa Universalis V/mod/all-mapmodes-selector"
```

Em seguida, ative o **All Mapmodes Selector** no seu conjunto de mods (Playset) através do Inicializador da Paradox e abra o jogo.
