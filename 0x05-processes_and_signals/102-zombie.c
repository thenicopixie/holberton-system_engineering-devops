#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * main - entry poiny
 * Return: 0
 */
int main(void)
{
	pid_t child;
	int i = 0;

	while (i < 5)
	{
		child = fork();
		if (child)
			printf("Zombie process created, PID: %d\n", child);
		else
			exit(0);
		i++;
	}
	sleep(200);
	return (0);
}
