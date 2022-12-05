# X = [l.strip() for l in open('in\\1.txt')]
# # XS = [int(x) for x in open('1.in')]
# # X = [int(x) for x in X]

# depth = int(X[0])
# tot = 0

# for x in X:
#     if int(x) > depth:
#         tot += 1
#     depth = int(x)

# print(tot)

# depth = sum(int(x) for x in X[0:3])
# tot = 0

# for x in range(2, len(X)):
#     newDepth = sum(int(x) for x in X[x:x+3])
#     if newDepth > depth:
#         tot += 1   
#     depth = newDepth
 
# print(tot)



'''
X = [l.strip() for l in open('in\\1.txt')]
for elf in ('\n'.join(X)).split('\n\n'):
    for line in elf.split('\n'):
        asd =1 # do logic here
'''