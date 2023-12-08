# PyFrameDecoder

Is an advanced Python script designed for detailed analysis of network frame data. It decodes and extracts crucial information directly from a sequence of bytes in a network frame. This script is capable of handling a variety of data elements, providing deep insights into the structure and content of network traffic.

## Features

- **MAC Address Analysis**: Extracts destination and source MAC addresses, offering visibility into the devices involved in the communication.
- **IP Decoding**: Identifies and displays the source and destination IP addresses.
- **Protocol Identification**: Determines the used protocol, such as TCP, UDP, etc.
- **TCP Flags**: Analyzes TCP flags to understand the state and control of the transmission.
- **Additional Information**: Includes analysis of other elements like Ethernet type, IP version, header length, total length, and TTL (Time To Live).

## Usage Example

To use PyFrameDecoder, run the script with network frame data as an argument:

```bash
python3 PyFrameDecoder.py 'network frame data'
```

![PyFrameDecoder](https://img001.prntscr.com/file/img001/JlHhd7X1Q_ay5K8Rzwx4mA.png)
