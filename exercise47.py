### Exercise 47 - Curso em Video
## Develop a program that shows a regressive count on screen for fireworks. From 10 to 0 with a 1 sec pause between them.

from time import sleep
import emoji

for f in range(10, 0, -1):
    print('{}...'.format(f))
    sleep(1)
print('HAPPY NEW YEAARRRR!!!')
print(emoji.emojize(':fireworks: :fireworks: :fireworks:'))
