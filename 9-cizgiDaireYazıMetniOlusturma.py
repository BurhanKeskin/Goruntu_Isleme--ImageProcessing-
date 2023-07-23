import cv2
import numpy as np

# zeros fonks. ile 500'e 500'lük 3 kanallı bir pencere oluşturduk
image = np.zeros((500,500,3), dtype="uint8")

#                         ----------- ÇİZGİ OLUŞTURMA -----------
# cv2 modülü içindeki line() fonksiyonu çizgi oluşturmamızı sağlar.
# cv2.line(img: , pt1: , pt2: , color: , thickness: )

# img :  oluşturduğumuz resim penceresini yazıyoruz, istersek okuduğumuz (imread ile) hazır bir resim de yazabiliriz.
# pt1 :  çizginin başlayacağı ilk x ve y koordinatlarını tutar. (sol üst köşeden x birim sağ'da ve sol üst köşeden
# y birim aşağı bir nokta) 
# pt2 : aynı şekilde çizginin biteceği x ve y koordinatlarını tutar.
# color : çizginin rengini bgr olarak gireriz. 
# thickness : çizginin kalınlığını temsil ediyor.

cv2.line(image,(150,75),(200,250),(0,50,255),2)
#cv2.imshow("panel", image)

#                         ----------- DAİRE OLUŞTURMA -----------
# daire oluşturmak için cv2 modülü içindeki circle() fonksiyonunu kullanırız.
# cv2.circle(img: , center: , radius: , color: , thickness: )

# img : oluşturduğumuz resim penceresini yazıyoruz, istersek okuduğumuz (imread ile) hazır bir resim de yazabiliriz.
# center : dairenin orta noktasını konumlandırağımız piksel değerlerini tutar.
# radius : dairenin yarıçağını (piksel karşılığını) giriyoruz.
# color : daire çizgisinin rengini bgr olarak gireriz. 
# thickness : daire çizgisinin kalınlığını tutar.

cv2.circle(image, (250,250), 30, (0,255,35), 2)
#cv2.imshow("panel", image)

#                         ----------- YAZI YAZMA -----------
# YAZI YAZMAK için ise cv2 modülü içerisindeki putText() fonksiyonunu kullanırız.
# cv2.putText(img: , text: , org: , fontFace: , fontScale: , color: , thickness: )

# image : oluşturduğumuz resim penceresini yazıyoruz, istersek okuduğumuz (imread ile) hazır bir resim de yazabiliriz.
# text : yazdırmak istediğimiz string ifadeyi yazarız.
# org : resime yazdırdığımız yazının sol alt köşesinin koordinatlarını tutar.
# fontFace : yazının fontunu giriyoruz. örnek vermek gerekirse cv2 içindeki FONT_HERSHEY_SIMPLEX
# fontScale : fontun temel boyutu ile girilen sayının çarpımı kadar yazıyı büyütür kısaca font büyütme parametresi.
# thickness : yazı çizgisinin kalınlığını piksel cinsinden temsil eder.

image[(399,115)] = (255,255,255)
cv2.putText(image, "GubBy", (115, 399), cv2.FONT_HERSHEY_DUPLEX, 3, (255,0,0), 1)
cv2.imshow("panel", image)

cv2.waitKey(0)
cv2.destroyAllWindows()