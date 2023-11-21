import paramiko

def execute_remote_script(hostname, username, password, remote_script_path):
    # Establish an SSH connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname, username=username, password=password)

        # Run the remote script
        stdin, stdout, stderr = ssh.exec_command(f"python {remote_script_path}")

        # Print the output and errors
        print("Output:")
        print(stdout.read().decode())
        print("Errors:")
        print(stderr.read().decode())

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the SSH connection
        ssh.close()

if __name__ == "__main__":
    # Replace these with your actual server details
    remote_hostname = "your_server_ip"
    remote_username = "your_username"
    remote_password = "your_password"
    remote_script_path = "/path/to/remote_script.py"

    execute_remote_script(remote_hostname, remote_username, remote_password, remote_script_path)
