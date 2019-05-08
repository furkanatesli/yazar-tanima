# -*- coding: utf-8 -*-
import os
import re
import codecs
import string

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
      yazar_dosya_oku = yazar_dosya_oku.lower()
      yazar_dosya_oku = yazar_dosya_oku.replace("\xf6","o").replace("\xe7","c").replace("\xfd","i").replace("\xdc","u").replace("\xf0","g").replace("\xfc","u").replace("\xfe","s").replace("\xdd","i").replace("\xd6","o").replace("\x91","").replace("(","").replace(")","").replace("\x85","").replace("\xee","i")
      yazar_dosya_oku = yazar_dosya_oku.replace(".","").replace(",","").replace("'","").replace('"','').replace("\x92","").replace("\x93","").replace("\x94","").replace("\xc7","c").replace("\xd0","g").replace("\xde","s").replace("?","").replace("\xe2","a").replace("!","").replace("\xc2","a").replace("\xfb","u")
      yazar_dosya_yaz = open("C:\\Users\\Furkan\\Desktop\\yazar-tanima\\egitim-verileri\\duzenli\\"+yazar_adi+".txt",  "w")
      yazar_dosya_yaz.write(str(yazar_dosya_oku.split()))
      yazar_dosya_yaz.close()

def kelime_say():
      dosya_oku=open("C:\Users\Furkan\Desktop\yazar-tanima\egitim-verileri\duzenli\yazarlar.txt", "r")
      yazarlar=dosya_oku.read().strip().split()
      for yazar_adi in yazarlar:
            kelime_dizi_oku = open("C:\\Users\\Furkan\\Desktop\\yazar-tanima\\egitim-verileri\\duzenli\\"+yazar_adi+".txt", "r").read()
            print("***********************************************"+yazar_adi+"*****************************************************")
            kelime_dizi_oku = kelime_dizi_oku.replace("[","").replace("]","").replace("'","").replace(",","")
            kelime_dizi_oku = kelime_dizi_oku.split()
            kelime_sayisi = {}
            for kelime in kelime_dizi_oku:
                  if kelime in kelime_sayisi:
                        kelime_sayisi[kelime] += 1
                  else:
                        kelime_sayisi[kelime] = 1
            for sayi in kelime_sayisi.keys():
                  print("%s %s" %(sayi,kelime_sayisi[sayi]))
            
            print("**************************************************************************************************************")

kelime_say()
