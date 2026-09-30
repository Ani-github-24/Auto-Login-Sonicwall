# SonicWall Captive Portal Auto-Login

A lightweight, event-driven Python script that automatically handles SonicWall captive portal authentication when connecting to your campus Wi-Fi or waking your computer from sleep.

---

## Features

* **Hands-Free Authentication:** Detects captive portal redirection and logs in automatically.
* **Battery-Friendly:** Runs only when triggered by network events or system unlock—no resource-heavy background loops.
* **Secure Credentials:** Keeps your student ID and password isolated in a local `.env` file that is ignored by Git.
* **Native Notifications:** Sends standard Windows toast notifications upon successful authentication or errors.

---

## Prerequisites

* [Python 3.8+](https://www.python.org/downloads/) installed (ensure **"Add Python to PATH"** is checked during installation).
* Git installed on your machine.

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Ani-github-24/sonicwall-autologin.git
cd sonicwall-autologin

```

### 2. Install Dependencies

```bash
pip install requests python-dotenv plyer

```

*(Or via requirements file: `pip install -r requirements.txt`)*

### 3. Configure Credentials

Create a `.env` file in the project root directory by copying the example template:

```bash
cp .env.example .env

```

Open `.env` and fill in your network credentials:

```ini
SONICWALL_USER="your_student_id"
SONICWALL_PASS="your_password"

```

> **Security Warning:** Never commit your `.env` file to GitHub. Verify that `.env` is listed inside your `.gitignore` file.

### 4. Adjust Firewall Endpoint (If Needed)

Open `auto_login.py` and ensure the `LOGIN_URL` and `PAYLOAD` keys match your campus gateway:

```python
LOGIN_URL = "https://192.168.1.1/auth.html"
PAYLOAD = {
    "userName": USERNAME,
    "password": PASSWORD,
    "domain": "LocalDomain"  # Remove if your portal does not require a domain
}

```

---

## Automating on Windows (Task Scheduler)

To make the script run invisibly whenever you wake your computer or reconnect to Wi-Fi:

1. Press `Win + R`, type **`taskschd.msc`**, and press Enter.
2. In the right panel, click **Create Task...** (not Basic Task).
3. Under the **General** tab:
* Name: `SonicWall AutoLogin`
* Select **Run only when user is logged on**.


4. Under the **Triggers** tab, add two triggers:
* **Trigger 1 (Wake/Unlock):** Click *New...* $\rightarrow$ Begin the task: **On workstation unlock** $\rightarrow$ Click **OK**.
* **Trigger 2 (Network Reconnect):** Click *New...* $\rightarrow$ Begin the task: **On an event**:
* **Log:** `Microsoft-Windows-NetworkProfile/Operational`
* **Source:** `NetworkProfile`
* **Event ID:** `10000`
* Click **OK**.




5. Under the **Actions** tab, click *New...*:
* **Action:** `Start a program`
* **Program/script:** `pythonw` *(Runs silently with no console window)*
* **Add arguments:** `"C:\Path\To\sonicwall-autologin\auto_login.py"` *(Use full path in quotes)*
* **Start in:** `C:\Path\To\sonicwall-autologin` *(Directory without quotes, needed to locate `.env`)*


6. Under the **Conditions** tab:
* **Uncheck** *Start the task only if the computer is on AC power* (ensures it runs on battery).
* Leave network condition unchecked.


7. Click **OK** to save.

---

## How It Works

1. **Connectivity Probe:** Queries `[http://gstatic.com/generate_204](http://gstatic.com/generate_204)`. If the status code is `204`, normal internet access is available and the script exits immediately.
2. **Authentication POST:** If intercepted (non-`204` response), the script dispatches a secure POST payload to the firewall gateway with your credentials.
3. **Notification:** Uses the `plyer` library to deliver a desktop notification confirming that access has been restored.

---

## License

Distributed under the MIT License. See `LICENSE` for more information.
