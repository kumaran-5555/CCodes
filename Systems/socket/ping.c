#include <sys/socket.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <netinet/ip.h>
//#include <linux/ip.h>
#include <linux/icmp.h>




unsigned short in_cksum(unsigned short *addr, int len);


int main(int argc, char *argv[])
{
	int socketFd, sts;
	char *request, *response;
	struct iphdr *ipHdr;
	struct icmphdr *icmpHdr;
	struct sockaddr_in peerAddr;


	request = calloc(1, sizeof(struct iphdr) + sizeof(struct icmphdr));
	response = calloc(1, sizeof(struct iphdr) + sizeof(struct icmphdr));

		
	if (argc != 3)
	{
		printf("Usage: %s <srcIpAddr> <dstIpAddr>\n", argv[0]);
		exit(1);
	}
	
	socketFd = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
	if(socketFd < 0)
	{
		perror("socket()");
		exit(2);
	}

	peerAddr.sin_family = AF_INET;
	inet_pton(AF_INET, argv[2], &peerAddr.sin_addr.s_addr);


	ipHdr = (struct iphdr *)request;
	icmpHdr = (struct icmphdr *)(request + sizeof(struct iphdr));

	ipHdr->version = 4;
	ipHdr->ihl = sizeof(struct iphdr);
	ipHdr->tos = 0;
	ipHdr->tot_len = sizeof(struct iphdr) + sizeof(struct icmphdr);
	ipHdr->id = 0x5555;
	ipHdr->frag_off = 0;
	ipHdr->ttl = 0xFF;
	ipHdr->protocol = IPPROTO_ICMP;
	inet_pton(AF_INET, argv[1], &ipHdr->saddr);
	inet_pton(AF_INET, argv[2], &ipHdr->daddr);
	ipHdr->check = in_cksum(ipHdr, sizeof(struct iphdr));
	
	icmpHdr->type = ICMP_ECHO;
	icmpHdr->code = 0;
	icmpHdr->un.echo.id = 0x555;
	icmpHdr->un.echo.sequence = 0x01;
	icmpHdr->checksum = in_cksum(icmpHdr, sizeof(struct icmphdr));

	sts = sendto(socketFd, request, sizeof(struct iphdr) + sizeof(struct icmphdr), 0, &peerAddr, sizeof(struct sockaddr_in));

	
	
	
}


/*
 *  * in_cksum --
 *   * Checksum routine for Internet Protocol
 *    * family headers (C Version)
 *     */
unsigned short in_cksum(unsigned short *addr, int len)
{
    register int sum = 0;
    u_short answer = 0;
    register u_short *w = addr;
    register int nleft = len;
    /*
 *      * Our algorithm is simple, using a 32 bit accumulator (sum), we add
 *           * sequential 16 bit words to it, and at the end, fold back all the
 *                * carry bits from the top 16 bits into the lower 16 bits.
 *                     */
    while (nleft > 1)
    {
      sum += *w++;
      nleft -= 2;
    }
    /* mop up an odd byte, if necessary */
    if (nleft == 1)
    {
      *(u_char *) (&answer) = *(u_char *) w;
      sum += answer;
    }
    /* add back carry outs from top 16 bits to low 16 bits */
    sum = (sum >> 16) + (sum & 0xffff);       /* add hi 16 to low 16 */
    sum += (sum >> 16);               /* add carry */
    answer = ~sum;              /* truncate to 16 bits */
    return (answer);
}	
