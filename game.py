
input_data = open('input.txt', 'r') 
data = input_data.read() 
k = int(data)
a=9 
c = str(a-k) 
b=str(k)+str(a)+c

output_data = open('output.txt', 'w')

output_data.write(b)
 
input_data.close()
output_data.close()