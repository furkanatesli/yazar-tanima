# -*- coding: utf-8 -*-
import os
import re
import codecs
import string

os.system('ac.bat')

def egitim_isim_duzenle():
    dosya_oku = open("C:\Users\Furkan\Desktop\yazar-tanima\egitim-verileri\duzensiz\yazarlar.txt", "r").read()
    yazarlar = re.split(".txt|yazarlar.txt|yazarlar.bat|yazarlar1.txt",dosya_oku)
    dosya_yaz = open("C:\Users\Furkan\Desktop\yazar-tanima\egitim-verileri\duzenli\yazarlar.txt", "w")
    for i in yazarlar:
      dosya_yaz.write(i.strip()+"\n")
      print(i.strip()+"\n")
    dosya_yaz.close()

def test_isim_duzenle():
    dosya_oku = open("C:\\Users\\Furkan\\Desktop\\yazar-tanima\\test-verileri\\duzensiz\\yazarlar.txt", "r").read()
    yazarlar = re.split(".txt|yazarlar.txt|yazarlar.bat|yazarlar1.txt",dosya_oku)
    dosya_yaz = open("C:\\Users\\Furkan\\Desktop\\yazar-tanima\\test-verileri\\duzenli\\yazarlar.txt", "w")
    for i in yazarlar:
      dosya_yaz.write(i.strip()+"\n")
      print(i.strip()+"\n")
    dosya_yaz.close()

def egitim_metin_duzenle():
    dosya_oku=open("C:\Users\Furkan\Desktop\yazar-tanima\egitim-verileri\duzenli\yazarlar.txt", "r")
    yazarlar=dosya_oku.read().strip().split()
    for yazar_adi in yazarlar:
      yazar_dosya_oku = open("C:\\Users\\Furkan\\Desktop\\yazar-tanima\\egitim-verileri\\duzensiz\\"+yazar_adi+".txt", "r").read()
      yazar_dosya_oku = yazar_dosya_oku.lower()
      yazar_dosya_oku = yazar_dosya_oku.replace("\xf6","o").replace("\xe7","c").replace("\xfd","i").replace("\xdc","u").replace("\xf0","g").replace("\xfc","u").replace("\xfe","s").replace("\xdd","i").replace("\xd6","o").replace("\x91","").replace("(","").replace(")","").replace("\x85","").replace("\xee","i").replace("-","")
      yazar_dosya_oku = yazar_dosya_oku.replace(".","").replace(",","").replace("'","").replace('"','').replace("\x92","").replace("\x93","").replace("\x94","").replace("\xc7","c").replace("\xd0","g").replace("\xde","s").replace("?","").replace("\xe2","a").replace("!","").replace("\xc2","a").replace("\xfb","u").replace(":","").replace(";","")
      yazar_dosya_yaz = open("C:\\Users\\Furkan\\Desktop\\yazar-tanima\\egitim-verileri\\duzenli\\"+yazar_adi+".txt",  "w")
      yazar_dosya_yaz.write(str(yazar_dosya_oku.split()))
      yazar_dosya_yaz.close()

def test_metin_duzenle():
    dosya_oku=open("C:\\Users\\Furkan\\Desktop\\yazar-tanima\\test-verileri\\duzenli\\yazarlar.txt", "r")
    yazarlar=dosya_oku.read().strip().split()
    for yazar_adi in yazarlar:
      yazar_dosya_oku = open("C:\\Users\\Furkan\\Desktop\\yazar-tanima\\test-verileri\\duzensiz\\"+yazar_adi+".txt", "r").read()
      yazar_dosya_oku = yazar_dosya_oku.lower()
      yazar_dosya_oku = yazar_dosya_oku.replace("\xf6","o").replace("\xe7","c").replace("\xfd","i").replace("\xdc","u").replace("\xf0","g").replace("\xfc","u").replace("\xfe","s").replace("\xdd","i").replace("\xd6","o").replace("\x91","").replace("(","").replace(")","").replace("\x85","").replace("\xee","i").replace("-","")
      yazar_dosya_oku = yazar_dosya_oku.replace(".","").replace(",","").replace("'","").replace('"','').replace("\x92","").replace("\x93","").replace("\x94","").replace("\xc7","c").replace("\xd0","g").replace("\xde","s").replace("?","").replace("\xe2","a").replace("!","").replace("\xc2","a").replace("\xfb","u").replace(":","").replace(";","")
      yazar_dosya_yaz = open("C:\\Users\\Furkan\\Desktop\\yazar-tanima\\test-verileri\\duzenli\\"+yazar_adi+".txt",  "w")
      yazar_dosya_yaz.write(str(yazar_dosya_oku.split()))
      yazar_dosya_yaz.close()

