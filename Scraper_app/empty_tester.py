import re

item = {
    'data': 'Python',
    'replace': ('P', "D")
}

def replace_text(item):
    
    replace_setting = item['replace']
    
    if replace_setting:
        pattern, repl = replace_setting
        item['data'] = re.sub(pattern, repl, item['data'])
    
    # print(item['data'])
    
    return item

print(replace_text(item))