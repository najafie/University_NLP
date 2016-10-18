import codecs
import re
#---------------------------Begin Tokenization Function ----------------------
#                   input: senternse  output: listtoken sentense
def Tokenization(sentense):
    token=""
    arrayToken=[]
    for i in range(0,len(sentense)):
        if((ord(sentense[i]) != 32) & (ord(sentense[i]) != 13)):
            token=token+sentense[i]
        else:
            if(len(token)>0):
                arrayToken.append(token)
                token="";
    if (len(token) > 0):
        arrayToken.append(token)
    token=""
    return  arrayToken
#---------------------------------End Tokenization Function------------------



def Normalization(sentens):
    sentens = sentens.strip()   # remove space from begin and end of sentense
    sentens = re.sub(' +', ' ', sentens)  # remove extra space
    sentens = re.sub('([\d+])\.([\d+])', r'\1/\2', sentens)  # replace dot with point
    sentens = re.sub(r'[ـ\r]', '', sentens)  # replace character keshide
    sentens = re.sub(r'[ۀ]', 'ه', sentens)  # change arabic character ۀ to ه
    sentens = re.sub(r'[أإ]', 'ا', sentens)  # change arabic character آأإ to ا
    sentens = re.sub(r'[ئي]', 'ی', sentens)  # change arabic character ي ئ to ی
    sentens = re.sub(r'[ك]', 'ک', sentens)  # change arabic character ك to ک
    sentens = re.sub(r'[ؤ]', 'و', sentens)  # # change arabic character ؤ to و
    sentens = re.sub(r'[‌]', ' ', sentens)  # change nim fasele to fasele
    #sentens = re.sub(r'[ًٌٍَُِّْ]', '', sentens)  # remove arabic elemnts (eerab)
    sentens = re.sub(r'[({}<>»«“]', '', sentens)  # remove non text character
    sentens = sentens.replace('[', '')  # change [ character ة to ه
    sentens = sentens.replace(']', '')  # change ] character ة to ه
    sentens = re.sub(r'[۰٠]', '0', sentens)  # change farsi charachter to finglish charachter 0
    sentens = re.sub(r'[۱١]', '1', sentens)  # change farsi charachter to finglish charachter 1
    sentens = re.sub(r'[۲٢]', '2', sentens)  # change farsi charachter to finglish charachter 2
    sentens = re.sub(r'[۳٣]', '3', sentens)  # change farsi charachter to finglish charachter 3
    sentens = re.sub(r'[۴٤]', '4', sentens)  # change farsi charachter to finglish charachter 4
    sentens = re.sub(r'[۵٥]', '5', sentens)  # change farsi charachter to finglish charachter 5
    sentens = re.sub(r'[۶٦]', '6', sentens)  # change farsi charachter to finglish charachter 6
    sentens = re.sub(r'[۷٧]', '7', sentens)  # change farsi charachter to finglish charachter 7
    sentens = re.sub(r'[۸٨]', '8', sentens)  # change farsi charachter to finglish charachter 8
    sentens = re.sub(r'[۹٩]', '9', sentens)  # change farsi charachter to finglish charachter 9
    return sentens


def Translation(sentens):
    sentens = re.sub(r'[َ]', 'a', sentens)  # change arabic character َ to a
    sentens = re.sub(r'[ُ]', 'o', sentens)  # change arabic character ُ to o
    sentens = re.sub(r'[ِ]', 'e', sentens)  # change arabic character ِ to e
    sentens = re.sub(r'[ّ]', '#', sentens)  # change arabic character ّ to sharp
    sentens = re.sub(r'[ً]', 'aN', sentens)  #  change arabic character ً to an
    sentens = re.sub(r'[ٌ]', 'oN', sentens)  #  change arabic character ٌ to on
    sentens = re.sub(r'[ٍ]', 'eN', sentens)  #  change arabic character ٍ to en
    sentens = re.sub(r'[ْ]', '×', sentens)  #  change arabic character saken to ×
    sentens = re.sub(r'[ء]', "'", sentens)  # change character hamze to '
    sentens = re.sub(r'[اأإ]', 'A', sentens)  # change farsi charachter to finglish charachter 
    sentens = re.sub(r'[آ]', '~', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ب]', 'b', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[پ]', 'p', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ت]', 't', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ة]', '@', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ث]', 'C', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ج]', 'j', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[چ]', 'c', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ح]', 'H', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[خ]', 'x', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[د]', 'd', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ذ]', 'D', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ر]', 'r', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ز]', 'z', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ژ]', 'J', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[س]', 's', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ش]', '$', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ص]', 'S', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ض]', 'X', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ط]', 'T', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ظ]', 'Z', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ع]', 'E', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[غ]', 'G', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ف]', 'f', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ق]', 'q', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[كک]', 'k', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[گ]', 'g', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ل]', 'l', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[م]', 'm', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ن]', 'n', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ۀه]', 'h', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[وؤ]', 'V', sentens)  # change farsi charachter to finglish charachter
    sentens = re.sub(r'[ئيی]', 'y', sentens)  # change farsi charachter to finglish charachter
    return sentens

ListToken=[]
sent=""
file = codecs.open('sent.txt' , 'r','utf-8')
line=file.read().splitlines()
sent = " ".join(line)
file.close()

print("Main Sentense: ",sent)
normalsent=Normalization(sent)
print("Normalization Sentense: ",normalsent)
translatesent=Translation(normalsent)
print("Translation Sentense: ", translatesent)

ListToken=Tokenization(translatesent)
print("Tokens Count: ",len(ListToken))

AllToken=""
for token in ListToken:
    AllToken=AllToken+'['+token+'], '

print("Tokenations Sentense: ", AllToken)

quit()