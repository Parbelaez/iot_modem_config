import customtkinter as ctk
import os
from PIL import Image, ImageTk
import threading
from gui_logic.ati_cgsn_cclk_check import initialize_info
from gui_components.parent_panel import Panel
from gui_logic.update_buttons import update_buttons_states
import at_commands
from comms.ssh_connection_send_at import SSHConnection


class GeneralFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Configure rows and columns of the GeneralFrame to expand
        self.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure((0, 1), weight=0)
        self.grid_rowconfigure(2, weight=1)

        # Create the welcome label
        self.welcome_label = ctk.CTkLabel(self,
                                        text="Loading modem information...",
                                        font=('Helvetica', 24, 'bold'),
                                        padx=10, pady=10)
        self.welcome_label.grid(column=0, row=0, sticky="nsew")

        # Create the extra information frame
        self.extra_info_frame = ctk.CTkFrame(self)
        self.extra_info_frame.grid(column=0, row=1,
                                padx=10, pady=10,
                                sticky="n")
        self.extra_info_frame.grid_columnconfigure((0, 1, 2), weight=0)

        # Create the clock label
        self.clock_label = ctk.CTkLabel(
            self.extra_info_frame, text="Clock: Loading...")
        self.clock_label.grid(column=0, row=1,
                            padx=10, pady=5,
                            sticky="nse")

        # Create the Revison label
        self.revision_label = ctk.CTkLabel(
            self.extra_info_frame, text="Revision: Loading...")
        self.revision_label.grid(column=1, row=1,
                                padx=10, pady=5,
                                sticky="ns")

        # Create the IMEI label
        self.imei_label = ctk.CTkLabel(
            self.extra_info_frame, text="IMEI: Loading...")
        self.imei_label.grid(column=2, row=1,
                            padx=10, pady=5,
                            sticky="nsw")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        LOADING = False
        ALL_BUTTONS = []
        ssh = SSHConnection()
        connected = ssh.connect()

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("dark-blue")

        self.title("IoT Modem Configuration and Testing")
        self.geometry("1700x1080")

        # Check if the icon path is correct
        icon_path = os.path.join("assets", "icon.png")
        if os.path.exists(icon_path):
            self.iconpath = ImageTk.PhotoImage(file=icon_path)
            self.iconphoto(False, self.iconpath)
        else:
            print("Icon image not found, skipping icon setup.")

        # Configure the grid of the App window to expand
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create the main frame
        self.gral_frame = GeneralFrame(master=self)

        # Create Panels Frame
        self.panels_frame = ctk.CTkFrame(self.gral_frame)
        self.panels_frame.grid(column=0, row=2, sticky="nsew",
                                padx=10, pady=10)
        self.panels_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.panels_frame.grid_rowconfigure((0, 1, 2), weight=1)

        # Create Panel Column 0
        self.column_0_frame = ctk.CTkFrame(self.panels_frame)
        self.column_0_frame.grid(column=0, row=0, sticky="nsew",
                                padx=10, pady=10)
        self.column_0_frame.grid_columnconfigure(0, weight=1)
        self.column_0_frame.grid_rowconfigure((0, 1, 2, 3), weight=0)

        # Create Panel Column 1
        self.column_1_frame = ctk.CTkFrame(self.panels_frame)
        self.column_1_frame.grid(column=1, row=0, sticky="nsew",
                                padx=10, pady=10)
        self.column_1_frame.grid_columnconfigure(0, weight=1)
        self.column_1_frame.grid_rowconfigure((0, 1, 2), weight=0)

        # Create Panel Column 2
        self.column_2_frame = ctk.CTkFrame(self.panels_frame)
        self.column_2_frame.grid(column=2, row=0, sticky="nsew",
                                padx=10, pady=10)
        self.column_2_frame.grid_columnconfigure(0, weight=1)
        self.column_2_frame.grid_rowconfigure(0, weight=0)
        self.column_2_frame.grid_rowconfigure(1, weight=1)

        # Create the connected frame
        self.connected_frame = ctk.CTkFrame(self.column_0_frame)
        self.connected_frame.grid(column=0, row=0, sticky="n",
                                padx=10, pady=(20, 10))
        self.connected_frame.grid_columnconfigure(0, weight=0)
        self.connected_frame.grid_columnconfigure(1, weight=1)
        self.connected_frame.grid_rowconfigure(0, weight=0)

        if connected:
            # Create connected image
            connected_image_path = os.path.join("assets", "connected.png")
            if os.path.exists(connected_image_path):
                connected_image = ctk.CTkImage(light_image=Image.open(connected_image_path),
                                            dark_image=Image.open(connected_image_path),
                                            size=(30, 30))
                self.connected_image_label = ctk.CTkLabel(
                    self.connected_frame, image=connected_image, text="")
                self.connected_image_label.grid(column=0, row=0, padx=10, pady=10)
            else:
                print("Connected image not found, skipping connected image setup.")
        else:
            # Create disconnected image
            disconnected_image_path = os.path.join("assets", "disconnected.png")
            if os.path.exists(disconnected_image_path):
                disconnected_image = ctk.CTkImage(
                                            light_image=Image.open(disconnected_image_path),
                                            dark_image=Image.open(disconnected_image_path),
                                            size=(30, 30))
                self.disconnected_image_label = ctk.CTkLabel(
                    self.connected_frame, image=disconnected_image, text="")
                self.disconnected_image_label.grid(
                    column=0, row=0, padx=10, pady=10)
            else:
                print("Disconnected image not found, skipping disconnected image setup.")
        
        # Create connected label
        connected_text = f"Connected to {ssh.host}" if connected else "Not connected"
        self.connected_label = ctk.CTkLabel(self.connected_frame, text=connected_text)
        self.connected_label.grid(column=1, row=0, padx=10, pady=10)
            

        # Create a subpanel for IMSI and ICCID
        self.imsi_iccid_panel = ctk.CTkFrame(self.column_0_frame)
        self.imsi_iccid_panel.grid(column=0, row=1, sticky="n",
                                padx=10, pady=10)
        self.imsi_iccid_panel.grid_columnconfigure((0, 1), weight=1)
        # Create the CIMI -IMSI- panel
        cimi_panel = Panel(
            master=self.imsi_iccid_panel, column=0, row=0,
            distribution='horizontal',
            at_command=at_commands.cimi, LOADING=LOADING, ALL_BUTTONS=ALL_BUTTONS)
        cimi_panel.grid(column=0, row=0, padx=10, pady=10, sticky="ns")
        
        # # Create the QCCID -ICCID- panel
        qccid_panel = Panel(
            master=self.imsi_iccid_panel, column=1, row=0,
            distribution='horizontal'
            , at_command=at_commands.qccid, LOADING=LOADING, ALL_BUTTONS=ALL_BUTTONS)
        qccid_panel.grid(column=1, row=0, padx=10, pady=10, sticky="ns")

        # # Create the COPS -Operator Selection- panel
        cops_panel = Panel(
            master=self.column_0_frame, column=0, row=2,
            distribution='horizontal',
            at_command=at_commands.cops, LOADING=LOADING, ALL_BUTTONS=ALL_BUTTONS)
        cops_panel.grid(column=0, row=2, columnspan=2, padx=20, pady=10, sticky="nwe")
        
        # Create the GDCONT -PDP Context- panel
        cgdcont_panel = Panel(
            master=self.column_0_frame, column=0, row=3,
            distribution='horizontal',
            at_command=at_commands.cgdcont, LOADING=LOADING, ALL_BUTTONS=ALL_BUTTONS)
        cgdcont_panel.grid(column=0, row=3, columnspan=2, padx=20, pady=10, sticky="nw")
        
        # Create the CREG -Network Registration- panel
        creg_panel = Panel(
            master=self.column_1_frame, column=0, row=0,
            distribution='vertical',
            at_command=at_commands.creg, LOADING=LOADING, ALL_BUTTONS=ALL_BUTTONS)
        creg_panel.grid(column=0, row=0, padx=10, pady=10, sticky="nwe")
        creg_panel.info_panel.info_labels[0].grid(columnspan=2)
        
        # Create the CFUN -Modem Functionality- panel
        cfun_panel = Panel(
            master=self.column_1_frame, column=0, row=1,
            distribution='vertical',
            at_command=at_commands.cfun, LOADING=LOADING, ALL_BUTTONS=ALL_BUTTONS)
        cfun_panel.grid(column=0, row=1, padx=10, pady=10, sticky="nwe")

        # Create the QIACT -PDP Context Activation- panel
        qiact_panel = Panel(
            master=self.column_1_frame, column=0, row=2,
            distribution='horizontal',
            at_command=at_commands.qiact, LOADING=LOADING, ALL_BUTTONS=ALL_BUTTONS)
        qiact_panel.edit_panel.entries[1].set("1 - Activated")
        qiact_panel.edit_panel.entries[1].configure(state="disabled")

        # Create the QIDEACT -PDP Context Deactivation- panel
        qideact_panel = Panel(
            master=self.column_1_frame, column=0, row=3,
            distribution='horizontal',
            at_command=at_commands.qideact, LOADING=LOADING, ALL_BUTTONS=ALL_BUTTONS)
        qideact_panel.grid(sticky="ns", pady=0)
        qideact_panel.title_label.grid(pady=(0, 0))
        qideact_panel.edit_panel.grid(pady=(0, 5))

        # Create the CGATT -Attach or Detach- panel
        cgatt_panel = Panel(
            master=self.column_2_frame, column=0, row=0,
            distribution='vertical',
            at_command=at_commands.cgatt, LOADING=LOADING, ALL_BUTTONS=ALL_BUTTONS)

        # Create the ping panel
        qping_panel = Panel(
            master=self.column_2_frame, column=0, row=1,
            distribution='horizontal',
            at_command=at_commands.qping, LOADING=LOADING, ALL_BUTTONS=ALL_BUTTONS)
        qping_panel.grid(sticky="wens", rowspan=2)
        qping_panel.edit_panel.grid(column=0, columnspan=2, sticky="wens", pady=(0, 5))
        qping_panel.rowconfigure(0, weight=0)
        qping_panel.rowconfigure(1, weight=1)

        # Connect to the device
        ssh = SSHConnection()

        #Load the modem information
        self.start_thread(initialize_info, self.gral_frame, LOADING, ALL_BUTTONS)
        # self.start_thread(update_buttons_states, LOADING, ALL_BUTTONS)


    # Start a thread method
    def start_thread(self, target, *args):
        threading.Thread(target=target, args=args).start()

# Create an instance of App
app = App()
# Start the main loop (so the window is always displayed)
app.mainloop()
