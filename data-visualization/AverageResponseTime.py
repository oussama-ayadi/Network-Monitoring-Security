import os
from scapy.all import *
import matplotlib.pyplot as plt

def parse_packets(pcap_file):
    pcap_file = os.path.expanduser(pcap_file)
    packets = rdpcap(pcap_file)
    response_times = []
    for packet in packets:
        if packet.haslayer(IP) and packet.haslayer(TCP):
            if TCP in packet and packet[TCP].flags & (0x01 | 0x02):  # SYN or SYN/ACK
                response_times.append(packet.time - packets[0].time)
    return response_times

def calculate_average_response_time(response_times):
    if not response_times:
        return 0
    return sum(response_times) / len(response_times)

def plot_average_response_time(average_response_time):
    plt.bar(['Average Response Time'], [average_response_time])
    plt.ylabel('Response Time (ms)')
    plt.title('Average Response Time')
    plt.show()

pcap_file = '~/GNS3/test1.pcapng'  
response_times = parse_packets(pcap_file)
average_response_time = calculate_average_response_time(response_times)
print(f'Average Response Time: {average_response_time} ms')
plot_average_response_time(average_response_time)
