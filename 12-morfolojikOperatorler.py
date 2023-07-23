# Öncelikle Morfoloji, biçim ya da yapı anlamına gelmektedir.
# Morfolojik işlemlerdeki amacımız ise bir yapılandırma elemanı kullanarak (kernel, yani zeros() veya ones() fonksiyonları ile oluşturduğumuz yapılar)
# nesnelerin,görüntülerin biçimini dönüştürmektir.


#                                         ---------------- MORFOLOJİK OPERATÖRLER ----------------
# Bir görüntünün şekline bağlı olarak yapılan basit işlemlere morfolojik dönüşümler denir.
# Morfolojik işlemler, görüntüyü şekle göre işleyen Görüntü işleme tekniklerinden biridir.
# Bu morfolojik işlemler genellikle ikili (binary) görüntüler üzerinde uygulanır.

# Morfolojik işlemler için önemli olan bir diğer gereksinim ise görüntü üzerinde işlem yapabilmek için 1'lerden oluşan bir kernel yapısıdır.
# bunu numpy kütüphanesi içerisinde bulunan ones() fonksiyonu ile elde ederiz.
# Daha önceki konularda yine numpy kütüphnasi içerisinde bulunan zeros() fonksiyonunu kullanmıştık, aklınıza şu soru gelebilir -
# "peki şimdi burada neden zeros() değil de ones() fonksiyonunu kullanıyoruz ? "
# Cevabını şöyle açıklayayım, birazdan morfolojik fonksiyonları kullanınca daha iyi göreceksiniz, bu fonksiyonlar içerisine kaynak resim ile 
# kernel yapısını ve son olarak iterasyon değerini parametre olarak yazarız. Burada - fonksiyon içerisinde - kernel yapısı içerisindeki değer ile 
# kaynak görüntüsündeki piksellerin değerleri çarpılarak iterasyon değerine göre gerekli işlemler uygulanır.
# gerekli işlemlerden kastım eğer Erosion işlemi için erose() fonksiyonunu kullandıysak görüntünün sınırlarını aşındırma işlemi yapılır. gibi gibi
# Eğer ki kernel yapısını zeros() ile tanımlarsak görüntüdeki tüm piksel değerleri 0 ile çarpılır ve finalde her bir piksel değeri için
# 0 değerini alırız, sonuç olarak elimizde görüntü olmaz.
# lakin burada olduğu gibi ones() ile tanımlarsak görüntünün piksel değerleri 1 değerleri ile çarpılır ve orijinal piksel değerlerinin üzerine
# istediğimiz morfolojik işlemler uygulanır.

# OpenCV'de bulunan temel Morfolojik Operatörler şunlardır :
    # Erosion
    # Dilation
    # Opening
    # Closing
    # Morphological Gradient
    # Top hat
    # Black hat

# Burada önemli olan nokta "Erosion" ve "Dilation" işlemleri dışındaki diğer tüm morfolojik işlemler için cv2 modülü içerisinde bulunan "morphologyEx()"
# fonksiyonunu kullanırız. Kullanmak istediğimiz işlemleri bu fonksiyon içerisine parametre olarak girerek kullanırız.

# Kısaca "morphologyEx()" fonksiyonun aldığı parametre yapısına bir bakalım.
# morphologyEx(src, op, kernel, iterations = )
# src : üzerinde işlem yapacağımız temel görüntü değişkeni
# op : Uygulayacağımız morfolojik operatör tipi
#      -> Opening için : cv2.MORPH_OPEN
#      -> Closing için : cv2.CLOSE
#      -> Morphological Gradient için : cv2.GRADIENT
#      -> Top Hat için : cv2.TOPHAT
#      -> Black Hat için : cv2.MORPH_BLACKHAT

  
# En yaygın kulanılan 2 dönüşüm ise "Erosion" ve "Dilation" işlemleridir.

#                                                     ---------- EROSION ----------
# Erosion (erezyon/aşınma), ön plandaki (foreground) görüntünün dış yüzeyinin/sınırlarının aşındırılmaasını sağlar.
# Bu işlem beyaz gürültülerin giderilmesi için kullanışlıdır dolayısıyla ön planın beyaz olması önerilir.

# Erosion işlemi için cv2 modülü içerisindeki "erode()" fonksiyonu kullanılır, fonksiyonun aldığı parametrelere bakacak olursak :
#                        erode(src, kernel, iterations = )
# src : üzerinde erosion işlemini uygulamak istediğimiz temel görüntü
# kernel : numpy modülü içerisindeki ones() fonksiyonu ile oluşturduğumuz kernel yapısını tutan değişkenin adı
# iterations = : uygulanacak erosion işleminin şiddetini yani o işlemin kaç defa yapılacağını belirtir, eğer ki iterations = 1 yazarsak bu işlem
# 1 defa uygulanır, eğer ki iterations = 2 yaparsak erosion işlemi 2 defa uygulanır ve daha ince/aşınmış bir görüntü elde etmiş oluruz, gibi gibi devam eder.
 

