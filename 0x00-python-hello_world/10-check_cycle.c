#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks if linked list is circular or not
 * @list - the linked list
 * Return 0 (No cycle) or 1 (cycle)
 */

int check_cycle(listint_t *list)
{
	listint_t *twice = list;
	listint_t *once = list;

	if(!list)
		return (0);

	while (1)
	{
		/* traverse will nodes exists */
		if (once->next != NULL && twice->next->next != NULL)
		{
			twice = twice->next->next;
			once = once->next;

			if(once == twice) /* match found */
				return (1);
		}
		else
			return (0);
	}
}
