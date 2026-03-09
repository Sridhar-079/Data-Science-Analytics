# WEEK 2 – DATA STRUCTURES & FUNCTIONS

def sum_of_squares(numbers):
    return sum(x**2 for x in numbers)

print(sum_of_squares([1,2,3,4]))

data = [1,2,2,3,4,4,5]
print(list(set(data)))

nums = [10,15,20,25,30]
filtered = list(filter(lambda x: x > 20, nums))
print(filtered)

data = [10,20,20,30,None,40,None,50]
cleaned = [x for x in data if x is not None]
cleaned = list(set(cleaned))
print(cleaned)
