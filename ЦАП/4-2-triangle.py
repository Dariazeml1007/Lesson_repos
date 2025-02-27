import RPi.GPIO as GPIO
import time

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

inc_flag = 1
t = 0
x = 0

try:
    period = float(input("Type a period for sygnal: "))

    while True:
        GPIO.output(dac, dec2bin(x))

        if   x == 0:    inc_flag = 1
        elif x == 255:  inc_flag = 0

        x = x + 1 if inc_flag == 1 else x - 1

        time.sleep(period/512)

except ValueError:
    print("Inapropriate period!")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
