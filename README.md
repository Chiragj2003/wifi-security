# Wi-Fi Security alert system 
![Logo](https://png.pngtree.com/png-vector/20220615/ourlarge/pngtree-lost-wireless-connection-or-disconnected-cable-png-image_5085743.png)

## Introduction 
The Wi-Fi Security Alert System is a Python script designed to monitor Wi-Fi network activity and provide alerts when an unkonwn Network 
attempts to connect to the Device . It utilizes various modules supported by the python such as ssl, smtplib, requests, subprocess, and GUI 
elements from tkinter to achieve its functionality and work properly . It also send notification email to the owner if anything occurs with the system . 

## Features 

### 1. IP and MAC Address Retrieval:
The script uses the requests library to fetch the external IP address of the network and 
it utilizes the subprocess module to extract MAC addresses associated with connected devices using the arp command which help us to prevent the network system . 

### 2. Email Notification: 
When an unknown network attempts to connect to the users device , the script sends an email alert about the intrusion that occured .
Email details such as sender, receiver, subject, and content are defined within the script and are send to the owner of the device whose emial is save in the database .
The "smtplib" library is employed for sending the email via a Gmail SMTP server.
