# Caesar Şifresi (Bash)

Bu proje, Bash ile yazılmış bir Caesar şifresi aracıdır. Metindeki harfleri 3 ileri (şifreleme) veya 3 geri (çözme) kaydırır. Boşluk, sayı gibi diğer karakterler değişmez.

## Özellikler
- Harfleri 3 ileri kaydırarak şifreler.
- Şifrelenmiş metni 3 geri kaydırarak çözer.
- Kullanıcı dostu arayüz: Şifreleme veya çözme seçimi.
- Hata kontrolü: Boş metin veya geçersiz seçim için uyarı.

## Kurulum
1. Repoyu klonlayın:
   ```bash
   git clone https://github.com/zuhre1here/PROCESS.git
   cd PROCESS


Script’e çalıştırma izni verin:chmod +x ceasarbash.sh

Kullanım
Script’i çalıştırın ve talimatları izleyin:
./ceasarbash.sh

Örnekler
Şifreleme
1) Şifrele  2) Çöz
Seçim (1 veya 2): 1
Metni gir: zuhre mi
Sonuç: }xkuh pl

Çözme
1) Şifrele  2) Çöz
Seçim (1 veya 2): 2
Metni gir: }xkuh pl
Sonuç: zuhre mi

Hata: Boş Metin
1) Şifrele  2) Çöz
Seçim (1 veya 2): 1
Metni gir: 
Metin girmedin!

```
