# def function_mine():
#     print("my name is kaleab")
#     print("my id number is ugr/22886/13/14")

# function_mine()


# def function_mine(name):
#     print(f"my name is {name}")
#     print(f"{name} is ADAMA SCIENCE AND TECHNOLOGY UNIVERSITY STUDENT")

# function_mine("kaleab")


# .........................................
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




def calculate_love_score(name1, name2):
    combined_name=(name1 + name2).lower()
    Inside_true =(
        combined_name.count("t") +
        combined_name.count("r") +
        combined_name.count("u") +
        combined_name.count("e") 
  
                 )
                 
    inside_love=(
        
          combined_name.count("l") +
          combined_name.count("o" )+
          combined_name.count("v") +
          combined_name.count("e") 
          
        )
        
    true_love=int(str(Inside_true) + str(inside_love))
    print(f"Your love score is: {true_love}")
    

calculate_love_score("kaleab","bemnet")
