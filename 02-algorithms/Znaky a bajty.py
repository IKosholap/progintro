#Text: Kůň
#K  U+004B  1 B
#ů  U+016F  2 B
#ň  U+0148  2 B
#Znaků: 3, bajtů: 5

text = input("Text: ")
pocet_bajty = 0
for i in text:
    unicode_code = ord(i)
    
    code = i.encode("utf-8")
    bajty_znaku = len(code)

    pocet_bajty += bajty_znaku

    print(f"{i} {unicode_code:04X} {bajty_znaku}B")
print (f"Znaků: {len(text)}, bajtů: {pocet_bajty}")