y=int(input("**********  Number To Words Converter***********-\n\nEnter Number: ")) 
x,tyu=str(y),print("\n") 
import sys 
if int(x)>10**100 or int(x)<0:sys.exit("Range Is From Zero To One Googol!") 
def num1wrd(x,w={0:"",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"},f={2:"Twen",3:"Thir",4:"For",5:"Fif",6:"Six",7:"Seven",8:"Eigh",9:"Nine"},t={11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}): 
    if len(x)==1:return(w[int(x)]) 
    elif len(x)==2 and x[0]=="0" and x[1]=="0":return("") 
    elif len(x)==2 and x[0]=="0":return (w[int(x[1])]) 
    elif len(x)==2: 
        if int(x) in range(11,20):return(t[int(x)]) 
        elif int(x[1])==0: 
            if int(x)==10:return("Ten") 
            else:return(f[int(x[0])]+"ty") 
        else:return(f[int(x[0])]+"ty"+"-"+w[int(x[1])]) 
def hun_num(x,w1={0:"",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}): 
    if len(x)==3 and x[0]!="0" and x[1]=="0" and x[2]=="0": return(w1[int(x[0])]+" "+"Hundred") 
    elif len(x)==3 and x[0]!="0": 
        a1=(x[1]+x[2]) 
        return(w1[int(x[0])]+" "+"Hundred "+"and "+num1wrd(a1)) 
    elif len(x)==3 and x[0]=="0": return(num1wrd(x[1]+x[2])+" ") 
    else: return(num1wrd(x)) 
def seg3(s,out = []): 
    while len(s): 
        out.insert(0, s[-3:]) 
        s = s[:-3] 
    return out 
def q(x): 
    if x=="000":return(0) 
    elif x=="00":return(0) 
    elif x=="0":return(0) 
    else:return(1) 
aa,v={0:"",1:"Thousand",2:"Million",3:"Billion",4:"Trillion",5:"Quadrillion",6:"Quintillion",7:"Hextillion",8:"Septillion",9:"Octillion",10:"Nonillion",11:"Decillion",12:"Undecillion",13:"Duodecillion",15:"Quattuordecillion",16:"Quindecillion",17:"Hexdecillion",18:"Septdecillion",19:"Octodecillion",20:"Novemdecillion",21:"Vigintillion",14:"Tredecillion",22:"Unvigintillion",23:"Duovigintillion",24:"Trevigintillion",25:"Quattuorvigintillion",26:"Quinvigintillion",27:"Hexvigintillion",28:"Septvigintillion",29:"Octovigintillion",30:"Novemvigintillion",31:"Trigintillion",32:"Untrigintillion",33:"Duotrigintillion"},seg3(x) 
if int(x)==10**100: s="One Googol" 
elif int(x)==0: s="Zero" 
else: 
    s1="" 
    for i in range(len(v)):s1=s1+(hun_num(v[i]))+(" "+aa[len(v)-1-i]+", ")*q(v[i]) 
    s=s1[:len(s1)-3] 
    d="dollor"
print(""+s+" dollors") 

