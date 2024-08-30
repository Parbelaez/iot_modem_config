import customtkinter as ctk
import os
from PIL import Image, ImageTk
import threading
from gui_logic.ati_cgsn_cclk_check import initialize_info

LOADING = False


class GeneralFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Configure rows and columns of the GeneralFrame to expand
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1), weight=0)
        self.grid_rowconfigure(2, weight=1)

        # Create the welcome label
        self.welcome_label = ctk.CTkLabel(self,
                                        text="Loading modem information...",
                                        font=('Helvetica', 24, 'bold'),
                                        padx=10, pady=10)
        self.welcome_label.grid(column=0, columnspan=3, row=0, sticky="nsew")

        # Create the extra information frame
        self.extra_info_frame = ctk.CTkFrame(self)
        self.extra_info_frame.grid(column=0, columnspan=3,
                                row=2,
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
        self.gral_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Load the modem information
        
        self.start_thread(initialize_info, self.gral_frame, LOADING)


    # Start a thread method
    def start_thread(self, target, *args):
        threading.Thread(target=target, args=args).start()


app = App()
app.mainloop()
