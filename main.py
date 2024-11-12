
import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x500")
        
        self.current_expression = ""
        self.result_var = tk.StringVar()

        # Display area (Entry widget)
        self.create_display()

        # Button layout
        self.create_buttons()

    def create_display(self):
        # Display to show the expression and result
        self.display = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 20), bd=10, relief="sunken", justify="right")
        self.display.grid(row=0, column=0, columnspan=4)

    def create_buttons(self):
        # Define button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2)
        ]

        # Create buttons and place them in the grid
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Arial", 16), width=5, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        if char == "=":
            try:
                # Calculate and update result
                self.current_expression = str(eval(self.current_expression))
                self.result_var.set(self.current_expression)
            except Exception as e:
                self.result_var.set("Error")
                messagebox.showerror("Error", f"Invalid expression: {e}")
        elif char == "C":
            # Clear display
            self.current_expression = ""
            self.result_var.set("")
        else:
            # Update the expression as user types
            self.current_expression += str(char)
            self.result_var.set(self.current_expression)

# Initialize the Tkinter window
root = tk.Tk()

# Create the calculator object
calculator = Calculator(root)

# Run the main loop
root.mainloop()

