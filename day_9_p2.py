                #   dictionary exerise
# ____________________________________________________________

student_scores = {
    "kal":"81",
    "dagi":"78",   
    "tsedi":"99",              
    "eyob":"74",       
    "ermi":"62",      
}

student_grades = {}
# knowing the value from the dictionary
for element in student_scores:
    value = student_scores[element]

    if int(value) > int(90): 
        # this is adding new element in to dictionary
        student_grades[element] = "Outstanding"

    elif int(value) > int(80): 
        # this is adding new element in to dictionary
        student_grades[element] = "exceds expectation"

    elif int(value) > int(70): 
            # this is adding new element in to dictionary
            student_grades[element] = "acceptable"

    else:
            # this is adding new element in to dictionary
            student_grades[element] = "Fail"

print(student_grades)



