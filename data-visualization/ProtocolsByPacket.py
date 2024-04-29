import os
from scapy.all import *
import matplotlib.pyplot as plt

def detect_protocol(packet):
    if 'ssh' in packet:
        return 'SSH'
    elif 'ftp' in packet:
        return 'FTP'
    elif 'dns' in packet:
        return 'DNS'
    elif 'http' in packet:
        return 'HTTP'
    elif 'https' in packet:
        return 'HTTPS'
    elif 'sftp' in packet:
        return 'SFTP'
    elif 'tftp' in packet:
        return 'TFTP'
    elif 'smtp' in packet:
        return 'SMTP'
    elif 'imap' in packet:
        return 'IMAP'
    elif 'telnet' in packet:
        return 'Telnet'
    elif 'snmp' in packet:
        return 'SNMP'
    return None
def parse_packets(pcap_file):
    pcap_file = os.path.expanduser(pcap_file)
    packets = rdpcap(pcap_file)
    protocol_counts = {}
    for packet in packets:
        protocol = packet.payload.name  # Extract protocol name from the packet's payload
        protocol_counts[protocol] = protocol_counts.get(protocol, 0) + 1
    return protocol_counts
'''def parse_packets(pcap_file):
    pcap_file = os.path.expanduser(pcap_file)
    packets = rdpcap(pcap_file)
    protocol_counts = {}
    for packet in packets:
        protocol = packet.transport_layer
        detected_protocol = detect_protocol(packet)
        if detected_protocol:
            protocol = detected_protocol
        elif len(packet.layers) >= 3:
            protocol = packet.layers[2].layer_name
        protocol_counts[protocol] = protocol_counts.get(protocol, 0) + 1
    return protocol_counts
'''
def plot_protocol_counts(protocol_counts):
    protocols = list(protocol_counts.keys())
    counts = list(protocol_counts.values())
    plt.bar(protocols, counts)
    plt.xlabel('Protocol')
    plt.ylabel('Number of Packets')
    plt.title('Packet Count by Protocol')
    plt.show()
    
pcap_file = '~/GNS3/test1.pcapng'
protocols = parse_packets(pcap_file)
plot_protocol_counts(protocols)
