#include "lists.h"

/**
 * check_cycle - determines whether a linked list contains a cycle
 * @list: to be checked linked list
 * Return: 1 or 0
 *
 */
int check_cycle(listint_t *list)
{
        listint_t *low = list;
        listint_t *ast = list;

        if (!list)
                return (0);

        while (low && ast && ast->next)
        {
                low = low->next;
                ast = ast->next->next;
                if (low == ast)
                        return (1);
        }

        return (0);
}
