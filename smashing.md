# Stack Smashing

## Questions

1. Stack canary is a random value stored before the return address in stack such that if stack overflows, the canary value would have to be overwritten first. This mechanism detects stack
overflow, which can then be handled accordingly.

2. Concept is similar to the use of canaries in mines. Canaries would be affected by any toxic gases released before humans. Hence, in the same way, it worked as an early way to detect before
any damage is done.

3.

// Recursive function without exit path would eventually overflow to heap.
int a()
{
    return int a();
}


## Debrief

1. Googling on stack overflow

2. 15min
