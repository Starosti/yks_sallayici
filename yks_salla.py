
# == FULL SALLAMA YKS İÇİN ==
# yanlış olasılığı = 4/5
# doğru olasılığı = 1/5

# her doğru = +1 net
# her yanlış = -0.25 net
# o zaman nötr için her doğru başına 4 yanlış gerekli

# <== 4 soru için bütün olasılıklar ==>
# a= 4 y 0 d (-1.00) = (0.8)^4 = 0.4096 = 256/625
# b= 3 y 1 d (+0.25) = (0.8)^3.(0.2)^1 = 0.1024 = 64/625
# c= 2 y 2 d (+1.50) = (0.8)^2.(0.2)^2 = 0.0256 = 10000/390625 = 625.16/625.625 = 16/625
# d= 1 y 3 d (+2.75) = (0.8)^1.(0.2)^3 = 0.0064 = 100/15625 = 20/3125 = 4/625
# e= 0 y 4 d (+4.00) = (0.2)^4 = 0.0016 = 1/625
# toplam faktör = 0.5456
# kâr olasılığı = b+c+d+e-a/0.5456 = 0.4985~

# kar / zarar hesaplanarak mantık olaslığı

# [16*(4)+64*(2.75)+256*(1.50)+1024*(0.25)+4096*(-1.00)]/5456
# [64+176+384+256-4096]/5456
# -3216/5456
# -0.58944~

# yani full blind sallama yapılmamalı, 100 soruda -59 net xd

# permütasyon = (a) (b) (c) (d) (e)
# tüm evren = 5^4 = 625
# 4y 0d = 1 tane
# 3y 1d = 4
# 2y 2d = 6
# 1y 3d = 4
# 0y 4d = 1
# toplam 16 olasılık

#olaslık ile =
# 4y 0d = 1/16*.4096 =.0256
# 3y 1d = 4/16*.1024 =.4096
# 2y 2d = 6/16*.0256 =.0096
# 1y 3d = 4/16*.0064 =.
# 0y 4d = 1/16*.0016 =

# iki soruda
# 0d 2y(-0.50) = 16/25
# 1d 1y(+0.75) = 8/25
# 2d 0y(+2.00) = 1/25

#2y = -0.32
#1d1y = 0.24
#2d = 0.8

# deneysel olasılık için py=

from numpy import random
import numpy as np
from sys import argv as args
#p = doğru sayısı, s= soru sayısı, tk= tekrar sayısı, prn= print bool,tkmax = const tk
soru =0
s=0
tk=0
p = 0.0
puan = 0
prn=""
for xx in range(len(args)):
	x = args[xx]
	if x=="-soru":
		soru=int(args[xx+1])
	if x=="-sec":
		s=int(args[xx+1])
	if x=="-tk":
		tk=int(args[xx+1])
	if x=="-prn":
		prn=str(args[xx+1]).lower()
if soru == s == tk == 0 or prn=="":
	soru = int(input("soru?"))
	s = int(input("seçenek?"))
	tk = 1
	tk = int(input("tekrar?"))
	prn = "e"
	prn = input("print?").lower()

tmax = tk
#yüzde,puan
dk = {}
print("")
def prwc(x,y):
	if prn == "true" or prn=="t":
		if y == "e":
			print(x,end="")
			return
		print(x)
def rprn(x):
	if prn =="ff":
		return
	print(x)

while tk>0:
	rprn("-----------------------------------------------------------------------------"+"\nTEKRAR "+str(tmax-tk+1)+"\n-----------------------------------------------------------------------------")
	for x in range(soru):	
		r = random.randint(s)
		prwc("["+str(x+1) +"] = "+ str(r)+" | puan="+str(puan),"e")
		if r == 0 : 
			p=p+1
			puan= puan+1.25
			prwc(" **DOĞRU** ="+str(p),"e")
		puan = puan-0.25
		prwc("","")
	yzd = (float(p)/soru)*100
	dk["tkyzd"+str(tk)]=yzd
	dk["tkyp"+str(tk)]=puan
	rprn("\n"+str(p)+" doğru, "+str(soru-p)+" yanlış \n"+"%"+str(yzd)+"\n"+str(puan)+"puan")
	tk= tk-1
	puan = 0
	p= 0
yzdS= [val for key, val in dk.items() if "yzd" in key] 
pS=[val for key, val in dk.items() if "yp" in key] 
yzdSP = sum(yzdS)/len(yzdS)
pSP = sum(pS)/len(pS)
print("\n==SONUÇ=="+"\nPuan ortalaması="+str(pSP)+" Yüzde ortalaması="+str(yzdSP))