#include "queue.h"
#include <stdio.h>


int main()
{
	int i=0;
	queuePtr_t q=newQueue(25);

	for(i=0;i<25;i++)
	{
		enQueue(q,i);
	}
	printQueue(q);

	while(!isEmptyQueue(q))
	{
		deQueue(q,&i);
		printf("Dequeued %d\n",i);
	}

	delQueue(q);
}
	
