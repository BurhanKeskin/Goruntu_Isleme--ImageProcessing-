#                                     ------------------ Bitwise Operatörleri ------------------
# Bitwise bir diğer adıyla mantık öperatörlerinin görüntü işlemedeki çalışma mantığına yakından bakalım.
# Görüntümüzdeki siyah pikseller 0, beyaz pikseller ise 1 olarak algılanır.
# Sonrasında ise iki görüntüdeki pikseller kullandığımız operatöre göre 1 veya 0 olarak çıktı olarak yeni görüntüyü oluşturur.

# Burada kullanacağımız bitwise operatörleri : AND - OR - XOR - NOT
# AND : İki görüntüden ele alınan pikseller 1 yani beyaz ise çıktı olarak 1 (beyaz) döndürür, diğer tüm durumlarda 0 (siyah) döndürür.
# OR : İki görüntüden ele alınan pikseller 0 (siyah) ise çıktı olarak 0 (siyah) döndürür, diğer tüm durumlarda 1 (beyaz) döndürür.
# XOR : İki görüntüden ele alınan piksellerin aynı olduğu durumlarda 0 (siyah), farklı olduğu durumlarda 1 (beyaz) döndürür.
# NOT : Girdi olarak verilen görüntüdeki 0 (siyah) olan pikselleri 1 (beyaz), 1 (beyaz) olan pikselleri 0 (siyah) olarak tersine çevirir.

# Tüm bu işlemleri gerçekleştirebilmek için cv2 modülü içerisinde bulunan "bitwise_and()", "bitwise_or()", "bitwise_xor()" ve "bitwise_not()"
# fonksiyonlarından yararlanırız.

# Fonksiyonların aldıkları parametrelere bakacak olursak :
#       --> bitwise_and(src1, src2)
#       --> bitwise_or(src1, src2)
#       --> bitwise_xor(src1, src2)
#       --> bitwise_not(src1)

#       src1 : üzerinde işlem yapılacak birinci kaynak görüntü 
#       src2 : üzerinde işlem yapılacak ikinci kaynak görüntü

import cv2
from matplotlib import pyplot as plt

image1 = cv2.imread("Images//bitwise1.png")
image2 = cv2.imread("Images//bitwise2.png")

bitwiseAnd = cv2.bitwise_and(image1,image2)
bitwiseOr = cv2.bitwise_or(image1,image2)
bitwiseXor = cv2.bitwise_xor(image1,image2)
bitwiseNot = cv2.bitwise_not(image1)

titles = ["image 1", "image 2", "bitwise_and", "bitwise_or", "bitwise_xor", "bitwise_not"]
images = [image1, image2, bitwiseAnd, bitwiseOr, bitwiseXor, bitwiseNot]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()