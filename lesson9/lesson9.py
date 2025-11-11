import os
import random
import csv
def save_csv(s,filename):
    fieldnames = s[0].keys()
    current_dir = os.path.dirname(os.path.abspath("__file__"))
    file_path = os.path.join(current_dir,'assets',filename)

    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for d in s:
            writer.writerow(d)
def getnames(file_names):
    current_dir = os.path.dirname(os.path.abspath("__file__"))
    file_path = os.path.join(current_dir,'assets',file_names)


    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content.split('\n')
def get_scores(names,num=10):
    l=random.sample(names,num)
    scores=[]
    for n in l:
        s={'姓名':n,
            '國文':random.randint(50,100),
            '數學':random.randint(50,100),
            '英文':random.randint(50,100)
            }
        scores.append(s)
    return scores
names=getnames('names.txt')
num=int(input('請輸入學生數量'))
scores=get_scores(names,num)
save_csv(scores,'學生.csv')
#print("\n".join(str(item) for item in scores))

