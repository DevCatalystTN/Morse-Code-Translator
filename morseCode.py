from time import sleep
from gpiozero import LED

morseCode = { 
    'A': (0,1),
    'B': (1,0,0,0),
    'C': (1,0,1,0),
    'D': (1,0,0),
    'E': (0,),
    'F': (0,0,1,0),
    'G': (1,1,0),
    'H': (0,0,0,0),
    'I': (0,0),
    'J': (0,1,1,1),
    'K': (1,0,1),
    'L': (0,1,0,0),
    'M': (1,1),
    'N': (1,0),
    'O': (1,1,1),
    'P': (0,1,1,0),
    'Q': (1,1,0,1),
    'R': (0,1,0),
    'S': (0,0,0),
    'T': (1,),
    'U': (0,0,1),
    'V': (0,0,0,1),
    'W': (0,1,1),
    'X': (1,0,0,1),
    'Y': (1,0,1,1),
    'Z': (1,1,0,0),
    '1': (0,1,1,1,1),
    '2': (0,0,1,1,1),
    '3': (0,0,0,1,1),
    '4': (0,0,0,0,1),
    '5': (0,0,0,0,0),
    '6': (1,0,0,0,0),
    '7': (1,1,0,0,0),
    '8': (1,1,1,0,0),
    '9': (1,1,1,1,0),
    '0': (1,1,1,1,1)
    }
    
    
timeUnit = 0.15
led = LED(21)


string = input("Please enter a message: ")
sleep(timeUnit * 4)
for char in string:
    
    if char.upper() in morseCode:
        c = morseCode[char.upper()]
        for dash in c:
            led.on()
            if dash:
                sleep(timeUnit * 3)
            else: sleep(timeUnit)
            led.off()
            sleep(timeUnit)
        sleep(timeUnit * 2)
    elif char == ' ': sleep(timeUnit * 7)
    
    
    
    
    