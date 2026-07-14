# ⏰ Python Digital Alarm Clock

A simple command-line **Digital Alarm Clock** built using Python. The program continuously displays the current system time, allows users to set an alarm in **HH:MM:SS** format, and triggers a visual alarm when the specified time is reached.

## 📌 Features

- User-friendly alarm time input
- Input validation for `HH:MM:SS` format
- Live digital clock display
- Automatic alarm triggering
- Flashing visual alert in the terminal
- Beginner-friendly Python project

---

## 🛠️ Technologies Used

- Python 3
- `datetime` module
- `time` module
- `os` module

---

## 📂 Project Structure

```
alarm-clock/
│
├── alarm.py
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository.

```bash
git clone https://github.com/your-username/your-repository-name.git
```

2. Navigate to the project folder.

```bash
cd your-repository-name
```

3. Run the Python program.

```bash
python alarm.py
```

---

## 📷 Example

```
--- Professional Cloud Alarm ---

Set alarm time (HH:MM:SS): 14:30:00

Alarm successfully set for 14:30:00...

Current Time: 14:29:55 | Alarm: 14:30:00
Current Time: 14:29:56 | Alarm: 14:30:00
Current Time: 14:29:57 | Alarm: 14:30:00
Current Time: 14:29:58 | Alarm: 14:30:00
Current Time: 14:29:59 | Alarm: 14:30:00

==============================
!!! ALARM TRIGGERED !!!
   WAKE UP! WAKE UP!
==============================

ALARM RINGING!!
```

---

## ⚠️ If the Displayed Time Is Incorrect

If the alarm shows the wrong time while running in VS Code, it is **not related to GitHub**. The program reads the **system time** from your computer.

Check the following:

- Ensure your computer's **date and time** are correct.
- Verify the **time zone** settings.
- Enable **automatic time synchronization** in your operating system.
- Restart VS Code after correcting the system clock.

You can verify your system time by running:

```python
from datetime import datetime
print(datetime.now())
```

If this shows the wrong time, the issue is with your system clock rather than the Python code.

---

## 🔮 Future Improvements

- Add alarm sound using `playsound` or `winsound`
- Multiple alarms
- Snooze option
- GUI using Tkinter
- Custom alarm message
- Cross-platform notification support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Open a Pull Request.

---

## 📄 License

This project is open source and available under the MIT License.

---

## 👨‍💻 Author

**Your Name**

If you like this project, consider giving it a ⭐ on GitHub!
