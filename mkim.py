e2f =  {"dog":"chien", "cat":"chat", "walrus":"morse"}
print(e2f)
e2f_all = list(e2f.items())
f2e = dict([e2f_all[0][::-1], e2f_all[1][::-1], e2f_all[2][::-1]])
print(type(f2e))
print(f2e)
"""
e2f[::-1]は逆順にするという意味。スクラッチ
items()は辞書のキーとバリューを全て取得して
"""