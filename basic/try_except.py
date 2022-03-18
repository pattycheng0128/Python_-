# # 一般的例外處理try..except
# try:
#     num = input("請輸入一個數字:")
#     num = int(num)
#     total = num + 1
#     print(total)
# except ValueError:
#     print("發生錯誤")

# try..except..else..finally
try:
    num = input("Please input a number:")
    num = int(num)
    total = num + 1
    print(total)
except ValueError:
    print("請輸入數字:")
except:
    print("發生錯誤")
else:
    print("沒有發生任何錯誤時,會成功執行")
finally:
    print("程式結束")
