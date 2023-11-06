#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is palindrome or not
 * @head: pointer to head of the list.
 * Return: 1 or 0
 *
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (palindrome(head, *head));
}
/**
 * palindrome - function that check if is palindrome
 * @head: head list
 * @nd: end list
 */
int palindrome(listint_t **head, listint_t *nd)
{
	if (nd == NULL)
		return (1);
	if (palindrome(head, nd->next) && (*head)->n == nd->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
