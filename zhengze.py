import re
with open(r"C:\Users\linao\Desktop\language\EnglishTransformationEnum.txt", 'r+', encoding='utf-8') as f:
    file = f.read()
    print(file)
    patten = re.compile(', "(.*?)"\)', re.S)  # ×ªÒå·û \£¬
    items = re.findall(patten, file)
    print(items)