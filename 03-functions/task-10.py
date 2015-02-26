# Task 10
# Press the 'Run File' menu button to execute

def fn_hw_para(word1,word2):
      return word1 + " " + word2
a="Monty"
b="Python"

#create a list of two strings
my_list_1=[a,b]

print("getting input parameters off lists")

#each list item is accessed through [index]. [0] is Monty, [1] is Python
print(fn_hw_para(my_list_1[0],my_list_1[1]))