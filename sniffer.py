import pyshark
import pkt
capture = pyshark.LiveCapture(interface='en0')

for packet in capture.sniff_continuously(packet_count=1):
    #packetTensor = [packet.frame_info.time_epoch, packet.frame_info.len, , , , packet.ip.dst]
    pkt = pkt.PacketFeatures()
    pkt.frame_time_epoch = packet.frame_info.time_epoch
    pkt.frame_len = packet.frame_info.len

    d = dir(packet)

    if 'eth' in d:
        pkt.eth_dst = packet.eth.dst
        pkt.eth_src = packet.eth.src
    if 'ip' in d:
        pkt.ip_src = packet.ip.src
        pkt.ip_dst = packet.ip.dst
    if 'tcp' in d:
        pkt.tcp_srcport = packet.tcp.srcport
        pkt.tcp_dstport = packet.tcp.dstport
    if 'udp' in d:
        pkt.udp_srcport = packet.udp.srcport
        pkt.udp_dstport = packet.udp.dstport
    if 'icmp' in d:
        pkt.icmp_code = packet.icmp.code
        pkt.icmp_type = packet.icmp.type
    if 'arp' in d:
        pkt.arp_dst_hw_mac
        pkt.arp_src_hw_mac
        pkt.arp_opcode
        pkt.arp_dst_proto_ipv4
        pkt.arp_src_proto_ipv4
        
    print(pkt.to_list())
    
    # , 
    # packet.udp.srcport, packet.udp.dstport, 
    # ]# 
    # packet.arp.opcode, packet.arp.src.hw_mac, packet.arp.src.proto_ipv4, packet.arp.dst.hw_mac, packet.arp.dst.proto_ipv4, 
    # packet.ipv6.src, packet.ipv6.dst]