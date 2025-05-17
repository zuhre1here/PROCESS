# Basit bir ATM simülasyonu
# Kullanıcı bakiye sorgulayabilir, para çekebilir/yatırabilir
def menu_goster():
    print('''
***********************\nATM'ye hoşgeldiniz.\n**********************

1-mevcut bakiye
2-para cekme
3-para yatırma     
q- çıkış yapmak           
   '''   )
    
def bakiye_ogren(bakiye):
    print(f"Bakiyeniz {bakiye} TL'dir.")    

def para_cek(bakiye):
    try:
       miktar = int(input("Çekmek istediğiniz miktarı giriniz:"))    
       if miktar > bakiye:
           print("Bakiye yetersiz.")

       else:   
           bakiye -= miktar
           print(f"Para çekildi.Mevcut bakiyeniz {bakiye} TL.")

    except ValueError:
        print("Lütfen geçerli bir sayı giyiniz.")
    
    return bakiye

def para_yatir(bakiye):
    try:
      miktar = int(input("Yatırmak istediğiniz miktarı girin:"))           
      if miktar <= 0:
          print("Geçersiz işlem!Geçerli miktar giriniz")

      else:
          bakiye += miktar
          print(f"Çekim başarılı.Güncel tutar {bakiye} TL.")    
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")

    return bakiye    

def atm_calısır():
    bakiye = 1000
    while True: #temel işlemler,girdi doğru olduğu sürece döngü çalışacak
        menu_goster()
        islem = input("Yapmak istediğiniz işlemi giriniz: ").lower()
        if islem == "q":
            print("Yeniden bekleriz.")
            break
        elif islem == "1":
            bakiye_ogren(bakiye) 

        elif islem == "2":
            bakiye = para_cek(bakiye)

        elif islem == "3":
            bakiye = para_yatir(bakiye)

        else:
            print("Lütfen geçerli bir işlem girin.")

#komutu çalıştırır.
atm_calısır()                                  
