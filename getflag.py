from scapy.all import *
import sys
import binascii

cap = rdpcap("./Assignment9.pcap")
dump = open("./hex3",mode='a+')
for p in cap:
    if ICMP in p:
        if p[IP].src == '192.168.64.137' and p[IP].dst == '138.197.108.176':
            bin = binascii.hexlify(bytes(p[ICMP][Raw]))
            dump.write(str(bin))

dump.close()
print("ok")
