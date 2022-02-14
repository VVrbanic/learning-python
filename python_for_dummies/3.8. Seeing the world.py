#zašto kada mjenjamo varijavlu za stalno moramo prvo izvršiti naredbu pa tek onda printati varijablu?

coun=['japan', 'thailand', 'island', 'australia', 'vietnam']

print(coun)
print(sorted(coun))
print(coun)

coun.reverse()
print(coun)

coun.reverse()
print(coun)

coun.sort()
print(coun)

coun.sort(reverse=True)
print(coun)