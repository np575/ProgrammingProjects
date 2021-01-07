/**
* srtheap.c file / np575
*
* to compile with heap sort:
*     gcc -std=c99 -DRAND -DTYPE=double -DHEAP *.c
*
*/
#include <stdlib.h>
#include <string.h>
#include "srt.h"

void heapify(char *array, size_t nelem, size_t size, size_t parent, int (*compar)(const void *, const void *));

void srtheap(void *base, size_t nelem, size_t size, int (*compar)(const void *, const void *)) {
char *array;
size_t i;

/* build heap */
array = malloc((size + 1) * nelem);
memcpy(array + size, base, nelem * size);

for (i = nelem / 2; i >= 1; i--) {
    heapify(array, nelem, size, i, compar);
}

/* sort */
for (i = nelem; i > 1; i--) {
    /* move the largest one to the last position */
    swap(array + size, array + i * size, size);
    heapify(array, i - 1, size, 1, compar);
}

memcpy(base, array + size, nelem * size);
free(array);

}


void heapify(char *array, size_t nelem, size_t size, size_t parent, int (*compar)(const void *, const void *)) {
size_t child;
while ((child = 2 * parent) <= nelem) {
    if (child + 1 <= nelem && compar(array + child * size, array + (child + 1) * size) < 0) {
      child = child + 1; /* right child is larger */
    }
    if (compar(array + parent * size, array + child * size) < 0) {
      swap(array + parent * size, array + child * size, size); /* child is larger, swap */
      parent = child;
    } else {
      break;
    }
}
}
