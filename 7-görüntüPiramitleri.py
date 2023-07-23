import cv2
import numpy as np

# numpy kütüphanesindeki zeros fonksiyonu ile istediğimiz boyutlara (yükseklik, genişlik, kanal sayısı) sahip bir resim
# çerçevesi,yapısı oluşturabiliriz. Bunu fonskiyonun ilk parametresine aşağıdaki gibi belirterek yapabiliriz.
# fonksiyonun 2.parametresine ise veri tipini belirtmemiz gerekiyor. Resimlerimiz 8 bitlik piksellerden oluşuyordu bu da
# "uint8" olarak geçiyor dolayısıyla bunu belirttik.
emptyImage = np.zeros((300, 300, 3), "uint8")

print(emptyImage)

cv2.waitKey(0)
cv2.destroyAllWindows()