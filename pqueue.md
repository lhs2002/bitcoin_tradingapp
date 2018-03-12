# Now Boarding

## Questions

1.

typedef struct
{
   int front;
   int *numbers;
   int size;
   unsigned int group;
   int capacity;
}
pqueue;

2.
check current size of array can still add on elements (if size >= capacity, return 1)
    else
        check queue is empty
            if(size = 0), put new element in queue array, increment int front
            if(size!=0), go to each element in group from back of queue and compare int group
                if group of new element < group of existing element, move to next element
                else
                insert new element behind existing element
                increment size by 1

3. O(n), Worst case scenario where iteration over entire array of n size elements before successful enqueuing.

4.

check queue is empty
    if(size = 0), return 1
    else
    Go to 1st element (front =1 ) and return element
    Increment front by 1
    Decrease size by 1

5. O(1), since queue is sorted by priority (group) with higher priority at the front, dequeue each time is just removing the 1st element of array.

## Debrief

1. Lecture 5

2. 30min
