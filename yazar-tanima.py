import os
import re
import codecs
os.system('ac.bat')
def isim_duzenle():
    dosya_oku = open("C:\Users\Furkan\Desktop\yazar-tanima\egitim-verileri\duzensiz\yazarlar.txt", "r").read()
    yazarlar = re.split(".txt|yazarlar.txt|yazarlar.bat|yazarlar1.txt",dosya_oku)
    dosya_yaz = open("C:\Users\Furkan\Desktop\yazar-tanima\egitim-verileri\duzenli\yazarlar.txt", "w")
    for i in yazarlar:
      dosya_yaz.write(i.strip()+"\n")
      print(i.strip()+"\n")
    dosya_yaz.close()

def metin_duzenle():
    dosya_oku=open("C:\Users\Furkan\Desktop\yazar-tanima\egitim-verileri\duzenli\yazarlar.txt", "r")
    yazarlar=dosya_oku.read().strip().split()
    for yazar_adi in yazarlar:
      yazar_dosya_oku = open("C:\\Users\\Furkan\\Desktop\\yazar-tanima\\egitim-verileri\\duzensiz\\"+yazar_adi+".txt", "r").read()
      yazar_dosya_oku = yazar_dosya_oku.lower().decode('iso-8859-9')
      yazar_dosya_oku = yazar_dosya_oku.encode("utf-8","ignore")
      yazar_dosya_yaz = open("C:\\Users\\Furkan\\Desktop\\yazar-tanima\\egitim-verileri\\duzenli\\"+yazar_adi+".txt",  "w")
      yazar_dosya_yaz.write(str(yazar_dosya_oku.split()))
      yazar_dosya_yaz.close()
metin_duzenle()
