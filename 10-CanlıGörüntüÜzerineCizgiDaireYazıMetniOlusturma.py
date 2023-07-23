import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:

    # ret burada camera okumasının başarılı olup olmadığını tutar
    ret,frame = camera.read()
    frame = cv2.flip(frame,1)

    if ret == True:

        cv2.line(frame, (320,270), (380,270), (0,0,255),2)

        cv2.rectangle(frame, (200,150), (500,300), (255,0,0), 2)

        cv2.circle(frame, (310,190), 20, (0,255,0), 2)
        cv2.circle(frame, (380,190), 20, (0,255,0), 2)

        cv2.putText(frame, "Say My Name", (120,130), cv2.FONT_HERSHEY_COMPLEX, 2, (0,155,255), 1)
        cv2.putText(frame, "You are god damn right !", (90,400), cv2.FONT_HERSHEY_COMPLEX, 1, (0,155,255), 1)

        cv2.imshow("Panel", frame)

        # ord() fonksiyonu içerisine girilen karakterin unicode karşılığını döndürür.
        # ASCII ile Unicode arasındaki fark şudur, ASCII sadece ingilizce karakterler (latin alfabesi) üzerinde etkili iken
        # Unicode evrenseldir yani diğer tüm dillerin kolay bir şekilde dijital ortama aktarımını ve kullanımını sağlar. 
        # Unicode’un geliştirilmesinin amacı evrensel olması ve platformlar arası yaşanan karmaşaların ortadan kaldırılmasıdır.

        # "0xFF", burada FF, 8 bitlik 11111111'i temsil eder çünkü bir karakteri temsil etmek için yalnızca 8 bit gerekir.
        # Klavyeden girdiğimiz karakter'in unicode karşılığı ile bunu eşleştirir ve şart sağlandığında if'e girerek break yapar.
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break

camera.release()

cv2.destroyAllWindows()


