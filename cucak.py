print("cucak")

#sarking cucak dartak u guzenq erkarutyun@
lst = []
ellen = input("сколько элементов будет в списке? : ")
#amen andami hamar viklov uzum enq int
for i in range(0, int(ellen)):
    print("элемент номер", i, ": ", end="")
    el = input()
    # kpcnum enq
    lst.append(el)
# listi print@!
print(lst)
# ete ka grum enq vorerordn e
n = input("информацию о каком элементе получить?: ")
if n in lst:
    print("такой элемент есть. это элемент номер", lst.index(n))
else:
    print("такого элемента нет. ")
