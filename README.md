Is an advanced Python script designed for detailed analysis of network frame data. It decodes and extracts crucial information directly from a sequence of bytes in a network frame. This script is capable of handling a variety of data elements, providing deep insights into the structure and content of network traffic.

## Features

- **MAC Address Analysis**: Extracts destination and source MAC addresses, offering visibility into the devices involved in the communication.
- **IP Decoding**: Identifies and displays the source and destination IP addresses.
- **Protocol Identification**: Determines the used protocol, such as TCP, UDP, etc.
- **TCP Flags**: Analyzes TCP flags to understand the state and control of the transmission.
- **Additional Information**: Includes analysis of other elements like Ethernet type, IP version, header length, total length, and TTL (Time To Live).

### Prerequisites

Before using PyFrameDecoder, make sure you have the required libraries installed:

| Library              | Description                                   | Installation Command         |
|----------------------|-----------------------------------------------|-----------------------------|
| [tabulate](https://pypi.org/project/tabulate/)   | To format tables in Python.                  | `pip install tabulate`      |
| [requests](https://pypi.org/project/requests/)   | For making HTTP requests in Python.          | `pip install requests`      |

### Running PyFrameDecoder

To analyze network frame data using PyFrameDecoder, follow these steps:

1. Install the required libraries (if not already installed) as mentioned above.

2. Open your terminal.

3. Execute the PyFrameDecoder script with network frame data as an argument. Replace `'network frame data'` with your actual frame data.

```bash
   python3 PyFrameDecoder.py 'network frame data'
```

![PyFrameDecoder](https://img001.prntscr.com/file/img001/JlHhd7X1Q_ay5K8Rzwx4mA.png)
