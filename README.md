# PyFrameDecoder: Network Frame Data Analysis Tool

PyFrameDecoder is a comprehensive tool designed for detailed analysis of network frame data. It provides a range of features that allow users to decode and understand the intricacies of network communications.

## Key Features

- **MAC Address Analysis**: Extract and display both the source and destination MAC addresses, offering insights into the devices participating in the network communication.
- **IP Decoding**: Clearly identify and exhibit source and destination IP addresses.
- **Protocol Identification**: Determine the protocols in use, such as TCP, UDP, and others.
- **TCP Flags Analysis**: Examine TCP flags to gain an understanding of the transmission's state and control mechanisms.
- **Additional Information**: The tool also analyzes other essential elements like Ethernet type, IP version, header length, total length, and TTL (Time To Live).

## Getting Started with PyFrameDecoder

Follow these simple steps to start analyzing network frame data using PyFrameDecoder:

### Prerequisites

Before you begin, ensure that you have the following libraries installed:

| Library | Description | Installation Command |
|---------|-------------|----------------------|
| [tabulate](https://pypi.org/project/tabulate/) | To format tables in Python. | `pip install tabulate` |
| [requests](https://pypi.org/project/requests/) | For making HTTP requests in Python. | `pip install requests` |

### Installation and Execution

1. **Open your terminal.**

2. **Install the required libraries** using the installation commands provided above (if not already installed).

3. **Execute PyFrameDecoder** by entering the following command:

```bash
   python3 PyFrameDecoder.py
```

4. Enter your frame data when prompted. For example:

```bash
00 0c 29 76 43 e1 d4 ab 82 45 c4 0c 08 00 45 00 00 28 b5 f5 40 00 31 06 ff 0b 25 3b ae e1 c0 a8 00 0a 23 82 8f 48 00 00 00 00 04 81 18 d0 50 14 00 00 4a e6 00 00 00 00 00 00 00 00
```

### Here's an example output of PyFrameDecoder:

![PyFrameDecoder](https://img001.prntscr.com/file/img001/JlHhd7X1Q_ay5K8Rzwx4mA.png)
