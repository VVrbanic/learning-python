from collections import Counter


def checkio(text):
    alfa= "abcdefghijklmnoqprwxyz"
    alfa_list= ["a","b","c","d","e","f","g","h","i","j,","k","l","m","n","o","q","p","r","w","x","y","z"]
    #lowercases
    text = text.lower();
    #sortirati_po_abecedi
    text=sorted(text);
    for i in range (0, len(text)):
        if text[i] not in alfa_list :
            del text[i]
    #vratiti_u_string
    text="".join(text);
    #obrnuti_abecedu
    text= text [::-1];
    najvise = Counter(text).most_common()
   
    for i in range (1, len(najvise)):
        if najvise[i][0] not in alfa:
           next
        elif najvise[i][1] == najvise[i+1][1]:
            najvise=sorted(najvise)
            a=najvise[i][0]  
        
    print(a)