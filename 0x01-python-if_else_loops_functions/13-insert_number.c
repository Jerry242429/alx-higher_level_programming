#include "lists.h"

/**
 * insert_node - a function Inserts a number in sorted list
 * @head: pointer the head
 * @number: number to insert the linked list.
 * Return: If the function fails - NULL.
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *de = *head, *w;

        w = malloc(sizeof(listint_t));
        if (w == NULL)
                return (NULL);
        w->n = number;

        if (de == NULL || de->n >= number)
        {
                w->next = de;
                *head = w;
                return (w);
        }

        while (de && de->next && de->next->n < number)
                de = de->next;

        w->next = de->next;
        de->next = w;

        return (w);
}
