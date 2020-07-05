# Mail Sender

This repo is showing how to send email via gmail in python.
Messege and Title are encodend intro utf-8.
Don't forget to Turn Allow less secure apps to ON in your gmail account. Be aware that this makes it easier for others to gain access to your account. 

## Installation

After you clone repo, don't forget to download additional python modules 
```bash
pip install zipfile36
pip install argparse
```

## Usage

To use it you simply do this:
```bash
python sender.py -f folder -r recipient@mail.com -s mymail@gmail.com -t title -m message
```
Plese be alone when you use this program, becouse it will ask you a password and everything you type will by show on screen
```bash
Type your password and press enter: Password
```

## Author

This code was made with help of stackoverflow by **InKronos**


