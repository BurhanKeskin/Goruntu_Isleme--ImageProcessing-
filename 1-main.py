import cv2

# öncelikle resmimizi imread() fonskiyonu ile okuduk ve image değişkeninin içine atadık
# okumak istediğimiz resmi siyah beyaz bir şekilde okumak istiyorsak resmin dosya yolundan sonra 2.parametre olarak
# 0 yazarsak istediğimizi elde ederiz.
image = cv2.imread("Images//the boys.jpg") 

image2 = cv2.imread("Images//the boys.jpg",0) 

# sonrasında okuduğumuz resmi pencerede output olarak göstermek için imshow() fonskiyonunu kullandık
# bu fonksiyon 2 adet parametre alıyor : 1.si açılan pencerenin sol üst köşesinde yazan pencere adını belirler
# 2.si ise pencerede output olarak göstermek istediğimiz resmin imread() ile okunmuş ve içinde tutulan değişkenin adı
#       cv2.imshow("The Boys", image)

# 2.parametrede gösterdiğiniz ve okunmuş resmi 1.parametrede gösterdiğiniz isimde ve formatta ayrıyeten kaydeder.f
#       cv2.imwrite("Images/griBoys.jpg", image2)

# başta imread() ile okuduğumuz resmi print içinde çalıştırdığımızda resimdeki her bir pikselin renk detaylarını 
# (0-255 arası sayısal değerlerini) öğrenebiliriz.
# çıktıyı verirken iki boyutlu dizide nasıl dolaşılırsa ona göre sonuçları gösterir yani önce ilk satırdaki baştan sona
# tüm sütünda bulunan piksellerin bgr değerlerini basar ondan sonra bir alt satıra geçer böyle sona kadar gider.
# kısaca başta elde ettiğimiz resmin matrissel karşılığını öğrenmiş oluruz.
print(image2)

# resmin boyutunu verir yani yükseklik*genişlik*renk kanalı sayısı ile hesaplanır
print(image.size)
# resmin data type'ını döndürür bu satır için "uint8" döner yani 8 bitlik piksellerden oluşan resim
print(image.dtype)
# resmin yükseklik, genişlik ve renk kanalı sayısını döndürür. Renkli resimlerde renk kanalı 3 iken 
# siyah-beyaz resimler de 1'dir.
print(image.shape)

# RESİM ÜZERİNDE İSTEDİĞİMİZ KONUMDAKİ PİXEL'İN BGR RENK KODUNU ÖĞRENME
# print(image[(x,y)]) yazarak belirttiğimiz resimin 0'a 0 noktasından yani sol üst köşesinden x piksel aşağıda
# ve y piksel sağda bulunan piksel'in bgr renk detaylarına ulaşabiliriz.
# Örneğin image değişkenimizin (625, 2163) noktasında bulunan pikselin bgr renk detaylarını öğrenelim.
# çıktı olarak [221 161  77] sonucunu alırız. (625, 2163) noktasındaki pikselin blue değeri 221, green değeri 161 ve
# red değeri ise 77 olduğunu öğrenmiş oluruz.
print(image[(625, 2163)])

f1 = cv2.imread("Images//f1.png")  # başka bir resimi okuduk ve değişkene atadık
f1[505,612] = [255, 255, 255]    # resmimizin 505'e 612 noktasında bulunan pikselin rengini [255, 255, 255] yaptık yani kırmız
# cv2.imshow("asd", f1)  # yeni halini ekranda gösterdik

# RESMİN BELLİ BİR BÖLGESİNDEKİ PİKSELLERİN RENK'İNİ DEĞİŞTİRME
# döngüler sayesinde istediğin aralıktaki pikseller üzerinde renk değişikliği yapabiliriz.
for i in range(222, 333):
    for j in range(129, 541):
        f1[i,j] = [255, 255, 255]
        
cv2.imshow("asd", f1)        

# açılan pencereyi bir tuşa basana kadar açık tutar. Burada 0 özel bir değerdir ve sonsuza kadar pencereyi açık tutar.
cv2.waitKey(0)

# açılan pencerenin çarpısına bastıktan sonra cv2 ile ilgili ve açık olan tüm pencereleri kapatır.
cv2.destroyAllWindows()
