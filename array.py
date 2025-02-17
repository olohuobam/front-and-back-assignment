# Name - Obam Isaiah Olohu
# Dept - Computer Science
#level - 200l
# main - A program that will read an array of 200 characters and
#  display to the screen a count of the occurrences 
# of each of the five vowels (a, I , e ,o , u) in an array.....

# @return :  Return 0 on sucess






# create a function
def count_vowels(input_str):
    # Initialize vowel counters
    a_count = e_count = i_count = o_count = u_count = 0

    # Loop through each character in the string
    for ch in input_str:
        if ch.lower() == 'a':
            a_count += 1
        elif ch.lower() == 'e':
            e_count += 1
        elif ch.lower() == 'i':
            i_count += 1
        elif ch.lower() == 'o':
            o_count += 1
        elif ch.lower() == 'u':65
            u_count += 1

    # Print the counts of vowels
    print(f"A/a: {a_count}")
    print(f"E/e: {e_count}")
    print(f"I/i: {i_count}")
    print(f"O/o: {o_count}")
    print(f"U/u: {u_count}")

# Read a string of up to 200 characters from the user
input_str = input("Enter a string (max 200 characters): ")[:200]

# you cann the function here
count_vowels(input_str)
