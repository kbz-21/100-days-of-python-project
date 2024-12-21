# def function_mine():
#     print("my name is kaleab")
#     print("my id number is ugr/22886/13/14")

# function_mine()


# def function_mine(name):
#     print(f"my name is {name}")
#     print(f"{name} is ADAMA SCIENCE AND TECHNOLOGY UNIVERSITY STUDENT")

# function_mine("kaleab")


# __________________________________________________________________________
# our life in a weeks

# def life_in_weeks(age):
#      remaining_years = 90-age
#      remaining_weeks = remaining_years * 52
#      print(f"you have {remaining_weeks}  weeks left.")
# life_in_weeks(23)

# def two_parameter(name, location):
#     print(f"my name is {name}.")
#     print(f"i live in {location}.")

# two_parameter(location="Meki", name="kaleab" )
# def my_function(a,b,c):
#     print(f"this is {a}")
#     print(f"thi is {b}")
#     print(f"this is {c}")
# my_function(1,2,3)


# def calculate_love_score(name1, name2):
#     combined_name=(name1 + name2).lower()
#     Inside_true =(
#         combined_name.count("t") +
#         combined_name.count("r") +
#         combined_name.count("u") +
#         combined_name.count("e") 
  
#                  )
                 
#     inside_love=(
        
#           combined_name.count("l") +
#           combined_name.count("o" )+
#           combined_name.count("v") +
#           combined_name.count("e") 
          
#         )
        
#     true_love=int(str(Inside_true) + str(inside_love))
#     print(f"Your love score is: {true_love}")
    
# calculate_love_score("kaleab", "bemnet")
# -------------------------------------------------------------------
# def my_parameter(name, age):
#     print(f"my name is {name}")
#     print(f"{name}'s age is {age}.")

# my_parameter( age="23" , name="kaleab")


# -------------------------------------------------------------------

# fruits=("apple", "mango","papaya","orange")
# index_no=fruits.index("orange")
# print(index_no)

# fruits=(21,23,45,67,67,54,43)
# A=fruits.index(67)
# print(A)

# __________________________________________________________

# alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# direction = input("type 'encode' to encrypt,type 'decode'to decrypt: \n ").lower()
# text = input("type your message:\n")
# shift = int(input("type the shift number:\n"))

# def encrypt(submitted_text, shift_amount):
#         cipher_text = ""
#         for letter in submitted_text:
#             position = alphabet.index(letter)
#             shifted_index = (position + shift_amount) % len(alphabet)
#             shifted_value = alphabet[shifted_index]
#             cipher_text += shifted_value
#         print(f"The encoded text is: {cipher_text}")

# def decrypt(submitted_text, shift_amount):
#         cipher_text = ""
#         for letter in submitted_text:
#             position = alphabet.index(letter)
#             shifted_index = abs(position - shift)
#             shifted_value = alphabet[shifted_index]
#             cipher_text += shifted_value
#         print(f"the decoded text is: {cipher_text}")
    
# if direction == "encode":
#     encrypt(submitted_text=text, shift_amount=shift)

# elif direction == "decode":
#     decrypt(submitted_text=text, shift_amount=shift)
# else:
#      print("Invalid word!")

#  ____________________________________________________________
                    # DAY 8 COMPLETE PROJECT

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def caesar(submitted_text, shift_amount, cipher_direction):
        
    cipher_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in submitted_text:
        if char in alphabet:
            position = alphabet.index(char)
            shifted_index = (position + shift_amount)
            cipher_text += alphabet[shifted_index]
        else:
            cipher_text  += char 
       
    print(f"The {cipher_direction}d text is: {cipher_text}") 
    

should_continue = True
while should_continue:
    direction = input("type 'encode' to encrypt,type 'decode'to decrypt: \n ").lower()
    text = input("type your message:\n").lower()
    shift = int(input("type the shift number:\n"))

    shift = shift % 26

    caesar(submitted_text=text, shift_amount=shift, cipher_direction=direction)

    result=input("Type 'yes' if you want to countinue. and Type 'no' if you want to Exit: \n")
    if result == "no":
        should_continue = False
        print("GoodBye!")


#  ____________________________________________________________

    