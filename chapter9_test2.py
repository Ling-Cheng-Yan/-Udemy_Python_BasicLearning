'''
寫一個function來印出誰的成績是第二高，如果超過一個人的分數是第二高，請把人名一行一行印出來。
'''
def second_highest(students):
    grades = [s[1] for s in students] # 只把成績拿出來
    grades = sorted(grades, reverse=True)
    second = grades[1] # grades[0]是最高，grades[1]是第二高
    
    # 再下來找誰是這個分數
    # 底下這句話的意思是拿到 所有分數跟第二高一樣的人的"人名"也就是s[0]的部分
    # 記得嗎 參數的這個students清單裡面的東西，s[0]是人名，s[1]是分數
    second_high_students = [s[0] for s in students if s[1] == second]
    for student in second_high_students:
        print(student)




second_highest([['Terry', 84], ['Allen', 90], ['Peter', 84]])