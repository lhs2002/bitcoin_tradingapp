a = "test"

n=2

length_a = len(a)


x = (a[i:(i+n)] for i in range(length_a - (n-1)))



print(length_a)

print(x)
