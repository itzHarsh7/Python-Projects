import os
import sys
import json
import time
import requests
import subprocess
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtCore import QThread, pyqtSignal
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

# --------- CONFIGURATION ----------
CHROME_EXE = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE_PROFILE_DIR = rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data\MyCustomProfiles"
DEBUG_PORT = 9222
DEBUG_URL = f"http://127.0.0.1:{DEBUG_PORT}/json"
USERNAME = os.environ.get("GITHUB_USERNAME") or "your_username"
PASSWORD = os.environ.get("GITHUB_PASSWORD") or "your_password"
# ----------------------------------


class GitHubLoginWorker(QThread):
    log_signal = pyqtSignal(str)

    def run(self):
        try:
            self.log_signal.emit("Connecting Selenium to Chrome...")
            opt = Options()
            opt.add_experimental_option("debuggerAddress", f"127.0.0.1:{DEBUG_PORT}")
            driver = webdriver.Chrome(options=opt)

            self.log_signal.emit("Navigating to GitHub login page...")
            driver.get("https://github.com/login")

            wait = WebDriverWait(driver, 15)
            wait.until(EC.visibility_of_element_located((By.ID, "login_field"))).send_keys(USERNAME)
            driver.find_element(By.ID, "password").send_keys(PASSWORD, Keys.ENTER)

            wait.until(lambda d: d.current_url != "https://github.com/login")
            self.log_signal.emit("Logged into GitHub.")

        except Exception as e:
            self.log_signal.emit(f"Login failed: {e}")


class ChromeAutomationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chrome Debug + GitHub Login")
        self.setGeometry(200, 200, 600, 400)

        layout = QVBoxLayout()

        self.log = QTextEdit(self)
        self.log.setReadOnly(True)

        self.launch_btn = QPushButton("Launch Chrome")
        self.login_btn = QPushButton("Login to GitHub")

        self.launch_btn.clicked.connect(self.launch_chrome)
        self.login_btn.clicked.connect(self.start_login_thread)

        layout.addWidget(self.launch_btn)
        layout.addWidget(self.login_btn)
        layout.addWidget(self.log)

        self.setLayout(layout)
        self.current_profile_path = None
        self.login_thread = None

    def log_msg(self, msg):
        self.log.append(f"[{time.strftime('%H:%M:%S')}] {msg}")
        QApplication.processEvents()

    def is_debug_port_open(self):
        try:
            r = requests.get(DEBUG_URL)
            return r.status_code == 200
        except:
            return False

    def create_unique_profile(self):
        if not os.path.exists(BASE_PROFILE_DIR):
            os.makedirs(BASE_PROFILE_DIR)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        profile_name = f"MyCustomProfile_{timestamp}"
        profile_path = os.path.join(BASE_PROFILE_DIR, profile_name)
        os.makedirs(profile_path, exist_ok=True)
        self.current_profile_path = profile_path
        self.log_msg(f"Created new Chrome profile: {profile_name}")
        return profile_path

    def launch_chrome(self):
        profile_path = self.create_unique_profile()

        self.log_msg("Launching Chrome with remote debugging...")
        cmd = [
            CHROME_EXE,
            f"--remote-debugging-port={DEBUG_PORT}",
            f"--user-data-dir={profile_path}",
            "--no-first-run",
            "--no-default-browser-check"
        ]
        subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        self.log_msg("Waiting for debugger port...")
        for _ in range(20):  # wait up to 10 seconds
            if self.is_debug_port_open():
                self.log_msg("Chrome debugger is ready.")
                return
            time.sleep(0.5)

        self.log_msg("Failed to detect Chrome debugger.")

    def start_login_thread(self):
        self.launch_chrome()
        self.login_thread = GitHubLoginWorker()
        self.login_thread.log_signal.connect(self.log_msg)
        self.login_thread.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ChromeAutomationApp()
    win.show()
    sys.exit(app.exec_())
