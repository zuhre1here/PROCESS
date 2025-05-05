#!/bin/bash

#ceasar şifresi:Harfleri 3 karakter ileri kaydırır(A-->D)

#seçim aşaması
echo "1) Şifrele 2-) Çöz"
read -p "seçiminiz: " secim

if [[ ! $secim =~ ^[1-2]$ ]]; then
    echo "Seçiminiz geçersiz! 1 veya 2 seçin."
    exit 1

fi

echo "Metni gir:"
read metin

#boş metin kontrolü
if [ -z "$metin" ]; then
   echo "Metin girilmedi!"
   exit 1

fi

sifreli=""
for (( i=0; i<${#metin}; i++  )); do
   char="${metin:$i:1}" #i'nci karakteri al
   if [[ $char =~ [a-zA-Z] ]]; then
      printf -v ascii "%d" "'$char" #ASCII değerini bul
      if [ "$secim" = "1" ]; then
         ascii=$((ascii+3)) #sifrele: 3 ileri karakter

      else 
         ascii=$((ascii-3)) #çöz: 3 geri karakter
      fi
      sifreli+=$(printf \\$(printf '%03o' $ascii)) #ASCII önce oktal,daha sonr harfe çevir.
   else
      sifreli+="$char" #harf dışında bir karakterse aynı kalsın
   fi   

done

echo "Sonuç: $sifreli"
