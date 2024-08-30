import customtkinter as ctk


class Panel(ctk.CTkFrame):
    def __init__(self, master, column, row, distribution, at_command, **kwargs):
        super().__init__(master, **kwargs)

        self.at_command = at_command

        # Default number of columns
        number_of_columns = 1
        self.grid(column=column, row=row, sticky="nsew")

        # Configure rows and columns of the GeneralFrame to expand
        print(self.at_command)
        print(self.at_command['send_parameters'])
        if len(at_command['send_parameters']) > 0:
            if distribution == 'vertical':
                self.grid_rowconfigure((0, 1, 3), weight=1)
                self.grid_columnconfigure(0, weight=1)
            else:
                self.grid_columnconfigure((0, 1), weight=1)
                self.grid_rowconfigure((0, 1), weight=1)
                number_of_columns = 2
        else:
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
        
        self.title_label = ctk.CTkLabel(self, text=at_command['title'], font=('Helvetica', 18, 'bold'))
        self.title_label.grid(column=0, row=0, columnspan=number_of_columns, sticky="nsew")
