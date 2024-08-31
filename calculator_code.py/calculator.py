import tkinter as tk

def click_button(item):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(item))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def key_press(event):
    if event.keysym in '0123456789/*-+.':
        click_button(event.keysym)
    elif event.keysym == 'Return':
        calculate()
    elif event.keysym == 'BackSpace':
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text[:-1])

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg='#333333')

# Entry widget for displaying the numbers and results
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=8, insertwidth=2, bg="#444444", fg="#FFFFFF", justify='right')
entry.grid(row=0, column=0, columnspan=4)
entry.bind("<Key>", key_press)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    '@','()','%','$','#'
]

button_colors = {
    'text': '#000000', # Black text color
    'bg': '#666666',
    'highlight': '#888888'
}

# Create and place buttons on the grid
row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: click_button(x)
    if button == "=":
        action = calculate
    elif button == "C":
        action = clear_entry

    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), 
              command=action, fg=button_colors['text'], bg=button_colors['bg'], 
              activebackground=button_colors['highlight']).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Add a clear button
tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), 
          command=clear_entry, fg=button_colors['text'], bg=button_colors['bg'], 
          activebackground=button_colors['highlight']).grid(row=row_val, column=0)

# Run the application
root.mainloop()    
    
    
