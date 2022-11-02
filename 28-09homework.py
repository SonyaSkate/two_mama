from datetime import * 

def diary(date, write):
    da = timedelta(days=1)
    with open('diary.txt', 'w') as f:
        for i in write:
            f.write(str(date) + i + "\n")
            da += da
diary((1857, 3, 5), ('первый день','второй день', 'третий день', 'четвертый день'))