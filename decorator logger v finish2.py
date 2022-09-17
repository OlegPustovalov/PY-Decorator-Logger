import datetime

def logger (path_):
    def logger1 (func):
        def logger2(*args):
            now = datetime.datetime.now()
            result = func(*args)
            s_data_time = str(now)+'\n'
            s_name = str(func)+'\n'
            s_result = str(result)+'\n'
            print(s_data_time)
            print(f'Имя функции: {s_name}')
            print('Аргументы функции:')
            s_args = ''
            for st in args:
                s_args = s_args + str(st)+ ';'
                print(st)
            s_args = s_args + '\n'
            print(f'Возвращаемое значение функции: {s_result}\n')
#создание файла логга в нужной директории
            with open(path_,'w') as document:
                document.write(s_data_time)
                document.write('Имя функции: \n')
                document.write(s_name)
                document.write('Аргументы функции: \n')
                document.write(s_args)
                document.write('Возвращаемое значение функции: \n')
                document.write(s_result)
            return s_result
        return logger2
    return logger1



@logger('D:\\Олег\\0 Python\\script\\log.txt')
#Функция преобразования строки инградиента в словарь
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }
    dict_={}
    list_2 = []
    for name_dishes in dishes:
        for name,list_ingrad in cook_book.items():   
            if name == name_dishes: 
                list_2 = list_2 + list_ingrad         
    for dict_ in list_2:
        dict_['quantity'] = dict_['quantity'] * person_count 
    return list_2

list_zakaz = get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2)  
print (' ->', list_zakaz)
