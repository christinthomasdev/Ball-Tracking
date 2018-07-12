import cv2
import numpy as np




#defining ranges of color for HSV profile
low = {'red':(166, 84, 141), 'green':(66, 122, 129), 'blue':(97, 100, 117), 'yellow':(23, 59, 119), 'orange':(0, 50, 80)}
high = {'red':(186,255,255), 'green':(86,255,255), 'blue':(117,255,255), 'yellow':(54,255,255), 'orange':(20,255,255)}

#defining color in RGB for circle color
colors = {'red':(0,0,255), 'green':(0,255,0), 'blue':(255,0,0), 'yellow':(0, 255, 217), 'orange':(0,140,255)}


def main():
    cam = cv2.VideoCapture(0)
    if cam.isOpened():
        r,frame = cam.read()

    else:
        r = False


    while r:
    
        r, frame = cam.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        for key, value in high.items():
            mask = cv2.inRange(hsv, low[key], high[key])

            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)[-2]
            

            if len(cnts) > 0:
        		
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                cv2.circle(frame, (int(x), int(y)), int(radius), colors[key], 2)
                cv2.putText(frame,key + " ball", (int(x-radius),int(y-radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,colors[key],2)
            cv2.imshow("Frame", frame)
            if cv2.waitKey(1)==27:
                break


	

	

    cv2.destroyAllWindows()
    cam.release()



if __name__ == "__main__":
    main()



