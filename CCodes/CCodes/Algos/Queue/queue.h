#ifndef QUEUE_H
#define QUEUE_H


struct queue
{
	// front points to next available place
	int front;
	// end points to the element added first not yet removed
	int end;
	int *storage;
	int size;
	int currSize;
};

typedef struct queue queue_t;
typedef struct queue *queuePtr_t;


queuePtr_t newQueue(int size);
int deQueue(queuePtr_t s, int *val);
int enQueue(queuePtr_t s, int val);
void delQueue(queuePtr_t s);
void printQueue(queuePtr_t s);
int isEmptyQueue(queuePtr_t s);

#endif
 
