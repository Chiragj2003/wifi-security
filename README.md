# Wi-Fi Security alert system 
![Logo](https://png.pngtree.com/png-vector/20220615/ourlarge/pngtree-lost-wireless-connection-or-disconnected-cable-png-image_5085743.png )

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

### 3.Device Approval Mechanism:
Approved IP addresses are encrypted and stored within the code .The code decrypts the MAC address of the connected device and checks its validity against the approved list of the wi-fi that can get safely connect to the device .

### 4.Wi-Fi Connection Monitoring:
The script continuously monitors the Wi-Fi connection status using the arp command.
It triggers the main functionality when a connection is detected and waits for disconnection before repeating and this functionality repeat over and over again thus preventing the system from any faulty devices 

### 5.User Interface:
The Tkinter library is utilized to create a simple GUI for displaying connection status of the network on the device . It includes visual indicators and informative messages based on the approval status of the connected Wi-Fi network .

## Python Modules used :
#### ssl, smtplib: 
For secure email communication.
#### requests: 
To fetch external IP address and location details.
#### subprocess: 
For executing system commands and retrieving network-related information.
#### tkinter: 
For creating a basic graphical user interface.
#### PIL: 
For working with images in the GUI.

## Advantages :
### 1. Unauthorized Access Detection:
The system effectively identifies and alerts the user about any unauthorized network trying to connect to the device network.
### 2. Email Notification:
Immediate email notifications provide users with timely alerts, allowing them to take swift action against potential security threats.
### 3. User-Friendly Interface:
The graphical user interface (GUI) provides a simple and visual representation of the connection status, making it easy for users to understand the security status at a glance.
### 4. Continuous Monitoring:
The system continuously monitors the Wi-Fi network, ensuring ongoing protection against unauthorized access attempts.
### 5. Customizable Configuration:
Users can easily configure the script by updating email addresses, passwords, and approved MAC addresses, making it adaptable to different network environments. 

## Conclusion:
The Wifi Security Alert System offers a robust solution for monitoring and securing devices from unknown Wi-Fi networks. By combining network information such as MAC address , IP address of the device and the network , and send email notification, it provides a comprehensive security mechanism. The advantages include quick detection of unauthorized access, immediate alerting, and user-friendly interaction. While the system serves as a valuable tool for enhancing device security . 

