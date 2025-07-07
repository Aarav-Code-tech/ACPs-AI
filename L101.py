import cv2
import numpy as np

def a(img, filter):
    copy1 = img.copy()
    if filter == "red_tint":
        copy1[:, :, 0] = 0
        copy1[:, :, 1] = 0
    elif filter == "green_tint":
        copy1[:, :, 0] = 0
        copy1[:, :, 2] = 0
    elif filter == "blue_tint":
        copy1[:, :, 1] = 0
        copy1[:, :, 2] = 0
    elif filter == "canny":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        copy1 = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    elif filter == "sobel":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        combine = cv2.bitwise_or(sobelx.astype("uint8"), sobely.astype("uint8"))
        copy1 = cv2.cvtColor(combine, cv2.COLOR_GRAY2BGR)
    return copy1

img_path = "Bear.jpg"
img = cv2.imread(img_path)

if img is None:
    print("Error, image not found")
    exit()
else:
    print("press:\n R for Red Tint \n G for Green Tint \n B for Blue Tint \n C for Canny Edge Detection \n S for Sobel Edge Detection \n Q for Quit")

filter = "red_tint"

while True:
    filtered_img = a(img, filter)
    cv2.imshow("filtered image", filtered_img)
    keys = cv2.waitKey(0) & 0xFF  # wait indefinitely until a key is pressed
    if keys == ord("R") or keys == ord("r"):
        filter = "red_tint"
    elif keys == ord("G") or keys == ord("g"):
        filter = "green_tint"
    elif keys == ord("B") or keys == ord("b"):
        filter = "blue_tint"
    elif keys == ord("C") or keys == ord("c"):
        filter = "canny"
    elif keys == ord("S") or keys == ord("s"):
        filter = "sobel"
    elif keys == ord("Q") or keys == ord("q"):
        print("exit")
        break

cv2.destroyAllWindows()