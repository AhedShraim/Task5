# Q1 : Write a Python program to concatenate following dictionaries to create a new one :
# First dictionary represent the personal information of myself.
Per_info = {"Name" : "Ahed" ,
            "Last name": "Shraim",
            "Age" : 27 ,
            "Gender" : "Male" ,
            "Nationality" : "Palestinian"
}
    # Second dictionary represent Where I live.
address = {"Country" : "Palestine" ,
           "City" : "Gaza",
           "Street" : "The First"
}
# In third step, showing the dictionaries before we concatenate them together.
print("Personal Information is ",Per_info, "\n")
print("Where do I live ?",address, "\n")

# defining where will we concatenate the dictionaries by adding an empty one.
All_info ={}

# concatenating the dictionaries in All_info dictionary.
for result in (Per_info,address):
    All_info.update(result)


# In last printing the result of concatenating.
print(All_info,"\n")



# Q2: Write a Python program that prompts the user to calculate Area and perimeter for rectangle
# and raises a exception if the input is not a positive input.

# Defining the area formula by using a function.
def area(length , width):
    total = length * width
    return total
# Defining the perimeter formula by using a function.
def perimeter(length , width):
    total = 2 * (length + width)
    return total
# Asking the user to input the length and width of the rectangle.
length = float(input("Enter the Length of the rectangle: "))
width = float(input("Enter the Width of the rectangle: "))

# Raising an exception if the user inputs one of the above as a negative value.
if length < 0 or width < 0:
    raise Exception(f"One of the inputs{length , width} is a negative number")
# if the inputs bigger or equal zero then the code will continue working without problem.
# And we will have the outputs.
else:
    total = area(length, width)
    print("The area of the rectangle is: ", total, "\n")

    total = perimeter(length, width)
    print("The perimeter of the rectangle is: ", total, "\n")







