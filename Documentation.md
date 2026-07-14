# Python Digital Alarm Clock - Documentation

## 1. Introduction

The Python Digital Alarm Clock is a command-line application that allows users to set an alarm using the HH:MM:SS format. The program continuously monitors the system time and triggers a visual notification when the specified alarm time is reached.

---

## 2. Objective

The objective of this project is to demonstrate the use of Python loops, functions, input validation, and the datetime module to create a simple alarm clock application.

---

## 3. Technologies Used

- Python 3.x
- datetime module
- time module
- os module

---

## 4. Modules Used

### datetime

Used to obtain the current system time.

```python
from datetime import datetime
```

### time

Used to pause the program for one second while checking the current time.

```python
time.sleep(1)
```

### os

Imported for future enhancements such as clearing the console screen.

---

## 5. Functions

### validate_time()

Purpose:
- Validates user input.
- Ensures the entered time follows HH:MM:SS format.

Returns:
- True if valid.
- False if invalid.

---

### set_alarm()

Purpose:
- Accepts alarm input.
- Displays current time.
- Compares current time with alarm time.
- Triggers the alarm.

---

## 6. Program Workflow

1. Start the program.
2. Ask the user to enter an alarm time.
3. Validate the input.
4. Display the current time continuously.
5. Compare current time with alarm time.
6. Trigger the alarm when both match.
7. Display a flashing alert.
8. End the program.

---

## 7. Flowchart

```
Start
  │
  ▼
Enter Alarm Time
  │
  ▼
Validate Input
  │
  ├── Invalid → Ask Again
  │
  ▼
Display Current Time
  │
  ▼
Compare Current Time
  │
  ├── No → Wait 1 Second
  │        │
  │        └───────────────┐
  │                        │
  ▼                        │
Alarm Time Reached? ───────┘
  │
  ▼
Display Alarm Message
  │
  ▼
End
```

---

## 8. Sample Output

```
Set alarm time (HH:MM:SS): 08:30:00

Alarm successfully set for 08:30:00...

Current Time: 08:29:58
Current Time: 08:29:59

==============================
!!! ALARM TRIGGERED !!!
==============================
```

---

## 9. Advantages

- Easy to use
- Lightweight
- Beginner-friendly
- Demonstrates Python fundamentals

---

## 10. Limitations

- No alarm sound
- Single alarm only
- Command-line interface
- Stops after one alarm

---

## 11. Future Scope

- GUI using Tkinter
- Alarm sound
- Multiple alarms
- Snooze button
- Desktop notifications

---

## 12. Conclusion

The project successfully implements a digital alarm clock using Python. It demonstrates the practical use of loops, functions, input validation, and time management while providing a foundation for more advanced alarm applications.
