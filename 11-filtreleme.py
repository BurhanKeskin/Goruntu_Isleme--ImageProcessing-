import cv2

image = cv2.imread("Images//noisy.png")
cv2.imshow("orijinal",image)

#                                                     ------- MEAN FILTERING -------
# Mean (ortalama) Filtreleme, resimde bizim belirlediğimiz ölçüdeki bir alanda (3'e 3, 5'e 5, 7'e 7 gibi) bulunan her bir karedeki pikselin 
# renk değerlerinin toplanıp ortalamasının alınıp en sonunda başta belirlediğimiz alandaki ortada bulunan piksel yerine yazılmasıyla uygulanır 
# ve bu işlem sırasıyla tüm resim için uygulanır.
# belirlediğimiz alan büyüdükçe resimdeki gürültü miktarı azalır lakin resim daha yumuşak bir hâl alır yani resimin ana hatları kaybolmaya başlar.

meanFilter = cv2.blur(image, (3,3))
meanFilter2 = cv2.blur(image, (5,5))
meanFilter3 = cv2.blur(image, (7,7))

cv2.imshow('mean 3*3', meanFilter)
cv2.imshow('mean 5*5', meanFilter2)
cv2.imshow('mean 7*7', meanFilter3)

#                                                     ------- MEDIAN FILTERING -------
# Median Filtreleme, resimde bizim belirlediğimiz ölçüdeki bir alanda (3'e 3, 5'e 5, 7'e 7 gibi) bulunan karedeki piksellerinin renk değerlerinin 
# küçükten büyüğe doğru sıralanıp sıralama sonucu ortada bulunan değeri alıp başta belirlediğimiz alanda ortanca piksel yerine yazılmasıyla yapılır.
# bu tüm resim için adım adım uygulanır (yani ilk başta sol üst köşeden 3'e 3'lük bir alana uygulandı sonra bir piksel sağa kayar ve böyle devam eder
# sonra bir piksel aşağı iner ve soldan sağa tüm resime uygulanır.)

medianFilter = cv2.medianBlur(image,3)
medianFilter2 = cv2.medianBlur(image,5)
medianFilter3 = cv2.medianBlur(image,7)

cv2.imshow('median 3*3', medianFilter)
cv2.imshow('median 5*5', medianFilter2)
cv2.imshow('median 7*7', medianFilter3)


#                                                     ------- GAUSSIAN FILTERING -------
# Gaussian Filtreleme, resimde bizim belirlediğimiz ölçüdeki bir alanda bulunan karedeki piksellerinin ağırlıklı ortalamalarının hesaplanıp
# belirlediğimiz alandaki ortanca piksel yerine yazılmasıyla uygulanır ve adım adım tüm resim için uygulanır.
# GaussianBlur() fonksiyonunda diğer iki filtre fonksiyonuna ek olarak 3.bir parametre daha giriyoruz.
# bu fonksiyon içinde tanımlanan "sigmaX" argümanı yerine geçer.
# sigmaX argümanı, X eksenindeki/yönündeki Gaussian Kernel standart sapmasını temsil eder. 

gaussFilter = cv2.GaussianBlur(image,(3,3),0)
gaussFilter2 = cv2.GaussianBlur(image,(5,5),0)
gaussFilter3 = cv2.GaussianBlur(image,(7,7),0)

cv2.imshow('gauss 3*3', gaussFilter)
cv2.imshow('gauss 5*5', gaussFilter2)
cv2.imshow('gauss 7*7', gaussFilter3)


cv2.waitKey(0)
cv2.destroyAllWindows()