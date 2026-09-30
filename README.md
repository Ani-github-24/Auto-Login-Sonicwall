# SonicWall Captive Portal Auto-Login

A lightweight, event-driven Python script that automatically bypasses the SonicWall captive portal when you connect to your campus Wi-Fi or wake your computer. It runs silently in the background, logs its activity, and sends a Windows desktop notification when it successfully connects.

---

## Features

* **Hands-Free Authentication:** Automatically detects the captive portal and logs in without opening a browser.
* **Battery-Friendly & Event-Driven:** Runs only when triggered by a network connection or system unlock.
* **Automated Windows Setup:** Includes a one-click setup script (`setup_task.py`) to configure Windows Task Scheduler automatically.
* **Secure Credentials:** Keeps your username and password safe in a local, hidden `.env` file that is ignored by Git.
* **Native Notifications & Logging:** Alerts you via Windows toast notifications and logs all connection attempts to a `login.log` file.

---

## Prerequisites

* **Python 3.8+** (Ensure **"Add Python to PATH"** is checked during installation).
* **Git** installed on your machine.
* Windows OS (for Task Scheduler and native notifications).

---

## Installation & Setup

### 1. Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/Ani-github-24/sonicwall-autologin.git
cd sonicwall-autologin

```

### 2. Install Dependencies

Install the required Python libraries:

```bash
pip install requests python-dotenv plyer

```

### 3. Configure Your Credentials

Create a `.env` file in the project folder to store your credentials securely:

```bash
copy .env.example .env

```

Open the new `.env` file in a text editor and add your login details:

```ini
SONICWALL_USER="your_username"
SONICWALL_PASS="your_password"

```

> **Security Warning:** Never commit your `.env` file to GitHub. Make sure both `.env` and `login.log` are listed in your `.gitignore` file.

### 4. Adjust the Firewall IP (If Needed)

Open `auto_login.py` and ensure the `LOGIN_URL` matches your specific campus gateway:

```python
LOGIN_URL = "https://192.168.1.1/auth.html" 

```

---

## Activating the Automation (Windows)

You do not need to manually configure Windows Task Scheduler. You can use the included setup script to generate the rules automatically.

1. Open your terminal as an Administrator (optional but recommended).
2. Navigate to your project folder.
3. Run the setup script:

```bash
python setup_task.py

```

This will instantly create a background task named **SonicWall AutoLogin**. Windows will now silently execute `auto_login.py` whenever you wake your PC from sleep or connect to a new Wi-Fi network.

---

## Troubleshooting & Logs

If you want to check if the script is working or see why a login failed, open the `login.log` file in the project folder. It records exactly what happens every time you connect:

```text
2023-10-25 08:30:00 - INFO - Script triggered. Checking connection...
2023-10-25 08:30:03 - INFO - Captive portal detected. Sending login request...
2023-10-25 08:30:04 - INFO - Successfully authenticated to SonicWall.

```

---

## Files in this Repository

* `auto_login.py` - The core authentication and notification script.
* `setup_task.py` - The one-click Windows Task Scheduler configuration script.
* `.env.example` - A template showing how to format your secure credentials.
* `.gitignore` - Prevents Git from uploading your passwords and local logs.

---

## License

Distributed under the MIT License. Feel free to fork and modify for your own campus networks.