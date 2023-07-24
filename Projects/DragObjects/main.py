# -- Sözde Kod --
# kameradan görüntü al 
# el okumasını yaptır 
# ekrana rectangel ekle
# işaret parmağı rectangele içerisine girince tetiklensin, eğer orta parmakla arasındaki mesafe x'ten küçükse sürükleme devreye girsin.


import cv2
from cvzone.HandTrackingModule import HandDetector

class Rectangle():
    def __init__(self,centerX, centerY, size = [120,120], rectColor = (0,100,255)):
        self.centerX = centerX
        self.centerY = centerY
        self.size = size
        self.rectColor = rectColor
    
    # Cursor, belirtilen koordinatlar içerisine olduğunda rectangle'ı cursor ile aynı konuma taşımak için kullanılır.
    def updatePosition(self, cursor):
    
        if (self.centerX - self.size[0]//2 < cursor[0] < self.centerX + self.size[0]//2)  and (self.centerY - self.size[1]//2 < cursor[1] < self.centerY + self.size[1]//2):
           
            self.centerX, self.centerY = cursor[0], cursor[1]
            self.rectColor = (122,54,1)
            
        else:
            self.rectColor = (0,100,255)
            

rectangleList = []

for i in range(5):
    rectangleList.append(Rectangle((i*200)+100, 100))

# Oluşturacağımız dikdörtgenlerin renk'ini tanımladık
rectColor = (0,100,255)

# cv2 modülümüz içerisindeki VideoCapture() fonksiyonu ile kameramızı tanımladık.
camera = cv2.VideoCapture(0)

# öncelikle HandDetector() fonksiyonu ile El'i bulmamıza yarayacak bir değişken tanımlıyoruz.
# içerisine girdiğimiz paramatre ise el'i algılamayı ayarlamak için (güvenilen) minimum tespit eşik değeridir (Minimum Detection Confidence Threshold).
# bu parametre yerine bir şey yazmazsak default olarak 0.5 algılanır. 
detector = HandDetector(detectionCon=0.8)

while True:
    success, frame = camera.read()
    frame = cv2.flip(frame, 1)

    # addWeighted() işlemi için backgrounddaki ana görüntünün kopyasını oluşturduk ve alpha değerini tanımladık.
    SourceFrame= frame.copy()
    alpha = 0.5

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
        
        # Taşıma işlemini belli bir mesafenin altında gerçekleştireceğiz bunun için ilk olarak findDistance fonskiyonu ile iki nokta arasındaki mesafeyi hesaplıyoruz.
        # İki noktadan kastımız işaret parmağının uç noktası ile orta parmağın uç noktasıdır. Burada belirttiğimiz kısımlara karşılık gelen landmark değerlerini giriyoruz.
        # İşaret parmağının uç kısmı landmark List içinde 8.indekse, orta parmağın uç kısmı ise 12.indise denk geliyor.
        # nokta olarak belirtmemiz gerektiği için fonksiyona hem x hem de y koordinatlarını vermemiz gerekiyor bu yüzden lmList1[8][0], lmList1[8][1] olarak belirtiyoruz.    
        distance, info, frame = detector.findDistance((lmList1[8][0], lmList1[8][1]), (lmList1[12][0], lmList1[12][1]), frame)
        print(distance)


        if (distance<35):

            # iki parmak ucu arası mesafe 35'den küçükse ve rectangle'ların içindeyse her bir rectangle'ın konumlarını güncellemek için gerekli fonksiyon çalışır.
            for rectangel in rectangleList:
                rectangel.updatePosition(cursor)


    for rectengle in rectangleList:

        # ekranda rectangle oluşturmak için gerekli p1 ve p2 noktalarını girmemiz gerekiyor, bu noktaları rectangelList içindeki her bir rectangle'ın boyutlarını ve 
        # center noktalarını alarak belirliyoruz.
        # Bu sayede dinamik bir yapı elde etmiş oluruz.
        centerX, centerY = rectengle.centerX, rectengle.centerY
        width, height = rectengle.size[0], rectengle.size[1]

        cv2.rectangle(frame, ((centerX - width//2),(centerY - height//2 )), ((centerX + width//2), (centerY + height//2)), rectColor, cv2.FILLED)
        
        # Dikdörtgenlere saydamlık katmak için addWeighted() fonksiyonunu kullandık.
        frameNew = cv2.addWeighted(SourceFrame, alpha, frame, 1 - alpha, -1 )

    cv2.imshow("Live Camera", frameNew)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()

cv2.destroyAllWindows()