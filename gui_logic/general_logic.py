import customtkinter as ctk
from time import sleep
from comms.ssh_to_serial import send_at_command_and_get_response
from gui_logic.update_buttons import update_buttons_states
from gui_logic.update_entries import update_entries_texts


def check_config(panel, master, at_command, LOADING, ALL_BUTTONS):

    LOADING = LOADING
    panel.ALL_BUTTONS = ALL_BUTTONS

    LOADING = True
    panel.after(0, update_buttons_states, LOADING, panel.ALL_BUTTONS)

    """
    Check the configuration of the device
    """
    # Set the labels to 'checking...'
    for label in panel.info_labels:
        label.configure(
            text=f"{label.cget('text').split(':')[0]}: checking...",
            text_color=["gray14", "gray84"])
        sleep(0.5)
    # Send the check at command
    try:
        response = send_at_command_and_get_response(at_command['commands']['check'])
        sleep(1)
    except Exception as e:
        response = None
        print(e)
    # Creates a list to store the fields values
    # to send them to the edit panel and fill the entries
    fields_text = []
    # Checks that the response is not empty
    if response:
        # Checks that the response is not an error / OK
        if response[0] != 'OK':
            break_outer_loop = False
            for i, label in enumerate(panel.info_labels):
                if response[i] == 'OK':
                    for j in range(len(panel.info_labels)-i):
                        panel.info_labels[i+j].configure(
                            text=f"{panel.info_labels[i+j].cget('text').split(':')[0]}: NA")
                    break_outer_loop = True
                # Checks if the field is a literal or a value
                if at_command['result_fields_values'][i] == 'literal':
                    text = response[i]
                # Checks that the options start in 0 or 1
                # This to prevent that i is correspondent to the index
                elif at_command[
                            'result_fields_values'][i][0][0] == '1':
                        text = at_command['result_fields_values'][i][int(
                            response[i])-1]
                # Check if the array is a list of non-enumerated values
                elif at_command['result_fields_values'][i][0][0] not in ['0', '1']:
                    text = response[i]
                else:
                    text = at_command['result_fields_values'][i][int(
                        response[i])]
                fields_text.append(text)
                label_name = label.cget('text').split(':')[0]
                field_value = text
                label.configure(
                    text=f"{label_name}: {field_value}")
                # Update the entries of the EditPanel according to the
                # received values for the InfoPanel
                for i, entry_label in enumerate(master.edit_panel.edit_labels):
                    if entry_label.cget('text')[:-1] == label_name:
                        entry = master.edit_panel.entries[i]
                        if isinstance(entry, ctk.CTkComboBox):
                            entry.set(text)
                        else:
                            entry.delete(0, ctk.END)
                            entry.insert(0, text)
                if break_outer_loop:
                    break
        else:
            for label in panel.info_labels:
                label_name = label.cget('text').split(':')[0]
                label.configure(
                    text=f"{label_name}: please, check prior configuration",
                    text_color='darkorange1')
    else:
        for label in panel.info_labels:
            label.configure(text=f"{label.cget('text').split(':')[0]}: error")

    LOADING = False
    # panel.after(0, update_entries_texts, panel, master, at_command)
    # Schedule UI update on the main thread
    panel.after(0, update_buttons_states, LOADING, panel.ALL_BUTTONS)
    # panel.after(0, update_combos, self)


def set_config():
    pass