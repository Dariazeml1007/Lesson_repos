import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)


pwm = GPIO.PWM(27, 1000)
pwm.start(0)

try:
    while True:
        duty_cycle = int(input())
        pwm.ChangeDutyCycle(duty_cycle)
        print(3.3*duty_cycle/100)

finally:
    pwm.stop()
    GPIO.output(27,0)
    GPIO.cleanup()
