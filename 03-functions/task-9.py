# Task 9
# Press the 'Run File' menu button to execute

print("Taking x parameters")

def fn_hw_para_x(word1,*args):
    num_of_para=len(args)
    print(args)
    return word1 + " " + " ".join(args)
print(fn_hw_para_x("Hello","new","world"))