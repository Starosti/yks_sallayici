
# == FULL SALLAMA YKS İÇİN ==
# yanlış olasılığı = 4/5
# doğru olasılığı = 1/5

# her doğru = +1 net
# her yanlış = -0.25 net
# o zaman nötr için her doğru başına 4 yanlış gerekli

# deneysel olasılık için py=

import numpy as np
from sys import argv as args
#p = doğru sayısı, s= seçenek sayısı, tk= tekrar sayısı, prn= print bool,tkmax = const tk
soru =120
s =5
tk =10
p = 0.0
net = 0
prn="a"
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

tmax = tk
#yüzde,net
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
		r = np.random.randint(s)
		prwc("["+str(x+1) +"] = "+ str(r)+" | net="+str(net),"e")
		if r == 0 : 
			p=p+1
			net= net+1.25
			prwc(" **DOĞRU** ="+str(p),"e")
		net = net-0.25
		prwc("","")
	yzd = (float(p)/soru)*100
	dk["tkyzd"+str(tk)]=yzd
	dk["tkyp"+str(tk)]=net
	rprn("\n"+str(p)+" doğru, "+str(soru-p)+" yanlış \n"+"%"+str(yzd)+"\n"+str(net)+"net")
	tk= tk-1
	net = 0
	p= 0
yzdS= [val for key, val in dk.items() if "yzd" in key] 
pS=[val for key, val in dk.items() if "yp" in key] 
yzdSP = sum(yzdS)/len(yzdS)
pSP = sum(pS)/len(pS)
print("\n==SONUÇ=="+"\nYapılan test:\n"+"Tekrar başına soru:"+str(soru)+", seçenek miktarı:"+str(s)+", tekrar miktarı:"+str(tmax)+"\nNet ortalaması="+str(pSP)+" Yüzde ortalaması=%"+str(yzdSP))