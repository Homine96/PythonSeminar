import view


dict_student = {}
students = []
lessons = []


def start():
    while True:
        op = view.operations()
        if op == 1:
            while True:
                name = view.add_student()
                if name not in students:
                    dict_student[name] = {}
                    students.append(name)
                    if lessons:
                        for less in lessons:
                            dict_student[name][less] = []
                print('-' * 20)
                exit = input('Нажмите 1, если хотите еще добавить студента \n'
                             'Нажмите 0, если хотите вернуться в главное меню \n')
                if exit == '1':
                    continue
                elif exit == '0':
                    break

        elif op ==2:
            while True:
                less=view.add_less()
                lessons.append(less)
                for k in dict_student:
                    dict_student[k][less]=[]
                print('-' * 20)
                exit = input('Нажмите 1, если хотите еще добавить предмет  \n'
                             'Нажмите 0, если хотите вернуться в главное меню \n')
                if exit == '1':
                    continue
                elif exit == '0':
                    break

        elif op == 3:
            while True:
                print('Перед вами представлен список учеников: ')
                for k, name in enumerate(students, 1):
                    print(k, name)
                print('Перед вами представлен список предметов: ')
                for k, less in enumerate(lessons, 1):
                    print(k, less)
                print('-'*20)
                view.add_mark_student(dict_student)
                print('-' * 20)
                exit = input('Нажмите 1, если хотите еще поставить оценку \n'
                           'Нажмите 0, если хотите вернуться в главное меню \n')
                if exit =='1':
                    continue
                elif exit == '0':
                    break

        elif op == 4:
            while True:
                for k, name in enumerate(students, 1):
                    print(k, name)
                print('-' * 20)
                exit = input('Нажмите 0, чтобы вернуться в главное меню \n')
                if exit == '0':
                    break

        elif op == 5:
            while True:
                view.out_mark_stdent(dict_student)
                print('-' * 20)
                exit = input('Нажмите 1, если хотите посмотреть оценки других учеников \n'
                             'Нажмите 0, если хотите вернуться в главное меню \n')
                if exit == '1':
                    continue
                elif exit == '0':
                    break
        elif op == 6:
            while True:
                view.sr_mark_student_less(dict_student)
                print('-'*20)
                exit = input('Нажмите 1, если хотите посмотреть ср.балл по предмету другого ученика \n'
                             'Нажмите 0, если хотите вернуться в главное меню \n')
                if exit == '1':
                    continue
                elif exit == '0':
                    break

        elif op == 7:
            while True:
                view.sr_mark_lessOnSchool(dict_student)
                print('-' * 20)
                exit = input('Нажмите 1, если хотите посмотреть средний балл по школе по другому предмету \n'
                             'Нажмите 0, если хотите вернуться в главное меню \n')
                if exit == '1':
                    continue
                elif exit == '0':
                    break


        elif op == 8:
            print('   До свидания!')
            break