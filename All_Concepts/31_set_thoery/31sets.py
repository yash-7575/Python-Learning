import cv2

# from PIL import Image

# try:
#     # Open and show the image
#     img = Image.open("c:/Users/Yash/Desktop/PYTHON/100days/set.jpg")
#     img.show()
# except FileNotFoundError:
#     print("Error: Image not found or unable to load.")

img = cv2.imread("c:/Users/Yash/Desktop/PYTHON/100days/31set.jpg")
cv2.imshow("Displayed Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


s={11,12,43,32,11,2}
print(s)
s1=set() #Most imp => it's is used for creation of empty set
print(type(s1))
s1.add(11)
print(s1)

for i in range(10):
    s1.add(i)
print(s1)

for i in s1:
    print(i)
    
l1=list()
print(type(l1))
l1.append(11)
print(l1)

t1=tuple()
print(type(t1))

dict1=dict()
print(type(dict1))
dict1["Name"]=["Yash"]
print(dict1)