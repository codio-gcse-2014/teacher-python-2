# Task 3
# Press the 'Run File' menu button to execute

#initialise our variables
global_input_seconds=0 
global_output_minutes=0

#function definitions block
def get_seconds():
    global_input_seconds=int(input("Enter time in seconds >> "))

def convert_to_minutes():
    global_output_minutes = global_input_seconds/60

def output_result():
    print(global_output_minutes)

def main_program_sub():    
    get_seconds()
    convert_to_minutes()
    output_result()

main_program_sub()
