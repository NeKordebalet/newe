from decimal import Decimal as doc
input_data = open('input.txt', 'r') 
output_data = open('output.txt', 'w')
a=doc('2.7182818284590452353602875')
data = input_data.read() 

b=round(a,int(data))

output_data.write(str(round(a)),int(data))
input_data.close()
output_data.close()
