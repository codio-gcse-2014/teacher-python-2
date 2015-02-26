# Task 4
# Press the 'Run File' menu button to execute

#initialise our variables
global_input_seconds=0 
global_output_minutes=0

#function definitions block
def get_seconds() -> int:
    return int(input("Enter time in seconds >> "))

def convert_to_minutes(local_input_seconds) ->float:
    return local_input_seconds/60

def output_result() ->str:
    print(global_output_minutes)

def main_program_sub():
    global global_output_minutes
    global_input_seconds=get_seconds()
    global_output_minutes=convert_to_minutes(global_input_seconds)
    output_result()

main_program_sub()