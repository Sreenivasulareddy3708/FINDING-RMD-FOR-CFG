import tkinter as tk
from tkinter import scrolledtext

FILE_LR = "lr.txt"
FILE_INPUT = "input.txt"

def show_result(output):
    # Create a Tkinter window
    window = tk.Tk()
    window.title("LR(1) Parsing Table Results")

    # Create a scrolled text widget to display the output
    result_text = scrolledtext.ScrolledText(window, width=80, height=20)
    result_text.pack()

    # Insert the output into the text widget
    result_text.insert(tk.END, output)

    # Start the Tkinter main loop
    window.mainloop()

# function for LR(1)
def LR(input):
    #files

FILE_LR = "lr.txt"
FILE_INPUT = "input.txt"
stack = []

# function for LR(1)
def LR(input):
    input = input.strip() #remove \n
    state_stack = "1"
    alphabet = {} # use to keep state order
    operators = {} # use to keep operators (a c d $ B S )
    products = [] # use to keep LR table
    no = 1
    print("\n")
    print("Processing input string {0} for LR(1) parsing table".format(input))
    print("\n")
    lr_file = open(FILE_LR, "r", encoding='utf-8') # open the FILE_LR to read file
    for line_no, line in enumerate(lr_file):
        line = line.strip()
        line = line.replace(" ", "").split(";")

        if (line_no == 1):
            for no, symbols in enumerate(line):
                symbols = symbols.strip()
                operators[symbols] = no # keep operators -->  {'a': 1, 'c': 2, 'd': 3, '$': 4, 'S': 5, 'B': 6}
        else:
            products.append(line)    # for example state 1 line  --->  ['State_1', 'State_3', '', '', '', 'State_2', '']
            alphabet[line[0][-1]] = line_no - 1        # '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7  --> order of states

    state_stack = products[1][0][-1]  # last element of stack
    no = 1
    input_control = 0  # for reading stack element

    print("NO  | STATE STACK | READ |  INPUT  |  ACTION ", end="\n" )

    if products[alphabet[state_stack[-1]]][operators[input[input_control]]] == '':
 # if does not have an action/step for
        print(f"{no:<4}| {state_stack:<12}|{input[input_control]:^6}|{input:>7} "
        "REJECTED  ({0} does not have an action/step for {1})".format(products[alphabet[state_stack[-1]][0]], input[input_control]))
        print("\n")
        exit()
    else:  # if have an action
        print(f"{no:<4}| {state_stack:<12}|{input[input_control]:^6}|{input:>7}  | "
            "Shift to state {0}".format(products[1][operators[input[input_control]]]))
        state_stack += " " + products[1][operators[input[input_control]]][-1]
    while True:
        no += 1
        input_control += 1

        if "->" in products[alphabet[state_stack[-1]]][operators[input[input_control]]]:
  # if we need to reverse stack for example B -> d
            temp = products[alphabet[state_stack[-1]][operators[input[input_control][0]]]]   # temp is B
            length = len(products[alphabet[state_stack[-1]][operators[input[input_control][3:]]]])  # len("d") for delete states from stack

            print(f"{no:<4}| {state_stack:<12}|{input[input_control]:^6}|{input:>7}  | "
            "Reverse {0}".format(products[alphabet[state_stack[-1]][operators[input[input_control]]]]))

            for i in range(length):
                state_stack = state_stack[0:-1]  # for delete last element
                state_stack = state_stack.strip()
            str_temp = input[input_control:]
            input = input[:input_control - length] + temp + str_temp  # for update input
            input_control -= length + 1
        else:
            if products[alphabet[state_stack[-1]]][operators[input[input_control]]] == "Accept":
 # if state is accepted for special operator
                print(f"{no:<4}| {state_stack:<12}|{input[input_control]:^6}|{input:>7}  |  ACCEPTED")
                print("\n")
                break
            else:
                if products[alphabet[state_stack[-1]]][operators[input[input_control]]] == '':
  # if state not have a match
                    print(f"{no:<4}| {state_stack:<12}|{input[input_control]:^6}|{input:>7}  | "
                    "REJECTED  ({0} does not have an action/step for {1})".format(products[alphabet[state_stack[-1]], operators[input[input_control]]]))
                    print("\n")
                    break
                else:
                    print(f"{no:<4}| {state_stack:<12}|{input[input_control]:^6}|{input:>7}  | "  # if have an action for an operator
                    "Shift to state {0}".format(products[alphabet[state_stack[-1]][operators[input[input_control]]]]))


                    state_stack += " " + products[alphabet[state_stack[-1]][operators[input[input_control]]][-1]]

input_file = open(FILE_INPUT, "r", encoding='utf-8')
print("Read LR(1) parsing table from file " + FILE_LR)
print("Read input strings from file " + FILE_INPUT)
for line in input_file:   # to read the input file line by line
    line = line.split(";")
    if line[0].strip() == "LR":
        LR(line[1])
print("\n")

    output = ""  # Initialize an empty string to capture the LR results

    # Modify your print statements to append to the output string instead
    def print_to_output(text):
        nonlocal output
        output += text + "\n"

    # Replace your print statements with calls to print_to_output
    print_to_output("\n")
    print_to_output("Processing input string {0} for LR(1) parsing table".format(input))
    print_to_output("\n")
    # Rest of your LR function...

    # Show the result in a GUI popup window
    show_result(output)

# Main code to read the LR(1) parsing table and input strings
if __name__ == "__main__":
    input_file = open(FILE_INPUT, "r", encoding='utf-8')
    print("Read LR(1) parsing table from file " + FILE_LR)
    print("Read input strings from file " + FILE_INPUT)
    for line in input_file:
        line = line.split(";")
        if line[0].strip() == "LR":
            LR(line[1])
    print("\n")
