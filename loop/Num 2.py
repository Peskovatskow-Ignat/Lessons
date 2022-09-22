Game = input('Game - начать игру - ')
Game = Game.lower()
while Game != 'off':
    if Game == 'game':
        print('Отгадай число от 1 до 10')
        for Game in range(3):
            prikol = int(input('Число - '))
            if prikol == 5:
                print('Ты победил')
                break
            else:
                print('Попробуй ещё раз')
        Game = input('Game - начать игру (завршить - off) - ')
print('Спаасибо за Игру')