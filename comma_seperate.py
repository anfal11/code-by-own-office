import tkinter as tk
from tkinter import simpledialog

def split_input(input_str):
 
    data_array = input_str.split()
    
    output = ', '.join(data_array)
    
    return output

def main():
    root = tk.Tk()
    root.withdraw()  
    
    user_input = simpledialog.askstring("Input", "Enter some numbers separated by spaces, commas, or newlines:")
    
    if user_input is not None:
        
        output = split_input(user_input)

        with open("output.txt", "w") as f:
            f.write(output)

        print("Output has been written to output.txt")

if __name__ == "__main__":
    main()
