import cv2

#                  RESİMİN BELLİ BİR KISMINI DİKDÖRTGEN İÇİNE ALMA
# Bunun için cv2 kütüphanesinin bize sunduğu "rectangle()" fonksiyonunu kullanabiliriz.
# Öncesinde bu foksiyonunun aldığı parametrelere bir göz atalım.
# rectangle(src, (x0, y0), (x1, y1), color, thickness)
# src = üzerinde oynama yapacağımız kaynak resim
# (x0, y0) = resim üzerinde oluşturmak istediğimiz dikdörtgenin sol alt köşesinin x ve y koordinatları/piksel sayısı.
# (x1, y1) = resim üzerinde oluşturmak istediğimiz dikdörtgenin sağ üst köşesinin x ve y koordinatları/piksel sayısı.
# önemli olan karşı köşeli iki point girmektir yani istersen sol üst köşe ile sağ alt köşeyi de girebilirsin.
# burada istersen önce sol alt köşeyi sonra sağ üst köşeyi yaz istersen tam tersi şekilde, değişen bir şey olmuyor.
# color = çizeceğimiz dikdörtgenin renk'ini BGR türünde girmeliyiz.
# thickness = dikdörtgenin kenar kalınlığını belirler. 1-9 (dahil) arası bir rakam girebiliriz.

image = cv2.imread("Images//f1.png")
cv2.rectangle(image, (3,698), (363,104), (12,37,154), 2)
cv2.imshow("Kareli Max", image)

cv2.waitKey(0)
cv2.destroyAllWindows()