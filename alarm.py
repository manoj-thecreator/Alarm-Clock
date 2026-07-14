import time
from datetime import datetime
import os

def validate_time(alarm_time):
    """Check if the user input is in correct HH:MM:SS format"""
    if len(alarm_time) != 8:
        return False
    try:
        # Try to parse the input string into a time object
        datetime.strptime(alarm_time, "%H:%M:%S")
        return True
    except ValueError:
        return False

def set_alarm():
    print("--- Professional Cloud Alarm ---")
    
    # 1. LOOP for Input Validation
    while True:
        alarm_time = input("Set alarm time (HH:MM:SS): ")
        if validate_time(alarm_time):
            break
        print("Invalid Format! Please use HH:MM:SS (e.g., 14:30:00)")

    print(f"Alarm successfully set for {alarm_time}...")

    # 2. LOOP for Time Checking & Live Display
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        # Visual Feedback: Clear screen and show live time
        # (This makes the loop look like a real clock)
        print(f"Current Time: {current_time} | Alarm: {alarm_time}", end="\r")

        if current_time == alarm_time:
            print("\n" + "="*30)
            print("!!! ALARM TRIGGERED !!!")
            print("   WAKE UP! WAKE UP!")
            print("="*30)
            
            # 3. LOOP for Visual Alert (Flashing)
            for i in range(10):
                print("ALARM RINGING!!", end="\r")
                time.sleep(0.5)
                print("                ", end="\r")
                time.sleep(0.5)
            break

        time.sleep(1)

if __name__ == "__main__":
    set_alarm() 
