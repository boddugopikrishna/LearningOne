import re
tran = "buy 10 shares at 5 each"
x = re.findall("[\d]+",tran)
print(x[0])
