#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import codecs
import string
from math import sqrt
import operator
os.system('isim_cek.bat')

def egitim_isim_duzenle():
      dosya_oku = open("egitim-verileri\duzensiz\yazarlar.txt", "r").read()
      yazarlar = re.split(".txt|yazarlar.txt|yazarlar.bat|yazarlar1.txt",dosya_oku)
      dosya_yaz = open("egitim-verileri\duzenli\yazarlar.txt", "w")
      for i in yazarlar:
            dosya_yaz.write(i.strip()+"\n")
      dosya_yaz.close()
      print u"Eğitim Yazar İsimleri Alındı"

def test_isim_duzenle():
      dosya_oku = open("test-verileri\\duzensiz\\yazarlar.txt", "r").read()
      yazarlar = re.split(".txt|yazarlar.txt|yazarlar.bat|yazarlar1.txt|testler",dosya_oku)
      dosya_yaz = open("test-verileri\\duzenli\\yazarlar.txt", "w")
      for i in yazarlar:
            dosya_yaz.write(i.strip()+"\n")
      dosya_yaz.close()
      print u"Test Yazar İsimleri Alındı"

def egitim_metin_duzenle():
      dosya_oku=open("egitim-verileri\duzenli\yazarlar.txt", "r")
      yazarlar=dosya_oku.read().strip().split()
      for yazar_adi in yazarlar:
            yazar_dosya_oku = open("egitim-verileri\\duzensiz\\"+yazar_adi+".txt", "r").read()
            yazar_dosya_oku = yazar_dosya_oku.lower()
            yazar_dosya_oku = yazar_dosya_oku.replace("\xf6","o").replace("\xe7","c").replace("\xfd","i").replace("\xdc","u").replace("\xf0","g").replace("\xfc","u").replace("\xfe","s").replace("\xdd","i").replace("\xd6","o").replace("\x91","").replace("(","").replace(")","").replace("\x85","").replace("\xee","i").replace("-","")
            yazar_dosya_oku = yazar_dosya_oku.replace(".","").replace(",","").replace("'","").replace('"','').replace("\x92","").replace("\x93","").replace("\x94","").replace("\xc7","c").replace("\xd0","g").replace("\xde","s").replace("?","").replace("\xe2","a").replace("!","").replace("\xc2","a").replace("\xfb","u").replace(":","").replace(";","")
            yazar_dosya_yaz = open("egitim-verileri\\duzenli\\"+yazar_adi+".txt",  "w")
            yazar_dosya_yaz.write(str(yazar_dosya_oku.split()))
            yazar_dosya_yaz.close()
      print u"Eğitim Metinleri Düzenlendi"

def test_metin_duzenle():
      dosya_oku=open("test-verileri\\duzenli\\yazarlar.txt", "r")
      yazarlar=dosya_oku.read().strip().split()
      for yazar_adi in yazarlar:
            yazar_dosya_oku = open("test-verileri\\duzensiz\\"+yazar_adi+".txt", "r").read()
            yazar_dosya_oku = yazar_dosya_oku.lower()
            yazar_dosya_oku = yazar_dosya_oku.replace("\xf6","o").replace("\xe7","c").replace("\xfd","i").replace("\xdc","u").replace("\xf0","g").replace("\xfc","u").replace("\xfe","s").replace("\xdd","i").replace("\xd6","o").replace("\x91","").replace("(","").replace(")","").replace("\x85","").replace("\xee","i").replace("-","")
            yazar_dosya_oku = yazar_dosya_oku.replace(".","").replace(",","").replace("'","").replace('"','').replace("\x92","").replace("\x93","").replace("\x94","").replace("\xc7","c").replace("\xd0","g").replace("\xde","s").replace("?","").replace("\xe2","a").replace("!","").replace("\xc2","a").replace("\xfb","u").replace(":","").replace(";","")
            yazar_dosya_yaz = open("test-verileri\\duzenli\\"+yazar_adi+".txt",  "w")
            yazar_dosya_yaz.write(str(yazar_dosya_oku.split()))
            yazar_dosya_yaz.close()
      print u"Test Metinleri Düzenlendi"

def kelimeler():
      dosya_oku=open("egitim-verileri\duzenli\yazarlar.txt", "r")
      yazarlar=dosya_oku.read().strip().split()
      global kelimeler
      kelimeler = {}
      for yazar_adi in yazarlar:
            egitim_kelime_dizi_oku = open("egitim-verileri\\duzenli\\"+yazar_adi+".txt", "r").read()
            egitim_kelime_dizi_oku = egitim_kelime_dizi_oku.replace("[","").replace("]","").replace("'","").replace(",","")
            egitim_kelime_dizi_oku = egitim_kelime_dizi_oku.split()
            for kelime in egitim_kelime_dizi_oku:
                  if kelime not in kelimeler:
                        kelimeler[kelime] = 0
      dosya_oku=open("test-verileri\\duzenli\\yazarlar.txt", "r")
      yazarlar=dosya_oku.read().strip().split()
      for yazar_adi in yazarlar:
            test_kelime_dizi_oku = open("test-verileri\\duzenli\\"+yazar_adi+".txt", "r").read()
            test_kelime_dizi_oku = test_kelime_dizi_oku.replace("[","").replace("]","").replace("'","").replace(",","")
            test_kelime_dizi_oku = test_kelime_dizi_oku.split()
            for kelime in test_kelime_dizi_oku:
                  if kelime not in kelimeler:
                        kelimeler[kelime] = 0
      print u"Kelime Sayısı Hesaplandı."
      print "Toplam Kelime Sayisi= ",len(kelimeler)

