
#game Stone paper sissor


import random
Username=input('Enter your name:')
Username=Username.upper()
score=0
stat='win'
while stat=='win':
    
           print('****************************')   
           user=input('rock ,paper or sissor:')
           com=random.choice(['rock','paper','sis'])
           if user == com:
              print('Computer:{} __User:{}\nTRY AGAIN'.format(com,user))

              continue
           elif user=='rock':
               
              
               if com=='paper':
                  stat='lose'
                  print('Computer:{} __User:{}'.format(com,user))
                  print('You '+stat +' ' +Username)
                
               else:
                  stat='win'
                  score+=1
                  print('Computer:{} __User:{}'.format(com,user))
                  print('You '+stat +' ' +Username)
                
           elif user =='paper' :
               if com=='rock':
                  stat='win'
                  score+=1
                  print('Computer:{} __User:{}'.format(com,user))
                  print('You '+stat +' ' +Username)
               else:
                  stat='lose'
                  print('Computer:{} __User:{}'.format(com,user))
                  print('You '+stat +' ' +Username)
           elif user=='sis':
               if com=='rock':
                  stat='lose'
                  print('Computer:{} __User:{}'.format(com,user))
                  print('You '+stat +' ' +Username)
               else:
                  stat='win'
                  score+=1
                  print('Computer:{} __User:{}'.format(com,user))
                  print('You '+stat +' ' +Username)
           else:pass
print('Game over:')
print(Username +' Your score is :{}'.format(score))
                
                
                
