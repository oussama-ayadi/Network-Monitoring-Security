import os
from scapy.all import *
import matplotlib.pyplot as plt

def parse_packets(pcap_file):
    pcap_file = os.path.expanduser(pcap_file)
    packets = rdpcap(pcap_file)
    response_times = []
    for packet in packets:
        if packet.haslayer(IP) and packet.haslayer(TCP) and packet.haslayer(Raw):
            response_time_ms = packet.time - packets[0].time  
            response_times.append(response_time_ms)
    return response_times  # Corrected indentation here

def calculate_performance_details(response_times):
    if not response_times:
        return 0, 0, 0
    num_packets = len(response_times)
    min_response_time = min(response_times)
    max_response_time = max(response_times)
    average_response_time = sum(response_times) / num_packets
    return min_response_time, max_response_time, average_response_time

def plot_performance_details(min_response_time, max_response_time, average_response_time):
    plt.bar(['Min Response Time', 'Max Response Time', 'Average Response Time'], [min_response_time, max_response_time, average_response_time])
    plt.ylabel('Response Time (ms)')
    plt.title('Performance Details')
    plt.show()

pcap_file = '~/GNS3/test1.pcapng' 
response_times = parse_packets(pcap_file)
min_response_time, max_response_time, average_response_time = calculate_performance_details(response_times)
print(f'Min Response Time: {min_response_time:.2f} ms')
print(f'Max Response Time: {max_response_time:.2f} ms')
print(f'Average Response Time: {average_response_time:.2f} ms')
plot_performance_details(min_response_time, max_response_time, average_response_time)
