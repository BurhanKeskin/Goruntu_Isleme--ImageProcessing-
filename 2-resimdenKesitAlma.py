import cv2

image = cv2.imread("Images//f1.png")
cv2.imshow('Lewis "Fucking" Hamilton', image)

#                                  RESİMİN BELLİ ALANINI KESME/KIRPMA
# köşeli parantez içinde iki nokta kullanarak y ve x ekseninde belirlediğimiz aralıkta kalan resmi kırpıp değişkenin içine atabiliriz.
# burada 250:500 ifadesi y ekseninde sol üst köşeden referans alarak aşağı doğru git 250.piksel ile 500.piksel arasında
# kalan alanı seç
# aynı işlem 300:700 ifadesi ile x ekseninde de yapılır ve resmin belli bir alanı seçilir.
# dikkat etmen gereken nokta köşeli parantez içindeki 1.parametre y eksenini, 2.parametre ise x eksenini temsil eder.
croppedImage = image[250:500, 300:700]   #y, x
#cv2.imshow("Croped Image", croppedImage)

#                                KESİLEN RESMİ BAŞKA BİR RESMİN ÜZERİNE YAPIŞTIRMA
# yukarıda kestiğimiz resim parçasını başka bir resmin üzerine istediğimiz alana yapıştırmak isteyelim.
# bunun için önce imread() ile başka bir resim tanımlaması yapalım
image2 = cv2.imread("Images//tokyo2.jpg")

# resim tanımlamasını yaptıkktan sonra o resimde belirlediğin y ve x aralıklarından oluşan bölgeye önceden kırptığın
# resmi atama yaparak başka bir resmin üzerine ekleyebiliriz.
# burada dikkat etmemiz gereken nokta ana resimde seçtiğin piksel aralıklarının kırptığın resmin aralıkları ile aynı olması
# mesela yukarıda kırptığımız resmin y aralığı 250 px, x aralığı 400 px iken ana resimde seçtiğimiz alanın da
# y ve x eksenlerinde aynı px değerine sahip aralık yazmamız gerekiyor. 
image2[430:680, 200:600] = croppedImage
#cv2.imshow("Üst üste resim", image2)


# RESİME FİLTRE EKLEME / RENK KANALLARI ÜZERİNDE DEĞİŞİKLİK YAPMA
# köşeli parantez içinde 3.parametre yerinde üzerinde değişiklik yapmak istediğimiz renk kanalının indeksi yazılır.
# Biz BGR Renk düzeninde çalışıyoruz yani Blue - Green - Red. Burada Blue kanalının indeksi 0, Green kanalının 1 ve
# Red kanalının indeks numarası ise 2'dir. Bunları son parametre yerine yazarak üzerinde değişiklikler yapabiliriz.
# resmin tamamı üzerinde red kanalının renk değerini 255 yaptık.
image2[ : , : , 2] = 255
cv2.imshow("1", image2)

# RESİMİN BELLİ ALANINI BOYAMA
# belirttiğimiz resimin girdiğimiz piksel aralığında oluşan kısımdaki pikselleri eşitliğin sağında belirttiğimiz renkten yap
image2[200:500, 300:700] = (0, 121, 65)
cv2.imshow("2", image2)

cv2.waitKey(0)
cv2.destroyAllWindows()