import urllib, requests
import os
from bs4 import BeautifulSoup
from goPro import GoPro

url = GoPro.GetDir(0)
#Descomentar linea para poner url manual
url = 'http://10.5.5.9:8080/DCIM/105GOPRO/'
locDir = '/home/pi/Desktop/goProPython/img/'


def DownloadAll():
   response = requests.get(url)
   soup = BeautifulSoup(response.content,'html5lib')
      
   for img in soup.findAll('a'):
      if '.JPG' in img.get('href') or '.jpg' in img.get('href'):
         if img.get('href') not in os.listdir(locDir):
            urllib.urlretrieve(url + img.get('href'),locDir + img.get('href'))
            print u'Descargando fichero %s' % img.get('href')



def ImgToTxt():
   f1 = open(locDir + "Files.txt","a+")
   allfiles = []
   while True:
      str1 = f1.readline()
      if str1 == '':
         break
      else:
         allfiles.append(str1)
   img = os.listdir(locDir)
   for i in img:
      if i not in allfiles:
         if '.jpg' in i or '.JPG' in i:
            f1.write(i + '\n')
   
   f1.close()    

def DownloadNew():
   f1 = open(locDir + "Files.txt","r")
   allfiles = []
   while True:
      str1 = f1.readline().strip()
      if str1 == '':
         break
      else:
         allfiles.append(str1)
   f1.close()
   response = requests.get(url)
   
   soup = BeautifulSoup(response.content,'html5lib')   
   for img in soup.findAll('a'):
      if '.JPG' in img.get('href') or '.jpg' in img.get('href'):
         if img.get('href') not in allfiles:
            urllib.urlretrieve(url + img.get('href'),locDir + img.get('href'))
            print u'Descargando fichero %s' % img.get('href')
   
   ImgToTxt()

DownloadNew()
