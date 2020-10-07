'''
寫一個function來做商品計數，function會接收一個data清單中裝著'麥香奶茶 2'這樣的字串，字串中空格分開商品名稱跟數量，
特別注意，商品名稱可以重複，重複時請把數量壘加上去計數。
''' 
def count_products(data):
    products = {}
    for d in data:
        name, count = d.split(' ') #name和count是字串
        count = int(count)
        if name in products:
            products[name] += count
        else:
            products[name] = count #新增key，並且賦予他value
    return products

print(count_products(['麥香奶茶 2', '綠茶 1', '麥香奶茶 2']))