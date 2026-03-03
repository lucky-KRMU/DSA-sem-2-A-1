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
# Using Tower