import timeit

def time_recusive(fun):
  k=1
  while True:
    start = timeit.default_timer()
    fun(k)
    stop = timeit.default_timer()
    time = stop - start
    if time > 60
      break
    k += 1

def time_iterative(fun):
  lower = 10000000
  upper = 300000000
  found = False
  midpoint = (lower + upper)//2
  while True:
    start = timeit.default_timer()
    fun(midpoint)
    stop = timeit.default_timer()
    time = stop - start
    print time
    if time > 60 and not found:
      midpoint = (midpoint + lower)//2
      upper = midpoint
    elif time < 59 and not found:
      midpoint = (midpoint + upper)//2
      lower = midpoint
    elif 59 <= time <= 60 and not found:
      return midpoint

def time_matrix():
  A = [[0,1], [1,1]]
  start = timeit.default_timer()
  k = 0
  while True:
    A = mult(A,A)
    stop = timeit.default_timer()
    time = stop - start
    if time > 60:
      return k -1
    else:
      k += 1
#278453313,2^33985775

# the recursive implementation of Fibonacci

def recursive(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return (recursive(n-1) + recursive(n-2))%65536

# the iterative implementation of Fibonacci
def iterative(n):
  A = []
  A.append(0)
  A.append(1)
  for i in range(2,n+1):
    A.append((A[i-1] + A[i-2])%65536)
  return A[n]

# the matrix implementation of Fibonacci
def matrix(n):
  A = [[0,1], [1,1]]
  result = pow(A,n)
  return result[0][1]

# multiply matrix X and Y
def mult(X,Y):
  result = [[0,0],[0,0]]
  # iterate through rows of X
  for i in range(len(X)):
     # iterate through columns of Y
     for j in range(len(Y[0])):
         # iterate through rows of Y
         for k in range(len(Y)):
             result[i][j] = (result[i][j] + X[i][k] * Y[k][j])%65536
  return result

def pow(X,n):
  if n == 1:
    return X
  if n % 2 == 0:
    return pow(mult(X, X), n//2)
  else:
    return mult(X, pow(mult(X, X), (n-1)//2))
