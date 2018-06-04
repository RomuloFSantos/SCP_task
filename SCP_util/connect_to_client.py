import paramiko

def connect_to_client(credentials):

    client = paramiko.SSHClient()   # instantiate object
    client.load_system_host_keys()  # Load known host keys
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Auto add a client that is not in your policy key

    try:
        transport = paramiko.Transport((credentials['server'], 22))
        transport.connect(username=credentials['username'], password=credentials['password'])
        sftp = paramiko.SFTPClient.from_transport(transport)

        return sftp

    except paramiko.SSHException as e:
        print('Connection Failed on Transport ')
        raise e
