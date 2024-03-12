weights=input("enter the weights with space between weights:")
weights_list=weights.split()
count=0
for weights in weights_list:
    count=count+1
print(count)
for i in range(count):
    weights_list[i]=int(weights_list[i])
print(weights_list)
