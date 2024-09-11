import os
import paramiko


class SSHConnection:
    def __init__(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if os.path.exists('env.py'):
            import env


        # SSH configuration
        self.host = os.environ['HOST']
        self.username = os.environ['USERNAME']
        self.ssh_key_path = os.environ['SSH_KEY_PATH']
        self.raspi_ssh_file_path = os.environ['RASPI_SSH_FILE_PATH']
    
    def connect(self):
        try:
            private_key = paramiko.RSAKey.from_private_key_file(
                self.ssh_key_path)
            self.ssh.connect(hostname=self.host,
                             username=self.username, pkey=private_key)

            print(f"Connected to SSH server {self.host}")
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    def send_at_command_and_get_response(self, at_command):
        try:
            # Execute the Python script with the AT command as input
            command = f"echo '{at_command}' | python3 {
                self.raspi_ssh_file_path}"
            stdin, stdout, stderr = self.ssh.exec_command(command)

            # Read the output
            output = stdout.read().decode()
            error = stderr.read().decode()

            if error:
                print(f"Error occurred: {error}")
            else:
                print(f"Modem response:\n{output}")

        except Exception as e:
            print(f"An error occurred: {e}")
        
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
    
    def close(self):
        self.ssh.close()
        print("SSH connection closed")


def main():
    print("This script is not intended to be run directly.")
    print("If you want to send an AT command, use the send_at.py script.")


if __name__ == '__main__':
    main()