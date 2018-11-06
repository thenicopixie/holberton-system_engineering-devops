#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - infinite loop
 * Return: 0
 */
int infinite_while(void);

/**
 * main - entry poiny
 */
void main(void)
{
	pid_t pid;
	int i = 0;

	while (i < 5)
	{
		pid = fork();
		if (pid > 0)
			return;
		else if (pid == 0)
			printf("Zombie process created, PID: %d\n", getpid());
		else
			exit;
		i++;
	}
	infinite_while();
}

/**
 * infinite_while - infinite loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
