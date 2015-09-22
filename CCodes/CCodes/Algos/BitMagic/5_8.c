#include <stdio.h>
#include <stdlib.h>


/*
 * 5.8 fifth edition
 * monochrome horizantal line
 */
void printBin(unsigned char n)
{
	char bit[8];
	int i;
	
	for(i=7; i>=0; i--)
	{
		bit[i] = (n&1);
		n=n>>1;
	}
	for(i=0; i<8; i++)
	{
		printf("%d", bit[i]);
	}
	printf("+");
}


void printScreen(char *screen, int length, int width)
{
	int i,j;
	for(j=0; j<length; j++)
	{
		for (i=0; i<width;i++)
		{
			printBin(screen[(j*width)+i]);
		}
		printf("\n");
	}
}


void setBits(char *c, int start, int len)
{
	int positionFromRight = 7-start;
	int mask = 1<<positionFromRight;
	while(len)
	{
		//printf("%d %d %d\n", start, len, positionFromRight);
		*c|=mask;
		len--;
		mask=mask>>1;
	}

}

void horizontalLine(char *screen, int length, int width, int x1, int x2, int y)
{

	int widthInBytes = width;
	int currRowStartingByte = y*widthInBytes;
	
	int lineSize = x2-x1;

	printf("%d\n", sizeof(char));	
	while(lineSize)
	{
		printf("lineSize %d x1 %d currRow %d\n", lineSize, x1, currRowStartingByte);
		if(x1%8 == 0 && lineSize >= 8)
		{
			printf("case1\n");
			screen[currRowStartingByte+x1/8]=(unsigned char)0xFF;
			x1+=8;
			lineSize-=8;
		}
		else if(x1%8 != 0 && lineSize >= (8-x1%8))
		{
			printf("case2\n");
			setBits(&(screen[currRowStartingByte+x1/8]), x1%8, 8-(x1%8));
			lineSize-=(8-(x1%8));
			x1+=(8-x1%8);
		}
		else
		{
			printf("case3\n");
			setBits(&(screen[currRowStartingByte+x1/8]), x1%8, lineSize);
			lineSize-=lineSize;
		}
	}

		

}



int main()
{

	char *c= (char *)calloc(50, sizeof(char));
	printScreen(c, 10, 5);
	horizontalLine(c, 10, 5, 2, 18, 3);
	printScreen(c, 10, 5);



}
