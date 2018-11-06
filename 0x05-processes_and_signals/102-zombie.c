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
	pid_t child;
	int i = 0;

	while (i < 5)
	{
		child = fork();
		if (child)
			printf("Zombie process created, PID: %d\n", child);
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
