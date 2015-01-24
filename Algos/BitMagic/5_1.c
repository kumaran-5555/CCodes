#include <stdio.h>

/*
 * #5.1 fifth edition
 */

void printBin(unsigned int n)
{
	char bitStr[32];
	int i;
	
	for(i=31; i>=0; i--)
	{
		bitStr[i] = (n&1);
		n=n>>1;
	}
	for(i=0; i<32; i++)
	{
		printf("%d", bitStr[i]);
	}
	printf("\n");
}



void setBits(unsigned int n, unsigned int m, int i, int j)
{
	int mask=1;
	mask=mask<<(j-i+1);
	printBin(mask);
	mask-=1;
	printBin(mask);
	mask=mask<<i;
	printBin(mask);
	
	m=m<<i;
	n&=~mask;
	m&=mask;
	n=n|m;

	printBin(n);	
}

int main()
{
	setBits(1024, 19, 2, 6);
}


