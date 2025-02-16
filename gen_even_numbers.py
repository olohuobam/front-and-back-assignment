# main - a  python programm to generate even numbers between 0 and 1000:
#      - the total numbers:
# -----&&-----------------:             the average of the even numbers:

# @Return : Return 0 on seccess


# main 1---1
even_numbers = [num for num in range(0, 1001) if num % 2 == 0]

# sum++
total_numbers = len(even_numbers)

# --main-- ++
average = sum(even_numbers) / total_numbers if total_numbers > 0 else 0

# result
print("Even numbers between 0 and 1000:", even_numbers)
print("Total number of even numbers:", total_numbers)
print("Average of the even numbers:", average)

