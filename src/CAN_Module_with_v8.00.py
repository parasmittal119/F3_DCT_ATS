from usb_can_analyzer import Converter
convertor = Converter("COM10", baudrate=9600)
while True:
    data = convertor.readMessage()
    print(data)