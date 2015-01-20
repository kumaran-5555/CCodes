#include "stack.h"
#include <stdio.h>


int main()
{
	int i=0;
	stackPtr_t s=newStack(25);

	for(i=0;i<25;i++)
	{
		pushStack(s,i);
	}
	printStack(s);

	while(!isEmptyStack(s))
	{
		popStack(s,&i);
		printf("Popped %d\n",i);
	}

	delStack(s);
}
	
