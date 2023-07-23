import cv2

# piksellerin renk değerlerini toplayabiliriz.Şuan ne işe yarar tam bilmiyorum
# her renk kanalının değerleri kendi arasında toplanır ve eğer bu sayi 255'i geçerse sonuç olarak 255 ile modu yazılır.
# örnek verirsem diyelim ki blue kanalının değerleri toplandı ve 355 çıktı sonuç olarak blue kanalında (355 mod 255) - 1 = 99 yazar.

image = cv2.imread("Images//cayir.jpg")

print(image[(50,101)])
print(image[(102,654)])
print(image[(50,101)] + image[(102,654)])


#                                 İKİ ADET RESMİ ÜST ÜSTE TOPLAMA
# Burada bahsettiğimiz "aynı boyutta" olan iki adet resmin aynı konumdaki piksellerinin renk değerlerinin toplanmasıdır.
# Sonuçta ortaya yeni bir resim çıkar
# Dediğim gübü burada önemli olan iki resminde aynı boyutta olması çünkü aynnı konumdaki piksellerin birbirleriyle eşleşmesi gerekiyor.

image2 = cv2.imread("Images//f1.png")

üstüste = cv2.add(image, image2)
cv2.imshow("üst üste", üstüste)

# resimleri istediğimiz oranda opaklıkta da birleştirebiliriz.
# alttaki kod image'ı %40 oranında image2'yi ise %90 oranında opaklıkta birleştiriyor. oran 0-1 arasında olmalıdır.
# son parametrede yazdığımız 0 ise gamma değerini temsil etmektedir, duruma göre onu da değiştirebilir (emin değilim ama default 0 yap geç).
üstüste2 = cv2.addWeighted(image, 0.4, image2, 0.9, 0)
cv2.imshow("üst üste 2", üstüste2)

cv2.waitKey(0)
cv2.destroyAllWindows()
