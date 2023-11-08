#include <Python.h>
void print_python_list(pyobject *p);
void print_python_bytes(pyobject *p);

/**
 * print_python_list - prints basic info about python lists.
 * @p: a py object 
 */
void print_python_list(pyobject *p)
{
	int size, alloc, i;
	const char *type;
	pylistobject *list = (pylistobject *)p;
	pyvarobject *var = (pyvarobject *)p;

	size = var->ob_size;
	alloc = list->allocted;

	printf("[*] Python list info\n");
	printf("[*] size of the python list = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0 i < size; i++)
	{
		type = list->ob_
