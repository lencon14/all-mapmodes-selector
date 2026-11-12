# All Mapmodes Selector (EU5 Mod)

[English](README.md) | [Deutsch](README_DE.md) | [Español](README_ES.md) | [Français](README_FR.md) | [日本語](README_JA.md) | [한국어](README_KO.md) | [Polski](README_PL.md) | [Português (Brasil)](README_PT.md) | [Русский](README_RU.md) | [Türkçe](README_TR.md) | **简体中文**

《欧陆风云5》（Europa Universalis V / Project Caesar）地图模式扩展模组。  
通过右下角HUD按分类整理的菜单，提供对全部 **119种常规可用地图模式** 的一键快速切换界面。

---

## 主要特点与改进

1. **全面涵盖全部119种可用地图模式（补全原版缺失）**
   - 修复并恢复了原版UI中无法选择或缺失的地图模式：
     - `government`: `timeline_ownership`（历史领地时间线 - Group 99）
     - `geography`: `expeditions`（远征探险 - Group 4）
     - `geography`: `rivers`（专属河流地图模式按钮）
2. **双列（2列）网格布局（告别繁琐翻页与滚动）**
   - 针对选项众多的分类（经济 26种、人口统计 19种、阶级人口 17种、外交 16种、地理 16种）优化为 **双列左右排列**。
   - 解决纵向菜单过长导致屏幕底部被遮挡的问题，**无需滚动即可一目了然、一键选择所有项目**，且不会大面积遮挡游戏主画面。
3. **完美契合原版界面风格与多语言支持**
   - 忠实还原原版羊皮纸底色、金边边框、官方图标与字体风格。
   - 地图模式名称与悬停提示（Tooltip）自动采用游戏官方本地化（简体中文、英语等全语言自适应）。

---

## 收录地图模式一览（共119种）

| 分类 | 数量 | 布局 | 主要包含的地图模式 |
|---|---|---|---|
| **Economy (经济)** | **26** | 2列 | 税基、发展度、繁荣度、城镇、原料、食物、控制力、近邻度、道路、市场、市场准入等 |
| **Demography (人口统计/文化宗教)** | **19** | 2列 | 国家文化、当地文化、语言、礼仪语言、国教、当地宗教、圣地、识字率、思潮（Institution）等 |
| **Population (阶级/人口)** | **17** | 2列 | 满意度、总人口、人口类型、阶级比例与分布（贵族/市民/劳工/农民/士兵）、移民、动乱等 |
| **Diplomacy (外交)** | **16** | 2列 | 外交关系、态度、AI倾向、大国、战争、包围网/联盟、停战、AI征服欲等 |
| **Geography (地理/地形)** | **16** | 2列 | 地块、省份、区域、大区、大陆、地形、植被、气候、冬季、河流、探险等 |
| **Government (国家/统治)** | **13** | 1列 | 政治、政体、国家等级、王朝、宫廷语言、整合度、稳定度、进度、领地时间线等 |
| **Geopolitics (地缘政治/海洋)** | **7** | 1列 | 流行病、海域、天然良港适宜度、港口容量、航程、私掠、殖民地 |
| **Military (军事)** | **5** | 1列 | 战术、堡垒、补给、军事通行权、战争分数 |

*注：已排除5种调试专用地图模式以及51种引擎内部处理专用地图模式（`category = hidden`）。*

---

## 目录结构

```text
all-mapmodes-selector/
├── metadata.json              # 模组元数据文件 (Interface标签 / v1.*)
├── README.md                  # 模组说明文档 (英文)
├── README_JA.md               # 模组说明文档 (日文)
├── README_ZH.md               # 模组说明文档 (简体中文)
├── in_game/
│   ├── gui/
│   │   └── hud_bot.gui        # 优化后的地图模式选择器GUI
│   └── localization/
│       ├── english/           # 英语文本
│       └── japanese/          # 日语文本
└── tools/
    ├── extract_mapmodes.py    # 地图模式提取脚本
    └── playable_mapmodes.json # 提取的数据 (119项)
```

---

## 安装方法（本地模组安装）

将本模组文件夹 `all-mapmodes-selector` 的软链接（快捷方式）或完整副本放入EU5的用户模组目录中（通常为 `~/Documents/Paradox Interactive/Europa Universalis V/mod/` 或 `~/Library/Application Support/Paradox Interactive/Europa Universalis V/mod/`）。

```bash
# 示例: 在Documents目录下创建软链接
mkdir -p "$HOME/Documents/Paradox Interactive/Europa Universalis V/mod"
ln -s "/Users/lencon/games/EU5mod/all-mapmodes-selector" "$HOME/Documents/Paradox Interactive/Europa Universalis V/mod/all-mapmodes-selector"
```

之后在 Paradox 启动器的「播放集（Playset）」中启用 **All Mapmodes Selector** 并启动游戏即可。
