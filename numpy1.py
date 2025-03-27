import numpy as np

'''NumPy Array Properties'''

arr = np.array([4, 5, 6])
print(arr,arr.ndim,arr.shape,arr.dtype,arr.size)

arr2d = np.array([[7, 8, 9],
                  [10, 11, 12]])
print(arr2d,arr2d.ndim,arr2d.shape)

arr2d = np.array([[13, 14, 15],
                  [16, 17, 18],
                  [19, 20, 21]])
print(arr2d, arr2d.ndim, arr2d.shape)
print(arr2d[0])
print(arr2d[0][1])

arr3d = np.array([[[1,2,3], 
                   [4,5,6]], 
                  [[7,8,9], 
                   [10,11,12]]])
print(arr3d)

'''Creating Special Arrays'''

zeros=np.zeros((3,3))
print(zeros)

ones=np.ones((2,4))
print(ones)

eye=np.eye(4)
print(eye)

arr = np.arange(3)
print(arr)
arr=np.arange(0,9)
print(arr)
arr=np.arange(0,9,2) # (start, stop, step)
print(arr)

'''Random numbers'''
arr2d=np.random.rand(3,3)
print(arr2d)

'''NumPy Indexing & Slicing'''

arr = np.array([10, 20, 30, 40, 50])
print(arr[2])
print(arr[1:4])  # [20, 30, 40]
print(arr[:3])   # [10, 20, 30]
print(arr[-2:])  # [40, 50]

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[1, 2])  # Row 1, Column 2 → 6
print(matrix[:, 1])  # All rows, column 1 → [2 5 8]

print(matrix[1][2]) #1st row 2nd clm
print(matrix[:][2]) # All rows 2nd clm
print(matrix[1][:]) # 1st row, all clms

'''NumPy Operations'''

arr1=np.array([1,2,3])
arr2=np.array([2,4,6])
sum_arr=arr1+arr2
sub_arr=arr1-arr2
mul_arr=arr1*arr2
div_arr=arr1/arr2
print(sum_arr, sub_arr, mul_arr, div_arr)

'''Aggregate Functions'''

arr = np.array([10, 20, 30, 40, 50])
print(np.sum(arr))
print(np.min(arr))
print(np.min(arr))
print(np.max(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.median(arr))

'''NumPy Reshaping'''

arr=np.array([1,2,3,4,5,6])
reshaped=arr.reshape(2,3)
print(reshaped)

'''NumPy Stacking (Joining Arrays)'''

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(np.vstack((arr1,arr2))) # joins arrays in vertical way
print(np.hstack((arr1,arr2))) # joins arrays in horizontal way

'''NumPy Filtering'''

arr = np.array([10, 20, 30, 40, 50])
filter=arr[arr>25]
print(filter)

'''NumPy Broadcasting'''

arr = np.array([[1, 2, 3], 
                [4, 5, 6]])
print(arr+10)

'''NumPy Linear Algebra'''

A = np.array([[1, 2], 
              [3, 4]])
B = np.array([[5, 6], 
              [7, 8]])
print(np.dot(A,B)) # Return matrix multiplication
''' use row vs clm method 
    -> * ↓ '''

print(np.linalg.det(A)) # return det of A. det fn is from linear algebra module of np library

x=np.linspace(10,100,10) 
'''linspace = linear space '''
''' np.linespace(start,stop, num) evenly distribute the array into num parts'''
''' in this example it will generate an array from 10 to 100 and it will divide that array into 10 equal parts'''
print(x)

x=np.linspace(10,100,10, endpoint=False) #doesnt take endpoint
print(x)

arr, step = np.linspace(0, 10, 5, retstep=True)
print(arr)
print("Step size:", step)
