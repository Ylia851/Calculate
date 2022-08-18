import algoritm

regim = algoritm.Interface()
res = algoritm.Calc()
primer = algoritm.meny()
def Output_Result():
    print(f'Вы выбрали режим {regim}')
    print(f'Введенный пример {primer}')
    print(f'Полученный результат {res}')

Output_Result()