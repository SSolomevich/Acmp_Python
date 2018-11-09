import re




op = ['*', '/', '+', '-']
res = re.compile(r'\s*(\d+)\s*([+*\/-])\s*(\d+)\s*=\s*(\d+)\s*')  # не понимаю почему по группам не разбежались

if res.match(String):

   equality = res.findall(str)
   one = int(equality[0][0])  # костыль, после вернуться и исправить
   two = int(equality[0][2])  # разбить по группам
   res = int(equality[0][3])
   i = op.index(equality[0][1])

   if op[i] == '*':
       if one * two == res:
           print('YES')
       else:
           print('NO')
   elif op[i] == '/':
       if one / two == res:
           print('YES')
       else:
           print('NO')

   if op[i] == '+':
       if one + two == res:
           print('YES')
       else:
           print('NO')

   if op[i] == '-':
       if one - two == res:
           print('YES')
       else:
           print('NO')

else:
   print('ERROR')