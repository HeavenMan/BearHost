

def BubbleSort(s):
    for i in range(len(s)):
        max=-1;
        maxindex=0;
        jlen = len(s)-i
        for j in range(jlen):
            if s[j]>max:
                max = s[j]
                maxindex = j
        temp = s[jlen-1]
        s[jlen-1] = max
        s[maxindex] = temp

if __name__ =="__main__":
    s = [34,2,3,41,22,12,32]
    BubbleSort(s)
    print(s)