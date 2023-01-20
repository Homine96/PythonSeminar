import input_data
import write_data
# import new_write
import output_data
# import output_name


# n=input('''Привет!
# Если вы хоитте записаться в телефонную книгу, то нажмите - 1!
# Если вы хотите посмотреть, контакты телефонной книги нажмите - 2!
# Если вы хотите видеть только Имя и Фамилию контакта , нажмите-3!
# ''')

def vybor(n):
    # write_data.get_write_data()
    if n == '1':
        return write_data.get_new_write(input_data.get_input_data())
    elif n == '2':
        return output_data.get_output_data()
    elif n == '3':
        return output_data.get_output_name()