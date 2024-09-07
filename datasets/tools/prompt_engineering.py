from transformers import AutoModelForCausalLM, AutoTokenizer

model_directory = "t3ai-org/pt-model"
tokenizer = AutoTokenizer.from_pretrained(model_directory)
model = AutoModelForCausalLM.from_pretrained(model_directory)\

input_text = f"Ama Commodore, Plus/4'ü C64 ile uyumsuz yaparak büyük bir stratejik hata yapmıştı. Birleşik Krallık'ta (UK), C64'ün en büyük rakipleri Sinclair ZX Spectrum ve Amstrad CPC 464 idi. C64'ten birkaç ay önce üretilen Spectrum, düşük ücretiyle kısa sürede pazar lideri oldu. 1983'ün başlarında Spectrum 175£ iken C64 399£ idi. C64'ün Spectrum karşında işi zordu. Ama C64, 1980'lerin ikinci yarısında popülerlikte Spectrum ile rekabet edecekti ve Kasım 1990'da üretimine son verilen Spectrum'dan daha fazla yaşayacaktı. Commodore birkaç kere C64’ün üretimine son vermeyi düşündü. Ama talepler yüzünden sonlandıramadı. 1988’de dünya çapında 1,5 milyon C64 satıyordu. 1990’da ABD’de taleplerin düşmesine rağmen İngiltere ve diğer Avrupa ülkelerinde popülerliğini korudu. Mart 1994 CeBIT (Hanover, Almanya) fuarında C64’ün üretiminin 1995'te durdurulacağı duyuruldu. Commodore, C64’ün disket sürücünü üretmenin C64’ün kendisini üretmekten daha pahalıya mal olduğunu söylüyordu. Tarihin 1995 olarak planlanmasına rağmen şirket 1 ay sonra Nisan 1994'te iflas etti. C64 ailesi 1982’de Commodore, Commodore MAX Machine’i Japonya’da üretti. Max, sınırlı hesaplama kapasiteli bir oyun konsolu olarak tasarlanmıştı. Tutulmadığı için piyasaya çıkışından birkaç ay sonra üretimine son verildi. 1984'te C64’ün taşınabilir sürümü SX-64 üretildi. SX-64, ilk tam renkli taşınabilir bilgisayardı. 5 inçlik (127 mm) bir CRT ekrana ve 1541 disket sürücüsüne sahipti. Kaset konnektörü yoktu. 1986 : Commodore 64C (C64C) üretildi. İşlevsellik bakımından C64’ün aynısıydı. Ama kasası yeniden tasarlanmıştı. SID, VIC ve I/O çiplerinin çekirdek voltajı 12’den 5’e düşürülmüş yeni sürümleri kullanılmıştı. Daha sonra daha ufak olan 1541-II ve 800KB 3,5” lik 1581 disket sürücüleri üretildi. 1990 : C64, C64 Games System (C64GS) denen oyun konsolu şeklinde üretildi. C64C’nin anakartına yapılan ufak bir modifikasyonla kartuşları yukarıdan takılabilecek hale getirildi." 
cevap_text = f"ABD’de buna Ultimax, Almanya’da ise VC-10 dendi."
    
prompt = f"{input_text} \n Yukarıdaki bilgiye göre, cevabı \"{cevap_text}\" olan soru nedir? (```...?``` şeklinde markdown hücresi içerisinde ver) Soru:```"

input_ids = tokenizer(input_text, return_tensors="pt").input_ids
output_ids = model.generate(input_ids, num_return_sequences=1, max_new_tokens=124)
output_text = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
print(output_text)
