# Questions

## What's `stdint.h`?

Header file within standard C library that provides specific width integer types with defined minimum and maximum values for each type.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

uint8_t defines that an integer is unsigned and uses exactly 8 bits to store its value. Unsigned integers can hold a larger positive value but no negative value while signed ones may hold both positive or negative values.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE = 1 byte
DWORD= 4 bytes
LONG = 4 bytes
WORD = 2 bytes

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

ASCII: BM must be the first 2 bytes in BMP file.

## What's the difference between `bfSize` and `biSize`?

bfSize is the total size, in bytes, of the bitmap file. biSize is the number of bytes required in the BITMAPINFOHEADER.

## What does it mean if `biHeight` is negative?

The bitmap is a top-down DIB and 1st byte in memory is top left corner of image. The top row of the image is the first row in memory while the bottom row of the image is the last row in the buffer.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount specifies the bits per pixel in the bitmap.

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

NULL would be returned if file opening failed. Eg. if file does not exist.

## Why is the third argument to `fread` always `1` in our code?

Implies that fread will read only once from file.

## What value does line 63 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

3

## What does `fseek` do?

Allows the changing of the offset of the file pointer. In particular, offset within fseek specifies the number of bytes to offset by.

## What is `SEEK_CUR`?

Specifies the current position of the file pointer.
