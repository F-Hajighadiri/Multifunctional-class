import cv2
import numpy as np
import vlc
import time

class Multifunctional() :
    def __init__(self):
        self.cap = cv2.VideoCapture(1)
        self.faceDetector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.eyeDetector = cv2.CascadeClassifier("haarcascade_eye.xml")


    def detect(self) :
        while True:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.flip(frame, 1)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                face = self.faceDetector.detectMultiScale(gray)
                for (x, y, w, h) in face :
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0, 2))
                    faceFrame = frame[y:y + h, x:x + w]

                eye = self.eyeDetector.detectMultiScale(faceFrame)
                for (x, y, w, h) in eye :
                    cv2.rectangle(faceFrame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
                
                cv2.imshow("detector", frame)
                if cv2.waitKey(1) == ord('q'):
                    break

        self.cap.release()
        cv2.destroyAllWindows()




    def showMedia(self, key) :

        if key == "music" :
            music = vlc.MediaPlayer("Shape Of My Heart .mp3")
            music.play()
            time.sleep(15)

        elif key == "movie" :
            poster = cv2.imread("poster.jpeg")
            cv2.imshow("Movie Poster", poster)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif key == "book" :
            print("The Picture of Dorian Gray")

        else :
            print("Please enter a valid key!")




myClass = Multifunctional()
# myClass.detect()

print("Enter your favorite media :")
print("(music _ movie _ book)")
media = str(input())
myClass.showMedia(media)
