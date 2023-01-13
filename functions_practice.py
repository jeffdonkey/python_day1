# function 1

def hello():
    print("Hello Instructor")

hello()


# function 2

def pack(first, second, third):
    return[first, second, third]

pack("bird", "fish", "lizard")

    # below is a different way I would do this
    # the idea is to have the function be re-usable

def pack2(some_list):
    for x in some_list:
        print(x)
    return some_list
         
a_list = ["bird", "fish", "lizard"]

pack2(a_list)


# function 3


def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

# got this from the solution code.  I don't think i would 
# solved this on my own.  Below are notes explaining the code above:

    # Line 32 starts a function named "eat_lunch".  Agruments passed to the function will be given the name of "my_1st"
    # Lines 33-40 are if/else statements with prints
    # Line 33 is checking the length (len) of the "my_1st" (argument). If no argument is sent when "eat_lunch" is called
        #then the message on line 34 will print; otherwise continue to else statement on line 35.
    # Line 36 uses the "range" function.  In the range function it is using the length of "my_first" to set the number of 
        #items in the incomming list
    # Line 37 "if" catches the first item in the list [index 0] and then goes to line 38 print statement
    # Line 39 "else" catches all indexes greater than [index 0] and then goes to print
    # If there are more than two items in "my_list" Lines 39 and 40 will continue to run until list iteration
        #is complete. 

eat_lunch(["turkey"])

eat_lunch(["fish", "chips", "apple"])

eat_lunch([])