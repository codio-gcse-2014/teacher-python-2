# Task 7
# Press the 'Run File' menu button to execute

def fn_hw_para(word1,word2):
    return word1 + " " + word2

a="Monty"
b="Python"

print("Insert a function into another function? no problem\n",
      "here the function is inserted twice into itself")
print(fn_hw_para(fn_hw_para(a,b),
                 fn_hw_para(a,b)))
