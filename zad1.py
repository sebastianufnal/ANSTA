def postCodes(string1, string2):
    firstCode=list(string1)
    secondCode=list(string2)
    Codelist = []


    while(firstCode[0]!=secondCode[0] or firstCode[1]!=secondCode[1] or firstCode[3]!=secondCode[3] or firstCode[4]!=secondCode[4] or firstCode[5]!=secondCode[5]):
      firstCode[5] = str(int(firstCode[5])+1)
      if(firstCode[5]=="10"):
           firstCode[4] = str(int(firstCode[4])+1)
           firstCode[5] ="0"
           if(firstCode[4]=="10"):
             firstCode[3] = str(int(firstCode[3])+1)
             firstCode[4] ="0"
             if(firstCode[3]=="10"):
               firstCode[1] = str(int(firstCode[1])+1)
               firstCode[3] ="0"
               if(firstCode[1]=="10"):
                    firstCode[0] = str(int(firstCode[0])+1)
                    firstCode[1] ="0"
      Codelist.append(''.join(firstCode))
    return(Codelist)
print(postCodes("79-900","80-155"))