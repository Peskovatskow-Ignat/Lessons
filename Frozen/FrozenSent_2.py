"""
Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое.
75 семей выписывают газету, 27 - журнал, 13 - и журнал, и газету.
Даны списки семей в квартирах.
Используя операции со множествами вычислите колько семей живёт в доме N.
"""
newspaper = range(1, 76)
magazine = range(77, 104)
both = range(21, 34)

newspaper1 = set(newspaper)
magazine1 = set(magazine)
both1 = set(both)

print(len(newspaper1) ^ len(magazine1))
print(len(newspaper1) | len(magazine1))