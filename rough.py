import array as arr
#int
x = arr.array("i",[1,2,3,3,4,6,7])
print(type(x),x)
#char no need of using brackets
y = arr.array("u","cricket")
print(y)
z = arr.array("d",[1,2,3,4,5,6])
z.append(8)
print(z)
z.remove(5)
print(z)
z.append(1)
print(z)
z.pop(4)
print(z)
#changing of arrays
z[1]=20
print(z[1])
print(z)
z[0]=10
z[2]=13
z[3]=12
z[4]=15
z[5]=11
print(z[0])
print(z)
z.append(2)
print(z)
z.pop(5)
print(z)
z.remove(2)
print(z)
#increasing order
c = z.tolist()
print(c)
c.sort()
print(c)
z = arr.array('d')
z.fromlist(c)
print(z)
sorted_z_desc = sorted(z, reverse=True)
print(sorted_z_desc)
z.reverse()
print(z)
#adding of two arrays
A= x.tolist()
B= z.tolist()
c = A+B
print(c)
A.extend(B)
print(A)
