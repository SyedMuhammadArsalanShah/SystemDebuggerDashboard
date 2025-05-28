
## 📊 System Debugger Dashboard

A modern **dashboard system** to monitor real-time logs and system health — built with **Python (Tkinter + FastAPI)** and a **Tailwind CSS-based HTML frontend**. It shows logs, alerts, CPU/memory stats, and supports light/dark themes.

---

### 🧾 Features

* ✅ Real-time log streaming
* ⚠️ Alert filtering (WARNING/ERROR)
* 💻 System health monitor (CPU, RAM, Disk)
* 🌗 Light/Dark theme toggle
* 📁 No database, simple file-based logs
* ⚙️ 100% in Python (backend) + HTML/CSS (frontend)

---

### 📂 Project Structure

```
📁 your_project/
├── backend_api.py         # FastAPI backend
├── tkinter_app.py         # Log simulator with Tkinter
├── app.log                # Live log file (auto-generated)
├── index.html             # Frontend dashboard UI
└── README.md              # Project documentation
```

---

### 🚀 Getting Started

#### 1️⃣ Start Log Generator

```bash
python tkinter_app.py
```

> 💡 This creates `app.log` and adds random logs (INFO, WARNING, ERROR) continuously.

#### 2️⃣ Start FastAPI Backend

```bash
uvicorn backend_api:app --reload --host 0.0.0.0 --port 8000
```

> ⚙️ Runs backend server at: `http://localhost:8000`

#### 3️⃣ Launch the Dashboard

* Double-click `index.html` or
* Right-click → "Open with Browser"

---

### 🔗 Available APIs

| Endpoint  | Description                    |
| --------- | ------------------------------ |
| `/logs`   | Returns last 50 logs           |
| `/alerts` | Returns last 20 warning/errors |
| `/health` | Returns CPU, RAM, Disk stats   |

---

### 🖼️ Screenshot

![Dashboard Screenshot](https://github.com/user-attachments/assets/667a0dd1-7010-46a8-bb7e-241840ab898b)

---

### 🛠️ Requirements

* Python 3.8+
* FastAPI
* Uvicorn
* psutil

#### Install:

```bash
pip install fastapi uvicorn psutil
```

---

### 👨‍💻 Author

**Syed M Arsalan Shah Bukhari**
📚 Instructor | 👨‍💻 Mobile & Web Developer | 🧠 Data Scientist

---

### 📜 License

MIT License. Free for personal & academic use.
