# state-controller-scripts
Helper scripts to test corresponding Android App 

Run this server on a VM to test the android app in the repo found here:
https://github.com/xylo99/state_controller

For example, if you're using VMware Workstation Player:
* create an Ubuntu (18.04+) VM
* clone this repo onto your host machine
* Use bridged networking
* copy server.py onto guest VM
    scp server.py 
    <vm_name>@<vm_ip>:~/
* run the server as python3 server.py
