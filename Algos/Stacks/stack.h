#ifndef STACK_H
#define STACK_H


struct stack
{
	// top points to next available place
	int top;
	int *storage;
	int size;
};

typedef struct stack stack_t;
typedef struct stack *stackPtr_t;


stackPtr_t newStack(int size);
int popStack(stackPtr_t s, int *val);
int pushStack(stackPtr_t s, int val);
void delStack(stackPtr_t s);
void printStack(stackPtr_t s);
int isEmptyStack(stackPtr_t s);

#endif
 
