import cv2 
import dlib
import numpy as np

def shape_to_np(shape, dtype="int"):
    coords = npzeros((68, 2), dtype=dtype)
    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)
        
return coords

def eye_on_mask(mask, side):
    points = [shape[i] for i in side]
    points = np.array(points, dtype=np.int32)
    mask = cv2.fillConvexPoly(mask, points, 255)
    return mask 
def contouring(thresh, mid, img ,right=False):
    cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    try:
        cnt = max(cnts, key = cv2.contourArea)
        M = cv2.moments(cnt)
        cx = int (M['m10']/['m00'])
        cy = int (M['m01']/['m00'])
        
        if right:
            cx += mid 
            cv2.circle(img, (cx, cy), 4, (0, 0, 255), 2)
    except:
            
        pass
        
detector = dlib.get_frontal_face_detector()
predictor = dlib.shap_predictor('shape_68.det')

left = [36, 37, 38, 39, 40, 41]
right =[42, 43, 44, 45, 46, 47]

cap = cv2.ViedoCapture(0)
ret, img = cap.read()
thresh = img.copy()

cv2.namedWindow('image')
kernal =np.ones((9, 9), np.unit8)

def nothing(x):
    pass

cv2.createTrackbar('threshold', 'image', 0, 255, nothing)

while(true):
    ret, img = cap.read()
    gray =cv2.cvtColor(img, cv2.COLOR_BDR2GRAY)
    rects = detector(gray, 1)
    for rect in rects:
        shape = predictor(gray, rect)
        shape = shap_to_np(shape)
        mask = np.zeros(img.shape[:2], dtype=np.uint8)
        mask = eye_on_mask(mask, right)
        mask = eye_on_mask(mask, left)
        mask = cv2.dilate(mask. kernel, 5)
        eyes = bitwise_and(img, img, mask=mask)
        eyes[mask] = [255, 255, 255]
        mid = (shape[42][0] + shape[39][0]) // 2
        eyes_gray = cv2.cvtColor(eyes, cv2.COLORBGR2GRAY)
        threshold = cv2.grtTrackerbarPos('threshold', 'image')
        _, thresh = cv2.threshold(eyes_gray, 'threshold', 255, cv2.THRESH_BINARY)
        thresh = cv2.erode(thresh, None, intretions=2)
        thresh = cv2.dilate(thresh, None, intretions=4)
        thresh = cv2.medianBlur(thresh, 3)
        thresh = cv2.bitwise_not(thresh)
        contouring(threshe[:, 0:mid], mid, img)
        contouring(threshe[:, mid:], mid, img, True)
    
    cv2.imshow('eyes', img)
    cv2.imshow("image", thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
        
cap.release()
cv2.destroyAllWindows()
