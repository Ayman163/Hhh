import math

def check_sudden_stop(previous_speed, current_speed):
    # 1. Calculate the difference in speed between the previous and current speed
    drop_in_speed = previous_speed - current_speed
    
    # 2. If the drop is very high 
    if previous_speed > 30 and current_speed == 0:
        return True, drop_in_speed
    else:
        return False, drop_in_speed

# A car was speeding (moving 45 pixels) and suddenly stopped (0 pixels) due to a collision
prev_s = 45
curr_s = 0

is_stopped_abruptly, drop = check_sudden_stop(prev_s, curr_s)

print(f"Speed drop amount: {drop} pixels")
if is_stopped_abruptly:
    print("Hazard Alert: Abrupt and sudden vehicle stop (Accident Indicator)!")
else:
    print("Normal Movement")
