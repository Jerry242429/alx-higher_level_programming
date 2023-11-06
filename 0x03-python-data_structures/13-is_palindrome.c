#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is palindrome or not
 * @head: pointer to head of the list.
 * Return: 1 or 0
 *
 */
int is_palindrome(listint_t **head)
{
	int array[10000];
	int j, m = 0;
	listint_t *t;

	if (head == NULL)
		return (0);

	t = *head;
	while (t)
	{
		array[m++] = t->m;
		t = t->next;
	}
	for (j = 0; j < m / 2; j++)
	{
		if (array[j] != array[m - j - 1])
			return (0);
	}
	return (1);
}
