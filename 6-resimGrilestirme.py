import cv2

image = cv2.imread("Images//f1.png")

# Resim'i grileştirmek için cv2 kütüphanesi içerisinde bulunan cvtColor yani convert color fonksiyonu ile resmimizi
# gri yapabiliriz. Kullanımı aşağıdaki gibidir.
# Resim'i grileştirdiğimizde resmin kanal sayısı 1'e düşer (normal renkli bir resimde bu değer 3'tür. BGR renk kanallarıdır)
# dolayısıyla renkli bir resim ile gri bir resmin boyutunu karşılaştırdığımızda gri resmin boyutunun renkliye oranla 1/3
# oranında olduğu görürüz. Renkli 3MB iken gri resim 1MB'tır, bu gri resimin kanal sayısının 1 olmasından ötürüdür.
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("Renkli resmin boyutu :", image.size)
print("Gri resmin boyutu : " + str(grayImage.size))


# resim'i gri yapmanın bir diğer ve pratik yoluda imread() ile okuduktan sonra parantezin içine 2.parametre yerine 0 yazmak
# bu da aynı işe yarar
# image = cv2.imread("Images//f1.png", 0)

cv2.imshow("gri resim", grayImage)


cv2.waitKey(0)
cv2.destroyAllWindows()