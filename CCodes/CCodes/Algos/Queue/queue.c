#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <my_helpers.h>
#include "queue.h"


#undef DBG_ON
#define DBG_ON 1



queuePtr_t newQueue(int size)
{
	queuePtr_t q;
	q=calloc(1, sizeof(queue_t));
	q->front=0;
	q->end=0;
	q->storage=calloc(size, sizeof(int));
	q->size=size;
	q->currSize=0;
	return q;
}

int deQueue(queuePtr_t q, int *val)
{
	// check underflow
	if(q->currSize<=0)
		return -1;
	*val=q->storage[q->end];
	q->currSize--;
	q->end=(q->end+1)%q->size;
	return 0;
}

int enQueue(queuePtr_t q, int val)
{
	// check overflow
	if(q->currSize>=q->size)
		return -1;
	q->storage[q->front]=val;
	q->currSize++;
	q->front=(q->front+1)%q->size;
	return 0;
}


void delQueue(queuePtr_t q)
{
	free(q->storage);
	free(q);
}

void printQueue(queuePtr_t q)
{
	int i,j;
	if(q->currSize==0)
	{
		printf("EmptyQueue");
		return;
	}
	j=q->end;
	for(i=q->currSize;i>0;i--)
	{
		printf("%d ",q->storage[j]);
		j=(j+1)%q->size;
	}
	printf("\n");

}	

int isEmptyQueue(queuePtr_t q)
{
	return q->currSize==0;
}



