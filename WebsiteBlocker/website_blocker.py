import time
from datetime import datetime as dt

"""
For Windows:
    Run cmd as admin then, cd in to the project and enter the command:
        python website_blocker
    to run the program.

For Mac/Linux:
    host_path must be set to: "/etc/hosts"
    Then enter the command:
        sudo python3 website_blocker.py
        
hosts_temp was created for proof of concept.
"""

hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_lists = ["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 12) < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        # Blocked from Noon to 5PM
        print("blocked hours")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in website_lists:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
            print(content)
    else:
        print("unblocked hours")
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_lists):
                    file.write(line)
            file.truncate()
    time.sleep(5)
