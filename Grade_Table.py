header = "Item".center(20) + "Grade".center(20)

print("*" * 40)
print(header)
print("*" * 40)

quiz_1 = 10
quiz_2 = 9
quiz_3 = 10

test_1 = 95
test_2 = 87
test_3 = 90

quiz_average = ((quiz_1 + quiz_2 + quiz_3) / 30) * 100
test_average = (test_1 + test_2 + test_3 + quiz_average) / 4

item = "Quiz 1".center(20) + "10".center(20)
print(item)
item = "Quiz 2".center(20) + "9".center(20)
print(item)
item = "Quiz 3".center(20) + "10".center(20)
print(item)
item = "Test 1".center(20) + "95".center(20)
print(item)
item = "Test 2".center(20) + "87".center(20)
print(item)
item = "Test 3".center(20) + "90".center(20)
print(item)
item = "Average: ".center(20) + "92.17".center(20)
print(item)

print()

print (f"quiz average is: {quiz_average:9.2f} ")
print (f"class average is: {test_average:9.2f} ")