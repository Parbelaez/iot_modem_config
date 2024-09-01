import threading


# Start a thread method
def start_thread(target, *args):
    threading.Thread(target=target, args=args).start()
