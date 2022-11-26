sentence=str(input("Enter a sentence: "))
l=sentence.split()
ACRONYM=""
for i in l:
    s=i[0]
    ACRONYM+=s
ACRONYM=ACRONYM.upper()
print(ACRONYM)    