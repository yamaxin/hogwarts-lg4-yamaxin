# 定义life类
class Life:
    animal = 'cat'
    flower = 'F4'

    def fav_book(self):
        book = 'Gone with the wind'
        print(f'my favourite book is {book}')
        heroine = 'Scarlett'
        male_leading = 'Rhett Butler'
        print(f'{heroine} love {male_leading}')

life = Life()
print(life.animal)
print(life.flower)
life.fav_book()


