#                    ----------------- Videodan Alınan Görüntünün Kayıt Edilmesi -----------------

# Daha önce kameradan görüntünün nasıl alınacağını öğrenmiştik.
# Şimdi ise bunun üzerine bir kaç ilave yaparak kameradan aldığımız görüntüyü bir dizine kaydetmeyi uygulayacağız.

import cv2

camera = cv2.VideoCapture(0)

# Öncelikle kaydedeceğimiz görüntünün genişlik ve yüksekliği belirleyelim.
# Burada kameramızın genişlik ve yüksekliğini almak istedim ve böyle bir yöntem uyguladım.

width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

# yüksek boyutlu dosyaları sıkıştırarak oluştururuz ve karşı taraf ise bu dosyayı encoding ederek kullanır.
# bu yüzden encode için "four character code" yani kısaca fourcc değişkeni tanımlayarak oluşturduğumuz
# dosyanın türünü tanımlamamız gerekiyor.
fourCC = cv2.VideoWriter_fourcc('m','p','4','v')

# cv2 modülü içerisindeki VideoWriter() fonksiyonu ile kayıt işlemine başlıyoruz. Aldığı parametrelere bakarsak :
#   1.parametre : Kayıt yapılacak yerin yolunu (path) alır.
#   2.parametre : encode işlemi için yukarıda tanımladığımız dosyanın türünü tutan değişkeni alır.
#   3.parametre : frame per second (fps) yani saniye başına görüntülenecek frame sayısını temsil eder.
#   4.parametre : kayıt penceresinin genişliğini ve yüksekliğini bir tuple olarak vermemiz gerekiyor.

output = cv2.VideoWriter("Records//kayit.mp4", fourCC, 30, (width,height))

while True:

    ret, frame = camera.read()
    frame = cv2.flip(frame,1)
    
    # anlık olarak aldığımız frameleri write() fonksiyonunu kullanarak yukarıda tanımladığımız output içerisin yazıyoruz. 
    output.write(frame)

    cv2.imshow("Video Capture", frame)

    if cv2.waitKey(15) & 0xFF == ord('q'):
        break

camera.release()

# kamerada yaptığımız gibi output işlemine de release() fonksiyonu ile serbest bırakıyoruz.
output.release()

cv2.destroyAllWindows()