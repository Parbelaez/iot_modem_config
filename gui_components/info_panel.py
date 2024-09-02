import customtkinter as ctk
from gui_logic import general_logic
from gui_logic.start_thread import start_thread


class InfoPanel(ctk.CTkFrame):
    def __init__(self, master, column, row,
                 LOADING, at_command, ALL_BUTTONS, **kwargs):
        super().__init__(master, **kwargs)
        
        self.at_command = at_command
        self.ALL_BUTTONS = ALL_BUTTONS

        self.grid(column=column, row=row, sticky="wen",
                    padx=10, pady=(10, 5))
        
        # Create the labels
        self.labels_text = at_command['fields_names']
        self.info_labels = [
            ctk.CTkLabel(self, text=f'{
                label_text}: please, retrieve it')
                for label_text in self.labels_text
        ]

        # Position the labels
        for i, label in enumerate(self.info_labels):
            column = at_command['info_fields_positions'][i][0]
            row = at_command['info_fields_positions'][i][1]
            label.grid(column=column, row=row,
                    padx=(5, 5), pady=(5, 0), sticky="nw")
        
        # Create the read button
        if len(at_command['fields_names']) == 1 and at_command['short_name'] not in ['IMSI', 'ICCID']:
            button_column = 1
            label.grid(column=0, row=0, padx=(5, 5), pady=(5, 5), sticky="nw")
        else:
            button_column = 0

        self.info_read_button = ctk.CTkButton(
            self, text=f'Check {at_command['short_name']}', command=lambda: start_thread(
                general_logic.check_config, self, master, at_command,
                    LOADING, self.ALL_BUTTONS)
        )
        self.ALL_BUTTONS.append(self.info_read_button)
        columnspan = self.grid_size()[0]
        self.info_read_button.grid(
            column=button_column, row=0, columnspan=columnspan, padx=(5, 5), pady=(5, 5), sticky="wen")
        
        # Configure the columns to expand
        # after the whole panel has been created
        for col in range(self.grid_size()[0]):
            self.grid_columnconfigure(col, weight=1)
