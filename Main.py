from pasteboard import set_string
from Sfsfile import *
partlist=[""]*256
partcnt=0
doublequote='"'
def counts(array):

    i=0
    for n in array:
        if n!="":
        
            i+=1
    
    return i
def firstspacecount(str):

    i=0
    e=0
    for n in str:
        if n==" "and(e<2):
            e=1
            i+=1
        if n!=" "and e==1:
            e=2
    
    return i
def co(array):

    i=0
    for n in array:
        if n=="":
        
            i+=1
    
    return i
def next_ava(arr):
    index=0
    for i in arr:
        if i=="":
            return index
        index+=1
def p2c(arr):
    array=arr.copy()
    while(co(array)!=0):array.remove("");
    return array
def findpos(str,pos,dir,key):
    if dir == 1:
        s=0
    elif dir==-1:
        s=len(str)
    i=pos
    for i in range(s,pos,dir):
        if(str[i]==key):
            break
    return i
        
def str2dict(str,k1,k2):
    out=dict()
    b=0
    for a in str:
        if a==k1:
            out[str[:a]]
        b+=1
def update():
    
    print(partcnt)
print(len(p2c(partlist)))
while True:
    partcnt= counts(partlist)
    rwin=input(">")
    inp=rwin.split(' ')
    cmd=inp[0].lower()
    args=pa2ca(inp[1:])
    if cmd=="?"or cmd=='help':
        print("info > get module info\nnew [name] [x] [y] [rotation] [attr] > new part file\npart > get part id list\nedit [part id] [attr] [value] > edit part\npartinfo [part id] > get data of part")
    elif cmd=="info":
        print("Sfs bp creator 1.0 by cjiscool")
    elif cmd=="new":
        print(len(args))
        if len(args) >= 3:
            if len(args) == 3:
                sx,sy,rot=1,1,0
                
            if len(args) == 4:
                sx=args[3]
                sy=1
                rot=0
                attr={}
            if len(args) == 5:
                sx,sy=args[3:5]
                rot=0
                attr={}
            if len(args) == 6:
                print(args,"arg")
                sx,sy,rot=args[3:6]
                attr={}
            if len(args) > 6:
                print(args,"arg")
                sx,sy,rot=args[3:6]
                attr=args[6:]
            name=doublequote+args[0]+doublequote
            partlist[next_ava(partlist)]=recreatepart(name,float(args[1]),float(args[2]),sx,sy,rot,attr)
            print(partlist[partcnt])
            print("%s Generated"%name)
        else:
            print("usage:n [name] [x] [y] [sx] [sy] [rot] [attr]")
    elif cmd=="part":
        index=0
        for n in partlist:
            if n=="":
                index+=1
                continue;
            print(partdata(n)[0],index)
            index+=1
    elif cmd=="partinfo":
        if(len(args)>=1):
            if(partlist[int(args[0])]!=''):print("name %s x %.1f y %.1f sx %i sy %i rot %i deg others %s"%partdata(partlist[int(args[0])]))
            else:
                print("invalid part id")
        else:
            print("Please specify part id")
    elif cmd=="del":
        if(len(args)>=1):
            inv_id=[""]*len(args)
            r=0
            for i in args:
                i=int(i)
                
                if( partlist [i]==''):
                    inv_id[r]=i
                r+=1
            if counts(inv_id)!=0:
                print("Invalid id(s)",inv_id)
            else:
                print("are u sure to delete these?:y/n")
                if(input()=="y"):
                    for i in args:
                        i=int(i)
                    partlist[i]=""
                else:
                    print("canceled")
        else:
            print("Please specify part id(s)")
        
    elif cmd=="import":
        dat=rwin[len(cmd)-1+firstspacecount(rwin):]
        
        data=decodebp(dat)
        
        if data==[]:
            print("not a bp")
        if True:
            for i in data:
                partlist[next_ava(partlist)]=i
                name=partdata(i)[0]
                print("%s Imported"%name)
    elif cmd=="export":
        data=encodebp(partlist)
        set_string(data)
        print("export complete paste in text editor and import to game!")
    else:
        print("unknown command try ? or help")
