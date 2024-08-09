import sys
import select

serial_poll = select.poll()
serial_poll.register(sys.stdin, select.POLLIN)


def readline_serial():
    """
    reads a single line over serial, stripped from the newline.

    :return: returns the characters which were read, otherwise returns None
    """
    msg = sys.stdin.readline() if serial_poll.poll(0) else None
    # filter out empty messages
    if msg is None:
        return None
    msg = msg.strip()
    if msg == "":
        return None
    return msg



if __name__ == "__main__":

    def handle_command(command):
        """
        Handle a command received over serial.

        :param command: (String) the command to handle
        """
        if command is None:
            return
        # sys.stdout.write(command + "\n")

        if command == "p":
            sys.stdout.buffer.write("test\n")
        else: # unrecognized command
            sys.stdout.buffer.write(f"{command!r} error\n")

    while True:
        # continuously read commands over serial and handle them
        message = readlineSerial()
        handle_command(message)
