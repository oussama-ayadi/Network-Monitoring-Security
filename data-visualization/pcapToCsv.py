import pyshark
import csv
import pandas as pd

def annotate_label(row):
    normal_protocols = ['icmp', 'snmp', 'imap']
    normal_sources = ['8.8.8.8']
    if row['protocol'] in normal_protocols or row['source'].endswith(tuple(normal_sources)):
        return '0'
    elif row['protocol'] not in normal_protocols or row['length'] > 74:
        return '2'
    else:
        return '1'
        
def pcapng_to_csv(interface, output_file):
    cap = pyshark.LiveCapture(interface)
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['timestamp', 'source', 'destination', 'protocol', 'length' , 'label']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for index, packet in enumerate(cap):
            try:
                timestamp = packet.sniff_time
                source = packet.ip.src
                destination = packet.ip.dst
                protocol = packet.transport_layer
                length = packet.length
                detected_protocol = detect_protocol(packet)
                if detected_protocol:
                    protocol = detected_protocol
                elif len(packet.layers) >= 3:
                    protocol = packet.layers[2].layer_name
                label = annotate_label({'protocol': protocol, 'source': source, 'length': length})
                writer.writerow({'timestamp': timestamp, 'source': source, 'destination': destination, 'protocol': protocol, 'length': length, 'label': label})
            except AttributeError:
                pass  

    print("CSV file '{}' has been created.".format(output_file))


def detect_protocol(packet):
    # Check for known protocols and return the detected protocol
    if 'ssh' in packet:
        return 'SSH'
    elif 'ftp' in packet:
        return 'FTP'
    elif 'dsn' in packet:
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

pcapng_to_csv("wlo1", "~/RealTime.csv")
