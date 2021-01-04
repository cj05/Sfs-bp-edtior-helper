import pasteboard
def nos(string):
    out=""
    for l in string:
        if l!= " " and l!='\n':
            out+=l
    return out
def validitycheck(a,b):
    str1=nos(a)
    str2=nos(b)
    index=0
    try:
        for i in str2:
            if i!=str1[index]:
                print(index,i,str1[index])
            index+=1
    except:
        print("error")
def count(array):

    i=0
    for n in array:
        if n!="":
        
            i+=1
    
    return i
def array2str(array):
    o=""
    e=""
    cnt=count(array)
    ind=0
    for i in array:
        if(ind>=cnt-1):e=""
        else:e=","
        o=o+i+e
        ind+=1
    return o
def pa2ca(array):
    return array[0:count(array)]

def get2chr(str,chr):
    o=""
    index=0
    for i in str:
        if i == chr:break
        o+=i
        
    return o
def findindex(str1,str2):
    cnt=0
    index=-1
    l=0
    for i in str1:
        if i == str2[cnt]:
            if(cnt==0):index=l
            cnt+=1
        else:
            cnt=0
        if cnt==len(str2):
            break
        l+=1
    return index
def extractattributes(part):
    out=dict()
    index=0
    level=0
    str=False
    k=0
    cid=""
    w=False
    for i in part:
        if i=='"': str=not str
        if i==' 'and not str:
            continue
        if i=='\n':
            continue
        if i=="{": level+=1; 
        if i=="[": level+=1; 
        if i=="}": level-=1; 
        if i=="]": level-=1;
        if k==0 and i=="{" and level==1:
            k=1
            continue
        if level==1 and i==":":
            w=True
            continue
        if level==1 and i==",":
            w=False
            cid=""
            continue
        if level<1:
            w=False
            cid=""
            continue
        if not w :
            cid+=i
        if w:
            try:out[cid]+=i
            except:out[cid]=i
            
        index+=1
    return out
#decode bps into part array
def decodebp(input):
    #init
    partlimit=256
    output=[None]*256
    level=0
    partindex=0
    value=False
    cvalue=False
    string=0
    st=False
    partdata=[""]*partlimit
    index=0
    time=0
    #decode to get part's data
    for i in input:
        
        #ignore space and newlines
        if i=='"':st=not st
        if i==" "and not st:continue
        if i=="\n":continue
        #track ascension level
        if i=="{": level+=1; 
        if i=="[": level+=1; 
        if i=="}": level-=1; 
        if i=="]": level-=1; 
        #put data in when reach certain level
        if level>2:
            partdata[index]+=i
        elif partdata[index]!="":
            partdata[index]+="}"
            index+=1
        time=max(time,level)
    
    return pa2ca(partdata)


def encodebp(array):
    ret='{\n"parts":['+array2str(array)
    return ret+"]}"
    
def partdata(part):
    data=extractattributes(part)
    name=data['"n"']
    pos=extractattributes(data['"p"'])
    x=float(pos['"x"'])
    y=float(pos['"y"'])
    scale=extractattributes(data['"o"'])
    sx=int(scale['"x"'])
    sy=int(scale['"y"'])
    rot=int(scale['"z"'])
    if len(data)>3:
        otherattr=dict()
        for i in data:
            if i=="'n'":
                continue
            if i=="'p'":
                continue
            if i=="'o'":
                continue
            otherattr[i]=(extractattributes(data[i]))
        return name,x,y,sx,sy,rot,otherattr
    return name,x,y,sx,sy,rot,{}
def recreatepart(name,x,y,sx,sy,rot,otherattr):
    attrformat="{0}: {{"
    lowerformat="{0}: {1}"
    partformat="""{{
      "n": {0},
      "p": {{
        "x": {1},
        "y": {2}
      }},
      "o": {{
        "x": {3},
        "y": {4},
        "z": {5}
      }}"""
    if otherattr=={}:
        out = partformat.format(name,x,y,sx,sy,rot)+"\n}"
    else:
        out= partformat.format(name,x,y,sx,sy,rot)+","
        si=3
        con=len(otherattr)
        for i in otherattr:
            if i=='"n"':continue
            if i=='"p"':continue
            if i=='"o"':continue
            out+=attrformat.format(i)+"\n"
            cnt=len(otherattr[i])
            index=0
            for l in otherattr[i]:
                if index+1<cnt:
                    c=","
                else:
                    c=""
                out+=lowerformat.format(l,otherattr[i][l])+c+"\n"
                index+=1
            if si+1<con:m=","
            else:m=""
            out+="\n}"+m
            si+=1
        out+="}"
    return out
    
"""file=open("Blueprint.txt",'r')
output=[""]*256
index=0
filedat=file.read()
for i in decodebp(filedat):
    n,x,y,sx,sy,rot,o=partdata(i)
    output[index]=recreatepart(n,x,y,sx,sy,rot,o)
    index+=1
output=encodebp(pa2ca(output))
pasteboard.set_string(output)
validitycheck(filedat,output)
print(len(nos(filedat)))
print(len(nos(output)))"""
