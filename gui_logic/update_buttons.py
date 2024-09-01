import customtkinter as ctk


def update_buttons_states(LOADING, ALL_BUTTONS):
    for button in ALL_BUTTONS:
        if LOADING:
            button.configure(state='disabled')
        else:
            button.configure(state='normal')
    if LOADING:
        LOADING = False
    else:
        LOADING = True
    return LOADING