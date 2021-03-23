
# YKS Sallayıcı

Verdiğiniz sayılara göre rastgele seçeceğiniz şıklar ile alacağınız puanı deneysel olasılık ile hesaplar.

## Gereklilikler (Requirements)

numpy

## Kullanım

    yks_salla.py [-soru] [-sec] [-tk] [-prn] 

- `-soru`: Soru sayısı. Default 120, n>1 ve int
- `-sec`: Sorudaki seçenek sayısı.Default 5, n>2 ve int
- `-tk`: Tekrar sayısı. Tekrar sayısını arttırmak daha doğru bir olasılık verebilir.Default 10, n>1 ve int
- `-prn`: Printleme boolu. Eğer farklı giriş yapılmazsa otomatik olarak sadece tekrarlar için çıktı verir. Seçenekler:

- `true`,`t`: Her çözülen soru başına detaylı çıktı verir.
- `ff`: Sadece sonuç çıktısı verir.