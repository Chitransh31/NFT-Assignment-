import math
import random

def sigmoid(x, alpha=0.3):
    a = math.exp(-alpha * x)
    b = (1 / (1 + a))
    return b


def der(x):
    a = sigmoid(x)
    return a * (1 - a)


def train(w, yin, y, x, b, t, a):
	err = 0
	err1=0
	expected = list()
	for k in range(int(1 * len(x))):
		for i in range(3):
			yintemp = b[i]
			for j in range(7):
				yintemp = yintemp + (w[j][i] * x[k][j])
			yin.append(yintemp)
			ytemp = sigmoid(yintemp)
			y.append(ytemp)
		if x[k][7]==1.0:
			err1 = ((1-y[0])*(1-y[0])+(0-y[1])*(0-y[1])+(0-y[2])*(0-y[2]))
			err1 = (err1/3.0)
			expected.append(1.0)
			expected.append(0.0)
			expected.append(0.0)
		if x[k][7]==2.0:
			err1 = ((0-y[0])*(0-y[0])+(1-y[1])*(1-y[1])+(0-y[2])*(0-y[2]))
			err1 = (err1/3.0)
			expected.append(0.0)
			expected.append(1.0)
			expected.append(0.0)
		if x[k][7]==3.0:
			err1 = ((0-y[0])*(0-y[0])+(0-y[1])*(0-y[1])+(1-y[2])*(1-y[2]))
			err1 = (err1/3.0)
			expected.append(0.0)
			expected.append(0.0)
			expected.append(1.0)
        
		i=0
		for i in range(7):
			for j in range(3):
				d = y[j] - expected[j]
				d = d * y[j]*(1-y[j]) * x[k][i] * a
				w[i][j] = w[i][j] - d
		 
		j=0
		for j in range(3):
			d = y[j] - expected[j]
			d = d * y[j]*(1-y[j]) * a
			b[j] = b[j] - d
	
		print("xinput")
		print(x[k])
		print("class:")
		print(t[k])
		print("y:")
		print(y)
		print("Final bias:")
		print(b)
		print("Final wts:")
		print(w)
		print("Final error:")
		print(err1)
		print()
		del y[:]
		del yin[:]
		del expected[:]
		err = err + err1
	err = (err/len(x))
	return err


def test(w,b,x):
	start = 0
	res = list()
	for k in range(int(1 * len(x))):
		for i in range(3):
			yintemp = b[i]
			for j in range(7):
				yintemp = yintemp + (w[j][i] * x[k][j])
			yin.append(yintemp)
			ytemp = sigmoid(yintemp)
			y.append(ytemp)
		if y[0] > y[1] and y[0] > y[2]:
			res.append(1.0)
		if y[1] > y[0] and y[1] > y[2]:
			res.append(2.0)
		if y[2] > y[0] and y[2] > y[1]:
			res.append(3.0)
		del y[:]
		del yin[:]
	return res

#.............main.............................#
file = open("finaldatasettrain_merge.txt", "r")
x = list()
yin = list()
y = list()
w = list()
#v = list()
t = list()
b1 = list()
b1.append(random.uniform(0.0, 1.0))
b1.append(random.uniform(0.0, 1.0))
b1.append(random.uniform(0.0, 1.0))
alpha = 0.3
i=0
for line in file:
    x.append([float(x) for x in line.split()[0:]])
    t.append(x[i][7])
    i=i+1

for i in range(7):
    w.append([random.uniform(0.0, 1.0) for j in range(3)])


err = 5
while err > 0.03:
 	#for x1 in range(200):
	err = train(w, yin, y, x, b1, t, alpha)
	print("Error on entire epoch: ",err)


res = test(w, b1, x)
count = 0
i=0
for i in range(len(res)):
	print(res[i],t[i])
	if res[i]!=t[i]:
		count = count + 1
		print("notequal")

print("No. of values=",len(res))
print("count of wrong=",count)


file.close()
file = open("test2.txt", "r")
i=0
del x[:]
for line in file:
    x.append([float(x) for x in line.split()[0:]])
    t.append(x[i][7])
    i=i+1


result = test(w,b1,x)
inc = 0
count = 0
i=0
for i in range(len(result)):
	print(result[i],t[i])
	if result[i]!=t[i]:
		count = count + 1
		print("notequal")
	
print("No. of values=",len(result))
print("count of wrong=",count)

