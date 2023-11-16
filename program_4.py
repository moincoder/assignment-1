#Check if the first and last number of a list is the same
numbers_x = [10,20,30,40,10]
numbers_y = [35,75,45,30,55]
def list_check(list):
     print(f"Given List {list}")
     if numbers_x[0] == numbers_x[-1]:
        print("True")
list_check(numbers_x)
list_check(numbers_y)