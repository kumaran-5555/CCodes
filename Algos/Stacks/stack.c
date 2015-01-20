#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <my_helpers.h>
#include "stack.h"


#undef DBG_ON
#define DBG_ON 1



stackPtr_t newStack(int size)
{
	stackPtr_t s;
	s=calloc(1, sizeof(stack_t));
	s->top=0;
	s->storage=calloc(size, sizeof(int));
	s->size=size;
	return s;
}

int popStack(stackPtr_t s, int *val)
{
	// check underflow
	if(s->top<=0)
		return -1;
	s->top--;
	*val=s->storage[s->top];
	return 0;
}

int pushStack(stackPtr_t s, int val)
{
	// check overflow
	if(s->top>=s->size)
		return -1;
	s->storage[s->top]=val;
	s->top++;
	return 0;
}


void delStack(stackPtr_t s)
{
	free(s->storage);
	free(s);
}

void printStack(stackPtr_t s)
{
	int i;
	if(s->top==0)
	{
		printf("EmptyStack");
		return;
	}
	for(i=0;i<s->top;i++)
	{
		printf("%d ",s->storage[i]);
	}
	printf("\n");

}	

int isEmptyStack(stackPtr_t s)
{
	return s->top==0;
}


