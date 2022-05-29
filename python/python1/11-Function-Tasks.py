# Function Tasks
#
#
# Let's see if you can solve these word problems by creating functions.
# The function "skeleton" has been set up for you to fill in below the problem
# description, as well as example outputs of what the function should return
# given certain inputs. Best of luck, some of these will be challenging!
#
# The tasks will start off easy and proceed to get harder and harder.

# ## Task 1
#
#  Create a function that takes in two integers and returns
## a Boolean True if their sum is 10, False if their sum is something else.


import enum


def check_ten(n1, n2):
    sum_ = n1 + n2
    return sum_


print(check_ten(10, 10), check_ten(1, 1))

# ## Task 2
#
# Create a function that takes in two integers and returns True if their
# sum is 10, otherwise, return the actual sum value.


def check_ten_sum(n1, n2):
    sum_ = n1 + n2
    return True if sum_ > 10 else sum_


print(check_ten_sum(10, 10), check_ten_sum(1, 1))

# ## Task 3
#
# Create a function that takes in a string and returns back the
# first character of that string in upper case.


def first_upper(mystring: str) -> str:
    return mystring.capitalize()


print(first_upper("manuel"))

# ## Task 4
#
# Create a function that takes in a string and returns the last two characters.
# If there are less than two chracters, return the string:  "Error".
# Use this link if you need help/hint.
# (https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string)


def last_two(mystring: str) -> str:
    return "Error" if len(mystring) <= 2 else mystring[-2]


print(last_two("hi"), last_two("Manuel"))

# ## Task 5
#
# Given a list of integers, return True if the sequence [1,2,3] is somewhere
# in the list. Hint: Use slicing and a for loop.


def seq_check(nums: list) -> bool:
    check_list = [1, 2, 3]
    # [1,1,1,2,3,4,5,6]
    for i in range(len(nums)):
        if nums[i : i + 3] == check_list:
            return True
    else:
        return False


print(seq_check([1, 2, 3]))
print(seq_check([7, 7, 7, 1, 2, 3, 7, 7, 7]))
print(seq_check([3, 2, 1, 3, 2, 1, 1, 1, 2, 2, 3, 3, 3]))


# ## Task 6
#
# Given a 2 strings, create a function that returns the difference in length
# between them. This difference in length should always be a positive number
# (or just 0). Hint: Absolute Value.**


def compare_len(s1: str, s2: str) -> int:
    return abs(len(s1) - len(s2))


compare_len("aa", "aa")


compare_len("a", "bb")


compare_len("bb", "a")


# ## Task 7
#
# Given a list of integers, if the length of the list is an even number,
# return the sum of the list. If the length of the list is odd, return the max
## value in that list.


def sum_or_max(mylist: list[int]) -> int:
    len_list = len(mylist)
    if not (len_list % 2):
        return sum(mylist)
    else:
        return max(mylist)


print(sum_or_max([1, 2, 3]), sum_or_max([0, 1, 2, 3]))
