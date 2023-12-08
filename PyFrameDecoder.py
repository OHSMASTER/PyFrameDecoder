from tabulate import tabulate
import requests


def extract_data_from_frame(frame):
    dest_mac = frame[:12]
    src_mac = frame[12:24]
    eth_type = frame[24:28]

    ip_version = int(frame[28:29], 16)
    header_length = int(frame[29:30], 16) * 4
    total_length = int(frame[32:36], 16)
    ttl = int(frame[40:42], 16)
    protocol = frame[42:44]
    src_ip = [int(frame[i:i+2], 16) for i in range(52, 60, 2)]
    dest_ip = [int(frame[i:i+2], 16) for i in range(60, 68, 2)]

    src_port = int(frame[68:72], 16)
    dest_port = int(frame[72:76], 16)
    tcp_flags = int(frame[94:96], 16)
    os = identify_os_by_ttl(ttl)

    flags = {
        'URG': (tcp_flags & 32) != 0,
        'ACK': (tcp_flags & 16) != 0,
        'PSH': (tcp_flags & 8) != 0,
        'RST': (tcp_flags & 4) != 0,
        'SYN': (tcp_flags & 2) != 0,
        'FIN': (tcp_flags & 1) != 0,
    }
    active_flags = ', '.join([key for key, value in flags.items() if value])
    data_start = header_length
    ascii_data = ''.join([chr(int(frame[i:i+2], 16)) for i in range(data_start, len(frame), 2)])

    return {
        "Dest MAC": dest_mac,
        "Dest Mac manufacturer": get_manufacturer_from_mac(dest_mac),
        "Source MAC": src_mac,
        "Source Mac manufacturer": get_manufacturer_from_mac(src_mac),
        "Ether Type": eth_type,
        "IP Version": ip_version,
        "Header Length": header_length,
        "Total Length": total_length,
        "TTL": ttl,
        "Protocol": protocol,
        "Source IP": '.'.join(map(str, src_ip)),
        "Dest IP": '.'.join(map(str, dest_ip)),
        "Source Port": src_port,
        "Dest Port": dest_port,
        "Active TCP Flags": active_flags,
        "Operating System": os,
        "ASCII Data": ascii_data,
    }
    
def get_manufacturer_from_mac(mac_address):
    url = f"https://macvendors.com/query/{mac_address}"
    headers = {
        "User-Agent": "PyFrameDecoder"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text 
        else:
            return "Manufacturer not found"
    except Exception as e:
        return str(e)  
    

def identify_os_by_ttl(ttl):
    os_mapping = {
        64: "Linux/Unix",
        128: "Windows",
        255: "Cisco",
    }

    return os_mapping.get(ttl, "Unknown operating system")

def get_frame_from_user():
    frame_input = input("Enter the bytes (with or without spaces): ")
    formatted_frame = frame_input.replace(" ", "") 
    return formatted_frame

def main():
    frame = get_frame_from_user()
    data = extract_data_from_frame(frame)
    
    table = []
    for key, value in data.items():
        if key != "ASCII Data":
            table.append([key, value])
    
    print(tabulate(table, headers=["tab", "value"], tablefmt="grid"))
    print("\nASCII Data:")
    print(data["ASCII Data"])

if __name__ == "__main__":
    main()
