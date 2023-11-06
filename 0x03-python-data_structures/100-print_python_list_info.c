#include <Python.h>
#include <stdio.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - function displays some basic info about 
 * Python lists.
 * @p: PyObject.
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int s, allocated, b;

	s = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", allocated);

	for (b = 0; b < s; b++)
	{
		printf("Element %d: ", b);
		printf("%s\n", ((PyList_GetItem(p, b))->ob_type)->tp_name);
	}
}
