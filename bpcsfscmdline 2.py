o=open("chrtk.txt",'r')
tempa='''{"n": "'''
tempb="""",
      "p": {
        "x": """
tempc=""",
        "y": """
tempd="""
      },
      "o": {
        "x": """
tempe=""",
        "y": """
tempf=""",
        "z": """
tempg="""
      }"""
mbasea='''
,"'''
mbaseb='''" :{
'''
mbaseen='''}'''
fangs='"'
mprend='": '
mend=""",
"""
#enter proc with psedocode
m=o.read().split('''
''')
thisdict =	{}
ast=""
for index in m:
    thisdict[ index[0]] = index.split("-")[1]
    c = index[0] +"="+index.split('-')[1]
    ast = ast+c+"""
    """
display = """enter a psedocode to create a bp syntax:keychar|xcord,ycord,xsize(default=1),ysize(default=1),rot(default=0),other attributes if possible()-(another part) keywords: 
    """+ast
print(display)
inp=input()
tsklist=inp.split('-')
print(tsklist)
processed = ""
i=0
end=''
more=""
for tsk in tsklist:
    i+=1
    xy=tsk.split("|")[1]
    print(xy)
    x=xy.split(",")[0]
    y=xy.split(",")[1]
    if len(xy.split(","))==2:
        xsize="1"
        ysize="1"
        rot="0"
        hasatt=False
    elif len(xy.split(",")) == 5:
        xsize=xy.split(",")[2]
        ysize=xy.split(",")[3]
        rot=xy.split(",")[4]
        hasattr=False
    elif len(xy.split(","))>5:
        xsize=xy.split(",")[2]
        ysize=xy.split(",")[3]
        rot=xy.split(",")[4]
        Attr=xy.split(",")
        print(Attr)
        hasattr=True
    else:
        print("Error cannot process:not correct amount of input")
    hh=0
    cou=0
    print(thisdict)
    attrcount=1
    for ptat in thisdict[ tsk[ 0]].split('.'):
        if (hasattr==True)and(len(ptat.split(':'))>1):
            print("first thread triggered")
            h=0
            preh=""
            for dicti in ptat.split(':'):
            
                if len(dicti.split(";"))==1:
                    hh+=1
                    h+=1
                    continue
                else:
                    hh+=1
                    cou+=1
                    h+=1
                    print(ptat)
                    
                    if not h == len(ptat.split(':')):
                        mends=mend
                    else:
                        mends='''
'''
                    print(cou+4)
                    preh = preh+fangs+dicti.split(';')[0]+mprend+Attr[cou+4]+mends
            more=more+mbasea+ptat.split(':')[0]+mbaseb+preh+mbaseen
                
        elif     len(ptat.split(':'))>1:
            print("secondary thread triggered")
            h=0
            preh=""
            for dicti in ptat.split(':'):
                
                if len(dicti.split(';')) == 1:
                    hh+=1
                    h+=1
                    continue
                else:
                    hh+=1
                    h+=1
                    if not h ==len(ptat.split(':')):
                        mends=mend
                    else:
                        mends='''
'''
                    print()
                    preh = preh+fangs+dicti.split(';')[0]+mprend+dicti.split(";")[1]+mends
            print(attrcount)
            more=more+mbasea+thisdict[tsk[0]].split(".")[attrcount].split(':')[0]+mbaseb+preh+mbaseen
            attrcount += 1
            
        else:
            more=""
    if not i==len(tsklist):
        end=','
    else:
        end=''
    processed += tempa+thisdict[tsk[0]].split('.')[0]+tempb+x+tempc+y+tempd+xsize+tempe+ysize+tempf+rot+tempg+more+tempg+end
output="""{
"parts":[
"""+processed+'''
]
}'''
print(output)
wr=open("Blueprint.txt",'w+')
wr.truncate(0)
wr.write(output)
wr.close()