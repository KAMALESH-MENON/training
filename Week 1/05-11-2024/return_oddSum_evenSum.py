import random
import timeit

def generate_random_number():
    arr=[]
    for i in range(5):
        arr.append(random.randint(0,100))
        
    return arr
    


def return_oddsum_evensum():
    arr = generate_random_number()
    odd_sum = 0
    even_sum = 0
    for item in arr:
        if item % 2 == 0:
            even_sum += item
        else:
            odd_sum += item
    return {"odd_sum" : odd_sum, "even_sum" : even_sum, "array" : arr}


print(return_oddsum_evensum())
execution_time = timeit.timeit(return_oddsum_evensum, number=10)  # Run the function 10 times
print(f"Average Execution Time over 10 runs: {execution_time / 10:.6f} seconds")