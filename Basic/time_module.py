import time
print(time.time()) #returns time in seconds from 1970
st=time.time()
print(time.strftime("%H,%M,%S"))
print(time.localtime().tm_year)
print(time.localtime())
print("wait for 3 seconds")
time.sleep(3) #for delay
print("Done")
end=time.time()
print(end-st) #for calculating time of compilation
print(time.ctime(time.time()))
