import os
import paramiko


if os.path.exists('env.py'):
    import env

# SSH configuration
HOST = os.environ['HOST']
USERNAME = os.environ['USERNAME']
SSH_KEY_PATH = os.environ['SSH_KEY_PATH']
RASP_SSH_FILE_PATH = os.environ['RASPI_SSH_FILE_PATH']


def send_at_command_and_get_response(at_command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        private_key = paramiko.RSAKey.from_private_key_file(SSH_KEY_PATH)
        ssh.connect(hostname=HOST, username=USERNAME, pkey=private_key)

        # Execute the Python script with the AT command as input
        command = f"echo '{at_command}' | python3 {RASP_SSH_FILE_PATH}"
        stdin, stdout, stderr = ssh.exec_command(command)

        # Read the output
        output = stdout.read().decode()
        error = stderr.read().decode()

        if error:
            print(f"Error occurred: {error}")
        else:
            print(f"Modem response:\n{output}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ssh.close()
    # Return the output as a list of strings
    output_splitlines = output.splitlines()
    result = []
    for item in output_splitlines:
        if item == '':
            output_splitlines.remove(item)
        elif item == at_command:
            output_splitlines.remove(item)
    for item in output_splitlines:
        temp = item.split(',')
        for item in temp:
            if item == '':
                temp.remove(item)
            else:
                item = item.replace(
                    at_command.upper().removeprefix("AT").replace("?", ": "), '').replace("'", "").replace(' ', '').replace('"', '').replace(':', '')
                result.append(item)
    print(f'{at_command} output splitlines filtered 2: ', result)
    return result


def main():
    at_command = input("Enter the AT command you want to send: ")
    send_at_command_and_get_response(at_command)


if __name__ == '__main__':
    main()
