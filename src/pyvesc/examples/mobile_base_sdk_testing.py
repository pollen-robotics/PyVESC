from reachy2_sdk import ReachySDK
import math

ANGLE_A = 179.0
ANGLE_B = -179.0
MAX_DRIFT = 0.4
NB_ITER = 100

def has_drifted(reachy):
    odom = reachy.get_current_odometry()
    x = odom['x']
    y = odom['y']
    error = math.sqrt(x**2 + y**2)
    if error > MAX_DRIFT:
        print(f"Too much drift {error}!!")
        return True
    return False

def main():    
    reachy = ReachySDK(host='localhost')

    reachy.mobile_base.reset_odometry()
    reachy.mobile_base.turn_on()
    
    for i in range(NB_ITER):
        print(f"Iteration {i+1}/{NB_ITER}...")
        reachy.mobile_base.goto(x=0.0, y=0.0, theta=ANGLE_A)
        if has_drifted(reachy):
            break
        reachy.mobile_base.goto(x=0.0, y=0.0, theta=ANGLE_B)
        if has_drifted(reachy):
            break
    print("Test finished!")
        


if __name__ == "__main__":
    main()