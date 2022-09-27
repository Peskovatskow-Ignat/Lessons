x=int(input())
x=x//60#min
x=x//60#hour
x=x//24#days
x=x//365#years
print(1970+round(x))