def kelimeler():
      dosya_oku=open("C:\Users\Furkan\Desktop\yazar-tanima\egitim-verileri\duzenli\yazarlar.txt", "r")
      yazarlar=dosya_oku.read().strip().split()
      global kelimeler
      kelimeler = {}
      
      for yazar_adi in yazarlar:
            egitim_kelime_dizi_oku = open("C:\\Users\\Furkan\\Desktop\\yazar-tanima\\egitim-verileri\\duzenli\\"+yazar_adi+".txt", "r").read()
            egitim_kelime_dizi_oku = egitim_kelime_dizi_oku.replace("[","").replace("]","").replace("'","").replace(",","")
            egitim_kelime_dizi_oku = egitim_kelime_dizi_oku.split()
            for kelime in egitim_kelime_dizi_oku:
                  if kelime not in kelimeler:
                        kelimeler[kelime] = 0
      dosya_oku=open("C:\\Users\\Furkan\\Desktop\\yazar-tanima\\test-verileri\\duzenli\\yazarlar.txt", "r")
      yazarlar=dosya_oku.read().strip().split()
      for yazar_adi in yazarlar:
            test_kelime_dizi_oku = open("C:\\Users\\Furkan\\Desktop\\yazar-tanima\\test-verileri\\duzenli\\"+yazar_adi+".txt", "r").read()
            test_kelime_dizi_oku = test_kelime_dizi_oku.replace("[","").replace("]","").replace("'","").replace(",","")
            test_kelime_dizi_oku = test_kelime_dizi_oku.split()
            for kelime in test_kelime_dizi_oku:
                  if kelime not in kelimeler:
                        kelimeler[kelime] = 0
      for sayi in kelimeler.keys():
                  print("%s %s" %(sayi,kelimeler[sayi]))
def egitim_kelime_say():
      dosya_oku=open("C:\Users\Furkan\Desktop\yazar-tanima\egitim-verileri\duzenli\yazarlar.txt", "r")
      yazarlar=dosya_oku.read().strip().split()
      for yazar_adi in yazarlar:
            kelime_sayisi = kelimeler.copy()
            kelime_dizi_oku = open("C:\\Users\\Furkan\\Desktop\\yazar-tanima\\egitim-verileri\\duzenli\\"+yazar_adi+".txt", "r").read()
            kelime_dizi_oku = kelime_dizi_oku.replace("[","").replace("]","").replace("'","").replace(",","")
            kelime_dizi_oku = kelime_dizi_oku.split()
            for kelime in kelime_dizi_oku:
                  if kelime in kelime_sayisi:
                        kelime_sayisi[kelime] += 1
                  else:
                        kelime_sayisi[kelime] = 1
            print("*************************"+yazar_adi+"*************************")
            yazar_sonuc_yaz = open("C:\\Users\\Furkan\\Desktop\\yazar-tanima\\egitim-verileri\\sonuclar\\"+yazar_adi+".txt",  "w")
            for sayi in kelime_sayisi.keys():
                  yazar_sonuc_yaz.write(("%s" %(kelime_sayisi[sayi])))
            yazar_sonuc_yaz.close()

def test_kelime_say():
      dosya_oku=open("C:\\Users\\Furkan\\Desktop\\yazar-tanima\\test-verileri\\duzenli\\yazarlar.txt", "r")
      yazarlar=dosya_oku.read().strip().split()
      for yazar_adi in yazarlar:
            kelime_sayisi = kelimeler.copy()
            kelime_dizi_oku = open("C:\\Users\\Furkan\\Desktop\\yazar-tanima\\test-verileri\\duzenli\\"+yazar_adi+".txt", "r").read()
            kelime_dizi_oku = kelime_dizi_oku.replace("[","").replace("]","").replace("'","").replace(",","")
            kelime_dizi_oku = kelime_dizi_oku.split()
            for kelime in kelime_dizi_oku:
                  if kelime in kelime_sayisi:
                        kelime_sayisi[kelime] += 1
                  else:
                        kelime_sayisi[kelime] = 1
            print("*************************"+yazar_adi+"*************************")
            yazar_sonuc_yaz = open("C:\\Users\\Furkan\\Desktop\\yazar-tanima\\test-verileri\\sonuc\\"+yazar_adi+".txt",  "w")
            for sayi in kelime_sayisi.keys():
                  yazar_sonuc_yaz.write(("%s" %(kelime_sayisi[sayi])))
            yazar_sonuc_yaz.close()  

egitim_isim_duzenle()
test_isim_duzenle()
egitim_metin_duzenle()
test_metin_duzenle()
kelimeler()
egitim_kelime_say()
test_kelime_say()
