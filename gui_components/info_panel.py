import customtkinter as ctk
from gui_logic import general_logic


class InfoPanel(ctk.CTkFrame):
    def __init__(self, master, column, row, LOADING, at_command, ALL_BUTTONS, **kwargs):
        super().__init__(master, **kwargs)
        
        self.at_command = at_command
        # self.column = column
        # self.row = row

        self.grid(column=column, row=row, sticky="nw",
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
        self.info_read_button = ctk.CTkButton(
            self, text=f'Check {at_command['short_name']}', command=lambda: self.start_thread(
                general_logic.check_config, self, at_command, LOADING, ALL_BUTTONS)
        )
        self.info_read_button.grid(
            column=0, row=0, padx=(5, 5), pady=(5, 0), sticky="we")
        
        ALL_BUTTONS.append(self.info_read_button)
