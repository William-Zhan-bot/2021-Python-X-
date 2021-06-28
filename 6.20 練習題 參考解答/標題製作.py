# 標題製作

# 英文字母當成標題的時候 開頭的字母必須是大寫 
# 寫一個可以轉換標題然後輸出的函式吧

def title_maker(word):
    w = []
    for i in range(len(word)):
        if i == 0:
            w.append(word[i].upper())
        else:
            w.append(word[i])
    result = "".join(w)
    return result

i = input()
i = i.split(" ")
box = []
for q in range(len(i)):
    box.append(title_maker(i[q]))
result = " ".join(box)
print(result)