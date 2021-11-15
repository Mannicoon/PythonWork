text = input("Sisesta nimi: ")
text = text.strip()
print("Teie sisestatud sõna või laue on:", text)

if len(text) >= 7 and len(text) % 2 != 0:
    i = int(len(text) / 2)
    print("Sõna või lause on pikkem kui 7 sümbolit")
    print(text[i-1], text[i], text[i+1])