# student_solution.py

# ---------- ЗАДАНИЕ 1 ----------
def task1(s):
    # s — строка вида "подстрока1,подстрока2"
    # вернуть кортеж: (len(sub1) > len(sub2), sub1==sub2, sub2 in sub1)
    ...
s=input()
a,b=s.split(',',1)
a=a.strip()
b=b.strip()
print(len(a)>len(b))
print(a==b)
print(b in a)
# ---------- ЗАДАНИЕ 2 ----------
def task2(s):
    # s — любая строка
    # вернуть кортеж:
    # (s.strip(), len(s), s.count('a'), s.replace('a','@'), s.istitle())
    ...
s=input()
t=s.strip()
print(t)
print(len(t))
print(t.count('a'))
print(t.replace('a','@'))
print(t and t[0].isupper())
# ---------- ЗАДАНИЕ 3 ----------
def task3(s):
    # s — строка
    # вернуть кортеж: (без первого и последнего символа, каждый второй символ, строка.lower() в обратном порядке)
    ...
input_string=input()
a=down_tab_shift=input_string[1:-1]
b=down_tab_shift=input_string[::2]
c=down_tab_shift=input_string[::-1]
print(a)
print(b)
print(c)
# ---------- ЗАДАНИЕ 4 ----------
def task4(nums):
    # nums — список чисел
    # вернуть кортеж: (отсортированный список, сумма, (min, max))
    ...
s=input().strip()
nums=list(map(int,s.split()))
print(sorted(nums))
print(sum(nums))
print(min(nums),max(nums))

# ---------- ЗАДАНИЕ 5 ----------
def task6(s):
    # s — строка
    # вернуть True если палиндром (без учёта регистра) и нет пробелов, иначе False
    ...

# ---------- ЗАДАНИЕ 6 ----------
def task7(n):
    # n — целое число
    # вернуть кортеж: (hex(n) без '0x', len(hex), True если 'a' есть в hex)
    ...

# ---------- ЗАДАНИЕ 7 ----------
def task8(month_num):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # вернуть название месяца по номеру (1-12)
    ...
