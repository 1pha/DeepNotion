from datetime import datetime

def today(option=None):
    today = datetime.today()
    fmt = lambda t: str(t).zfill(2)

    if option is None:
        return f'{today.year}.{fmt(today.month)}.{fmt(today.day)}.{fmt(today.hour)}:{fmt(today.minute)}'
    
    elif option=='kor':
        return f'{today.year}년 {today.month}월 {today.day}일'

    elif option=='eng':
        return f'{today.month} {today.day}, {today.year}'