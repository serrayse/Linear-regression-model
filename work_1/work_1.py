# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 09:36:51 2024

@author: aserrasimsek
"""

#Ayse Serra Simsek

import numpy as np
import matplotlib.pyplot as plt

# Veri setinin parametrelere uygun sekilde iceri aktarılmasi
veri = np.loadtxt('samples.txt')
x = veri[:, 0]
y = veri[:, 1]

# w1 ve w0 parametrelerinin hesaplanmasi
N = 100 #sample sayısı
x_mean = np.mean(x)
r_mean = np.mean(y)

num = np.sum(x * y) - (x_mean * r_mean) * N
den = np.sum(x ** 2) - N * (x_mean ** 2)

w1 = num / den
w0 = r_mean - w1 * x_mean

# Veri noktalarinin grafikte gosterilmesi
plt.scatter(x, y, color='purple', label='Veri Noktaları')

# Regresyon modeline gore dogrunun cizilmesi
plt.plot(x, w1 * x + w0, color='black', label='Doğru Çizgisi')
plt.title('Lineer Regresyon Modeli')
plt.xlabel('X ekseni')
plt.ylabel('Y ekseni')
plt.legend()
plt.show()

# Hesaplanan w1 ve w0 parametrelerinin yazdirilmasi
print(f"w1(egim) parametresi: {w1}")
print(f"w0(kesme noktasi) parametresi: {w0}")