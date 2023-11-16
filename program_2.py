#Print the sum of the current number and the previous number.
current_number = 1
for i in range(10):
    previous_number = current_number-1
    print(f"current number {current_number} previous number {previous_number} sum {current_number+previous_number}")