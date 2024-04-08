n=25
temp=n
sqr=n*n
count=1
while n>0:
  R=n%10
  n=n//10
  count=count+1
  lastnumber=sqr%10**count
if lastnumber==temp:
    print("automorphic number")
else:
    print("not a automorphic number")
