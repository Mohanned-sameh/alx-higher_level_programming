#include "lists.h"
/**
 * is_palindrome - checks if singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);
	return (check_pal(head, *head));
}
/**
 * check_pal - checks if linked list is a palindrome
 * @head: pointer to head of list
 * @end: pointer to end of list
 * Return: 1 if palindrome, 0 if not
 */
int check_pal(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (check_pal(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
