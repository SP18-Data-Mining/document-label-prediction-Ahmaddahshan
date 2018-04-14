def diabetes(file):
    file=open(file,"r")
    file= file.read()
    bagofword = []
    List= file.split()
    
    stopwords=["use","can","the","not","of","also","to","an","and",
    "too","or","which","puts","more","is","in","you","such","be","he","she","are"]
    labels={"body":['eyes','kidney','stomach','heart'],
    "diabetes":['insulin','diabetic','prediabetes'], 
    "blood sugar" : ['glucose','sugar','diet','blood']}
    
    for word in List:
        if word not in stopwords:
             bagofword.append(word)
    outputLabel={}
    for word in bagofword:
        newWord=''
        for charInString in word:
               if(charInString==',' or charInString == '.' or charInString == '?'):
                     continue
               newWord=newWord + charInString
    count=0
    
    for word in bagofword:
           for labelKey in labels:
                 associatedToLabel= labels[labelKey]
                 if word in associatedToLabel:
                    if word in outputLabel.keys():
                           outputLabel[word][0] +=1
                    else:
                          data=[]
                          data.append(1)
                          data.append(labelKey)
                          entry={word:data}
                          outputLabel.update(entry)
                          count=count + 1
					   
    return count 

def compsci(file):
    text=open(file,"r")
    text=text.read()
    bagofword = []
    List=text.split()
    stopwords=["use","can","the","not","of","also","to","an",
    "and","too","or","which","puts","more","is","in","you",
    "such","be","he","she","are"]
    labels={"parts":['mother board','cpu','hard drive'],
    "computer science":['algorithm','mathematics','program','engineer','theory'], 
    "function":['communication','storage','database','processing','output','networking']}
    for word in List:
        if word not in stopwords:
             bagofword.append(word)
    outputLabel={}
    for word in bagofword:
        newWord=''
        for charInString in word:
               if(charInString==',' or charInString == '.' or charInString == '?'):
                     continue
               newWord=newWord + charInString
    count=0
    for word in bagofword:
          
           for labelKey in labels:
                 associatedToLabel= labels[labelKey]
                 if word in associatedToLabel:
                    if word in outputLabel.keys():
                           outputLabel[word][0] +=1
                    else:
                          data=[]
                          data.append(1)
                          data.append(labelKey)
                          entry={word:data}
                          outputLabel.update(entry)
                          count=count + 1
    return count 
def checkdiab(file,score):
    fp='FP'
    tp='TP'
    if file=='unlabeled-1.txt':
        return fp
    elif file=='unlabeled-2.txt':
        return fp
    elif file=='unlabeled-3.txt':
        return fp
    elif file=='unlabeled-4.txt':
        return fp
    elif file=='unlabeled-5.txt':
        return tp
    elif file=='unlabeled-6.txt':
        return fp
def checkcomp(file,score):
    fp = 'false positive'
    tp = 'true positive'
    if file=='unlabeled-1.txt':
        return tp
    elif file=='unlabeled-2.txt':
        return tp
    elif file=='unlabeled-3.txt':
        return tp
    elif file=='unlabeled-4.txt':
        return tp
    elif file=='unlabeled-5.txt':
        return fp
    elif file=='unlabeled-6.txt':
        return fp
def main(): 
    documents=['unlabeled-1.txt','unlabeled-2.txt','unlabeled-3.txt',
                'unlabeled-4.txt','unlabeled-5.txt','unlabeled-6.txt']
    for file in documents:
        diabcount = diabetes(file)
        cscount = compsci(file)
        score = cscount-diabcount
        if score >= 1:
           result=checkcomp(file,score)
           print (file,"computer science score=",score,result)
           print('\n\n')
        elif score < 1:
              score = abs(score)
              result = checkdiab(file,score)
              print (file, "diabetes file score=",score,result) 
        else:
            print("N/A")
main()          