#                                                     ---------- DILATION ----------
# Erosion işleminin tam tersi gibi düşünülebilir.
# Ön plandaki (foreground) görüntünün dış yüzeyinin/sınırlarının genişletilmesini sağlar.

# Dilation işlemi için cv2 modülü içerisindeki "dilate()" fonksiyonu kullanılır, fonksiyonun aldığı parametrelere bakacak olursak :
#                        dilate(src, kernel, iterations = )
# src : üzerinde dilation (genişletme) işlemini uygulamak istediğimiz temel görüntü
# kernel : numpy modülü içerisindeki ones() fonksiyonu ile oluşturduğumuz kernel yapısını tutan değişkenin adı
# iterations = : uygulanacak dilation işleminin şiddetini yani o işlemin kaç defa yapılacağını belirtir, eğer ki iterations = 1 yazarsak bu işlem
# 1 defa uygulanır, eğer ki iterations = 2 yaparsak dilation işlemi 2 defa uygulanır ve daha geniş bir görüntü elde etmiş oluruz sanki 
# ön plandaki görüntüye border eklenmiş gibi düşünebilirsiniz.


import cv2
import numpy as np

image = cv2.imread("Images//text.png")
#cv2.imshow("default", image)

kernel = np.ones((5,5), np.uint8)

expandedImage = cv2.dilate(image, kernel, iterations=1)
cv2.imshow("Expanded Image", expandedImage)

# göreceğiniz üzere gürültülü bir resime dilation işlemi uygulandığında görüntüdeki gürültüler daha da belirgin hale geldi ve hiç hoş bir durum değil.

# eğer ki gürültülü bir resim üzerinde dilation işlemi yaparsak bu görüntü üzerindeki gürültülerin artmasına yol açar
# o yüzden gürültülü bir görüntüyü temiz bir şekilde genişletmek yani dilation işlemi uygulamak istersek öncelikle bu görüntüye erosion işlemi
# uygulayıp görüntüdeki gürültülerden arındırıp daha sonrasında dilation işlemi yaparak ana görüntüyü genişletmek en sağlıklı yoldur.

# şimdi gelin ilk olarak baştaki gürültülü görüntümüze erosion işlemi uygulayalıp gürültüleri kaldıralım ve sonrasında erosion uygulanmış 
# görüntünün üzerine dilation işlemi uygulayarak elde ettiğimiz görüntüye bir daha bakalım.  

erosedImage = cv2.erode(image, kernel, iterations=1)
expandedImage2 = cv2.dilate(erosedImage, kernel, iterations=1)
cv2.imshow("Expanded Image after Erosion", expandedImage2)


#                                                     ---------- OPENING ----------
# Opening işlemi iki temel method'un birleşiminden oluşur.
# Opening işlemi, temelde bir görüntüye sırasıyla "erosion" ve ardından "dilation" işlemlerinin uygulanmasıdır.
# Genellikle görüntüdeki gürültüleri kaldırmak için başvurduğumuz bir işlemdir.
# Temel iki işlemi tek bir fonksiyonla yapmamızı sağlar başka herhangi bir farkı yoktur.

# HATIRLATMA : "Erosion" ve "Dilation" işlemleri dışındaki diğer tüm morfolojik işlemler için cv2 modülü içerisinde bulunan "morphologyEx()"
# fonksiyonunu kullanırız.

opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow("opening", opening)

#                                                     ---------- CLOSING ----------
# Closing işlemi de iki temel method'un birleşiminden oluşur.
# Closing işlemi, temelde bir görüntüye sırasıyla "dilation" ve ardından "erosion" işlemlerinin uygulanmasıdır.
# Genel olarak bir görüntüde ön planda (foreground) bulunan nesnede aralıklar/kesiklikler varsa closing işlemi uygulanır.

imageForClosing = cv2.imread("Images//textForClosing.png")
closing = cv2.morphologyEx(imageForClosing, cv2.MORPH_CLOSE, kernel)
cv2.imshow("closing", closing)


#                                                     ---------- Morphological Gradient ----------
# Morphological Gradient, temelde kaynak görüntüye uygulanmış Dilation işlemi sonucunda elde edilen görüntüden, kaynak görüntüye uygulanmış Erosion işlemi 
# sonucunda elde edilen görüntünün çıkarılmasıyla ortaya çıkan görüntüdür.

morphologicalGradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("morphological gradient", morphologicalGradient)


#                                                     ---------- Top Hat ----------
# Top hat, kaynak görüntüden kaynak görüntüye opening işleminin uygulanmasıyla elde edilen görüntünün çıkarılması işlemidir.
# Kısaca "Top Hat = Source Image - Opening(Source Image)"

tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("top hat", tophat)


#                                                     ---------- Black Hat ----------
# Black hat, kaynak görüntüye closing işleminin uygulanmasıyla elde edilen görüntüden kaynak görüntünün çıkarılması işlemidir.
# Kısaca "Black Hat = Closing(Source Image) - Source Image"

cv2.waitKey(0)
cv2.destroyAllWindows()








