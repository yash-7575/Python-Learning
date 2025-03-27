import time
import random
dhanrashi=0
print("Namaskar Deviyo or Sajjano, Aapka bohot bohot swagat hai kbc ke naye episode me")
time.sleep(1)
name = input("Sir/Madam Aapka naam? ")
if name[-1].lower() in ["a", "i"]:
    print(f"All the best Mrs. {name}")
else:
    print(f"All the best Mr. {name}")
print("Chaliye Shuru krte hai")
time.sleep(2)

print("To ye raha pehla question aapke computer screen ke saamne 1000 rs ke liye")
time.sleep(1)
print("1. What is the Capital of India ?")
l=["Mumbai", "Delhi", "kolkata", "Benglore"]
random.shuffle(l)

# for t in range(60,0,-1):
#     time.sleep(0.5)
#     print(t)
for i in enumerate(l):
    print(i)
ans1=int(input("Write your option no. "))
if ans1==l.index("Delhi"):
    dhanrashi=1000
    print(f"Badhai Ho, aap {dhanrashi} rs dhanrashi jeet gaye ")
    print("To ye raha dusra question aapke computer screen ke saamne 5000 rs ke liye")
    time.sleep(0.5)
    print("1. Longest river in the world ?")
    l=["Ganga", "Amazon", "Nile", "Yamuna"]
    random.shuffle(l)
    for i in enumerate(l):
        print(i)
    ans1=int(input("Write your option no. "))
    if ans1==l.index("Nile"):
        dhanrashi+=5000
        print(f"Badhai Ho, aap {dhanrashi} rs dhanrashi jeet gaye ")
    else :
        dhanrashi=1000
        print(f"So sorry, aapka answer galat hai, aapko {dhanrashi} rs dhanrashi prapt huyi")
    print("Abhi ke liye itna hi, baaki ka game kal khelenge, dhanywad aapka samay dene ke liye, Bye Bye")
else :
    dhanrashi=0
    print("So sorry aapka answer galat hai, aapko khali haath jana hoga")
