import serial
import serial.tools.list_ports as list_ports

print("Microbit to PC USB serial bridge test.")

""" Code for finding the com port is copied from here:
    https://github.com/hardwaremonkey/microbit/blob/master/hand_gesture/base/blink_leo.py
    
    Microbit serial to USB inspiration from here:
    https://www.digikey.dk/en/maker/blogs/2018/how-to-use-the-serial-port-on-your-microbit
"""
PID_MICROBIT = 516
VID_MICROBIT = 3368
TIMEOUT = 0.1


def find_comport(pid, vid, baud):
    """ Open the serial port with device with <pid> and <vid> connected. """
    ser_port = serial.Serial(timeout = TIMEOUT)
    ser_port.baudrate = baud
    ports = list(list_ports.comports())
    print("scanning ports")
    for p in ports:
        print('pid: {} vid: {}'.format(p.pid, p.vid))
        if (p.pid == pid) and (p.vid == vid):
            print("found target device pid: {} vid: {} port: {}".format(p.pid, p.vid, p.device))
            ser_port.port = str(p.device)
            return ser_port
    return None


def main():
    print("looking for microbit")
    ser_micro = find_comport(PID_MICROBIT, VID_MICROBIT, 115200)
    if not ser_micro:
        print("microbit not found")
        return
    print('opening and monitoring microbit port')
    ser_micro.open()
    while True:
        line = ser_micro.readline().decode("utf-8")
        if line:  # If it isn't a blank line
            """ Here goes all code to interpret any type of command coming from the microbit."""
            print(line)
    ser_micro.close()


if __name__ == "__main__":
    main()
    print("exiting")
