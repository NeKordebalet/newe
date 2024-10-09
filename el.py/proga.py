input_data =  open('input.txt', 'r')
data = input_data.read()
output_data = open('output.txt', 'w')
a = int(input())
c = 0
if a > 0 and a<= 10^4:
 b = (a+1)*a/2
elif a < 0 and a> (-1)*10**4:
 b = (a-1)*a/2 *(-1)
print(b)