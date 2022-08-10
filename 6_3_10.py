#import sys
#lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['Главная home', 'Python learn-python', 'Java learn-java', 'PHP learn-php']
t = tuple([tuple(i.split(' ')) for i in lst_in])
print(t)