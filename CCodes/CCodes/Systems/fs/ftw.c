#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <my_helpers.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <dirent.h>


/*
 * take directory as an input and print as much as information
 * possible for all files and directory in that directory
 */
//   struct stat {
//               dev_t     st_dev;     /* ID of device containing file */
//               ino_t     st_ino;     /* inode number */
//               mode_t    st_mode;    /* protection */
//               nlink_t   st_nlink;   /* number of hard links */
//               uid_t     st_uid;     /* user ID of owner */
//               gid_t     st_gid;     /* group ID of owner */
//               dev_t     st_rdev;    /* device ID (if special file) */
//               off_t     st_size;    /* total size, in bytes */
//               blksize_t st_blksize; /* blocksize for file system I/O */
//               blkcnt_t  st_blocks;  /* number of 512B blocks allocated */
//               time_t    st_atime;   /* time of last access */
//               time_t    st_mtime;   /* time of last modification */
//               time_t    st_ctime;   /* time of last status change */
//           };
 




void printFileInfo(struct stat *s, char *fileName)
{
	int type;
	char *fileType;
	printf("%lu\t", s->st_ino);
	printf("%lu\t", s->st_size);
	printf("%u\t", s->st_nlink);
	printf("%u\t", s->st_uid);
	printf("%u\t", s->st_gid);
	
	type = s->st_mode & S_IFMT;
	switch(type)
	{
		case S_IFREG:
			fileType = "Regular";
			break;
		case S_IFLNK:
			fileType = "Link";
			break;
		case S_IFBLK:
			fileType = "Block";
			break;
		case S_IFDIR:
			fileType = "Directory";
			break;
		case S_IFSOCK:
			fileType = "Socket";
			break;
		case S_IFCHR:
			fileType = "Character";
			break;
		case S_IFIFO:
			fileType = "Fifo";
			break;
	}
	printf("%s\t", fileType);
	printf("%s\t", fileName);

	printf("\n");
}

void processDir(char *dirName)
{
	DIR *dir;
	struct dirent *dirEnt;
	struct stat s;
	int lenOfDirName = strlen(dirName);
	char *nameBuf;

	DBG("%s\n", dirName);

	dir = opendir(dirName);

	nameBuf = calloc(lenOfDirName + 1 + NAME_MAX, 1);
	if (!nameBuf)
	{
		perror("calloc()");
		exit(2);
	}
	strcpy(nameBuf, dirName);
	nameBuf[lenOfDirName]='/';
	nameBuf[lenOfDirName+1]='\0';
	
		
	if (!dir)
	{
		perror("opendir()");	
		exit(1);
	}
	while((dirEnt = readdir(dir)))
	{
		strcpy(nameBuf+lenOfDirName+1, dirEnt->d_name);
		if(stat(nameBuf, &s) < 0)
		{
			perror("stat()");
			exit(2);
		}
		printFileInfo(&s, nameBuf);
		// recurse if it is not own and not parent
		if(s.st_mode & S_IFDIR && strcmp(dirEnt->d_name, ".") && strcmp(dirEnt->d_name, ".."))
		{
			processDir(nameBuf);
		}
	}
}
		
	



int main(int argc, char *argv[])
{
	char *dirName;
	if (argc != 2)
	{
		printf("Usage: %s <dirName>\n", argv[0]);
		exit(0);
	}
	
	dirName = argv[1];
	processDir(dirName);

	
}
	
