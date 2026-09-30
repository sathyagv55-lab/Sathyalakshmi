def is_even(num):
    return num % 2 ==0

def find_max(*numbers):
    return max(numbers)

def perform_operation(num,operation):
     if operation == "square":
         return num*num
     if operation == "cube":
         return num*num*num
     else:
         return "Invalid operation"