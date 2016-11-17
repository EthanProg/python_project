import pickle

obj = {"a":1,"b":2,"c":3}

# 将obj持久化保存到文件中 tmp.txt
pickle.dump(obj, open("tmp.txt","wb"), True)

# 从 tmp.txt 中读取并恢复 obj 对象
obj2 = pickle.load(open("tmp.txt","rb"))

print(obj2)