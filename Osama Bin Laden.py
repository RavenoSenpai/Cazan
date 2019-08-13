from random import choice

pics=['''
=========||
    |    ||
         ||
         ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
         ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
    |    ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|    ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|\   ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|\   ||
   /     ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|\   ||
   / \   ||
         ||
         || ''',
]

word_list =['bakugan','subcarpati','ceausescu','negro','hipermetropie','raluca','ralkatraz']

def extrage_cuv():
     return choice(word_list)


def play_game():
     cuv = extrage_cuv()
     litere_ghicite = []
     how_dead_am_i = 0

     while how_dead_am_i < len(pics) - 1:
         print(pics[how_dead_am_i])

         castigat = True
         for ch in cuv:
             if ch in litere_ghicite:
                 print(ch, end='')
             else:
                 print('_', end='')
                 castigat = False

         print()

         if castigat:
             print("Felicitari! AI LUAT MOSTENIREA LU BUNATA")
             break

         letter = input("Zi in plm ceva")
         if letter in cuv and letter not in litere_ghicite:
             litere_ghicite.append(letter)
         else:
             how_dead_am_i += 1

     if not castigat:
         print(pics[how_dead_am_i])
         print("Ai dat coltu si te-au injunghiat doi baieti. Ce faci... Nu faci nimic ca esti mort")


play_game()