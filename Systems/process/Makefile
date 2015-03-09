all: parent_child process_chain mmap_record_locking semaphore



parent_child: parent_child.c

process_chain:	process_chain.c

mmap_record_locking: mmap_record_locking.c
	gcc -lrt mmap_record_locking.c -o mmap_record_locking 

semaphore: semaphore.c
	gcc -lpthread -lrt semaphore.c -o semaphore
