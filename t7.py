a={"erfan":[15,16,17,18],"mehrshad":[17,12,15,20]}
b=0
for i in a["erfan"]:
    b+=i
c=len(a["erfan"])
a["erfan"]=b/c
 

d=0
for j in a["mehrshad"]:
    d+=j
r=len(a["mehrshad"])
a["mehrshad"]=d/r

print(a)

