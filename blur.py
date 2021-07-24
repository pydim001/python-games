import cv2

x = [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]

def convert(pixels, kernel):
    sum = 0
    for i, pixel in enumerate(pixels):
        for j, num in enumerate(pixel):
            sum += num*kernel[i][j]
    return int(sum)

def getpixels(nparray, kernel, x1, x2, y1, y2):
    for row in range(y1, y2):
        for pix in range(x1, x2):
            group = [[nparray[row-1][pix-1], nparray[row-1][pix], nparray[row-1][pix+1]],
                     [nparray[row][pix-1], nparray[row][pix], nparray[row][pix+1]],
                     [nparray[row+1][pix-1], nparray[row+1][pix], nparray[row+1][pix+1]]]
            nparray[row][pix] = convert(group, x)
    return nparray

def blur_effect(stength, a, b, c, d, e, f):
    for repeat in range(stength):
        a = getpixels(a, b, c, d, e, f)
    return a

def Recording():
    cap = cv2.VideoCapture(0)
    while True:
        check, frame = cap.read()
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #cv2.imshow("frame", grayscale)
        cv2.imshow("frame", blur_effect(7, grayscale, x, 160, 480, 120, 360)) 
        
        if cv2.waitKey(1) & 0xFF == ord('q'):   #you can change the key to cut the webcam off
            break

    cap.release()
    cv2.destroyAllWindows()

try:
    Recording()
except IndexError:
    print("y1 and y2 have to be between 1 and 480 and x1 and x2 have to be between 1 and 640")
