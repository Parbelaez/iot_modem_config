import customtkinter as ctk
from comms.ssh_to_serial import send_at_command_and_get_response


'''
* Unique function to load the initial modem information
* This function is called in a separate thread to avoid blocking the GUI
* As an exception function, it will send 3 commands: ATI, AT+CGSN and AT+CCLK?
'''

def get_ati(self):
    ati_response = send_at_command_and_get_response('ATI')
    if len(ati_response) > 1:
        # Set the modem information
        self.welcome_label.configure(text=f"Welcome to the {ati_response[0]} {ati_response[1]} configuration!")
        self.revision_label.configure(text=f"Revision: {ati_response[2][8:]}")
    else:
        self.welcome_label.configure(text="Modem information not found.")
    return None

def get_cgsn(self):
    cgsn_response = send_at_command_and_get_response('AT+CGSN')
    if len(cgsn_response) > 0:
        # Set the IMEI
        self.imei_label.configure(text=f"IMEI: {cgsn_response[0]}")
    else:
        self.imei_label.configure(text="IMEI not found.")
    return None

def get_cclk(self):
    cclk_response = send_at_command_and_get_response('AT+CCLK?')
    if len(cclk_response) > 0:
        # Set the clock
        self.clock_label.configure(text=f"Clock: {cclk_response[0]}")
    else:
        self.clock_label.configure(text="Clock not found.")
    return None


def initialize_info(self, LOADING):
    LOADING = True
    # Load modem information
    get_ati(self)
    # Load the IMEI
    get_cgsn(self)
    # Load the clock
    get_cclk(self)
    LOADING = False
    return None

def main():
    print('Please, run the main.py file in the root directory')

if __name__ == '__main__':
    main()



