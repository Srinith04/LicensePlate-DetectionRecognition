import cv2
import pytesseract

def number_plate_recognition(file):
    # Path to tesseract executable.
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    image = cv2.imread(file)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    gray = cv2.medianBlur(gray,3)

    thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    rect_kern = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

    dilation = cv2.dilate(thresh, rect_kern, iterations = 1)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    sorted_contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])

    label = "Plate-"

    for cnt in sorted_contours:
        x,y,w,h = cv2.boundingRect(cnt)
        area_bound = h*w
        height, width = gray.shape  
        ratio = h / float(w)

        #Some conditions to remove unneccesary contours.
        if height / float(h) > 6: continue
        if ratio < 0.50: continue
        if width / float(w) > 15: continue
        if area_bound < 100: continue
        if 2*area_bound > height*width: continue

        lef_y = max(y-2,0)
        rig_y = min(y+h+4,height)
        lef_x = max(x-2,0)
        rig_x = min(x+w+4,width)

        #Getting the character
        char = thresh[lef_y:rig_y,lef_x:rig_x]
        text = pytesseract.image_to_string(char, lang='eng', config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 10 --oem 3')
        label += text.strip()

    cv2.waitKey(0)
    return label

# print(number_plate_recognition('runs\detect\exp5\crops\\number_plate\\PM1.jpg'))