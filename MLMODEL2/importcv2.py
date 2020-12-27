#import cv2 pkg
import cv2

#read img and convert it into numpay array where 1 is for colored img and 0 is for grayscaled
img = cv2.imread ("h.jpeg",1)
img1 = cv2.imread ("h.jpeg",0)

#print shape size of both just for undrstanding
print(img)
print(type(img))
print(img.shape)
print(img1)
print(type(img1))
print(img1.shape)

#showing img 

#cv2.imshow("h",img)
#cv2.waitKey(200)
#cv2.destroyAllWindows()

#imgr = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

#cv2.imshow("h",imgr)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

fc = cv2.CascadeClassifier("hc.xml")
gi=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face = fc.detectMultiScale(gi,scaleFactor=1.05,minNeighbors=5)

for x,y,w,h in face:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),6)

img = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
cv2.imshow("h",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



