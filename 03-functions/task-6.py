# Task 6
# Press the 'Run File' menu button to execute

def fn_hw_para(word1,word2):
    return word1 + " " + word2  #”+” joins the strings into one string

a="Monty" #two short strings Monty and Python
b="Python"
print("Using a function with two parameters taken from\n",
      "global variables a, b") 
#we can carry on a line of Python code onto a next line if: (1) there is an open bracket, (2) there is a #comma
print(fn_hw_para(a,b))