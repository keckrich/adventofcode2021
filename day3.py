from math import floor

X = [l.strip() for l in open('in\\3.txt')]
# X = [int(x) for x in X]

threshhold = len(X)//2

gamma = 0
epsilon = 0


for i in range(len(X[0])):
    sum1 = sum(int(x[i]) for x in X )
    gamma <<= 1
    epsilon <<= 1
    if sum1 > threshhold:
        gamma |= 1
    else:
        epsilon |= 1



print (gamma * epsilon)
# print (bin(gamma))

o2 = X
co2 = X

for i in range(len(X[0])):
    if len(o2) > 1:
        threshhold_o2 = len(o2)/2
        significant_o2 = floor(sum(int(x[i]) for x in o2 ) / threshhold_o2)
        o2 = [x for x in o2 if int(x[i]) == significant_o2]
        # o2 = list(filter(lambda x: int(x[i]) == significant_o2, o2))
    if len(co2) > 1:
        threshhold_co2 = len(co2)/2
        significant_co2 = floor(sum(int(x[i]) for x in co2 ) / threshhold_co2)
        co2 = [x for x in co2 if int(x[i]) != significant_co2]
        # co2 = list(filter(lambda x: int(x[i]) != significant_co2, co2))

# print (o2, co2)
print (int(o2[0], 2)* int(co2[0], 2))