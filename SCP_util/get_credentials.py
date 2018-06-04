def get_credentials(config):

    credentials = dict()

    try:
        with open(config, 'r') as file:

            for line in file:

                key, value = line.strip().split('=')

                if len(value)==0:
                    print(f'***** KEY ERROR: The field "{key}" has no value. Check your config ******')
                    #raise

                credentials[key] = value

    except IOError as e:
        raise e

    return credentials
