import math
""" 
CSC221
M1T1_Buckwell
Goal : Gold
Author: William Buckwell
A program to determine if you can get a fishing pole on a bus that only allow packages of 4 feet.
"""
def main():
    
    tryAgain = 'y'
    
    while tryAgain == 'y':
        ShowMenu()
        tryAgain = input('Try another pole Y/N? =>')
        tryAgain = tryAgain.lower()
        
def ShowMenu():
    ''' This Function will display a menu for the user to choose whether determine if they
        can get a fishing pole on the bus or to exit the program. '''
    
     answer = 'd'     
     print('(D)etermine if you can tranport pole on bus?')
     print('(E)xit program.')
     answer = input('(D/E) => ')
     answer = answer.lower()

     if answer == 'd':
         print('Lets determine if you can delever the pole.')
         print('')
         poleLength = int(input('What is the length of the pole in feet? => '))
         CalculateData(poleLength)
     else:
         exit()

def CalculateData(poleLength):
    ''' This Function uses the math lib and uses the Pythagorean formula to determine the size
        of a box the user would need for the pole '''

    knownSide = 4

    if poleLength <= 4:
        ShowResult(poleLength, 0)
    else:
        secondSide = pow(poleLength, 2) - pow(4, 2)
        secondSide = math.sqrt(secondSide)
        ShowResult(poleLength, secondSide)

def ShowResult(poleLength, boxWidth):
    ''' If the pole is shorter the 4 feet then the is no problem. If any side of the box is
        greater the 4 feet the the user can not get the pole on the bus. '''

    if boxWidth == 0:
        print('Your pole will fit in a box that is %d foot tall' %(poleLength))
        print('You can get the pole on the bus!')
    elif boxWidth > 4:
        print('The width of the box is %d feet, with is more then 4 feet.' % (boxWidth))
        print('You can not get the pole on the bus!')
    else:
        print('The box to get the pole on the bus would be 4 foot tall and %d feet wide.' % (boxWidth))
        print('You can get the pole on the bus!')
        
main()
