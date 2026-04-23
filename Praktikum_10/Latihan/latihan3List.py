
#soal 3
print("="*25)
print("     Soal nomor 3")
print("="*25)

stackku3 = []

stackku3.append('https://www.youtube.com/')
stackku3.append('https://www.w3schools.com/python/python_dsa_stacks.asp')
stackku3.append('https://www.assettoworld.com/')

print (f"Stack: {stackku3}")

topSur = stackku3 [-1]
print (f"Peek: {topSur}")

popop = stackku3.pop()
print (f"Pop: {popop}")

print(f"Back: {stackku3.pop()}")

print (f"Stack setelah pop: {stackku3}")

Empty = not bool(stackku3)
print(f"Stack's Empty: {Empty}")

print(f"Size: {len(stackku3)}")