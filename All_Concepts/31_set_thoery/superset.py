import cv2
s1={1,2,3,4}
s2={3,4}
print(s1.issuperset(s2))
print(s2.issubset(s1))

s1={1,2,3,4}
s2={3,4,5}
print(s1.issuperset(s2))
print(s2.issubset(s1))

img = cv2.imread("c:/Users/Yash/Desktop/PYTHON/100days/31_set_thoery/superset.png")
cv2.imshow("Displayed Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()