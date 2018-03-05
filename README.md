# Questions

## What is pneumonoultramicroscopicsilicovolcanoconiosis?

According to Google, its an invented long word said to mean a lung disease caused by inhaling very fine ash and sand dust.

## According to its man page, what does `getrusage` do?

It returns information about the resources used by the current process

## Per that same man page, how many members are in a variable of type `struct rusage`?

16

## Why do you think we pass `before` and `after` by reference (instead of by value) to `calculate`, even though we're not changing their contents?

This saves memory and computing time.

## Explain as precisely as possible, in a paragraph or more, how `main` goes about reading words from a file. In other words, convince us that you indeed understand how that function's `for` loop works.

Main first checks for the correct number of arguments in command line. Thereafter, it determines the dictionary to use and loads it. Large dictionary is used by default. If loading fails, program is stopped. It then calls getrusage() and calculate() to measure load times. Text fille
to be checked is opened using fopen. Text is then read by character selecting only alphabets or apostrophes. A word is completed when a non-alphabetical character is hit. If there are digits or if word is too long, the word is ignored and will
not be spell-checked. If a word is found, reset word index, update counter and check for misspellings. If word is misspelled, print it.


## Why do you think we used `fgetc` to read each word's characters one at a time rather than use `fscanf` with a format string like `"%s"` to read whole words at a time? Put another way, what problems might arise by relying on `fscanf` alone?

fscanf will not have the ability to validate for invalid words (eg. words with numbers within etc) since its reading the entire string.

## Why do you think we declared the parameters for `check` and `load` as `const` (which means "constant")?

Because check and load are not going to be changed anywhere in the program.
