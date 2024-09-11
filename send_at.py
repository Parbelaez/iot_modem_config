import os
# from comms.ssh_to_serial import send_at_command_and_get_response
from comms.ssh_connection_send_at import SSHConnection


def send_at_command():
    ssh = SSHConnection()
    ssh.connect()
    at_command: str = input("Enter the AT command you want to send: ")
    response = ssh.send_at_command_and_get_response(at_command)
    print(response)
    ssh.close()


# if os.path.exists('env.py'):
#     import env

# # SSH configuration
# HOST = os.environ['HOST']
# USERNAME = os.environ['USERNAME']
# # Update this path to your SSH private key
# SSH_KEY_PATH = os.environ['SSH_KEY_PATH']


# def send_at_command():
#     try:
#         at_command: str = input("Enter the AT command you want to send: ")
#         response = send_at_command_and_get_response(at_command)
#         print(response)
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None


def main():
    send_at_command()


if __name__ == '__main__':
    main()
