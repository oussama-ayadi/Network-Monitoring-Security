import os
import csv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

# Global variables for response times and packet index
response_times = []
packet_index = []

# Function to parse packets and extract response times
def parse_csv_packets(csv_file):
    global response_times, packet_index
    response_times.clear()  # Clear previous data
    packet_index.clear()  # Clear previous data

    csv_file = os.path.expanduser(csv_file)
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        packets = list(reader)

        if packets:
            start_time_str = packets[0]['timestamp']
            start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S.%f')
            start_time_seconds = start_time.timestamp()  # Convert datetime to timestamp in seconds

            for index, packet in enumerate(packets, start=1):
                timestamp_str = packet['timestamp']
                timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f')
                timestamp_seconds = timestamp.timestamp()  # Convert datetime to timestamp in seconds
                response_times.append(timestamp_seconds - start_time_seconds)
                packet_index.append(index)  # Update packet index for each packet

    return response_times, packet_index

# Function to update the plot in real-time
def update_plot(frame):
    global response_times, packet_index
    new_response_data, new_packet_index = parse_csv_packets(csv_file_path)
    if new_response_data:  # Check if new_response_data is not empty
        response_times = new_response_data
        packet_index = new_packet_index
        print("Packet Times:", packet_index)  # Fixed indentation
        print("Response Times:", response_times)  # Fixed indentation
        plt.cla()
        plt.plot(packet_index, response_times, marker='o')
        plt.xlabel('Packet Index')
        plt.ylabel('Response Time (ms)')
        plt.title('Real-Time Response Time of Packets')
        plt.grid(True)
        plt.tight_layout() 

# Example usage
#csv_file_path = '/home/PFAII/RealTest1.csv'  # Update with your CSV file path
csv_file_path = '/home/PFAII/test.csv'
ani = FuncAnimation(plt.gcf(), update_plot, interval=1000)
plt.show()


# Example usage
csv_file_path = '/home/PFAII/RealTest.csv'  # Update with your CSV file path
ani = FuncAnimation(plt.gcf(), update_plot, interval=1000)
plt.show()
