import customtkinter
import tkinter


class ButtonsGrid(customtkinter.CTkFrame):
    equation = []
    def __init__(self, command_callback, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command_callback = command_callback

        buttons = [
            'C', '+/-', '%', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', 
        ]
        rows = (len(buttons) + 3) // 4  # Calculate the number of rows needed

        button_index = 0  # Track the index in the buttons list

        
        for i in range(rows):
            self.grid_rowconfigure(i, weight=1)
            for j in range(4):
                self.grid_columnconfigure(j, weight=1)
                if button_index < len(buttons):  
                    button_text = buttons[button_index]
                    button = customtkinter.CTkButton(
                        self, text=button_text, bg_color="gray", border_spacing=2,
                        command=lambda bt=button_text: self.add_to_equation(bt, command_callback) if bt != 'C' else self.clear_last(command_callback)
                    )
                    padding = 1
                    if (button_text == '0'):
                        button.grid(row=i, column=j if i != 4 else j, sticky="nswe", columnspan=2, padx=padding, pady=padding)
                    else:
                        button.grid(row=i, column=j if i != 4 else j + 1, sticky="nswe", columnspan=1, padx=padding, pady=padding)

                    if i == 0: button.configure(fg_color="#3b3b3b", text_color="white")
                    if j == 3 or button_text == '=': button.configure(fg_color="#636363", text_color="white")
                     
                    button_index += 1  # Move to the next button index
                # Break the loop if button_index exceeds the length of the buttons list


    def clear_last(self, callback):
        if (len(self.equation) > 1):
            self.equation.pop()
            callback(self.equation)
        else:
            callback(0)

    def add_to_equation(self, value, callback):
        if (value == '='): 
            try:
                result = eval(''.join(self.equation))
                self.equation = [str(result)]
            except Exception as ex:
                self.equation = ['Error']
            callback(result)
            return
        self.equation.append(value)
        callback(self.equation)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x500")

        
        self.result_frame = customtkinter.CTkFrame(self)
        self.result_frame.place(relx=0, rely=0, relwidth=1, relheight=0.2)

        result = 0
        result_label = customtkinter.CTkLabel(self.result_frame, text=result if result >= 0 else 0, anchor='e', justify='center', )
        result_label.pack(expand=True, fill=tkinter.BOTH, padx=(0, 10))

        
        self.buttons_grid = ButtonsGrid(lambda eq: result_label.configure(text=eq))
        self.buttons_grid.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)


app = App()
app.mainloop()
