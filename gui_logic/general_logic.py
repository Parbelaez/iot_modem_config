import customtkinter as ctk
from time import sleep
from comms.ssh_to_serial import send_at_command_and_get_response
from gui_logic.update_buttons import update_buttons_states


def ping_response(response, panel):
    text_to_display = ''
    for response_item in response:
        if response_item == 'OK':
            response_item = ''
        elif response_item.startswith('+QPING'):
            response_item = '\n' + response_item
        text_to_display += response_item + ','

    # Remove the trailing comma and insert the text into the text box
    text_to_display = text_to_display.strip(',')
    panel.text_box.insert(ctk.END, text_to_display)

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
                if hasattr(master, 'edit_panel'):
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
    # Schedule UI update on the main thread
    panel.after(0, update_buttons_states, LOADING, panel.ALL_BUTTONS)


def set_config(panel, master, at_command, LOADING, ALL_BUTTONS):
    parameters = []
    for entry in panel.entries:
        entry.configure(state="disabled")

    for entry in panel.entries:
        entry_text = entry.get()
        if entry_text == 'Enter Option':
            panel.edit_button.configure(
                text=f'Please, select an option', fg_color="red")
            sleep(2)
            panel.edit_button.configure(
                text=f'Set {at_command['short_name']}', fg_color="lightblue4")
            for entry in panel.entries:
                entry.configure(state="normal")
        else:
            print('Check index: ', entry_text.split(' - ')[0])
            print('Type: ', type(entry_text.split(' - ')[0]))
            print('len: ', len(entry_text.split(' - ')))
            if entry_text.split(' - ')[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and len(entry_text.split(' - ')) >= 2:
                print('Index int and more than 2')
                parameter = entry_text.split(' - ')[0]
                print('Parameter: ', parameter)
            else:
                parameter = entry_text
            parameters.append(parameter)
    at_command_to_send = at_command['commands']['set']
    print('at_command_to_send: ', at_command_to_send)
    for parameter in parameters:
        at_command_to_send += parameter + ','
    if at_command_to_send[-1] == ',':
        at_command_to_send = at_command_to_send[:-1]
    print('at_command_to_send: ', at_command_to_send)

    LOADING = True
    panel.after(0, update_buttons_states, LOADING, ALL_BUTTONS)
    panel.edit_button.configure(text=f'Setting {at_command["short_name"]}...')

    try:
        response = send_at_command_and_get_response(at_command_to_send)
        sleep(1)
    except Exception as e:
        response = None
        print(e)
    if response:
        if not isinstance(response, list):
            response = [response]
        if response[0] == 'OK':
            panel.edit_button.configure(
                text=f'{at_command["short_name"]}  set', fg_color="green")
            sleep(2)
            # Check if the command is a test command or a set command
            if 'type' in at_command:
                match at_command['short_name']:
                    case 'PING':
                        ping_response(response, panel)
                panel.edit_button.configure(
                    text=f'Set {at_command["short_name"]}', fg_color="lightblue4")
            else:
                check_config(master.info_panel, master,
                                at_command, LOADING, ALL_BUTTONS)
                panel.edit_button.configure(
                    text=f'Set {at_command["short_name"]}', fg_color="lightblue4")
        else:
            panel.edit_button.configure(
                text=f'Error setting {at_command["short_name"]}', fg_color="red")
            sleep(2)
            panel.edit_button.configure(
                text=f'Set {at_command["short_name"]}', fg_color="lightblue4")
            for entry in panel.entries:
                entry.configure(state="normal")
    else:
        panel.edit_button.configure(
            text=f'Error setting {at_command["short_name"]}', fg_color="red")
        sleep(2)
        panel.edit_button.configure(
            text=f'Set {at_command["short_name"]}', fg_color="lightblue4")
        for entry in panel.entries:
            entry.configure(state="normal")
    LOADING = False
    panel.after(0, update_buttons_states, LOADING, ALL_BUTTONS)