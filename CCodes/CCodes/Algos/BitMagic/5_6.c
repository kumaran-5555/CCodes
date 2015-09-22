#include <stdio.h>

/*
 * 5.6 swap even and odd bits
 *
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



int swapEvenOddBits(int n)
{
	int evenBits = n&0xAAAAAAAA;
	int oddBits = n&0x55555555;

	printBin(evenBits);
	printBin(oddBits);
	evenBits = evenBits>>1;
	oddBits = oddBits<<1;

	return evenBits | oddBits;
}



int main()
{
	printBin(19);
	
	printBin(swapEvenOddBits(19));
}

