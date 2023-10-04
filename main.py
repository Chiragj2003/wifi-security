import ssl
import smtplib
import time
import requests
import subprocess
from tkinter import *
from PIL import ImageTk, Image
from email.message import EmailMessage
from decryption import decrypt_message


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def getOtherInformation() -> str:
    try:
        otherInfo = subprocess.check_output(["netsh", "wlan", "show", "interface"])
        otherInfo = otherInfo.decode()
        return otherInfo
    except Exception as e:
        return "Not Available"


def sendMail(bodyDetails):
    addresses = subprocess.check_output(['arp', '-a'])
    addresses = addresses.decode()
    deviceName = subprocess.check_output(['wmic', 'csproduct', 'get', 'name'])
    deviceName = deviceName.decode()
    sender_email = ""
    passWord = ""
    receiver_email = ""

    subject = "Alert! Someone is trying to connect with your system. "
    otherInfo = getOtherInformation()
    body = "PC " + deviceName + "\n" + bodyDetails + "\nOther Informations about the network\n" + otherInfo + "\nThe details of the network : \n" + addresses

    em = EmailMessage()
    em['From'] = sender_email
    em['To'] = receiver_email
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender_email, passWord)
        smtp.sendmail(sender_email, receiver_email, em.as_string())


def getAddress() -> str:
    addresses = subprocess.check_output(['arp', '-a'])
    addresses = addresses.decode()
    for addresses in addresses.split():
        if addresses.count('-') == 5:
            macAddress = addresses
            break
    return macAddress


def checkValidity(macAddress, approvedAddress) -> int:
    for address in approvedAddress:
        if decrypt_message(address) == macAddress:
            return 1
    return 0


def checkWifi() -> bool:
    response = subprocess.check_output(['arp', '-a'])
    response = response.decode()
    off = response.find('No')
    if off == 0:
        return False
    else:
        return True


def mainFunction():
    approvedAddresses = (b'gAAAAABlHRLlnFvEch7on6G38nV-BLOSQ9B1OAM-p7vIimmht9r0vZfy60ZA2V1iCXvwBzqviNkDemikXYrWt366BQGYAN7gy54dqpMiWRQjmty96llItcI=', b'gAAAAABlHRNimkI_ejuaaeCI28VdYNWA938Nft7SdTzUwWRL_56-YsUJuz4K5K8fcdnsxvAB2bLSG3btfRdyaOxTVsoxoZyr0LR9uIMofpkyQL2kp-2IbHs=')
    macAddress = getAddress()
    temp = checkValidity(macAddress, approvedAddresses)
    ip_address = get_ip()
    response = requests.post("http://ip-api.com/batch", json=
    [{"query": ip_address}]).json()

    location_details = "Country     : " + response[0]["country"] + "\nRegion Name : " + response[0][
        "regionName"] + "\nCity        : " + response[0]["city"] + "\nPincode     : " + response[0][
                           "zip"] + "\n\nNetwork operator  : " + response[0]["isp"] + "\n"
    bodyDetails = location_details
    root = Tk()
    root.title("Warning")
    root.iconbitmap(r'warning.ico')
    if temp == 1:
        root.geometry("350x40")
        img = Image.open("true.png")
        img = img.resize((20, 20))
        my_img = ImageTk.PhotoImage(img)
        myLabel1 = Label(root, image=my_img)
        myLabel2 = Label(root, text="Connected Wifi network is approved")
        myLabel1.grid(row=0, column=0, pady=10, padx=27)
        myLabel2.grid(row=0, column=1, pady=10)
    else:
        root.geometry("400x70")
        img = Image.open("denied.png")
        img = img.resize((30, 30))
        my_img = ImageTk.PhotoImage(img)
        myLabel1 = Label(root, image=my_img)
        myLabel2 = Label(root,
                         text="Connected Wifi network is not approved.\nEmail has been send to the admin successfully")
        myLabel1.grid(row=0, column=0, pady=15, padx=32)
        myLabel2.grid(row=0, column=1, pady=15)
        sendMail(bodyDetails)
    root.mainloop()


exit = 0
move = 0
while exit != 1:
    move = 0
    if (checkWifi() == True):
        print("Main function is called")
        mainFunction()
        while move != 1:
            if (checkWifi() == False):
                move = 1
            else:
                time.sleep(5)
    else:
        time.sleep(10)
