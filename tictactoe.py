win=0

list=[0,1,2,
      3,4,5,
      6,7,8]
def view():
    print('{} | {} | {} '.format(list[0],list[1],list[2]))
    print('----------')
    print('{} | {} | {} '.format(list[3],list[4],list[5]))
    print('----------')
    print('{} | {} | {} '.format(list[6],list[7],list[8]))
def cheak():
     global win
     if list[0]==list[1]==list[2]:
         win=1
         return '{} WINS '.format(list[0])
     elif list[3]==list[4]==list[5]:
         win=1
         return '{} WINS '.format(list[3])
        
     elif list[6]==list[7]==list[8]:
         win=1
         return '{} WINS '.format(list[6])
     elif list[0]==list[3]==list[6]:
         win=1
         return '{} WINS '.format(list[0])
     elif list[1]==list[4]==list[7]:
         win=1
         return '{} WINS '.format(list[1])
     elif list[2]==list[5]==list[8]:
         win=1
         return '{} WINS '.format(list[2])
     elif list[0]==list[4]==list[8]:
         win=1
         return '{} WINS '.format(list[0])
        
     elif list[2]==list[4]==list[6]:
         win=1
         return '{} WINS '.format(list[2])
     else:
         return 'DRAWS'
view()
print('USER 1 = x\nUSER 2 = o')
while win==0:
    usr1=int(input('Enter the location for x:'))
    usr2=int(input('Enter the location for o:'))
    if list[usr1] !='x' and list[usr1]!='o':
        list[usr1]='x'
    else:
        print('Enter x in another location:')
    if list[usr2]!='x'  and list[usr2]!='o':
        list[usr2]='o'
    else:
        print('Enter o another location:')
    view()
    print(cheak())

