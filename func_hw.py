#!/usr/bin/python3


documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
  {"type": "invoice", "number": "11-2"}
]

directories = {
'1': ['2207 876234', '11-2', '5455 028765'],
'2': ['10006'],
'3': []
}


def find_name(find_name_data):
  while True:
    number_input = input('Введите номер: ')
    for documents_item in find_name_data:
      if number_input in documents_item.values():
        return print(documents_item.get("name"))
    if number_input not in documents_item:
      print('Введён несуществующий номер!')


def find_place(find_place_data):
  while True:
    number_input = input('Введите номер: ')
    for key, value in find_place_data.items():
      if number_input in value:
        return print(key)
    if number_input not in value:
      print('Введён несуществующий номер!')

def person_list(person_list_data):
  for documents_item in person_list_data:
    a = documents_item.get('type')
    b = documents_item.get('number')
    c = documents_item.get('name')
    print(f'{a} "{b}" "{c}"')
    
def name_list(name_list_data):
  try:
    for name in name_list_data:
      print(name['name'])
  except KeyError:
    print('Здесь имя не задано')


def add_new():
  doc_type = input('Введите тип документа: ')
  doc_number = input('Введите номер документа: ')
  doc_name = input('Введите имя: ')
  dir_place = input('Введите номер полки: ')


  for key, value in directories.items():
    if dir_place == key:
      value.append(doc_number)
      documents.append(dict(type=doc_type, number=doc_number, name=doc_name))
  
  if dir_place not in directories.keys():
    return print('Введите правильный номер полки')


  print(f'Добавлен новый пользователь {documents[-1]}')
  print(f'Номер документа пользователя добавлен на полку {dir_place}')


def operation():
  while True:
    user_input = input('Введите команду: ')
    if user_input == 'p':
      find_name(documents)
    elif user_input == 's':
      find_place(directories)
    elif user_input == 'l':
      person_list(documents)
    elif user_input == 'a':
      add_new()
    elif user_input == 'n':
      name_list(documents)
    elif user_input == 'exit':
      print('Сеанс завершён. До свидания!')
      break
    else:
      print('Неверная команда! Повторите ввод')
  
operation()