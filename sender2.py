import smtplib
import zipfile
import tempfile
import ssl
from email import encoders
from email.message import Message
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart    
from email.mime.text import MIMEText
import os
import argparse

def get_all_file_paths(directory): 
  
    # initializing empty file paths list 
    file_paths = [] 
  
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(directory): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath) 
  
    # returning all file paths 
    return file_paths       

def send_folder_zipped(zipfile_name, recipient, sender='i15.piorkowski@gmail.com'):
  
    zf = tempfile.TemporaryFile(prefix='mail', suffix='.zip')
    file_paths = get_all_file_paths(zipfile_name)
    zip =  zipfile.ZipFile(zf,'w') 
    for file in file_paths: 
        zip.write(file)  
    zip.close()
    zf.seek(0)
    # Create the message
    themsg = MIMEMultipart()
    themsg['Subject'] = 'Hight Flyers Raport'
    themsg['To'] = recipient
    themsg['From'] = sender
    text = 'W załączniku znajduje się raport'
    part2 = MIMEText(text, "plain", "utf-8")
    themsg.attach(part2)
    msg = MIMEBase('application', 'zip')
    msg.set_payload(zf.read())
    encoders.encode_base64(msg)
    msg.add_header('Content-Disposition', 'attachment', 
                   filename=zipfile_name + '.zip')
    themsg.attach(msg)
    themsg = themsg.as_string()

    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context()
    password = input("Type your password and press enter:")
    # send the message
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender, password)
        server.sendmail(sender, recipient, themsg)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', dest='folder_name',
                        help='Store folder value', default='katalog')
    parser.add_argument('-r', action='store', dest='recipient',
                        help='Store recipient value', default='fnaticisthebest@gmail.com')
    parser.add_argument('-s', action='store', dest='sender',
                        help='Store sender value', default='highflyers.polsl@gmail.com')

    results = parser.parse_args()

    send_folder_zipped(results.folder_name, results.recipient, results.sender)
    
