
#Rock Paper Scissor Game
'''How to Play:- 1:Enter your Name 
2:enter your selection as:-[rock or paper or sic]
3:Score will be counted untill u lose the game '''

import random

Username=input('Enter your name:')
Username=Username.upper()
score=0
stat='win'

while stat=='win':
    
           print('****************************')   
           user=input('rock ,paper or sic:')
           com=random.choice(['rock','paper','sic'])
           if user == com:
              print('Computer:{} __User:{}\nTRY AGAIN'.format(com,user))

              continue
           elif user=='rock':
               
              #If user input rock then matching with computer selection
               if com=='paper':
                  stat='lose'
                  print('Computer:{} __User:{}'.format(com,user))
                  print('You '+stat +' ' +Username)
                
               else:
                  stat='win'
                  score+=1
                  print('Computer:{} __User:{}'.format(com,user))
                  print('You '+stat +' ' +Username)
            
            # If user input paper then matching with computer selection
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
                    
            #If user input sic then matching with computer selection
           elif user=='sic':
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
                
                
                
