# kameradan görüntü al --> DONE
# el okumasını yaptır  -->
# ekrana rectangel ekle
# işaret parmağı rectangele içerisine girince tetiklensin, eğer orta parmakla arasındaki mesafe x'ten küçükse sürükleme devreye girsin 

import cv2
from cvzone.HandTrackingModule import HandDetector

# Oluşturacağımız dikdörtgenlerin renk'ini tanımladık
rectColor = (0,100,255)

# Dikdörtgenleri dinamik bir şekilde oluşturmak için başlangıçta merkez x,y noktalarını ve genişlik-yüksekliklerini tanımladık.
centerX, centerY, widht, height = 100, 100, 120, 120

# cv2 modülümüz içerisindeki VideoCapture() fonksiyonu ile kameramızı tanımladık.
camera = cv2.VideoCapture(0)

# öncelikle HandDetector() fonksiyonu ile El'i bulmamıza yarayacak bir değişken tanımlıyoruz.
# içerisine girdiğimiz paramatre ise el'i algılamayı ayarlamak için (güvenilen) minimum tespit eşik değeridir (Minimum Detection Confidence Threshold).
# bu parametre yerine bir şey yazmazsak default olarak 0.5 algılanır. 
detector = HandDetector(detectionCon=0.8)

while True:
    success, frame = camera.read()
    frame = cv2.flip(frame, 1)

    # Yukarıda tanımladığımız detector değişkeninin içerisinde bulunan findHands() fonksiyonunu kullanarak içerisine verdiğimiz görüntüdeki
    # elleri ve landMarkları buluyoruz ve tekrardan geri landMarks ve frame değişkenlerinin içerisine atıyoruz.
    hands, frame = detector.findHands(frame)

    if hands:
        # hand1 = hands[0]
        # lmList1 = hand1["lmList"]
        
        lmList1 = hands[0]["lmList"]
        # lmList1 yani landmarks List, elimizin üzerinde tanımlanan her bir noktanın koordinatlarını tutan bir listedir.
        
        # Tekikleyici olarak işaret parmağımızın ucunu kullanmak istiyoruz bunun için lmList1 içerisinden buraya denk gelen noktayı seçmemiz gerekiyor
        # İşaret parmağımızın ucundaki mark, lmList1 içerisinde 8.indiste bulunmaktadır.
        # Bu yüzden cursor (imleç) olarak olarak lmList1'in 8.indisini kullanıyoruz.
        # cursor'a atamayı yaptıktan sonra artık cursor'ımız içerisinde 3 adet değer tutuyor.
        # cursor[0] --> anlık x koordinatı,  cursor[1] --> anlık y koordinatı,  cursor[2] --> anlık z koordinatı

        # Tetikleme işlemi için elin başka bir kısmını kullanmak isterseniz oraya denk gelen indis numarasını yazmalısınız.
        # Elin indis konumlarını öğrenmek isterseniz google'a "hand landmarks opencv" yazarak görsellerden öğrenebilirsiniz. 
        cursor = lmList1[8]
        #print(cursor)
    
        
        # cursor'ımız yani işaret parmağımızın uç noktası rectangle'ın içinde ise if'e girer ve içerideki işlemleri gerçekleştirir.
        # içinde değilse else blok'u çalışır.
        if (centerX - widht//2 < cursor[0] < centerX + widht//2)  and (centerY - height//2 < cursor[1] < centerY + height//2) :
            rectColor = (200,15,21)
 
            distance, info, frame = detector.findDistance((lmList1[8][0], lmList1[8][1]), (lmList1[12][0], lmList1[12][1]), frame)
            print(distance)

            if (distance<35):
                centerX, centerY = cursor[0], cursor[1]
        else:
            rectColor = (0,100,255)

    cv2.rectangle(frame, ((centerX - widht//2),(centerY - height//2 )), ((centerX + widht//2), (centerY + height//2)), rectColor, cv2.FILLED)

    cv2.imshow("Live Camera", frame)

    if cv2.waitKey(15) & 0xFF == ord('q'):
        break

camera.release()

cv2.destroyAllWindows()