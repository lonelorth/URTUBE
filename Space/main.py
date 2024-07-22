def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
        return
    inner_function() # Если отсутствует, то ничего не выводится
    return
# inner_function() - Ошибка поиска inner_function()
# test_function() - выводит print