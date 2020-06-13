# pyAWM




pyAWM is a module which automates to send whatsapp messages, media, files at a given time.

  - Send Messages to multiple contacts multiple times.
  - Send Multiple files to multiple contacts.
  - Schedule to send messages ot media.






### Installation

pyAWM requires Chrome to run(You might have this already).

Here are commands to install chrome in Ubuntu:

```sh
$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
$ sudo apt install ./google-chrome-stable_current_amd64.deb
```
Install Chrome Driver:

```sh
$ sudo apt install chromium-chromedriver
```
>Steps to use pyAWM module: <br />
>Step 1: Download Google Chrome and see if it is working fine. If that works fine, go to step 2.<br />
Step 2: Download Chrome Driver(latest and stable version) from https://chromedriver.chromium.org/ <br />
Step 3: Extract the the downloaded file and copy the path of chromedriver <br /> Example: .../chromedriver.exe  <br />
Step 4: Call add_path_to_driver(path) where path is text that you copied. <br />
Step 5: Call scan_QR_Code and open scanner in Whatsapp in your mobile and scan QR Code. <br />
Step 6: Now you can use the functions to automate messages. <br />









### Todos

 - Add Change profile name, picture, about.
 - Add to download contact's profile picture

License
----

MIT


**Free Software, Hell Yeah!**


