import cv2

s1={1,2,3,4}
s2={3,4,5,6}
s3=s1.union(s2) # .union() naya set dega 2 set ka union leke
print(s1)
print(s3)
s1.update(s2) # .update() usi set me union wali value store kr dega
print(s1,s2)

s1={1,2,3,4}
s2={3,4,5,6}
s3=s1.intersection(s2) # .intersection() 2 sets ka intersection new set me store krega
print(s3)
s1.intersection_update(s2) # .intersetion_update() ek hi set me intersection value store kr dega
print(s1,s2)

s1={1,2,3,4}
s2={3,4,5,6}
s3=s1.symmetric_difference(s2) # symmetric diff removes the intersection value
print(s3)
s1.symmetric_difference_update(s2)
print(s1,s2)

s1={1,2,3,4}
s2={3,4,5,6}
s3=s1.difference(s2) #same as s1-s2, difference_update() same work
print(s3)
s4=s1-s2
print(s4)
print("Image is shown for better understanding")

s1.difference_update(s2)
print(s1,s2)

img = cv2.imread("c:/Users/Yash/Desktop/PYTHON/100days/31_set_thoery/a-b.jpg")
cv2.imshow("Displayed Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()