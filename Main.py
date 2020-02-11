def step1():
    print('Привет, '+uname+'. Я хочу сыграть с тобой в игру! '                           
    'Утка-маляр решила погулять.'
    'Взять ей зонтик?')
    option=''
    options={'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option=input()
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print('Отличный выбор - ведь там сильный ливень. '
          'Теперь выбери, куда утке пойти гулять'
          )
    option=''
    options={'кино': True, 'кофейня': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option=input()
    if options[option]:
        return step3_movie()
    return step3_cafe()

def step2_no_umbrella():
    print('Там ливень, утка промокнет :('
          'Она возьмет такси или пойдет пешком?'
          )
    option=''
    options={'такси': True, 'пешком': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option=input()
    if options[option]:
        return step3_company()
    return step3_final()


def step3_final():
    print('Дождь и пешком? утка обиделась - game over')

def step3_movie():
    print('Но утка старая и плохо видит, она обиделась и остается дома.. '
          'game over'
          )


def step3_cafe():
    print('Отлично! это именно то, о чем мечтала утка :)')

def step3_company():
    print('На такси можно и без зонта:)'
          )
    return step2_umbrella()

uname=input("Привет! как тебя зовут?"
            "")


if __name__ == '__main__':
    step1()
