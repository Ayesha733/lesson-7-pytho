t= input(("Entre a sentence to find prominant word :"))
t=t.split()
BigWord =0

for wrd in t:
    lenw = len (wrd)
    if lenw>BigWord:
        BigWord = lenw

        for wrd in t :
            lenw =len (wrd)
            if lenw==BigWord:
                print("largest Word: ",wrd)