#include "lists.h"
/**
 * insert_node - inserts a number in a sorted singly linked list
 * @head: start of list
 * @number: number to insert
 * Return: address of new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp;

	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL)
		new_node->next = NULL;
	else
	{
		temp = *head;
		while (temp->next != NULL && temp->next->n < number)
			temp = temp->next;
		new_node->next = temp->next;
		temp->next = new_node;
		return (new_node);
	}
	return (NULL);
}
