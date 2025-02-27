import RPi.GPIO as GPIO

def dec2bin(decnum):
    if decnum == 0:
        return [0, 0, 0, 0, 0, 0, 0, 0]

    bins = [0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    while decnum > 0:
        bins[i] = decnum % 2
        decnum = decnum // 2
        i = i + 1

    bins.reverse()

    return bins    

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        num = input("Enter value from 0 to 255: ")
        try:
            num = int(num)
            if 0 <= num <= 255:
                GPIO.output(dac, dec2bin(num))
                voltage = float(num) / 256.0 * 3.3
                print(f"Output voltage is ~ {voltage:.4} V")
            else:
               print("Value is out of range [0,255]! Try again...")
        except ValueError:
            try:
                num = float(num)
                print("You have to type integer value , not floating")
            except ValueError:
                if num == "q": 
                    break
                else:
                    print("You have to type a number, not string")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

