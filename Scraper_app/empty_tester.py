import re

replace_lst = 'Heeey I"m txt To Be romved from chhccccc $'

txt = re.sub(r'[aBc$]', '', replace_lst)

print(txt)