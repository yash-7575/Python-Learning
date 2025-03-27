import cv2
s1={1,2,3,4}
s2={3,4,5,6}
s3=s1.isdisjoint(s2)
print(s3)

s1={1,2,3,4}
s2={5,6}
s3=s1.isdisjoint(s2)
print(s3)

img = cv2.imread("c:/Users/Yash/Desktop/PYTHON/100days/31_set_thoery/disjoint.png")
cv2.imshow("Displayed Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()