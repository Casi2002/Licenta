import time
import serial

class FingerprintSensor:
    def __init__(self, uart):
        self.uart = uart

    def _send_packet(self, packet_type, packet):
        header = b'\xEF\x01\xFF\xFF\xFF\xFF'
        length = len(packet) + 2
        checksum = sum(packet) + packet_type + (length >> 8) + (length & 0xFF)
        packet = header + bytes([packet_type, length >> 8, length & 0xFF]) + packet + bytes([checksum >> 8, checksum & 0xFF])
        self.uart.write(packet)

    def _get_reply(self):
        header = self.uart.read(9)
        if len(header) != 9 or header[:6] != b'\xEF\x01\xFF\xFF\xFF\xFF':
            return None, None
        packet_type = header[6]
        length = (header[7] << 8) | header[8]
        packet = self.uart.read(length)
        return packet_type, packet

    def get_image(self):
        self._send_packet(0x01, b'\x01')
        packet_type, packet = self._get_reply()
        if packet and packet[0] == 0x00:
            return True
        return False

    def image_2_tz(self, buffer_id):
        self._send_packet(0x01, b'\x02' + bytes([buffer_id]))
        packet_type, packet = self._get_reply()
        if packet and packet[0] == 0x00:
            return True
        return False

    def finger_search(self):
        self._send_packet(0x01, b'\x04\x01\x00\x00\x00\x00')
        packet_type, packet = self._get_reply()
        if packet and packet[0] == 0x00:
            return True
        return False

    def create_model(self):
        self._send_packet(0x01, b'\x05')
        packet_type, packet = self._get_reply()
        if packet and packet[0] == 0x00:
            return True
        return False

    def store_model(self, location):
        self._send_packet(0x01, b'\x06' + bytes([location >> 8, location & 0xFF]))
        packet_type, packet = self._get_reply()
        if packet and packet[0] == 0x00:
            return True
        return False

# High-Level Functions
def get_fingerprint(sensor):
    print("Waiting for image...")
    while not sensor.get_image():
        pass
    print("Templating...")
    if not sensor.image_2_tz(1):
        return False
    print("Searching...")
    if not sensor.finger_search():
        return False
    return True

def enroll_finger(sensor, location):
    for fingerimg in range(1, 3):
        if fingerimg == 1:
            print("Place finger on sensor...", end="")
        else:
            print("Place same finger again...", end="")

        while not sensor.get_image():
            print(".", end="")
            time.sleep(0.1)

        print("Image taken")
        print("Templating...", end="")
        if not sensor.image_2_tz(fingerimg):
            print("Error templating")
            return False
        print("Templated")

        if fingerimg == 1:
            print("Remove finger")
            time.sleep(1)
            while sensor.get_image():
                pass

    print("Creating model...", end="")
    if not sensor.create_model():
        print("Error creating model")
        return False
    print("Model created")

    print(f"Storing model #{location}...", end="")
    if not sensor.store_model(location):
        print("Error storing model")
        return False
    print("Model stored")
    return True

def get_num():
    i = 0
    while (i > 127) or (i < 1):
        try:
            i = int(input("Enter ID # from 1-127: "))
        except ValueError:
            pass
    return i

# Example Usage
if __name__ == "__main__":
    # Initialize the serial port
    uart = serial.Serial("/dev/ttyS0", baudrate=57600, timeout=1)

    # Initialize the custom fingerprint sensor
    finger = FingerprintSensor(uart)

    # Example: Get a fingerprint
    if get_fingerprint(finger):
        print("Fingerprint matched!")
    else:
        print("Fingerprint did not match.")

    # Example: Enroll a new fingerprint
    location = get_num()
    if enroll_finger(finger, location):
        print(f"Fingerprint enrolled successfully at location {location}.")
    else:
        print("Failed to enroll fingerprint.")
