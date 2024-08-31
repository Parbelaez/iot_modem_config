import customtkinter as ctk
from gui_components.info_panel import InfoPanel


class Panel(ctk.CTkFrame):
    def __init__(self, master, column, row, distribution, at_command, LOADING, ALL_BUTTONS, **kwargs):
        super().__init__(master, **kwargs)

        self.at_command = at_command

        # Default number of columns
        number_of_columns = 1
        self.grid(column=column, row=row, sticky="nw",
                    padx=10, pady=10)

        # Configure rows and columns of the GeneralFrame to expand
        if len(at_command['send_parameters']) > 0:
            if distribution == 'vertical':
                print('Vertical')
                self.grid_rowconfigure((0, 1, 3), weight=1)
                self.grid_columnconfigure(0, weight=1)
            else:
                print('Horizontal')
                self.grid_columnconfigure((0, 1), weight=1)
                self.grid_rowconfigure((0, 1), weight=1)
                number_of_columns = 2
        else:
            print('No parameters')
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
        
        self.title_label = ctk.CTkLabel(self, text=at_command['title'], font=('Helvetica', 12, 'bold'))
        self.title_label.grid(column=0, row=0, 
                            padx=10, pady=10,
                            columnspan=number_of_columns, sticky="nsew")
        
        # Create the info panel
        self.info_panel = InfoPanel(master=self, column=0, row= 1, LOADING=LOADING, at_command=at_command, ALL_BUTTONS=ALL_BUTTONS)

        # Create the edit panel
        # if distribution == 'horizontal':
        #     self.edit_panel = EditPanel(self, 1, 1, at_command, ALL_BUTTONS)
        # else:
        #     self.edit_panel = EditPanel(self, 0, 2, at_command, ALL_BUTTONS)
