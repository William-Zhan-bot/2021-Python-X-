# 建立使用者帳戶
# 帳戶要 1.8位數以上(包含8) 2.開頭必須為英文字母 3.結尾不可為英文
# 設定失敗打印False 設定成功打印True
account = input()
if len(account) < 8:
    print(False)
else:
    if account[0] not in "abcdefghijklmnopqrstuvwxyz":
        print(False)
    else:
        if account[len(account)-1] in "abcdefghijklmnopqrstuvwxyz":
            print(False)
        else:
            print(True)