def egitim_kelime_say():
      dosya_oku=open("egitim-verileri\duzenli\yazarlar.txt", "r")
      yazarlar=dosya_oku.read().strip().split()
      for yazar_adi in yazarlar:
            kelime_sayisi = kelimeler.copy()
            kelime_dizi_oku = open("egitim-verileri\\duzenli\\"+yazar_adi+".txt", "r").read()
            kelime_dizi_oku = kelime_dizi_oku.replace("[","").replace("]","").replace("'","").replace(",","")
            kelime_dizi_oku = kelime_dizi_oku.split()
            for kelime in kelime_dizi_oku:
                  if kelime in kelime_sayisi:
                        kelime_sayisi[kelime] += 1
                  else:
                        kelime_sayisi[kelime] = 1
            yazar_sonuc_yaz = open("egitim-verileri\\sonuclar\\"+yazar_adi+".txt",  "w")
            for sayi in kelime_sayisi.keys():
                  yazar_sonuc_yaz.write(("%s" %(kelime_sayisi[sayi]))+",")
            yazar_sonuc_yaz.close()
      print u"Eğitim Dosyası Kelimeleri Sayıldı."

def test_kelime_say():
      dosya_oku=open("test-verileri\\duzenli\\yazarlar.txt", "r")
      yazarlar=dosya_oku.read().strip().split()
      for yazar_adi in yazarlar:
            kelime_sayisi = kelimeler.copy()
            kelime_dizi_oku = open("test-verileri\\duzenli\\"+yazar_adi+".txt", "r").read()
            kelime_dizi_oku = kelime_dizi_oku.replace("[","").replace("]","").replace("'","").replace(",","")
            kelime_dizi_oku = kelime_dizi_oku.split()
            for kelime in kelime_dizi_oku:
                  if kelime in kelime_sayisi:
                        kelime_sayisi[kelime] += 1
                  else:
                        kelime_sayisi[kelime] = 1
            yazar_sonuc_yaz = open("test-verileri\\sonuc\\"+yazar_adi+".txt",  "w")
            for sayi in kelime_sayisi.keys():
                  yazar_sonuc_yaz.write(("%s" %(kelime_sayisi[sayi]))+",")
            yazar_sonuc_yaz.close()  
      print u"Test Dosyası Kelimeleri Sayıldı."

def test_data_al():
      global test_data
      test_dosya_oku=open("test-verileri\\duzenli\\yazarlar.txt", "r")
      test_yazarlar=test_dosya_oku.read().strip().split()
      for test_adi in test_yazarlar:
            test_data = open("test-verileri\\sonuc\\"+test_adi+".txt", "r").read()
            test_data = test_data.split(",")
            test_data = list(test_data)
            del test_data[-1]
      print u"Test Verileri Alındı."

def en_yakin_k_komsu(k):
      egitim_dosya_oku=open("egitim-verileri\\duzenli\\yazarlar.txt", "r")
      egitim_yazarlar=egitim_dosya_oku.read().strip().split()
      sonuclar = {}
      for yazar_adi in egitim_yazarlar:
            egitim_data = open("egitim-verileri\\sonuclar\\"+yazar_adi+".txt", "r").read()
            egitim_data = egitim_data.split(",")
            egitim_data = list(egitim_data)
            del egitim_data[-1]
            toplam = 0
            for siklik in range(len(egitim_data)):
                  toplam += ((float(egitim_data[siklik])-float(test_data[siklik]))**2)
            sonuclar[yazar_adi]=(sqrt(toplam))
      sonuclar = sorted(sonuclar.items(), key=operator.itemgetter(1))
      en_yakin_k_komsu_sonuc_yaz = open("SONUC.txt",  "w")
      for sonuc in range(k):
            en_yakin_k_komsu_sonuc_yaz.write("En Yakın "+str(sonuc+1)+". Tahmin= "+str(sonuclar[sonuc])+"\n")
      en_yakin_k_komsu_sonuc_yaz.close()
      print u"En Yakın K-Komşu Algoritması Uygulandı."
      print u"Sonuclar Gösteriliyor."
      os.system('sonuc.bat')


egitim_isim_duzenle()
test_isim_duzenle()
egitim_metin_duzenle()
test_metin_duzenle()
kelimeler()
egitim_kelime_say()
test_kelime_say()
test_data_al()
en_yakin_k_komsu(10)
