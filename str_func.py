

def func_upper(text: str):
    """"Функция делающая первые буквы заглавными"""
    return text.upper()


def func_title(text: str):
    """Функция преобразовывающая все буквы в заглавные """
    return ' '.join([x.title() for x in text.split(' ')])
