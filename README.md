# TCP_Hijacking_Attack_using_Python

Overview

This Python script utilizes the Scapy library to perform a TCP packet spoofing attack. The attack is aimed at creating a file on a target machine by injecting malicious commands into an existing TCP session. The script listens for TCP packets from a specific source to a specific destination and then manipulates these packets to execute arbitrary commands on the target machine.

Requirements

Python 3.x
Scapy library: Can be installed using pip install scapy
Configuration

Before running the script, you need to replace the placeholder IP addresses with the actual IP addresses of the machines involved:

M01_IP: IP address of Machine 1 (not used in the current script)
M02_IP: IP address of Machine 2 (the source machine)
M03_IP: IP address of Machine 3 (the target machine)
How it Works

The script defines a spoof function that takes a packet (pkt) as an argument.
It extracts the IP and TCP layers from the incoming packet and calculates new sequence and acknowledgment numbers.
A new IP packet is created with the source IP set to Machine 2 and the destination IP set to Machine 3.
A new TCP packet is created with the appropriate source port, destination port (23, which is typically used for Telnet), and flags. The sequence and acknowledgment numbers are set to the new values calculated earlier.
Malicious data (a command to create a file /tmp/xyz) is appended to the packet.
The packet is printed to the console for debugging purposes using ls(pkt).
The malicious packet is sent to the target machine using send(pkt, verbose=0).
The script then exits.
Running the Script

Ensure that Python 3.x and Scapy are installed on your system.
Replace the placeholder IP addresses in the script with the actual IP addresses of the machines involved.
Run the script using Python 3: python3 script_name.py
Security Implications

This script demonstrates a type of "Man-in-the-Middle" attack, where an attacker injects malicious packets into an existing TCP session. This type of attack can lead to unauthorized command execution, data breaches, and a variety of other security issues. It is crucial to ensure that networks are secure and that traffic is encrypted to prevent such attacks.

Disclaimer

This script is provided for educational purposes only. Performing network attacks without explicit permission is illegal and unethical. It is important to respect privacy and integrity of systems and networks. The author is not responsible for any misuse of this information.
