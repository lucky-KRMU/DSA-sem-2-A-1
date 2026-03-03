'''
Algorithmic Efficieny and Recursive Toolkit (AERT)

This is the python program file for the assignment.
'''

# PART: A -> Stack ADT

# Creating the class StackADT
class StackADT:

    # Calling the constructor
    def __init__(self, stack :list =[]):
        self.stack = stack
    
    # Making the push function
    def push(self, toPush):
        self.stack.append(toPush) # appeding the element to the last of the array (stack)
    
    # Making the pop function
    def pop(self):
        # Condition for checking underflow and popping element only if there exist an element in the stack
        if len(self.stack) > 0:
            self.stack.pop() # removing the last element
        else:
            print("Underflow") 
            return "Underflow"
    
    # Making the peek function
    def peek(self):
        # Checking for the condition that the stack isn't empty
        if len(self.stack) > 0:
            print(self.stack[-1])   # Displaying the last element
            return self.stack[-1]
        else:   
            print("Underflow")
            return "Underflow"

    # Adding function to check whether the stack is empty or not
    def is_empty(self):
        if len(self.stack) == 0:
            print(True)
            return True
        else:
            print(False)
            return False
    
    # Making a function to check the size of the element
    def size(self):
        print(len(self.stack))
        return len(self.stack)
    
# Implementation
# Using Tower of hanoi for implementation
def printMove(source: str, destination: str):
    print(f"Moving the Disk from {source} to {destination}")
    return f"Moving the Disk from {source} to {destination}"

hanoiTower = StackADT()

def hanoi_tower(n: str, source: str, auxiliary: str, destination: str):
    global hanoiTower
    if n == 1:  # Defining the base case
        move = printMove(source, destination)
        hanoiTower.push(move)
        return
    
    hanoi_tower(n-1, source, destination, auxiliary)
    move = printMove(source, destination)
    hanoiTower.push(move)
    hanoi_tower(n-1, auxiliary, source, destination)

# hanoi_tower(3, 'A', 'B', 'C')
# print(hanoiTower.stack)


# PART: B -> Factorial and Fibonacci

# Factorial Function
def factorial(n: int):
    # Defining the base case as 0 (0! = 1)
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(5))

# Fibonacci function

# Naive Fibonacci

naive_counter = 0 # counter for recursive calls in naive fibonacci

def fib_naive(n: int):
    global naive_counter
    naive_counter += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_naive(n-1) + fib_naive(n-2)

# print([fib_naive(i) for i in range(10)])
# print(fib_naive(10))
# print(naive_counter)

# Memoized Fibonacci
memo = {}   # Memoization dictionary

memo_counter = 0 # counter for the recursive calls in memoized fibonacci

# Fibonacci function using memoization
def fib_memo(n: int):
    global memo, memo_counter
    memo_counter += 1
    if n == 0:
        if n not in memo.keys():
            memo[n] = 0
        return memo[n]
    elif n == 1:
        if n not in memo.keys():
            memo[n] = 1 
        return memo[n]
    else:
        if n not in memo.keys():
            memo[n] = fib_memo(n-1) + fib_memo(n-2)
        return memo[n]

# print([fib_memo(i) for i in range(10)])
# print(fib_memo(10))
# print(memo_counter)

# PART: C -> Tower of Hanoi problem

# Making the hanoi auxiliary function to print the moves
def printMove(source: str, destination: str):
    print(f"Disk moved from {source} to {destination}")

# Making the hanoi function
def hanoi(n: int, source: str, auxiliary: str, destination: str):
    if n == 1:  # Defining the base case
        printMove(source, destination)
        return
    
    hanoi(n-1, source, destination, auxiliary)
    printMove(source, destination)
    hanoi(n-1, auxiliary, source, destination)

# hanoi(3, 'A', 'B', 'C')


# PART: D -> Recursive Binary search
# Defining the function
def binary_search(arr: list, key: float, low: int, high: int):

    # Defining the base case
    if low > high:
        return -1

    mid = (low + high) // 2 # Finding out the middle

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)

arr = [1,3,5,7,9,11,13]
print(binary_search(arr, 13, 0, (len(arr) - 1) ))



