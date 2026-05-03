import serial
import time
import gpiozero

led = gpiozero.PWMLED(18)


PORT = "/dev/ttyACM0"       #port in pi
BAUD = 9600                 #baud rate
def main():
    arduino = connect()
    if not arduino:
        return
    global integral
    try:
        integral = 0
        while True:
            raw = arduino.readline()
            line = raw.decode("utf-8", errors="replace").strip()

            if line:
                value = parse(line)
                #print(value)
                if value is not None:
                    pi_controller(value)

    except KeyboardInterrupt:
        arduino.close()
        led.close()


def connect():
    try:
        arduino = serial.Serial(PORT, BAUD, timeout=0.1)
        time.sleep(2)
        print(f"Arduino connected to {PORT}")
        return arduino
    except serial.SerialException:
        print(f"Could not connect to {PORT}")
        return None
    
def parse(line):
    try:
        value = float(line)
        return value
    except:
        return None
    
def pi_controller(current):            #PI controller
    global integral
    target = 600.0
    
    error = target - current

    kp = 0.001667
    ki = 0.00005
    dt = 0.5

    integral = integral + (error * dt)

    if integral > 500:
        integral = 500
    elif integral < -500:
        integral = -500

    p = kp * error
    i = ki * integral

    pwm = p + i

    if pwm < 0:
        pwm = 0
    elif pwm > 1:
        pwm = 1

    #print(pwm)    
    led.value = pwm


main()


