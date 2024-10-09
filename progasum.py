input_data =  open('input.txt', 'r')
data = input_data.read()
output_data = open('output.txt', 'w')
a = int(input())
b = 0
if a>1:
    for i in range (1, a+1):
        b += i
elif a<1:
    for i in range (a, 2):
        b += i
elif a == 1:
    print (2)
    exit
else:
    print (1)
    exit
print (b)
input_data.close()
output_data.close()