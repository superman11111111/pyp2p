from util import debug
from crypt import decrypt, encrypt


COMMANDS = [
    "start"
]


def parse_cmd(cmd, argv):
    debug(" == Parsing command == ")
    debug(cmd)
    if cmd == "start":
        print(f"Starting the service {argv[0]}")
        # Do stuff


def parse_bytes(recv):
    debug(" === Parsing bytes === ")
    debug(recv)
    try:
        dd = decrypt(recv)
        debug(f"Decrypted message: {dd}")
        try:
            dd = dd.decode()
            argv = dd.split(" ")
            if len(argv) > 1:
                cmd = argv[0]
                if cmd in COMMANDS:
                    parse_cmd(cmd, argv[1:])
        except:
            print(recv)
            raise Exception("Bytes could not be decoded properly")
    except:
        raise Exception("Decryption failed")
    debug(" ===================== ")
    print()



