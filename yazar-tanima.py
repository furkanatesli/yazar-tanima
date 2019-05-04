import os
import re
os.system('ac.bat')               
##ana dizindeki ac.bat dosyası çalışarak "\egitim-verileri\duzensiz\" dizininde "yazarlar.txt" isminde, içerisinde 
# duzensiz klasöründeki yazarlarin isimleri bulunan dosya oluşturuyor

##"yazarlar.txt" içerisindeki verileri kullanışlı yala getirmek için dosya içerisindeki verileri düzenleyip "\egitim-verileri\duzenli\" dizinine 
# "yazarlar.txt" olarak kayıt ediyoruz
def isim_duzenle():
    dosya_oku = open("C:\Users\Furkan\Desktop\yazar-tanima\egitim-verileri\duzensiz\yazarlar.txt", "r").read()
    yazarlar=re.split(".txt|yazarlar.txt|yazarlar.bat|yazarlar1.txt",dosya_oku)
    dosya_yaz = open("C:\Users\Furkan\Desktop\yazar-tanima\egitim-verileri\duzenli\yazarlar.txt", "w")
    for i in yazarlar:
      dosya_yaz.write(i.strip()+"\n")
      print(i.strip()+"\n")
    dosya_yaz.close()

#def metin_duzenle();
isim_duzenle()
