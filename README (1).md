# ⌨️ Ethical Python Keylogger with Real-Time Logging Animation

> ⚠️ **DISCLAIMER:** This project is strictly for **educational** and **authorized ethical use** only. Misuse of this tool is illegal and against GitHub policy.

---

## 1. 🧾 Project Overview

### 1.1 Description
This Python script is a **console-based keylogger** that includes:
- 🎯 Real-time keystroke capture
- 🔐 Ethical warning system
- 🎞️ Animated CLI visuals (typing effect, spinner, shutdown)
- 📁 Logging to `keystroke_log.txt` with timestamps
- ⏸️ Pause/resume control using the `ESC` key

### 1.2 Key Features
- **Consent System:** 🔒 Explicit user confirmation before logging
- **Timestamped Logging:** 🕒 Captures every key with a precise timestamp
- **ASCII Animations:** 🌀 Spinner, typing animation, warning signs
- **Live Feedback:** 📟 Terminal displays live logging status
- **Log File:** 📂 Keystrokes saved to `keystroke_log.txt`
- **Pause/Resume:** ⏹️ Press `ESC` to pause, then choose to continue or stop

---

## 2. 🚀 Getting Started

### 2.1 Installation
Install the required Python package:
```bash
pip install keyboard
```
> 📝 Note: Admin/root permissions may be required on some systems.

### 2.2 Usage
Run the script using Python:
```bash
python keylogger.py
```

### 2.3 Execution Steps
1. ⚠️ Ethical disclaimer is displayed.
2. ✍️ Type `I CONFIRM` to proceed.
3. ⌨️ Logging begins and writes data to `keystroke_log.txt`.
4. 🛑 Press `ESC` anytime to pause logging.
5. 🔁 Choose to resume or exit.

---

## 3. 📁 Project Structure

### 3.1 File Hierarchy
```
📦 your_repo/
├── keylogger.py
├── keystroke_log.txt  # (created automatically)
└── README.md
```

### 3.2 Log Output Format
Keystrokes are saved in the file `keystroke_log.txt` with timestamps:
```
2025-06-30 18:45:12.456 - H
e
l
l
o
[SPACE]
W
o
r
l
d
[ENTER]
```
Special keys are shown as:
```
[ENTER], [BACKSPACE], [CTRL], [SHIFT]
```

---

## 4. 🧠 Ethics & Usage Guidelines

### 4.1 Intended Use
This tool is meant for:
- 👨‍💻 Security professionals
- 👩‍🎓 Students of cybersecurity & ethical hacking
- 🧪 Pen-testing in controlled environments

### 4.2 Responsible Usage
- ✅ Must have explicit **written** consent
- 🖥️ Use only in **authorized environments**
- 📚 Purpose must be **educational or research-based**

> ❌ **NEVER** use for spying, unauthorized access, or any malicious intent.

---

## 5. 👤 Author Info

**Piyush Singh**  
🎓 Vivekananda Global University, Jaipur  
📧 [piyush.siingh2005@gmail.com](mailto:piyush.siingh2005@gmail.com)  
🔗 [GitHub](https://github.com/piyushsiingh)  
🔗 [LinkedIn](https://www.linkedin.com/in/piyush-singh-0b276332a)  
🌐 [Portfolio](https://bento.me/piyushsiingh)

---

## 6. 📜 License

### 6.1 MIT License Text
```text
MIT License

Copyright (c) 2025 Piyush Singh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 7. 🙏 Acknowledgements
- 🐍 Python's `keyboard` module
- 🎨 CLI animation inspiration from open source projects
- 🛡️ Educators and ethical hacking community promoting awareness
