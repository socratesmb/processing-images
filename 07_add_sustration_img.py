import cv2

img1 = cv2.imread('img/5-20.jpg')
img2 = cv2.imread('img/5-40.jpg')
img3 = cv2.imread('img/5-60.jpg')

union = cv2.add(img2, img1)

cv2.imshow('UNION', union)
cv2.waitKey(0)
cv2.destroyAllWindows()
