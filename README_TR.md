# All Mapmodes Selector (EU5 Mod)

[English](README.md) | [日本語](README_JA.md) | [简体中文](README_ZH.md) | [한국어](README_KO.md) | [Français](README_FR.md) | [Deutsch](README_DE.md) | [Español](README_ES.md) | [Português](README_PT.md) | [Русский](README_RU.md) | [Polski](README_PL.md) | **Türkçe**

Europa Universalis V (EU5 / Project Caesar) için arayüz geliştirme modu.  
Sağ alt HUD'daki kategorilere ayrılmış menüler aracılığıyla oynanabilir **119 harita modunun tamamına** fareyle tek tıklamayla hızlı erişim sağlar.

---

## Temel Özellikler ve İyileştirmeler

1. **Oynanabilir 119 Harita Modunun Eksiksiz Kapsamı (Orijinal Eksikliklerin Giderilmesi)**
   - Orijinal arayüzde seçilemeyen veya eksik olan harita modlarını açar ve geri getirir:
     - `government`: `timeline_ownership` (Mülkiyet Zaman Çizelgesi / Kronik - Grup 99)
     - `geography`: `expeditions` (Keşif Seferleri - Grup 4)
     - `geography`: `rivers` (Nehir harita modu için özel buton)
2. **2 Sütunlu Izgara Düzeni (Bitmek Bilmeyen Kaydırmalara Son)**
   - Çok sayıda öğe içeren kategoriler (Ekonomi 26, Demografi 19, Nüfus 17, Diplomasi 16, Coğrafya 16) **düzenli 2 sütunlu ızgaralar** halinde optimize edildi.
   - Ekranın altına taşan dikey menü sorununu ortadan kaldırarak, oyun ekranını kapatmadan tüm modları tek bakışta görüp seçmenizi sağlar.
3. **Orijinal Oyun Tasarımıyla Uyum ve Çoklu Dil Desteği**
   - Orijinal tasarıma sadık: parşömen dokusu, altın çerçeveler, resmi simgeler ve orijinal yazı tipleri.
   - Harita modu isimleri ve ipuçları (tooltip), oyununuzun resmi yerelleştirmesini otomatik olarak kullanır.

---

## Dahil Edilen Harita Modları (Toplam 119)

| Kategori | Sayı | Düzen | Başlıca Harita Modları |
|---|---|---|---|
| **Economy (Ekonomi)** | **26** | 2 Sütun | Vergi Tabanı, Gelişmişlik, Refah, Şehirler, Hammaddeler, Yiyecek, Kontrol, Yakınlık, Yollar, Pazarlar, Pazar Erişimi vb. |
| **Demography (Demografi)** | **19** | 2 Sütun | Ülke Kültürü, Yerel Kültür, Dil, Ayin Dili, Devlet Dini, Yerel Din, Kutsal Yerler, Okuryazarlık, Kurumlar (Institutions) vb. |
| **Population (Nüfus/Sınıflar)** | **17** | 2 Sütun | Memnuniyet, Toplam Nüfus, POP Türleri, Sınıf Oranları (Soylular, Kentliler, İşçiler, Köylüler, Askerler), Göç, Huzursuzluk vb. |
| **Diplomacy (Diplomasi)** | **16** | 2 Sütun | Diplomatik İlişkiler, Tutum, Yapay Zeka Tavrı, Büyük Güçler, Savaşlar, Koalisyonlar, Ateşkesler, Yapay Zeka Fetih Arzuları vb. |
| **Geography (Coğrafya/Yeryüzü)** | **16** | 2 Sütun | Konumlar, Vilayetler, Alanlar, Bölgeler, Kıtalar, Topoğrafya, Bitki Örtüsü, İklim, Kış, Nehirler, Keşifler vb. |
| **Government (Hükümet/Devlet)** | **13** | 1 Sütun | Siyaset, Hükümet Biçimi, Ülke Derecesi, Hanedanlar, Saray Dili, Entegrasyon, İstikrar, İlerleme, Mülkiyet Zaman Çizelgesi vb. |
| **Geopolitics (Jeopolitik/Deniz)** | **7** | 1 Sütun | Salgınlar, Deniz Bölgeleri, Doğal Limanlar, Liman Kapasitesi, Deniz Menzili, Korsanlık, Koloniler |
| **Military (Askeri)** | **5** | 1 Sütun | Taktikler, Kaleler, İkmal, Askeri Geçiş İzni, Savaş Skoru |

*Not: 5 hata ayıklama modu ve 51 dahili motor modu (`category = hidden`) hariç tutulmuştur.*

---

## Dizin Yapısı

```text
all-mapmodes-selector/
├── metadata.json              # Mod tanımlayıcı dosyası (Interface etiketi / v1.0.0)
├── README.md                  # Dokümantasyon (İngilizce)
├── README_JA.md               # Dokümantasyon (Japonca)
├── README_TR.md               # Dokümantasyon (Türkçe)
├── in_game/
│   ├── gui/
│   │   └── hud_bot.gui        # Optimize edilmiş harita modu seçici GUI
│   └── localization/
│       ├── english/           # İngilizce yerelleştirme
│       └── japanese/          # Japonca yerelleştirme
└── tools/
    ├── extract_mapmodes.py    # Harita modu çıkarma betiği
    └── playable_mapmodes.json # Çıkarılan veriler (119 kayıt)
```

---

## Kurulum (Yerel Mod)

`all-mapmodes-selector` klasörünün sembolik bağlantısını veya bir kopyasını EU5 mod dizinine yerleştirin (genellikle `~/Documents/Paradox Interactive/Europa Universalis V/mod/` veya `~/Library/Application Support/Paradox Interactive/Europa Universalis V/mod/`).

```bash
# Örnek: Documents altında sembolik bağlantı oluşturma
mkdir -p "$HOME/Documents/Paradox Interactive/Europa Universalis V/mod"
ln -s "/Users/lencon/games/EU5mod/all-mapmodes-selector" "$HOME/Documents/Paradox Interactive/Europa Universalis V/mod/all-mapmodes-selector"
```

Ardından Paradox Başlatıcısı'ndaki oynatma listenizde (Playset) **All Mapmodes Selector**'ı etkinleştirip oyunu başlatın.
