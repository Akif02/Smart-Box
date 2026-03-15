import machine
import time

TRIGGER_PIN = 3
ECHO_PIN = 2
SERVO_PIN = 15

trigger = machine.Pin(TRIGGER_PIN, machine.Pin.OUT)
echo = machine.Pin(ECHO_PIN, machine.Pin.IN)

servo = machine.PWM(machine.Pin(SERVO_PIN))
servo.freq(50)

def get_distance():
    trigger.low()
    time.sleep_us(2)
    trigger.high()
    time.sleep_us(10)
    trigger.low()
    
    try:
        pulse_time = machine.time_pulse_us(echo, 1, 30000)
        if pulse_time < 0:
            return 999
    except OSError:
        return 999
    
    distance = (pulse_time * 0.0343) / 2
    return distance

def set_servo_angle(angle):
    min_duty = 3000
    max_duty = 7000
    
    duty = min_duty + int((angle / 180.0) * (max_duty - min_duty))
    servo.duty_u16(duty)

print("Starte Smarte Box...")

set_servo_angle(0)
time.sleep(1)

while True:
    dist = get_distance()
    print("Gemessene Distanz:", round(dist, 1), "cm")
    
    if dist < 15:
        print("-> Objekt erkannt! Box öffnet sich.")
        set_servo_angle(90)
        
        time.sleep(3)
        
        print("-> Box schließt sich.")
        set_servo_angle(0)
        
        time.sleep(1)
        
    time.sleep(0.1)