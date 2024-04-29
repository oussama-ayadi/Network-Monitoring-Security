#     Network-Monitoring-Security
# 📝 Description
This repository contains a comprehensive solution for network monitoring security, including networking simulations, data ingestion to the cloud, data visualization, machine learning for anomaly detection, automation of reporting, and a user interface.

# 🖥️ Installation
# 📋 Requirements
▪️ Python 3.5+ 
▪️ Tensor, sklearn, numpy, pandas, seaborn, matplotlib, scapy, pyshark, csv
▪️ GNS3  
▪️ Wireshark  
▪️ MinIO  
▪️ Laravel  
▪️ VirtualBox (optional: for running GNS3 VM)
# ⚙️ Setup
    Networking Simulation:
        Install GNS3 following their official documentation: https://gns3.com/software/download
        Design and configure your enterprise architecture using GNS3, including protocols and devices.

    Packet Sniffing with Wireshark:
        Install Wireshark from their official website: https://www.wireshark.org/download.html
        Capture training and testing packets for network monitoring.

    Data Ingestion to the Cloud :
        Set up Minio for S3-compatible storage: https://min.io/download
        Configure Minio to store captured packets for later analysis.

    ML for Anomaly Detection :
        Install Python packages for machine learning using pip install.
        Train an Artificial Neural Network (RNN) model on labeled data for anomaly detection.
        Use the ML model to analyze packets stored in Minio for testing.

    Automation of Reporting:
        Implement scripts or tools for automating report generation based on network activity and anomalies detected.

    User Interface :
        Install Laravel following their official guide: https://laravel.com/docs/11.x
        Connect Laravel backend to Minio for data retrieval.
        Integrate the ML algorithm into the Laravel backend for real-time anomaly detection.
        Develop a frontend UI for user interaction and visualization.
