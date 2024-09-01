import customtkinter as ctk
from time import sleep
from comms.ssh_to_serial import send_at_command_and_get_response


def check_config(panel, at_command, LOADING, ALL_BUTTONS):

    LOADING = LOADING
    ALL_BUTTONS = ALL_BUTTONS

    LOADING = True
    # TODO: Update button states
    #panel.after(0, update_button_states, LOADING, ALL_BUTTONS)
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
        print(at_command['commands']['check'])
        response = send_at_command_and_get_response(at_command['commands']['check'])
        print(response)
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
                    print('fields_text: ', fields_text)
                    print('Breaking...')
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
    # panel.after(0, update_button_states, self, LOADING, all_buttons)
    # panel.after(0, update_combos, self)


def set_config():
    pass