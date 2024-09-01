import customtkinter as ctk
from gui_logic.general_logic import set_config


class EditPanel(ctk.CTkFrame):
    def __init__(self, master, column, row, at_command, LOADING, ALL_BUTTONS, **kwargs):
        super().__init__(master, **kwargs)

        self.at_command = at_command

        if len(at_command['send_parameters']) > 1 and len(at_command['fields_names']) == len(at_command['send_parameters']):
            sticky = "nw"
        else:
            sticky = "nwe"

        self.grid(column=column, row=row, sticky=sticky,
                    padx=10, pady=10)
        self.grid_columnconfigure((0, 1), weight=1)

        # Create the labels
        self.labels_text = at_command['send_parameters']
        self.edit_labels = [
            ctk.CTkLabel(self, text=f'{label_text}:')
            for label_text in self.labels_text
        ]
        self.entries = []

        column = 0
        row = 1
        # Position the labels
        for i, label in enumerate(self.edit_labels):
            # Prevents that when commands with more parameters than info fields
            # are displayed, the program crashes
            if len(at_command['parameters_fields_positions']) <= i:
                break
            column = at_command['parameters_fields_positions'][i][0]
            row = at_command['parameters_fields_positions'][i][1]
            label.grid(column=column, row=row,
                    padx=(5, 5), pady=(5, 0), sticky="nw")
            if len(at_command['fields_names']) > 0:
                for j, field in enumerate(at_command['fields_names']):
                    if label.cget('text')[:-1] == field:
                        if at_command['result_fields_values'][j] == 'literal':
                            entry = ctk.CTkEntry(self)
                            entry.grid(column=column+1, row=row,
                                    padx=(5, 5), pady=(5, 0), sticky="nwe")
                        else:
                            entry = ctk.CTkComboBox(self, values=at_command['result_fields_values'][j])
                            entry.grid(column=column+1, row=row,
                                    padx=(5, 5), pady=(5, 0), sticky="nwe")
                        self.entries.append(entry)
            else:
                for i, parameter in enumerate(at_command['send_parameters']):
                    if at_command['result_fields_values'][i] == 'literal':
                        entry = ctk.CTkEntry(self)
                        entry.grid(column=column+1, row=row,
                                padx=(5, 5), pady=(5, 0), sticky="nwe")
                    else:
                        entry = ctk.CTkComboBox(
                            self, values=at_command['result_fields_values'][i])
                        entry.grid(column=column+1, row=row,
                                padx=(5, 5), pady=(5, 0), sticky="nwe")
                    self.entries.append(entry)
        if 'parameters_fields_values' in at_command:
            for i in range(0, len(at_command['parameters_fields_values'])):
                for j, parameter_name in enumerate(at_command['parameters_fields_values'][i]):
                    for parameter in at_command['send_parameters']:
                        if parameter_name == parameter:
                            if at_command['parameters_fields_values'][i][1] == 'literal':
                                entry = ctk.CTkEntry(self)
                                entry.grid(column=column+1, row=row,
                                        padx=(5, 5), pady=(5, 0), sticky="nwe")
                            else:
                                entry = ctk.CTkComboBox(
                                    self, values=at_command['parameters_fields_values'][i][1])
                                entry.grid(column=column+1, row=row,
                                        padx=(5, 5), pady=(5, 0), sticky="nwe")
                            self.entries.append(entry)
        edit_button = ctk.CTkButton(
            self, text=f'Set {at_command['short_name']}', fg_color="lightblue4",
            command=lambda: self.start_thread(
                set_config, self, at_command, LOADING, ALL_BUTTONS)
        )
        if len(at_command['send_parameters']) > 1:
            edit_button.grid(
                column=1, row=row+1, padx=(5, 5), pady=(5, 5), sticky="we")
        else:
            label.after(0, lambda: label.destroy())
            entry.grid(column=0, row=0, padx=(5, 5), pady=(5, 5), sticky="we")
            edit_button.grid(
                column=1, row=0, padx=(5, 5), pady=(5, 5), sticky="we")