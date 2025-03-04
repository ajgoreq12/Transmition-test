import math

gears = [2.66, 1.78,1.3,1,0.8,0.63]
engine_torque = 455
engine_rpm = 6000
tiers = 28.7 * 0.0254 * math.pi
fdr = 3.73

def power_function(torque, rpm, ratio):
    power = ((torque * ratio) /5252) / ratio

    return power

def speed_calc(rpm , tires, ratio , fdr):
    speed = (rpm * tires * 60)/(ratio * fdr * 1000)
    
    return speed

while True:
    engine_rpm = int(input("Enter RPM: "))
    gear = int(input("Gear select (1-6): "))

    speed =  speed_calc(engine_rpm, tiers, gears[gear-1],fdr)
    print(f"Speed at {engine_rpm} RPM in {gear} is {speed} km/h")

