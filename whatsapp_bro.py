import psutil
import time 

import ctypes

# Call the LockWorkStation function to lock the computer



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
    applications = list_running_applications()
    
    if applications:
        print("Running applications:")
        for app in applications:
            if 'WhatsApp.exe' in app:
                x = 1
                #print("WhatsApp is running.")
                Click.clicking()  # Call the clicking method
                time.sleep(5)
                ctypes.windll.user32.LockWorkStation()
                
                  # Exit the loop once WhatsApp is found

    
    time.sleep(10)  # Add a delay between iterations to avoid excessive CPU usage
















'''import psutil
import time as t

    
def list_running_applications():
    running_applications = []

    for process in psutil.process_iter(attrs=['pid', 'name']):
        application_name = process.info['name']
        running_applications.append(application_name)

    return running_applications

class click:
    def clicking():
        import photo as click_photo


while True:
   applications = list_running_applications()

   if applications:
        print("Running applications:")
        for app in applications:
           #print(app)
           if 'WhatsApp.exe' in app:
               x=1
               print("yes it is ")
               click.clicking()
               t.sleep(5) 
           while True:
               if 'WhatsApp.exe' in app:
                   x=1
                   print("yes it is ")
                   import photo as click_photo
               else:
                   continue
           else:
               x = 0
               continue
            
            

       
   else:
      print("No applications are currently running.")
'''
