#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [num for num in num_list if num % 2 == 0]
    return even_numbers


num_list_odd = range(1, 10, 2)
result_odd = return_evens(num_list_odd)
print("Even numbers from range(1, 10, 2):", result_odd)

num_list_even = range(10)
result_even = return_evens(num_list_even)
print("Even numbers from range(10):", result_even)


def make_exclamation(sentence_list):
    exclamations = [sentence + "!" for sentence in sentence_list]
    return exclamations


sentence_list = [
    "I like computers",
    "I require coffee",
    "Live long and prosper",
]
result = make_exclamation(sentence_list)
print(result)
     