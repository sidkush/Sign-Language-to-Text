import cv2
import os

#Directory Define
if not os.path.exists("Data"):
    os.mkdir("Data")

if not os.path.exists("Data/Train"):
    os.mkdir("Data/Train")


cam = cv2.VideoCapture(0)

img_counter= 0


while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    minValue = 70

    # Coordinates of the ROI
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])

    #Declaring regions for drawing rectangle
    start_point = (200,9)
    end_point = (621, 419)
    color = (255,0,0)
    thickness = 1
    cv2.rectangle(frame, start_point, end_point, color ,thickness)
    
    #Declaring Region Of Interest
    roi = frame[10:410, 220:520]
    cv2.imshow("Frame", frame)
    #Converting the image to grayscale
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    #Applying gaussian blur to smoothen the image
    blur = cv2.GaussianBlur(gray,(5,5),2)  #std deviation in x,y co-ordinate(5,5) & sigma x = sigma y =2

    #Applying adaptive threshold
    th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)

    ret, test_image = cv2.threshold(th3, minValue, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    test_image = cv2.resize(test_image, (300,300))
    cv2.imshow("test", test_image)


    directory = 'Data/Train/'
    
    if cv2.waitKey(1) & 0xFF == 27:
        #ESC Pressed
        print("Esc hit, closing...")
        break
    
    elif cv2.waitKey(1) & 0xFF == ord('e'):
        #a Pressed
        if not os.path.exists('Data/Train/E/'):
            os.mkdir('Data/Train/E/')
        for i in range(1,50):
            img_name = "Data/Train/E/E{}.png".format(img_counter)
            cv2.imwrite(img_name, test_image)
            img_counter +=1


cam.release()

cv2.destroyAllWindows()

