import customtkinter as ctk


def update_entries_texts(panel, master, at_command):
    """
    Update the entries of the EditPanel with the values of the InfoPanel.
    """
    edit_panel = master.edit_panel
    for i, label in enumerate(edit_panel.edit_labels):
        print('label.cget(text): ', label.cget('text'))
        if len(at_command['fields_names']) > 0:
            for j, field in enumerate(at_command['fields_names']):
                if label.cget('text')[:-1] == field:
                    edit_panel.entries[i].set(at_command['result_fields_values'][j])
        else:
            for i, parameter in enumerate(at_command['send_parameters']):
                edit_panel.entries[i].set(at_command['result_fields_values'][i])