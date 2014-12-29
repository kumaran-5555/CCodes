#include <stdio.h>
#include <stdlib.h>


struct node{
	int val;
	struct node *next;
	};


struct node * create_node(int val)
{
	struct node * n = calloc(1, sizeof(struct node));
	n->val = val;
	return n;
}


void add_node(struct node * head, int val)
{
	// assumes head exists
	struct node *temp=head;
	while(temp)
	{
		if (temp->next)
		{
			temp=temp->next;
			continue;
		}
	
		temp->next = create_node(val);
		break;
	}
	return;
}

void print_list(struct node *head)
{
	struct node *temp=head;
	while(temp)
	{
		printf("%d->",temp->val);
		temp=temp->next;
	}
}	

int main()
{
	printf("hello");
	struct node * head = create_node(10);
	add_node(head,11);
	add_node(head,12);
	print_list(head);
	return 0;

}
