import random
import math

first_random_word = ""
excluded_letters = []
correct_letters = {}
misplaced_letters = {}
word_list = open("dict.txt", "r")
word_list_content = (word_list.read()).split()
WORD_LENGTH = 5
repeat_check = True

print("Disclaimer: there's a known issue with words containing repeating letters — still working on fixing it, but the algo should work for about 80–90% of games.")

def get_key_by_value(my_dict, target_value):
    return next((k for k, v in my_dict.items() if v == target_value), None)

def repeat_letters_check():
   compiled_list = []
   compiled_list.append(list(correct_letters.keys()))
   compiled_list.append(list(misplaced_letters.keys()))
   flattened_compiled_list = [item for container in compiled_list for item in container]
   for item in flattened_compiled_list:
      if item in excluded_letters:
         excluded_letters.remove(item)
   print(excluded_letters)
   first_filter()

def first_filter():
   print(repeat_check)
   if  not excluded_letters:
      # print("not excluded")
      second_filter(word_list_content)
      return
   excluded_letters_set = set(excluded_letters)
   first_filter = list(filter(
      lambda word: all(
         letter not in excluded_letters_set 
         for letter in word
         ), 
         word_list_content))
   if not first_filter:
      first_filter = word_list_content
      # print('not first filter')
   # print(first_filter, "first")
   second_filter(first_filter)

def second_filter(filterONE):
   if not filterONE:
      filterONE = word_list_content
   second_filter = []
   for words in filterONE:
      if (all(words[position] == key for key, position in correct_letters.items())):
         second_filter.append(words)
   # print(second_filter, "scond")
   third_filter(second_filter)
 
def third_filter(filterTWO):
   global repeat_check, word_list_content
   third_filter = []
   for words in filterTWO:
      if (all((words[position] != key) and (key in words) for key, position in misplaced_letters.items())):
         third_filter.append(words)
   # print(third_filter, "third")
   if not third_filter:
      third_filter = filterTWO
   # with open("possible_vars.txt", "w", encoding="utf-8") as file:
   #    file.write(" ".join(third_filter))
   word_list_content = third_filter
   repeat_check = False
   repeat_user_input()

def wait_user_input():
   global first_random_word
   excluded_letters.clear()
   correct_letters.clear()
   misplaced_letters.clear()
   user_input = input("Write the colors:")
   user_input_arr = user_input.split(' ')
   for i in range(WORD_LENGTH):
      user_i = user_input_arr[i].strip()
      if user_i in ("grey", "gray"):
         excluded_letters.append(first_random_word[i])
      elif user_i == "green":
            correct_letters[first_random_word[i]] = i
      elif user_i == "yellow":
         misplaced_letters[first_random_word[i]] = i

   if repeat_check is True:
      repeat_letters_check()
   else:
      first_filter()

def repeat_user_input():
   global first_random_word
   print(word_list_content, "heyyyy")
   first_random_word = input("New word: ")

   wait_user_input()

def first_random_try():
   global first_random_word
   first_random_word = word_list_content[math.floor(random.random() * len(word_list_content))]
   # first_random_word = "scarf" //use this if you already started the wordle game. uncomment it and comment the first_random_word above. 
   print("\nPut this in wordle:",first_random_word)
   wait_user_input()

first_random_try()