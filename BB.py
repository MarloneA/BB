
'''
z[0] reps lowerBB
z[1] reps middleBB
z[2] reps upperBB

'''

# Sample data
a =  [48.24,  49.38,  50.52]
b =  [48.34,  49.52,  50.7]
c =  [48.45,  49.63,  50.81]
d =  [48.62,  49.68,  50.74]
e =  [48.769999999999996,  49.73,  50.69]
f =  [48.92,  49.82,  50.72]
g =  [48.97,  49.83,  50.69]
h =  [49.05,  49.87,  50.69]
q =  [48.67,  49.77,  50.870000000000005]
j =  [48.29,  49.63,  50.970000000000006]
k =  [47.33,  49.41,  51.489999999999995]
l =  [46.199999999999996,  49.12,  52.04]
m =  [46,  48.98,  51.959999999999994]
n =  [45.84,  48.82,  51.8]
o =  [45.84,  48.7,  51.56]
p =  [45.8,  48.5,  51.2]

x = [a,b,c,d,e,f,g,h,q,j,k,l,m,n,o,p]

bandwidth=[]

for z in x:

	bw = ((z[2] - z[0])/z[1])*100 # formulae for calculating bandwidth 

	bandwidth.append(str(bw))

print ",       ".join(bandwidth)


