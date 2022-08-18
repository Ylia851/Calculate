import Interface
import meny
import loger
from rational_algoritm import Rational_calc
from complex_algoritm import Complex_calc

def Calc():
    regim = int(input(Interface.Interface()))
    print(regim)
    if regim == 1:
        print('Запущен режим для работы с рациональными числами')
        primer = input(meny.Input_Primer_Rat())
        loger.loger(primer)
        res = Rational_calc(primer)
        loger.loger(res)
        return regim    
    elif regim == 2:
        print('Запущен режим для работы с рациональными числами')
        primer = input(meny.Input_Primer_Compl())
        res = Complex_calc(primer)
        loger.loger(res)
        return regim
    elif regim == 3:
        print('Запущен режим вывода лога программы')
        n = loger.Loger()
        print(n)
    elif regim == 4:
        exit()
    else:
        print('Вы ввели некорректный режим! Введите один из предложенных вариантов: ')
Calc()

