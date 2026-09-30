import os
import requests
import urllib3
from dotenv import load_dotenv
from plyer import notification  # Add this new import

load_dotenv()
USERNAME = os.getenv("SONICWALL_USER")
PASSWORD = os.getenv("SONICWALL_PASS")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

LOGIN_URL = "https://192.168.1.1/auth.html" 
PAYLOAD = {
    "userName": USERNAME,
    "password": PASSWORD,
}

def check_and_login():
    try:
        test = requests.get("http://gstatic.com/generate_204", timeout=5)
        
        if test.status_code != 204:
            # Captive portal detected, attempting login
            response = requests.post(LOGIN_URL, data=PAYLOAD, verify=False)
            
            if response.status_code == 200:
                # Success Notification
                notification.notify(
                    title="SonicWall Auto-Login",
                    message="Successfully authenticated. Internet is connected!",
                    app_icon=None,  # You can add a path to an .ico file here if you want
                    timeout=5       # Notification stays for 5 seconds
                )
            else:
                # Failure Notification
                notification.notify(
                    title="SonicWall Auto-Login Error",
                    message=f"Login failed! HTTP Status: {response.status_code}",
                    timeout=7
                )
        # We do nothing if status is 204, so it doesn't spam you when already connected.
    except Exception as e:
        # Network error Notification
        notification.notify(
            title="SonicWall Script Error",
            message="Could not reach the network.",
            timeout=5
        )

if __name__ == "__main__":
    check_and_login()