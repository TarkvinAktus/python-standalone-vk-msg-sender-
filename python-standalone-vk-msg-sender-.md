# python-standalone-vk-msg-sender-

This is a python standalone exe application for sending same messages to different chats in VK social network.

In this app i've used python 3.7, pyinstaller 3.4.
Python libraries:
  - vk_api
  - threading
  - asyncio
  - json
  
and others

### Installation

Install vk_api,pyqt5 and pyinstaller.

```sh
$ pip install vk_api
$ pip install pyqt5
$ pip install pyinstaller
```

To build standalone exe file type pyinstaller command and don't forget about --noconsole and --onefile marks

```sh
$ pyinstaller --noconsole --onefile main.py
```

