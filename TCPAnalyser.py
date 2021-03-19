import os
import sys
import re
import subprocess
from pyfiglet import Figlet
import re
import socket

# print('int\t\t\tstatus\t\t\tU/d\t\t\tisRunning\t\t\t')

i = 0
line = '='
while i < 50:
    line = line + '='
    i += 1

cText = Figlet(font='slant')
os.system('clear')
print(cText.renderText('TCP Analyser'))
print(line)

hostname = socket.gethostname()
localIP = socket.gethostbyname(hostname)

print('Current Local IP: ' + str(localIP))

# ============================================================ #
# ============================================================ #
def IPvalidation(ip): 
    ipPattern = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    # pass the regular expression
    # and the string in search() method
    if(re.search(ipPattern, ip)): 
        return True 
    else: 
        return False

def AssignFeature(fetu, intf):
    if fetu == 8:
        FromDestinationIP(intf)
    elif fetu == 7:
        FromSourceIP(intf)
    elif fetu == 6:
        SpecificPort(intf)
    elif fetu == 5:
        TCPonly(intf)
    elif fetu == 4:
        SavePackets(intf)
    elif fetu == 3:
        HEXandASCII(intf)
    elif fetu == 2:
        ASCII(intf)
    elif fetu == 1:
        CapturePackets(intf)
    else:
        Features(intf)

def CapturePackets(intf):
    while True:
        qty = input('Capture how many packet? (e.g. 8) ')
        try:
            qty = int(qty)
        except:
            print('Please use numeric digits.')
            continue
        if qty < 1:
            print('Please enter a positive number.')
            continue
        break

    print('Interface: ' + str(intf) + '\nFunction: Regular Capture\nCaptures Frequency: ' + str(qty) + '\n\n')
    cm = os.popen('tcpdump -v -c ' + str(qty) + ' -i ' + str(intf))
    output = cm.read()
    
    OutputAnalyse(output)

def ASCII(intf):
    while True:
        qty = input('Capture how many packet? (e.g. 8) ')
        try:
            qty = int(qty)
        except:
            print('Please use numeric digits.')
            continue
        if qty < 1:
            print('Please enter a positive number.')
            continue
        break

    print('Interface: ' + str(intf) + '\nFunction: Captured in ASCII\nCaptures Frequency: ' + str(qty) + '\n\n')
    cm = os.popen('tcpdump -v -A -c ' + str(qty) + ' -i ' + str(intf))
    output = cm.read()
    
    OutputAnalyse(output)

def HEXandASCII(intf):
    while True:
        qty = input('Capture how many packet? (e.g. 8) ')
        try:
            qty = int(qty)
        except:
            print('Please use numeric digits.')
            continue
        if qty < 1:
            print('Please enter a positive number.')
            continue
        break

    print('Interface: ' + str(intf) + '\nFunction: Captured in HEX and ASCII\nCaptures Frequency: ' + str(qty) + '\n\n')
    cm = os.popen('tcpdump -v -XX -c ' + str(qty) + ' -i ' + str(intf))
    output = cm.read()
    
    OutputAnalyse(output)

def SavePackets(intf):
    while True:
        qty = input('Capture how many packet? (e.g. 8) ')
        try:
            qty = int(qty)
        except:
            print('Please use numeric digits.')
            continue
        if qty < 1:
            print('Please enter a positive number.')
            continue
        break

    name = input('How would you name the save file? ')

    print('Interface: ' + str(intf) + '\nFunction: Capture and Save Packets\nCaptures Frequency: ' + str(qty) + '\nFile Name: ' + name + '.pcap\n\n')
    cm = os.popen('tcpdump -v -XX -w ' + str(name) + '.pcap' + ' -i ' + str(intf) + ' -c ' + str(qty))
    output = cm.read()
    
    OutputAnalyse(output)

def TCPonly(intf):
    while True:
        qty = input('Capture how many packet? (e.g. 8) ')
        try:
            qty = int(qty)
        except:
            print('Please use numeric digits.')
            continue
        if qty < 1:
            print('Please enter a positive number.')
            continue
        break

    print('Interface: ' + str(intf) + '\nFunction: Capture TCP Packets only\nCaptures Frequency: ' + str(qty) + '\n\n')
    cm = os.popen('tcpdump -v -c ' + str(qty) + ' -i ' + str(intf) + ' tcp')
    output = cm.read()
    
    OutputAnalyse(output)

