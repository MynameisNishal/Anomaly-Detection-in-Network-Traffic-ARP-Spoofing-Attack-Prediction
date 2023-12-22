# Anomaly-Detection-in-Network-Traffic-ARP-Spoofing-Attack-Prediction

## Introduction

Detecting ARP spoofing is essential for maintaining robust network security in various aspects. By identifying and stopping ARP spoofing efforts, it's possible to avert man-in-the-middle attacks, thereby preserving the privacy of communications and safeguarding against unauthorized access to critical data. This detection is crucial in upholding the integrity of network resources, as ARP spoofing can be used to alter data or introduce harmful content. Moreover, it aids in ensuring the network's overall availability by avoiding issues like network congestion or unauthorized rerouting of traffic.

As network environments become increasingly complex, especially with the integration of IoT devices, having effective detection mechanisms is a key aspect of thorough network security measures.

## Contributors
* Anirudh Iyer (avi2011)
* Asish Boggavarapu (ab10535)
* Chinmay Nivsarkar (cmn8525)
* Nishal Sundarraman (ns5429)

## Dataset and Feature Analysis
### Dataset Description
1. Bandwidth of outbound traffic (packet size) - srcMAC-IP (mean)
2. Bandwidth of outbound traffic (packet size) - srcMAC-IP (standard deviation)
3. Bandwidth of outbound traffic (packet size) - srcIP (mean)
4. Bandwidth of outbound traffic (packet size) - srcIP (standard deviation)
5. Bandwidth of outbound traffic (packet size) - channel (mean)
6. Bandwidth of outbound traffic (packet size) - channel (standard deviation)
7. Bandwidth of outbound traffic (packet size) - socket (mean)
8. Bandwidth of outbound traffic (packet size) - socket (standard deviation)
9. Bandwidth of outbound and inbound traffic together (packet size) - channel (magnitude)
10. Bandwidth of outbound and inbound traffic together (packet size) - channel (radius)
11. Bandwidth of outbound and inbound traffic together (packet size) - channel (covariance)
12. Bandwidth of outbound and inbound traffic together (packet size) - channel (correlation coefficient)
13. Bandwidth of outbound and inbound traffic together (packet size) - socket (magnitude)
14. Bandwidth of outbound and inbound traffic together (packet size) - socket (radius)
15. Bandwidth of outbound and inbound traffic together (packet size) - socket (covariance)
16. Bandwidth of outbound and inbound traffic together (packet size) - socket (correlation coefficient)
17. Packet rate of outbound traffic (packet count) - srcMAC-IP (weight)
18. Packet rate of outbound traffic (packet count) - srcIP (weight)
19. Packet rate of outbound traffic (packet count) - channel (weight)
20. Packet rate of outbound traffic (packet count) - socket (weight)
21. Inter-packet delays of outbound traffic (packet jitter) - channel (mean)
22. Inter-packet delays of outbound traffic (packet jitter) - channel (standard deviation)
23. Inter-packet delays of outbound traffic (packet jitter) - channel (weight)


This dataset comprises a comprehensive collection of network traffic features, designed to analyze the dynamics of data communication over a network. It encompasses a variety of metrics that measure both the size and rate of traffic packets, as well as the temporal characteristics between them. The features are gathered from multiple aspects of network traffic such as source MAC-IP address pairs, source IP addresses, communication channels, and sockets. Each aspect provides a unique viewpoint on the traffic flow, offering insights into the behavior of the network at different granular levels.

The dataset is structured into five distinct sets based on the time intervals at which the data was collected: 100 milliseconds, 500 milliseconds, 1.5 seconds, 10 seconds, and 1 minute. This temporal segmentation is crucial for understanding the short-term and long-term patterns in network traffic, as well as for capturing transient and sustained network events.

The first four groups of features (1-8) focus on the outbound traffic from a particular source, measuring the average packet size (mean) and variability (standard deviation). These features are segregated by the source MAC-IP address pairs, source IP addresses, channels, and sockets, providing a multidimensional perspective on how data packets are distributed across different network paths and endpoints.

Features 9 to 16 extend this analysis to include both outbound and inbound traffic, reflecting the total load and interaction on a given communication channel or socket. These metrics include the magnitude and radius, which could represent the volume and spread of the data packets, respectively, and the covariance and correlation coefficient, which indicate the degree of variability and the strength of the relationship between outbound and inbound packet sizes.

The packet rate features (17-20) offer insights into the frequency of packet transmission over the network, highlighting potential bottlenecks or underutilized segments. These are calculated as the weight of the packet count, which may imply the importance or priority given to packets from different sources and through different mediums.

Lastly, the inter-packet delay features (21-23) focus on the timing aspect, which is critical for identifying network performance issues such as jitter. The mean and standard deviation of these delays can indicate the consistency of packet timing, while the weight might reflect the relative significance of these delays in the context of the network's overall traffic pattern.

Overall, this dataset provides a rich, multi-faceted view of network traffic, suitable for deep analysis in fields such as network security, traffic management, and performance optimization. Its structured time series approach allows for both real-time and historical analysis of network behavior.

## Downloading necessary packages
Download the requirements.txt file and run the following command in the terminal to download the necessary packages to run the program.

``` pip install -r requirements.txt ```

## Results
Our models demonstrated high accuracy in detecting ARP spoofing attacks, with the GRU models, in particular, showing superior performance.

