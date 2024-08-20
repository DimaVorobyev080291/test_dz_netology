def check_age(age: int):
    """Проверка на возрост."""
    if  age >= 18 :
        result = 'Доступ разрешён'
    else:
        result = 'Доступ запрещён'

    return result


def check_email(email: str) -> bool:
    """ Проверка email на корректность , если в нём есть символ @ и точки."""
    if  "@" in email and "." in email:
        if " " in email:
            return False 
        else:
            return True
    else :
        return False 
    

def distance_traveled(hare_distances: list, turtle_distances: list):
    """Подсчитаем кто из животных прошел большие растояние."""
    hare_all = 0 
    for i in hare_distances :
        hare_all += i 
    turtle_all = 0 
    for i in turtle_distances : 
        turtle_all += i 
    if hare_all > turtle_all :
        result = "заяц"
    elif hare_all < turtle_all:
        result = "черепаха"
    else:
        result = "одинаково"
    return result