def SpecificPort(intf):
    while True:
        port = input('Which port you wanna capture packets? (1-65536) ')
        try:
            port = int(port)
        except:
            print('Please use numeric digits.')
            continue
        if port < 1 or port > 65537:
            print('Please enter a positive number.')
            continue
        break

    while True:
        qty = input('Capture how many packet? (e.g. 8) ')
        try:
            qty = int(qty)
        except:
            print('Please use numeric digits.')
            continue
        if qty < 1:
            print('Please enter a positive number.')
            continue
        break

    print('Interface: ' + str(intf) + '\nFunction: Capture with Specific Port\nCaptures Frequency: ' + str(qty) + '\n\n')
    cm = os.popen('tcpdump -v -c ' + str(qty) + ' -i ' + str(intf) + ' port ' + port)
    output = cm.read()
    
    OutputAnalyse(output)

def FromSourceIP(intf):
    ip = input('Which source IP you wanna capture? ')
    if IPvalidation(ip) == False:
        print('Invalid IP address, try again.')
        FromSourceIP(intf)
    else:
        print('Interface: ' + str(intf) + '\nFunction: Capturing from Source IP\nCaptures Frequency: ' + str(qty) + '\n\n')
        cm = os.popen('tcpdump -v -c ' + str(qty) + ' -i ' + str(intf) + ' src ' + str(ip))
        output = cm.read()
        
        OutputAnalyse(output)

def FromDestinationIP(intf):
    ip = input('Which destination IP you wanna capture? ')
    FromDestinationIP(intf)
    if IPvalidation(ip) == False:
        print('Invalid IP address, try again.')
    else:
        print('Interface: ' + str(intf) + '\nFunction: Capturing from Destination IP\nCaptures Frequency: ' + str(qty) + '\n\n')
        cm = os.popen('tcpdump -v -c ' + str(qty) + ' -i ' + str(intf) + ' dst ' + str(ip))
        output = cm.read()
        
        OutputAnalyse(output)

def OutputAnalyse(output):
    packetsCaptured = re.findall(r'(\d+\spackets\scaptured)', output)
    foundPacketsCaptured = str(packetsCaptured)[2:-2]

    filtered = re.findall(r'(\d+\spackets\sreceived\sby\sfilter)', output)
    foundFiltered = str(filtered)[2:-2]

    dropped = re.findall(r'(\d+\spackets\sdropped\sby\skernel)', output)
    foundDropped = str(dropped)[2:-1]

    print(line)
    print('\n' + foundPacketsCaptured + '\n' + foundFiltered + '\n' + foundDropped)

    sourceIP = re.compile(r'(?P<sourceIP>IP(.*)[\s]\>)')
    print('\nSource IP:')
    for srcIP in re.findall(sourceIP, output):
        filteredSrcIP = re.sub(" ", "", str(srcIP[1]))
        print('> ' + str(filteredSrcIP) + ':')

    destinationIP = re.compile(r'(?P<destination>\>(\s)(.*):(\s))')
    print('\nDestination IP:')
    for dstIP in re.findall(destinationIP, output):
        print(str(dstIP[0]))
# ============================================================ #
# ============================================================ #

def Features(intf):
    print('\n' + line + '\n')

    features = [
        'Capture Packets', 'Captured in ASCII', 'Captured in HEX and ASCII', 
        'Capture and Save Packets', 'Capture only TCP Packets.', 'Capture Packet from Specific Port', 
        'Capture Packets from source IP', 'Capture Packets from destination IP'
    ]

    i=0
    for x in range(len(features)): 
        i += 1
        print(str(i) + '. ' + features[x])

    while True:
        fetu = input('\nWhich feature do you wanna choose? (e.g. 1) ')
        try:
            fetu = int(fetu)
        except:
            print('Please use numeric digits.')
            continue
        if fetu < 1:
            print('Please enter a positive number.')
            continue
        break

    print(line)
    AssignFeature(fetu, intf)

print(line + '\n')

print('All Available Interfaces on This Deivce:\n')
avaInt = os.popen('tcpdump -D')
avaIntList = avaInt.read()
print(avaIntList)

print(line + '\n')

while True:
    intf = input('Which interface you wanna spy? (e.g. 3) ')
    try:
        qty = int(intf)
    except:
        print('Please use numeric digits.')
        continue
    if qty < 1:
        print('Please enter a positive number.')
        continue
    break

Features(intf)

