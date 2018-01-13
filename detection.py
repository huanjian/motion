import cv2
import numpy as np
 
# stream dari kamera atau video
#no.1
cap = cv2.VideoCapture('http://localhost/car.mp4')

 
# jika kamera berhasil terkoneksi
if (cap.isOpened()== False): 
  print("gagal terhubung")

#7b
counter = 0
image = 0
 
# stream sampai finish
while(cap.isOpened()):
  # capture tiap frame
  ret, frame = cap.read()
  if ret == True:
    #no.4
    #resize x:500
    r = 500.0 / frame.shape[1]
    dim = (500, int(frame.shape[0] * r))    
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)


    #no.5
    rows,cols,cc = frame.shape 
    frame = frame[35:rows, 0:cols]

    #no.7a
    if counter == 1:
        print rows, cols


    #no.6
    for i in range(cols):
        frame[200,i] = [255,0,0]
        frame[201,i] = [255,0,0]


    #no.8
    if (counter == 2) :
        cv2.imwrite('0.jpg',frame)
        frame = cv2.imread('0.jpg', 0)
        cv2.imshow('Frame',frame)

    if (counter == 150) :
        cv2.imwrite('1.jpg',frame)
        frame = cv2.imread('1.jpg', 0)
        cv2.imshow('Frame',frame)
        
        #no.9
        frame1 = cv2.imread('0.jpg')       
        f1Rows, f1Cols,cc = frame1.shape

        frame2 = cv2.imread('1.jpg')       
        f2Rows, f2Cols,cc = frame2.shape
        
        for i in range(f2Rows):
            for j in range(f2Cols):
                R1,G1,B1 = frame1[i,j]
                R2,G2,B2 = frame2[i,j]
                         
                print R1, G1, B1
                print R2, G2, B2
                
                

                difR = abs(R2-R1)
                difG = abs(G2-G1)
                difB = abs(B2-B1)
                if (difR > 160) & (difG > 160) & (difB > 160) & (difR < 220) & (difG < 220) & (difB < 220):
                    frame2[i,j] = [difR,difG,difB]
                else:
                    frame2[i,j] = [0,0,0]

        cv2.imshow('Frame',frame2)  
        cv2.imwrite('result2.jpg',frame2)      

    if (counter == 200) :
        cv2.imshow('Frame',frame)
        cv2.imwrite('2.jpg',frame)
        
    
    counter = counter + 1


    #no.2
    #cv2.imshow('Frame',frame)    

    
    #no.3 
    # Q untuk exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  # break loop
  else: 
    break
 
# ketika selesai release semua object
cap.release()
 
# tutup semua window
cv2.destroyAllWindows()
