#                                      ----------- THRESHOLDING -----------

# Thresholding yani eşikleme, görüntüdeki her bir piksel değerini belirlediğimiz veya belirlenen eşik değeri ile 
# karşılaştırılması, sonrasında bu piksel değerinin eşik değerden küçük olması durumunda piksel değerinin 0'a
# büyük olması durumunda ise belirlenen maksimum değere eşitlenmesi işlemidir.

# 3 çeşit thresholding vardır. Bunlar :
#       Simple Thresholding
#       Adaptive Thresholding
#       Otsu's Thresholding


#                                                ----------- Simple Thresholding -----------

# Görüntüdeki her piksel için aynı threshold (eşik) değeri ile karşılaştırma yapılır. Eğer ki pikselin değeri eşik değerden küçük ise 
# piksel değeri 0 olarak, büyük ise fonksiyona girilen maksimum değer olarak ayarlanır.

# Simple Thresholding'i uygulamak için cv2 modülü içerisindeki threshold() fonksiyonu kullanılır. Aldığı parametrelere bakarsak :
#       cv2.threshold(src, thresh, maxval, type)  
#       src : kaynak görüntü, burada dikkat edilmesi gereken nokta kaynak görüntünün grayscale (gri tonlu) olmasıdır.
#       thresh : threshold (eşik) değeri, piksel değerlerini sınıflandırmak için kullanılır. Buna göre 0 veya max değer atanır.
#       maxval : threshold (eşik) değeri üzerinde olan piksellere atanan maksimum değerdir.
#       type : Uygulamak istediğimiz thresholding (eşikleme) türünü temsil eder. cv2 modülü bize birden fazla türde thresholding sağlar.
#              Bunlar : 
#              - cv2.THRESH_BINARY  --> eşik değerden aşağıdaki pikselleri 0 yani siyah, yukarıdaki pikselleri girilen max.değer yapar.       
#              - cv2.THRESH_BINARY_INV   --> eşik değerden aşağıdaki pikselleri max. değer, yukarıdaki pikselleri 0 yani siyah yapar.               
#              - cv2.THRESH_TRUNC   --> eşik değerden aşağıdaki piksellere aynı piksel değerini, yukarıdaki piksel değerleri için eşik değerini atar.       
#              - cv2.THRESH_TOZERO -->  eşik değerden aşağıdaki pikseller için 0 yani siyah, yukarıdaki piksel değerleri için aynı piksel değerini atar.        
#              - cv2.THRESH_TOZERO_INV  --> eşik değerden aşağıdaki piksel değeri için aynı piksel değerini, yukarıdaki piksel değerleri için 0 yani siyah değerini atar.        

# threshold() metodu 2 tane çıktı döndürür. Birincisi kullanılan threshold (eşik) ve ikincisi ise thresholded image yani eşiklenen resim.
# Bu yüzden bu fonskiyonu kullanırken 2 adet değişken tanımlayıp atamasını öyle yapmamız gerekiyor. Örnek vermek gerekirse :
# ret,simpleThreshold = cv2.threshold(image, thresh, maxval, type)

# simple thresholding'de 6 adet tür olduğu için pyplot kütüphanesini kullanarak bunların her birini tek bir pencere üzerinde gösterelim.

import cv2
from matplotlib import pyplot as plt

# kaynak görüntümüzü tanımladık
image = cv2.imread("Images//fingerPrint.png",0)
#cv2.imshow("orijinal", image)

# örnek olması açısından tek bir türü göstermek için kaynak görüntümüze simple thresholding uyguladık.
ret1,simpleTresholding1 = cv2.threshold(image, 80, 255, cv2.THRESH_BINARY)
#cv2.imshow("simple thresholding", simpleTresholding1)

# Şimdi ise simple thresholding içerisindeki tüm türler/types arasındaki farkı görmek için bunları pyplot ile tek bir pencerede gözlemleyelim.

ret2,simpleTresholding2 = cv2.threshold(image, 80, 255, cv2.THRESH_BINARY_INV)
ret3,simpleTresholding3 = cv2.threshold(image, 80, 255, cv2.THRESH_TRUNC)
ret4,simpleTresholding4 = cv2.threshold(image, 80, 255, cv2.THRESH_TOZERO)
ret5,simpleTresholding5 = cv2.threshold(image, 80, 255, cv2.THRESH_TOZERO_INV)

titles = ["Orijinal", "Binary", "Binary Inv", "Trunc", "To Zero", "To Zero Inv"]
images = [image, simpleTresholding1, simpleTresholding2, simpleTresholding3, simpleTresholding4, simpleTresholding5]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i], 'gray', vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()


#                                                ----------- Adaptive Thresholding -----------

# Simple Thresholding'de threshold (eşik) değeri olarak tek bir değer kullanmıştık. Bu durum, görüntünün farklı bölgelerinde farklı aydınlatma
# şartları olduğu gibi tüm durumlar için iyi bir seçenek olmayabilir.

