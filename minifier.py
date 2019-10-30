# -*- coding: utf-8 -*-
import sys
import requests

def ascii():
    print("""


  _____   _____  _____ 
 / ____| / ____|/ ____|
| |     | (___ | (___  
| |      \___ \ \___ \ 
| |____  ____) |____) |
 \_____||_____/|_____/ 
                                  
 __  __  _____  _   _  _____  ______  _____  ______  _____  
|  \/  ||_   _|| \ | ||_   _||  ____||_   _||  ____||  __ \ 
| \  / |  | |  |  \| |  | |  | |__     | |  | |__   | |__) |
| |\/| |  | |  | . ` |  | |  |  __|    | |  |  __|  |  _  / 
| |  | | _| |_ | |\  | _| |_ | |      _| |_ | |____ | | \ \ 
|_|  |_||_____||_| \_||_____||_|     |_____||______||_|  \_\
                                                            


Thx To Ardho
go follow Ig
https://instagram.com/ardho.ainullah

Support by 
Fakhri Alauddin
https://instagram.com/fakhrialauddin13

""")


ascii()

try:
    css_file = input("==> Masukkan File (/path/file.css) : ")
    with open(css_file, 'r') as c:
         css = c.read()
         
except FileNotFoundError:
       sys.exit("==> File Tidak Ditemukan")

payload = {'input': css}
url = 'https://cssminifier.com/raw'
print("Requesting mini-me of {}. . .".format(c.name))
result = requests.post(url, payload).text

rename = input("==> Mau Ganti Nama File? (default:file.min.css) (y/n) : ")
if rename.upper() == "Y":
    named = input("==> Input Nama File Baru (ex: script.min.css) : ")
elif rename.upper() == "N":
    named = "file.min.css"
else:
    print("[! Option False]");sys.exit()

with open(named, 'w') as m:
    m.write(result)

print("Minification complete. See {}".format(m.name))