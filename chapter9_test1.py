'''
寫一個function來找出清單中的最大數
'''
def find_max(a_list):
    # 首先我們要先檢查清單是不是空的
    if not a_list: # 請看底下講解
        return 0 # 既然是空的，我們就提早結束function, 回傳0
    max_num = a_list[0] # 先宣告一個變數出來儲存"目前看過的最大數"，先設成清單中的第一個東西
    for num in a_list: # 清單中的每一個東西，一個一個叫出來
        if num > max_num: # 如果此數字比目前最大數還大
            max_num = num # 那就把目前最大數變成此數字
    return max_num # 最後回傳看過的最大數


print(find_max([1, 3, 8, 9]))