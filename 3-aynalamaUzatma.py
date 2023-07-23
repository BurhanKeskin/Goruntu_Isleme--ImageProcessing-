import cv2

# İÇERİK : AYNALAMA - UZATMA - TEKRAR ETTİRME - ÇERÇEVE OLUŞTURMA
# cv2 kütüphanesi içinde bulunan copyMakeBorder() fonksiyonu sayesinde resim üzerinde bir çok efekti uygulayabiliriz.
# başlamadan önce fonksiyonun aldığı temel parametreler hakkında bilgi sahibi olalım.
# copyMakeBorder(src, top, bottom, left, right, borderType)
# src = bizim üzerinde oynama yapmak istediğimiz kaynak resmimiz
# top, bottom, left, right = yukarı,aşağı,sola,sağa ana resmimizin kaç pikselinin eklenmesini istediğimizi yazarız.    
# borderType = yapacağımız işleme göre "cv2.BORDER_(yapılacak işlemin adı)" yazarız.

image = cv2.imread("Images//f1.png")

#           RESMİ AYNALAMA
# resmi aynalamak için fonksiyonun içerisine gerekli parametreleri yazariz.
# aynalama yapacağımız için son parametrete "cv2.BORDER_REFLECT" yazmaliyiz.
aynalanmisResim = cv2.copyMakeBorder(image, 200,200,200,200,cv2.BORDER_REFLECT)
cv2.imshow("Tokyo Drift", aynalanmisResim)

#           RESMİ UZATMA
# resmi uzatmak için fonksiyonun içerisine gerekli parametreleri yazariz.
# uzatma yapacağımız için son parametrete "cv2.BORDER_REPLICATE" yazmaliyiz.
uzatilanResim = cv2.copyMakeBorder(image, 200,200,200,200,cv2.BORDER_REPLICATE)
cv2.imshow("Tokyo Drift", uzatilanResim)

#           RESMİ TEKRAR ETTİRME
# resmi tekrar ettirmek için fonksiyonun içerisine gerekli parametreleri yazariz.
# tekrar ettirme yapacağımız için son parametrete "cv2.BORDER_WRAP" yazmaliyiz.
tekrarEdenResim = cv2.copyMakeBorder(image, 200,200,200,200,cv2.BORDER_WRAP)
cv2.imshow("Tokyo Drift", tekrarEdenResim)

#           RESMİN ETRAFINA BORDER EKLEME
# resime border eklemek için fonksiyonun içerisine gerekli parametreleri yazariz.
# border ekleme yapacağımız için son parametrete "cv2.BORDER_CONSTANT" yazmaliyiz.
# border_constant'ı böyle bırakırsak default olarak siyah border ekler.
# borderın renk'ini değiştirmek için bir başka parametre olan value'yu eklemeliyiz ve istediğimiz BGR renk kodunu atamalıyız. 
cerceveliResim = cv2.copyMakeBorder(image, 10,10,10,10,cv2.BORDER_CONSTANT)
cerceveliResim = cv2.copyMakeBorder(image, 10,10,10,10,cv2.BORDER_CONSTANT, value=(15,62,128))
cv2.imshow("Tokyo Drift", cerceveliResim)


cv2.waitKey(0)
cv2.destroyAllWindows()
