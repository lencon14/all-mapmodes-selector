# All Mapmodes Selector (EU5 Mod)

[English](README.md) | **日本語** | [简体中文](README_ZH.md) | [한국어](README_KO.md) | [Français](README_FR.md) | [Deutsch](README_DE.md) | [Español](README_ES.md) | [Português](README_PT.md) | [Русский](README_RU.md) | [Polski](README_PL.md) | [Türkçe](README_TR.md)

Europa Universalis V (EU5 / Project Caesar) 用のマップモード拡張Modです。
一般プレイ用の **全119種類** のマップモードを、画面右下のカテゴリ別メニューからマウスで素早く切り替えられるUIを提供します。

---

## 主な特徴・改善点

1. **全119種類の完全網羅（バニラの欠落を解消）**
   - バニラではUIから選択できなかったマップモードをすべて修正・追加：
     - `government`: `timeline_ownership`（年代記/領有権タイムライン - Group 99）
     - `geography`: `expeditions`（探検 - Group 4）
     - `geography`: `rivers`（河川 - 専用ボタン登録）
2. **2カラム（2列）展開レイアウト（スクロールストレスの解消）**
   - 項目数が多いカテゴリ（経済 26種、人口動態 19種、人口 17種、外交 16種、地理 16種）を **左右2列のカラム表示** に最適化。
   - 縦長になりすぎて下部が見切れる問題を解消し、**画面の広い範囲を塞ぐことなく、全項目が一目で確認・ワンクリック選択** できます。
3. **バニラ純正デザインと多言語に完全調和**
   - バニラの羊皮紙・金枠バナー、公式アイコン、フォントスタイルを忠実に使用。
   - マップモード名やツールチップは公式ローカライズ（日本語、英語など全言語）がそのまま自動適用されます。

---

## 収録マップモード一覧（計119種類）

| カテゴリ | 件数 | 構成 | 主なマップモード |
|---|---|---|---|
| **Economy (経済)** | **26** | 2列 | 税基盤、開発度、繁栄度、都市、原料、食料、支配度、近接度、道路、市場、市場アクセス 等 |
| **Demography (人口動態・文化宗教)** | **19** | 2列 | 国家文化、地域文化、言語、典礼言語、国教、地域宗教、聖地、識字率、制度（Institution） 等 |
| **Population (階級・人口)** | **17** | 2列 | 満足度、人口数、POP種別、貴族/市民/労働者/農民/兵士等の比率・分布、移住、反乱 等 |
| **Diplomacy (外交)** | **16** | 2列 | 外交関係、態度、AI性向、大国、戦争、包囲網、休戦、AI征服欲 等 |
| **Geography (地理・地形)** | **16** | 2列 | ロケーション、プロヴィンス、エリア、リージョン、大陸、地形、植生、気候、冬、河川、探検 等 |
| **Government (国家・統治)** | **13** | 1列 | 政治、政府形態、国家ランク、王朝、宮廷言語、統合度、安定度、進歩、領有タイムライン 等 |
| **Geopolitics (地政学・海洋)** | **7** | 1列 | 疫病、海洋、天然の良港適性、港湾許容量、航続距離、私掠、植民地 |
| **Military (軍事)** | **5** | 1列 | 戦術、要塞、補給、軍事通行権、戦勝点 |

※ デバッグ専用の5種類および内部処理専用（`category = hidden`）の51種類は除外しています。

---

## ディレクトリ構成

```text
all-mapmodes-selector/
├── metadata.json              # Mod定義ファイル (Interfaceタグ / v1.0.0)
├── README.md                  # Mod概要・仕様書 (英語)
├── README_JA.md               # Mod概要・仕様書 (日本語)
├── in_game/
│   ├── gui/
│   │   └── hud_bot.gui        # 最適化されたマップモードセレクターGUI
│   └── localization/
│       ├── english/           # 英語テキスト
│       └── japanese/          # 日本語テキスト
└── tools/
    ├── extract_mapmodes.py    # マップモード抽出スクリプト
    └── playable_mapmodes.json # 抽出データ (119件)
```

---

## 導入方法（ローカルModとして読み込む場合）

EU5のユーザーModディレクトリ（通常は `~/Documents/Paradox Interactive/Europa Universalis V/mod/` または `~/Library/Application Support/Paradox Interactive/Europa Universalis V/mod/`）へ、本フォルダ `all-mapmodes-selector` のシンボリックリンクまたはコピーを配置してください。

```bash
# 例: Documents配下にシンボリックリンクを作成
mkdir -p "$HOME/Documents/Paradox Interactive/Europa Universalis V/mod"
ln -s "/Users/lencon/games/EU5mod/all-mapmodes-selector" "$HOME/Documents/Paradox Interactive/Europa Universalis V/mod/all-mapmodes-selector"
```

その後、Paradox Launcherの「プレイセット」で **All Mapmodes Selector** を有効化してゲームを起動します。
