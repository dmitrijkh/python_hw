#!/usr/bin/python3


def polska(user_input):
  operations = ['+', '-', '*', '/']
  operand, num1, num2 = user_input.split()
  num1 = int(num1)
  num2 = int(num2)
  if operand == '+':
    return print(num1 + num2)
  elif operand == '-':
    return print(num1 - num2)
  elif operand == '/':
    return print(num1 / num2)
  elif operand == '*':
    return print(num1 * num2)
  assert operand in operations
  

def operation():
  while True:
    inp = input('Введите пример: ')
    if inp == 'exit':
      print('Работа закончена')
      break
    else:
      try:
        polska(inp)
      except ZeroDivisionError:
        print ('Деление на ноль')
      except ValueError:
        print('Неправильное одно из чисел')
      except TypeError:
        print('Нельзя производить операции со строками')

operation() 