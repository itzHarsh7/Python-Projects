from plyer import notification
import time

if __name__ == "__main__":

    while True:
        notification.notify(
        title="*** Take Rest ***",
        message = "Yor should Take some Rest because you are using your PC for atleast an Hour. Take some Rest to prevent Eye damage and Have some Fresh Mindse.",
        app_icon = "E:\Languages\Python\WsCubeTech\clock.ico",
        timeout = 5
        )
        time.sleep(60*60)  # it will take a time delay of 1 hour

'''
To make it run in background, just write in Terminal or in CMD or in Powershell:---->>>>

python filename.py

and press enter. it will execute and will not stop notifying you

to stop getting notifications, just open task manager and search python and end that task

'''