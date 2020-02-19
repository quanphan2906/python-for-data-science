import numpy as np

#clearPrint func
def clearPrint(message = "", variable = ""):
    print("-------------")
    print(message)
    print("\n")
    print(variable)
    print("\n")

#create array
a = np.array([0, 1, 2, 3, 4]) #numpy array has only one type of data
b = np.random.rand(3, 2) * 100
clearPrint("type of a", type(a))
clearPrint("type of a's ele", a.dtype)
clearPrint("size of the array", b.size)
clearPrint("dimension of the array", b.ndim)
clearPrint("shape of the array", b.shape)

#create placeholder
clearPrint("array of zeros", np.zeros((3, 4)))
clearPrint("array of random values", np.random.rand(2,2))
clearPrint("array of constant", np.full((2,2), -1))
clearPrint("array of evenly spaced values", np.linspace(-2, 2, 5)) #start, end, number of records

#indexing
clearPrint("array of random values for indexing", b)
clearPrint("select whole column", b[:, 1])
clearPrint("select the whole row", b[2, :])
clearPrint("slicing", b[0:1, 0:1]) #this is equal to b[0,0] or b[0][0]
clearPrint("boolean index", b[b < 50])

#operations
c = np.random.rand(5) * 10
d = np.random.rand(3, 2) * 100
e = np.random.rand(2, 3) * 100
clearPrint("dot product of a and c, or a multiply by tranpose of c", np.dot(a, c))
clearPrint("Hadamard product (element-wise product)", b*d)
clearPrint("matrix multiplication", np.dot(b, e)) # #rows of b = #cols of e 

#universal funcs
clearPrint("calculate mean of a", a.mean())
clearPrint("", b)
clearPrint("cumulative sum of the elements", b.cumsum(axis = 0)) #since b is 2D array -> specify the axis
#axis 0  is along the columns
#axis 1 is along the rows
#axis 2 is along the depth
clearPrint("max of 2D array", b.max(axis = 0))
