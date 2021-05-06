__name__ = "Credentials"
__package__ = "Credentials"

import os
import Fernet

__key = ""
__key_file = "/Python/linkedin-bot/creds/.key.key"

if not os.path.exists(__key_file):
    __key = Fernet.generate_key()

    with open(__key_file, 'w') as key_file:
        key_file.write(__key.decode())
else:
    with open(__key_file, 'r') as key_file:
        __key = key_file.readline().encode()