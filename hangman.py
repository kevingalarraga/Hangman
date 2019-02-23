
import random

def hang():
  gallows = [',--;-', '| ', '| ', '| ', '| ', '| ', '|_____']
  parts = iter([' 0 ', '/', '|', '\\', ' | ', ' A ', '/ ', '\\'])
  sequence = [1, 3, 1, 1, 2]
  for i, v in enumerate(sequence, start=1):
    for k in range(v):
      gallows[i] += next(parts)
      yield '\n'.join(gallows)
  raise StopIteration


def word():
  with open('words.csv') as f:
    words= list(f)
    word_list=[word[:-1]for word in words if word== word.lower ]
    secret= random.choice(word_list)
    progress=['_' for letter in secret]
    print(progress)
    guess= input('chose a letter')
    if guess in secret:
      for idx,letter in enumerate(secret):
        if letter==guess:
          progress[idx]=guess
    else:
      word_bank=guess
      print(word_bank)
      f'(wrong letter)'
      next(hang)
    if guess==secret:
      f'(you win)'
    else:
      f'(keep going until you lose)'

  
