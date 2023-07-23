#                     ------------------ Canny Kenar Algılama / Canny Edge Detection ------------------ 

# Canny Kenar Algılaması, popüler bir kenar algılama algoritmasıdır ve çok aşamalı (multi stage) bir yapısı vardır.
# 1-) Öncelikle Kenar algılama işlemi grayscale bir görüntü üzerinde gerçekleştirilebilir eğer ki görüntümüz grayscale 
#     değilse ilk olarak görüntümüze grayscale'e çevirmeliyiz.
# 2-) Kenar algılama işlemi, görüntüdeki gürültüye duyarlı olduğundan bir sonraki adım olarak Gaussian Filtrelemesi ile 
#     görüntüdeki gürültüleri kaldırmalıyız.
# 3-) Görüntünün gradyen yoğunluğunun bulunması 
#     Pürüzsüzleştirilmiş görüntü sonrasında yatay yönde (Gx) ve dikey yönde (Gy) birinci türevlerini almak için hem yatay
#     hem de dikey yönde bir Sobel Çekirdeği (yapısı) ile filtrelenir.
#     Bu iki görüntüden her piksel için kenar gradyanını ve yönünü şu şekilde bulabiliriz.
#           Egde_gradient(G) = sqrt( Gx^2 + Gy^2) 
#           Angle(θ) = tan^-1 (Gy/Gx)
#     Gradyan yönü her zaman kenarlara diktir. Dikey, yatay ve iki çapraz yönü temsil eden dört açıdan birine yuvarlanır.
# 4-) Maksimum Olmayan Bastırma (suppression)
#     Gradyan büyüklüğü ve yönü elde edildikten sonra, kenarı oluşturmayan istenmeyen pikselleri kaldırmak için tam bir 
#     görüntü taraması yapılır.
#     Bunun için her pikselde gradyan yönündeki komşuluğunda yerel bir maksimum olup olmadığına bakılır.

# 5-) Histerezis Eşikleme (Hysteresis Thresholding)
#     Bu aşamada, hangi kenarların gerçekten kenar olduğuna ve hangilerinin olmadığına karar verilir.
#     Bunun için minVal ve maxVal olmak üzere iki eşik değere ihtiyacımız var. Yoğunluk gradyanı maxVal'den fazla olan 
#     tüm kenarların kesinlikle kenar olacağına ve minVal'in altındakilerin kesinlikle kenar olmayacağına karar verilir.


# OpenCV, tüm bu işlemleri tek bir fonksiyon ile yapabilmemiz için bize "Canny()" fonksiyonunu sunuyor.
# Fonksiyonun yapısına bakacak olursak : 
#       cv2.Canny(image, threshold1, threshold2, apertureSize, L2gradient)
#           image : Üzerinde kenar algılaması gerçekleştireceğimiz kaynak görüntü.
#           threshold1 : minimum threshold (eşik) değeri.
#           threshold2 : maksimum threshold (eşik) değeri.
#           apertureSize : Görüntü gradyanlarınu bulmak için kullanılan Sobel operatörünün açıklık boyutu.
#                          Fonksiyonda bir değer atanmaz ise Default olarak 3 değeri ile işlem yapar. 
#           L2gradient : Gradyan büyüklüğünü bulmak için kullanılan eşitliği belirtir. Eğer ki True ise daha doğru/kesin olan
#                        "Edge_Gradient(G) = sqrt( Gx^2 + Gy^2 )" eşitliğini kullanır.
#                        Aksi taktirde yani false olduğu durumda ise "Edge_Gradient(G) = |Gx| + |Gy|" eşitliğini kullanır.
#                        L2gradient parametresi default olarak "false"tur.
           
import cv2
from matplotlib import pyplot as plt

image = cv2.imread("Images//mcqueen.jpg")
grayscaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gaussianBlur = cv2.GaussianBlur(grayscaleImage, (3,3), 0)

CannyMcqueen = cv2.Canny(gaussianBlur,30,255)

titles = ["Orijinal", "Canny Edge Detection"]
images = [image, CannyMcqueen]

for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()