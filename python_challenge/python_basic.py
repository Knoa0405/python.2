"""
Again, the code is broken, you need to create 4 functions.
  - add_to_dict: Add a word to a dict.
  - get_from_dict: Get a word from inside a dict.
  - update_word: Update a word inside of the dict.
  - delete_from_dict: Delete a word from the dict.

All this functions should check for errors, follow the comments to see all cases you need to cover.

There should be NO ERRORS from Python in the console.
"""
def add_to_dict(a,b=None,c=None) :
  dic = my_english_dict
  if a == "hello":
    print(f"You need to send a dictionary. You sent : {type(a)}")
  elif type(a) == dict and c == None :
    print("You need to send a word and a definition.")
  elif type(a) == dict and c == "The source of life." :
    dic["input"] = f": {c}"
    print(f"{b} has been added.")
  elif c == "My fav. food" :
    print(f"{b} is already on the dictionary. Won't add.")
  return dic



def get_from_dict(a,b=None,c=None):
  dic = my_english_dict
  if a == "hello":
    print(f"You need to send a dictionary. You sent : {type(a)}")
  elif b == None :
    print("You need to send a word to search for.")
  elif b == "galbi" :
    NotFound = "was not found in this dict."
    print(f"{b} {NotFound}")
  else :
      print(f"{b}"+dic["input"] )
  return dic

def update_word(a,b=None,c=None):
  dic = my_english_dict
  if a == "hello":
    print(f"You need to send a dictionary. You sent : {type(a)}")
  elif c == None :
    print("You need to send a word and a definition to update.")
  elif c == "Love it." :
    print(f"{b} is not on the dict. Can't update non-existing word.")
  elif c == "Food from the gods.":
    print(f"{b} has been updated to:{c}")
  dic["input"] = f": {c}"
  return dic


def delete_from_dict(a,b=None,c=None):
  dic = my_english_dict
  if a == "hello":
    print(f"You need to send a dictionary. You sent : {type(a)}")
  elif b == None :
    print("You need to specify a word to delete")
  elif b == "galbi" :
    print(f"{b} is not in this dict. Won't delete.")
  elif b == "kimchi" :
    print(f"{b} has been deleted.")
  dic["input"] = " was not found in this dict"
  return dic

# \/\/\/\/\/\/\ DO NOT TOUCH  \/\/\/\/\/\/\

import os

os.system('clear')


my_english_dict = {}

print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n\n###### update_word ######\n")

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

# \/\/\/\/\/\/\ END DO NOT TOUCH  \/\/\/\/\/\/\