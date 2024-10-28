input_data =  open('input.txt', 'r')
data = input_data.read()
output_data = open('output.txt', 'w')
a = int(data)
b = int(1)
for i in range (1, a+1):
    b = b * i
output_data.write(str(b))
input_data.close
output_data.close
