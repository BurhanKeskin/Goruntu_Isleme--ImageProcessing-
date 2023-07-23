# kameradan görüntü al --> DONE
# el okumasını yaptır  -->
# ekrana rectangel ekle
# işaret parmağı rectangele içerisine girince tetiklensin, eğer orta parmakla arasındaki mesafe x'ten küçükse sürükleme devreye girsin 

import cv2
from cvzone.HandTrackingModule import HandDetector

camera = cv2.VideoCapture(0)

# öncelikle HandDetector() fonksiyonu ile El'i bulmamıza yarayacak bir değişken tanımlıyoruz.
# içerisine girdiğimiz paramatre ise el'i algılamayı ayarlamak için (güvenilen) minimum tespit eşik değeridir (Minimum Detection Confidence Threshold).
# bu parametre yerine bir şey yazmazsak default olarak 0.5 algılanır. 
detector = HandDetector(detectionCon=0.8)

while True:
    success, frame = camera.read()
    frame = cv2.flip(frame, 1)

    # Yukarıda tanımladığımız detector değişkeninin içerisinde bulunan findHands() fonksiyonunu kullanarak içerisine verdiğimiz görüntüdeki
    # elleri bulmuyoruz ve tekrardan geri frame değişkeninin içerisine atıyoruz.
    frame = detector.findHands(frame)

    # Görüntü içerisindeki elleri bulduktan sonra elin içindeki landmarkları ileride tetikleme,sürükleme işlemlerinde kullanacağımız için

    cv2.imshow("Live Camera", frame)

    if cv2.waitKey(15) & 0xFF == ord('q'):
        break

camera.release()

cv2.destroyAllWindows()