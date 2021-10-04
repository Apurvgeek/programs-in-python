#program t find hamming nmber 
def hamming(num):
    i = j = k =0
    i2=2 ; i3=3 ; i5=5 ;Next=1
   # hn=[1]*num
    hn[0]=1
    for n in range(1,num):
        Next=min(i2,i3,i5)
        hn[n]=Next
        if(Next==i2):
            i+=1
            i2=hn[i]*2
        if(Next==i3):
            j+=1
            i3=hn[j]*3
        if(Next==i5):
            k+=1
            i5=hn[k]*5
    return Next
no=int(input('enter the no upto which u want to get nth sequence: '))
hn=[1]*no
print('the',no,'th is ',hamming(no))
print('the sequence is ',hn)