# Bu durumda yardımımıza "Adaptive Thresholding" yetişiyor.
# Adaptive Threshold'da ki algoritma pikselin etrafındaki belirlenen alana göre bir threshold (eşik) değeri tanımlıyor.
# Bu sayede aynı görüntü içerisinde farklı bölgeler için farklı threshold (eşik) değeri elde etmiş oluyoruz bu da değişken aydınlatmaya sahip
# görüntüler için daha iyi sonuçlar almamıza olanak sağlıyor. 

# Görüntümüze adaptive thresholding uygulamak için cv2 modülü içerisindeki "adaptiveThreshold()" fonksiyonunu kullanırız. Gelin aldığı parametrelere bakalım :
#       cv2.adaptiveThreshold(src, maxval, adaptiveMethod, thresholdType, blockSize, C)  
#       src : kaynak görüntü, burada dikkat edilmesi gereken nokta kaynak görüntünün grayscale (gri tonlu) olmasıdır.
#       maxval : threshold (eşik) değeri üzerinde olan piksellere atanan maksimum değerdir.
#       adaptiveMethod : threshold (eşik) değerinin nasıl hesaplanacağını belirten parametredir. Bunun için 2 yöntem kullanılabilir :
#                        1 - cv2.ADAPTIVE_THRESH_MEAN_C --> threshold (eşik) değeri pikselin etrafındaki komşu piksel değerlerinin ortalamasından
#                            C sabitinin çıkarılmasıyla hesaplanır. Pikselin ne kadarlık bir alanındaki komşu pikselleri kapsadığını diğer bir 
#                            parametre olan "blockSize" ile belirleriz. blockSize * blockSize'lık bir alanı hesaba katar.  
#                        2 - cv2.ADAPTIVE_THRESH_GAUSSIAN_C --> threshold (eşik) değeri pikselin etrafındaki komşu piksel değerlerinin gaussian
#                            ağırlık toplamından C sabitinin çıkarılmasıyla hesaplanır. Pikselin ne kadarlık bir alanındaki komşu pikselleri 
#                            kapsadığını diğer bir parametre olan "blockSize" ile belirleriz. blockSize * blockSize'lık bir alanı hesaba katar.
#       thresholdType : Uygulamak istediğimiz thresholding (eşikleme) türünü temsil eder. cv2 modülü bize birden fazla türde thresholding sağlar.
#              Bunlar : 
#              - cv2.THRESH_BINARY  , cv2.THRESH_BINARY_INV , cv2.THRESH_TRUNC , cv2.THRESH_TOZERO , cv2.THRESH_TOZERO_INV
#       blockSize : hesaplamaya dahil edilecek komşu alanın (neighbourhood area) boyutunu belirler.
#       C : Komşu piksellerin ortalamasından veya gaussian ağırlıklı toplamından çıkarılan bir sabittir.

# adaptiveThreshold() fonksiyonu işlem sonucunda tek bir değer döndürür, threshold() fonksiyonu 2 adet değer döndürüyordu.

image2 = cv2.imread("Images//crossword.png",0)

ret6, th1 = cv2.threshold(image2, 120, 255, cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(image2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3)
th3 = cv2.adaptiveThreshold(image2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 3)

titles2 = ["Orijinal", "Constant (Global) Thresholding, V = 120", "Adaptive Mean Thresholding", "Adaptive Gaussian Thresholding"]
images2 = [image2, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images2[i], 'gray')
    plt.title(titles2[i])
    plt.xticks([])
    plt.yticks([])

plt.show()


#                                                ----------- Otsu's Thresholding -----------
# Simple Thresholding'de threshold (eşik) değeri olarak keyfi olarak seçilen bir değer kullanıyorduk. Tersine Otsu's metodunda bir değer seçmek 
# zorunda kalmayız ve bu değeri kendisi otomatik olarak belirler.

# Görüntü histogramının sadece iki tepeden meydana geldiğini, ve 2 farklı görüntü değeri olan bir görüntü düşünün. Etkili bir threshold (eşik)
# bu iki tepe değerlerinii ortasında olur.

# Benzer bir şekilde Otsu's Metodu, görüntünün histogramından en optimal threshold (eşik) değerini kendisi tanımlıyor.

# Bu işlemi yapmak için cv2 modülü içerisindeki "threshold()" fonksiyonunu kullanırız ve "cv.THRESH_OTSU" ekstra argüman olarak eklenir.
# threshold değeri keyfi olarak seçilebilir, sonrasında algoritma optimal threshold değerini bulur ve ilk çıktı olarak döndürür.

# simple thresholding
ret7,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)

# otsu's thresholding
ret8,thresh2 = cv2.threshold(image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Gaussian filtering'den sonra Otsu's thresholding
blur = cv2.GaussianBlur(image,(5,5),0)
ret9,thresh3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Tüm görüntü ve görüntülerin histogramlarını çizdirme
images3 = [image, 0, thresh1,
          image, 0, thresh2,
           blur, 0, thresh3]

titles3 = ['Original Image','Histogram','Simple Thresholding (v=127)',
          'Original Image','Histogram', "Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images3[i*3],'gray')
    plt.title(titles3[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images3[i*3].ravel(),256)
    plt.title(titles3[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images3[i*3+2],'gray')
    plt.title(titles3[i*3+2]), plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()