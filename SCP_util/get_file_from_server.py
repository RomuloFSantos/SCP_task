import os
import paramiko

def get_file_from_server(sftp, src, dest):

    if os.path.basename(src) not in dest:

        # Make sure the file name is in the destination
        dest = os.path.join(dest, os.path.basename(src))
        print('adding file name to dest')

    try:
        sftp.get(src, dest)
        print(f"File copied from {src}")

    except paramiko.SSHException as e:
        print('Problem to fetching file from {src}')
        raise e

    finally:
        sftp.close()