import random

def generate_stu()->list[int]:
    scores = []
    for _ in range(5):
        scores.append(random.randint(50,100))
    return scores

def getNames(num:int) -> list[str]:
    with open("names.txt",encoding="utf-8") as file:
        names = []
        for name in file:
            names.append(name.rstrip())
    return random.choices(names,k=num)

def save_csv_file(filename:str,data:list) -> bool:
    try:
        with open(filename,mode='w',encoding="utf_8",newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['姓名','國文','英文','數學','地理','歷史'])
            csv_writer.writerows(data)
    except:
        return False
    else:
        return True
    
    