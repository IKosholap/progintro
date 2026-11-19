#Věta: Jelen jede lesem
#e: 6
#j: 2
#l: 2
#d: 1
#m: 1
#n: 1
#s: 1
#Různých písmen: 7

text = input("Введіть речення: ").lower()


char_counts = {}
for char in text:
    if char.isalpha(): 
        char_counts[char] = char_counts.get(char,0) + 1

sorted_chars = sorted(char_counts.items(), key= lambda item: (-item[1]))


for char, count in sorted_chars:
    print(f"{char}: {count}")

print(f"Různých písmen: {len(char_counts)}")