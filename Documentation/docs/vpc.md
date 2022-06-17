[link to index](/readme.md)  
# Virtual Private Cloud (VPC)
A virtual private cloud (VPC) is a secure, isolated private cloud hosted within a public cloud. VPC customers can run code, store data, host websites, and do anything else they could do in an ordinary private cloud, but the private cloud is hosted remotely by a public cloud provider. (Not all private clouds are hosted in this fashion.) VPCs combine the scalability and convenience of public cloud computing with the data isolation of private cloud computing.

- why should we use it
    - because it is more fleixable than a standard network or VPN
    - you pay for what you use
    - they are more secure than a a public cloud

- benefits of vpc
    - Scalability
        - Because a VPC is hosted by a public cloud provider, customers can add more computing resources on demand.
    - Easy hybrid cloud deployment
        - It's relatively simple to connect a VPC to a public cloud or to on-premises infrastructure via the VPN. (Learn about hybrid clouds and their advantages.)
    - Better performance
        - Cloud-hosted websites and applications typically perform better than those hosted on local on-premises servers.
    - Better security
        - The public cloud providers that offer VPCs often have more resources for updating and maintaining the infrastructure, especially for small and mid-market businesses. For large enterprises or any companies that face extremely tight data security regulations, this is less of an advantage.

## Internet gateway
- A computer that sits between different networks or applications. The gateway converts information, data or other communications from one protocol or format to another. A router may perform some of the functions of a gateway. An Internet gateway can transfer communications between an enterprise network and the Internet.

## Subnet
- A subnet is a range of IP addresses within a network that are reserved so that they're not available to everyone within the network, essentially dividing part of the network for private use. In a VPC these are private IP addresses that are not accessible via the public Internet, unlike typical IP addresses, which are publicly visible.

## Classless Inter-Domain Routing (CIDR) block
- Classless Inter-Domain Routing (CIDR /ˈsaɪdər, ˈsɪ-/) is a method for allocating IP addresses and for IP routing. The Internet Engineering Task Force introduced CIDR in 1993 to replace the previous classful network addressing architecture on the Internet. Its goal was to slow the growth of routing tables on routers across the Internet, and to help slow the rapid exhaustion of IPv4 addresses.[1][2]
- [How to create one](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html)
- [creating the block specifically](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-cidr-reservation.html)


##  Network Access Control Lists (NACL)
- An optional layer of security that acts as a firewall for controlling traffic in and out of a subnet. You can associate multiple subnets with a single network ACL, but a subnet can be associated with only one network ACL at a time.
- It is network level security, because NACLs function at the subnet level of a VPC, each NACL can be applied to one or more subnets, but each subnet is required to be associated with one—and only one—NACL.
 - When traffic enters your network, it is filtered by NACLs before it is filtered by security groups.
- This means that traffic allowed by a NACL can then be allowed or denied by a security group, and traffic stopped by a NACL never makes it any further.
 - Given this "order of operations" in processing incoming traffic, here are two examples of implementing NACLs and security groups in tandem:
- Use cases
     - Use fine-grained rules with NACLs and let security groups handle inter-VPC connectivity.
        - For example, if you configure NACLs with granular rules for controlling inbound and outbound traffic, the NACLs can take the brunt of the work for filtering traffic. You can configure a NACL to allow inbound HTTP and HTTPS traffic from any IP address, deny all other inbound traffic, and allow all outbound traffic. As another example, you can allow inbound SSH access (port 22) from one IP address—yours—and allow outbound access on any port to the same IP address.
        - Meanwhile, you can configure a security group to allow inbound traffic from itself, enabling communication between resources. Or, you can configure the security group to allow traffic into and out of a different security group, which enables instances within different subnets to talk to each other.
    - Eliminate whole classes of traffic with NACLs and use fine-grained rules with security groups.
        - In this scenario, you can configure a NACL to deny all traffic from a wide range of IP addresses to a certain protocol and port and allow the rest to continue to the security group, which may be configured to evaluate incoming and outgoing traffic on a more granular level. The NACL takes a coarse-grained approach to controlling traffic, leaving the security group to filter the rest through a fine-toothed comb.


## Diagram
![nacl in aws](/Documentation/resources/aws/nacl_in_aws.png)  