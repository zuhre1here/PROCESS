#!/usr/bin/env python3
#caesar şifresi,harfleri 3 karakter ileri veya geri kaydırır.
#şifreleme veya çözme seçeneği ile klasik caesar sistemi

def caesar(metin, kaydır=3, sifre= True):
    result = ""
    for char in metin:
        if char.isalpha(): #karakter kontrolü
            base = ord('A') if char.isupper() else ord('a') #büyük ya da küçük harf kontrolü
            offset = kaydır if sifre else -kaydır
            ascii_val = (ord(char) - base + offset) % 26 + base
            result += chr(ascii_val)

        else:
            result += char

    return result

def main():
    print("1-)Şifrele  2-)Çöz")
    secim = input("Seçiniz(1 veya 2): ")

    if secim not in ["1", "2"]:
        print("Sadece 1 veya 2 seçiniz.")
        return
    
    metin = input("Metni girin: ") #boş metin kontrolü
    if not metin:
        print("Metin girin!")
        return
    
    sifre = (secim == "1")
    sonuc = caesar(metin, kaydır=3, sifre=sifre)
    print(f"Sonuç: {sonuc}")

if __name__ == "__main__" :
    main()    