name='python is good for coding'
print(name[0:6])
print(name[0:7])# so here we learnt the space is also counted 
print(name[0:8])
print(name[1:])#the first index is excluded and it take the empty space as indication to write till the last index 
print(name[1:-1])
#so here it started with index 1 but as last index -1 (g) is excluded the last one is always excluded 
#formated strings 
name="aditi"
title="singh"
msg=f"{name} {title} is cs engineer"# here the f is prefix for formatted string what we have to write have to be included in a single varible then write it 
print(msg)