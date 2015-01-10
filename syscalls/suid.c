#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>


int printIds()
{
	// print the uids 
	uid_t ruid;
	uid_t euid;
	uid_t suid;
	gid_t rgid;
	gid_t egid;
	gid_t sgid;

	getresuid(&ruid, &euid, &suid);
	printf("r %u e %u s %u \n", ruid, euid, suid);
	
	getresgid(&rgid, &egid, &sgid);
	printf("r %u e %u s %u \n", rgid, egid, sgid);

	
	
}


int main()
{
	printIds();
	
	// seteuid changes only the effective uid
	// when the current effective uid is root, it can be
	// changed to anything
	// if the current uid is non-root, it can be changed to either saved uid, real uid, current effective uid
	seteuid(1000);
	perror("");
	printIds();
	
	// setuid changes effectiive uid
	// when the current effective uid is root, all euid, ruid, suid are changed
	// thus we can't get root privilege	
	setuid(0);
	perror("");
	printIds();
}

