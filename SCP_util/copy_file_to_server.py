import os
import paramiko

def copy_file_to_server(sftp, src, dest):

    if os.path.basename(src) not in dest:

        # Make sure the file name is in the destination
        dest = os.path.join(dest, os.path.basename(src))
        print('adding file name to dest')

    try:
        sftp.put(src, dest)
        print(f"File copied to {dest}")

    except paramiko.SSHException as e:
        print('Problem to copy file {src}')
        raise e

    finally:
        sftp.close()