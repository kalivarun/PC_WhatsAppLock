import requests
import webbrowser
import pyautogui as pi
import time as t
import psutil
import smtplib
import os
import ssl
from email.message import EmailMessage
import ctypes
import pyttsx3

###sound 

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties for speech output (adjust as needed)
engine.setProperty('rate', 115)    # Adjust the speech rate (words per minute)
engine.setProperty('volume', 0.6)  # Adjust the speech volume (0.0 to 1.0)

# Get a list of available voices (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id) 

# Set a specific voice (optional)
# Example: engine.setProperty('voice', voices[1].id)  # Use the second available voice

# Text to be converted to speech
text = "   kindly ,Get permission to open this app sir "
text2 = " sent a mail to verify sir "




#for email bro

sender = "k.s.varunchandra@gmail.com"
sender_psd = "vxfl vsam lhwc jtnn"
res = "k.s.varunchandra@gmail.com"
subject = 'Someone new opened whatsapp in your pc'
body = """Virus reporting sir,
idk who but someone opended your whatsapp without your permission
kindly disconnect your whatsapp web from your pc 
"""

em = EmailMessage()
em.set_content(body)
em['Subject'] = subject
em['From'] = sender
em['To'] = res

#camera script
import cv2
import datetime
import time as t
# Define a global variable to store the file path
file_camera = ''

# Initialize the camera
class Camera:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)  # Initialize the camera
        self.current_time = datetime.datetime.now()

    def click_photo(self):
        global file_camera  # Access the global variable

        if not self.camera.isOpened():
            print("Error: Could not open camera.")
             
        else:
            # Capture a photo
            ret, frame = self.camera.read()

            if not ret:
                #print("Error: Could not capture a photo.")
                f=1
            else:
                # Save the captured photo
                save_path = 'D:\\Pythonnn\\Found_you\\'
                date_time = self.current_time.strftime("%d-%m_%H.%M")
                file = os.path.join(save_path, f"{date_time}.jpg")
                cv2.imwrite(file, frame)
                #print(f"Photo saved as '{file}'.")
                t.sleep(3)
                # Release the camera
                self.camera.release()
                # Update the global variable
                file_camera = file

        # Close any open windows
        cv2.destroyAllWindows()

#for internet check 

def is_connected_to_internet():
    try:
        # Attempt to make a GET request to a known website (e.g., Google)
        response = requests.get("https://www.google.com", timeout=5)
        # If the request was successful (status code 200), return True
        return response.status_code == 200
    except requests.ConnectionError:
        # If there was a connection error, return False
        return False
# for whatsapp check
def list_running_applications():
    running_applications = []

    for process in psutil.process_iter(attrs=['pid', 'name']):
        application_name = process.info['name']
        running_applications.append(application_name)

    return running_applications

class Click:
    @staticmethod
    def clicking():
        import photo as click_photo
        # Call the click_photo function here if it's defined in the "photo" module


while True:
    t.sleep(5)
    if is_connected_to_internet():
        #print("Connected to the internet")
        x=1
    else:
        #print("Not connected to the internet")
        x=0
        url = "http://10.0.0.11:8090/"
        try:
            webbrowser.open(url)
            #print(f"Opening {url} in your default web browser...")
            t.sleep(2)
            
            f = pi.locateOnScreen('search.png')
            #print(f)
            pi.moveTo(f)
            pi.click()
            t.sleep(1)
            pi.write("210303124178")
            # pi.press('up')
            pi.press('enter')
            t.sleep(0.1)
            pi.write("a5@51")
            pi.press('enter')
        except Exception as e:
            #print(f"An error occurred: {str(e)}")
            t.sleep(6)
    applications = list_running_applications()
    
    if applications:
        #print("Running applications:")
        for app in applications:
            if 'WhatsApp.exe' in app:
                x = 1
                #print("WhatsApp is running.")
                engine.say(text)
                engine.runAndWait()
                camera_instance = Camera()
                camera_instance.click_photo()  # Call the clicking method
                t.sleep(3)

                #sending mail (photo)
                current_time = datetime.datetime.now()

                date_time_1 = current_time.strftime("%d-%m_%H.%M")
                

                file_path = f'D:\\Pythonnn\\Found_you\\{date_time_1}.jpg'  # Replace with the path to your file
                with open(file_path, 'rb') as attachment:
                     em.add_attachment(
                         attachment.read(),
                         maintype='application',
                         subtype='octet-stream',
                         filename=os.path.basename(file_path)
                     )

                context = ssl.create_default_context()
                engine.say(text2)
                engine.runAndWait()
                try:
                   with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                      smtp.login(sender, sender_psd)
                      smtp.send_message(em)
                   #print("Email sent successfully!")
                except Exception as e:
                   #print("An error occurred:", e)
                   f=0
                ctypes.windll.user32.LockWorkStation()
                
                  # Exit the loop once WhatsApp is found

    
    t.sleep(10)  # Add a delay between iterations to avoid excessive CPU usage
     





            

