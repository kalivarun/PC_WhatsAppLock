# WhatsApp Intrusion Detection System

## Overview

This project is designed to detect unauthorized access to WhatsApp on a PC. When WhatsApp is opened, the system captures a photo using the webcam, sends an email notification with the photo attached, and then locks the computer.

## Features

- **Internet Connectivity Check**: Ensures that the system is connected to the internet.
- **Automatic Web Login**: Logs into a specified web portal if not connected to the internet.
- **Application Monitoring**: Continuously monitors running applications for WhatsApp.
- **Intruder Photo Capture**: Captures a photo using the webcam when WhatsApp is detected.
- **Email Notification**: Sends an email with the captured photo attached to a specified email address.
- **System Lock**: Locks the workstation after capturing the photo and sending the email.

## Setup and Installation

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/whatsapp-intrusion-detection.git
    cd whatsapp-intrusion-detection
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure email settings**:
    - Open the `wtcamint.py` file.
    - Replace the `sender`, `sender_psd`, and `res` variables with your email credentials and recipient email address.

4. **Configure paths and settings**:
    - Ensure the `save_path` in the `Camera` class points to an existing directory where photos will be saved.

### Running the Script

- To start monitoring, run:
    ```bash
    python wtcamint.py
    ```

## Usage

- The script will run in a continuous loop, checking for internet connectivity and monitoring running applications.
- If WhatsApp is detected, it will perform the specified actions (photo capture, email notification, and system lock).

## File Structure

- **wtcamint.py**: Main script for monitoring WhatsApp and handling actions.
- **Whatsapp_bro.py**: Auxiliary script to handle WhatsApp detection and system locking.
- **requirements.txt**: List of required Python packages.
- **README.md**: This readme file.

## Dependencies

The following Python packages are required for this project:
- requests
- webbrowser
- pyautogui
- psutil
- smtplib
- email
- opencv-python
- datetime
- os
- ssl
- pyttsx3

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

## Contributing

If you wish to contribute to this project, please create a fork and submit a pull request.

## Contact

For any issues or questions, please contact:
- **Email**: k.s.varunchandra@gmail.com

---

Feel free to modify and enhance this project as needed. Contributions are welcome!

---
