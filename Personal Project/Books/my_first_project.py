books_2021 = ['The Power of Now', 'The lost Hero', 'The Son of Neptune', 'The Guest List', 'Mistborn 1 The Final Empire', 'The Midnight Library' , 'Mistborn 2 The Well of Ascension'  ]
dict_books = dict ()
count = 0
# want to put here, how many pages I read; for how long I read 'today',week and month; 
i = print('1 - Read \n2 - Name of the books that you read so far \n3 - How many Books do you read already so far')
ihand = input('Type it the number:')


try:
    iihand = int(ihand)

except:

    print('You have to type number of 1 to 3')
    exit()
if iihand == 1:
    ri = input('How many hours/minutes do you read? ') #read input
elif iihand == 2:

    print(books_2021)
elif iihand == 3:
    for book in books_2021:
        count = count + 1
    print(count)
