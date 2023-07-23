import cv2

# öncelikle resimde yaptığımız gibi kameramızı değişkenin içerisine atamamız gerekiyor.
# bunun için cv2 kütüphanesinin içerisinde bulunan VideoCapture() fonksiyonunu kullanmamız gerekiyor.
# son olarakta fonks. içerisine parametre yazmamız gerekiyor.
# 0 yazarsak bilgisayarda tanımlı default kamerayı kullanacağımızı belirtiriz.
# 1 yazarsak usb portuna takılı başka bir kamerayı kullanacağımızı belirtiriz.
# 2 yazarsak önceden çekilmiş herhangi bir videoyu kullanacağımızı belirtiriz. 
camera = cv2.VideoCapture(0)

# belirli aralıklarla çekilen karelerden video oluşturmak için bir döngü içerisinde kameramızı okuyup görüntümüzü çıktı olarak vermemiz gerekiyor.
# bunun içinde while döngüsü kullanırız.

while True:

    # kamera'yı okuyarak her anı bir frame olarak tutup bunu göstermeye çalışıcaz.
    ret,frame = camera.read()

    # kameradan aldığımız görüntüyü y eksine göre aynaladım.
    frame = cv2.flip(frame,1)

    # kameradan okuduğumuz frame'i pencerede gösterdik.
    cv2.imshow("kamera deneme", frame)

    # bu satır ile delay ekleyerek 15ms de bir kameradan görüntü almayı ve q'ya basıldığında döngüden çıkmasını sağlıyoruz.  
    if (cv2.waitKey(15)) & (0xFF == 'q'):
        break

# döngüden çıktıktan sonra kamera ile işimiz biter ve kamerayı serbest bırakmak için .release() fonskiyonunu kullanırız.
camera.release()

cv2.destroyAllWindows()