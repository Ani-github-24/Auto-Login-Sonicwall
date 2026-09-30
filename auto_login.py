import os
import time
import requests
import urllib3
import logging
from dotenv import load_dotenv
from plyer import notification

# 1. Setup Logging and Paths (Crucial for Task Scheduler)
script_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(script_dir, "login.log")

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# 2. Load Credentials using absolute paths
load_dotenv(os.path.join(script_dir, ".env"))
USERNAME = os.getenv("SONICWALL_USER")
PASSWORD = os.getenv("SONICWALL_PASS")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

LOGIN_URL = "https://172.20.100.100:7806" 
PAYLOAD = {
    "userName": USERNAME,
    "password": PASSWORD
}

def check_and_login():
    # Give Windows 3 seconds to fully connect to the Wi-Fi adapter
    time.sleep(3)
    logging.info("Script triggered. Checking connection...")
    
    try:
        test = requests.get("http://gstatic.com/generate_204", timeout=5)
        
        if test.status_code != 204:
            logging.info("Captive portal detected. Sending login request...")
            response = requests.post(LOGIN_URL, data=PAYLOAD, verify=False)
            
            if response.status_code == 200:
                logging.info("Successfully authenticated to SonicWall.")
                notification.notify(
                    title="SonicWall Auto-Login",
                    message="Successfully authenticated. Internet is connected!",
                    timeout=5 
                )
            else:
                logging.error(f"Login failed! HTTP Status: {response.status_code}")
                notification.notify(
                    title="SonicWall Auto-Login Error",
                    message=f"Login failed! HTTP Status: {response.status_code}",
                    timeout=7
                )
        else:
            logging.info("Internet is already active. No login required.")
            
    except Exception as e:
        logging.error(f"Network error: {e}")
        notification.notify(
            title="SonicWall Script Error",
            message="Could not reach the network.",
            timeout=5
        )

if __name__ == "__main__":
    check_and_login()