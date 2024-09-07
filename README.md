*Bu proje TEKNOFEST 2024 Antalya T3AI Hackathon Yarışması İnce Ayarlama Kategorisi için geliştirilmiştir.*

# Proje Başlığı 
## Modelimiz, ilgili dikeylerde bilgi sahibi olmak isteyen kullanıcılara seri ve kapsamlı cevaplar vermektedir.


````
.
├── training
├── function_calling
├── datasets/
│   ├── turk-egitim-sistemi
│   ├── turk-hukuku
│   ├── surdurulebilirlik
│   └── tarim
├── assets
├── requirements.txt
└── README.md
````

## NexTech: 2321961
- 👤 Ahmet Emin Ünal
- 👤 Furkan Ünal


## Veri Seti Kaynakları
### Türk Eğitim Sistemi
https://ogm.meb.gov.tr/meb_iys_dosyalar/2017_06/13153013_TES_ve_ORTAYYRETYM_son10_2.pdf
https://tr.wikipedia.org/wiki/T%C3%BCrkiye%27de_e%C4%9Fitim
https://fulbright.org.tr/turk-egitim-sistemi
### Türk Hukuku
https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=5237&MevzuatTur=1&MevzuatTertip=5
https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=4721&MevzuatTur=1&MevzuatTertip=5
https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=2709&MevzuatTur=1&MevzuatTertip=5
### Sürdürülebilirlik
https://tr.wikipedia.org/wiki/S%C3%BCrd%C3%BCr%C3%BClebilirlik
http://www.surdurulebilirkalkinma.gov.tr/
### Tarım
https://www.tarimorman.gov.tr/Konular/Bitki-Sagligi-Hizmetleri
https://arastirma.tarimorman.gov.tr/tepge/Menu/53/Yayin-Arsivi

## İnce Ayarlama Süreci Başlatma
```bash
pip install --upgrade huggingface_hub
huggingface-cli login
```
```bash
git clone --depth 1 https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install -e ".[torch,metrics]"
```
```bash
finetune.sh
export.sh
```

## Sınama Görevi: Fonksiyon Çağırma
```bash
finetune_func.sh
```
