#include <Python.h>

/**
 * print_python_list_info - a function displays the basic info about 
 * python
 * @p: python object list
 * Return: void
 *
 */
void print_python_list_info(PyObject *p)
{
	int s, a, b;
	PyObject *obj;

	s = PY_SIZE(p);
	a = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", a);

	for (b = 0; b < s; b++)
	{
		printf("Element %d: ", b);

		obj = PyList_GetItem(p, b);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
