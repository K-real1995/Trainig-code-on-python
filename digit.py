import sys
x= sys.argv[1]
result=x + " " + bin(int(x))[2:]+ " " + oct(int(x))[2:]+ " " + hex(int(x))[2:]
print(result)
