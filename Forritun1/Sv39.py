# Skilaverkefni 38
# Tryggvi Ólafsson
# 0407042990

import math

def main():
    
  
 farenheit = [62, 61, 60, 64, 71, 73, 68, 64, 61]
 
 """
 farenheit = [66, 64, 60, 61, 63, 63, 68, 70, 71]
"""
 lenght = len(farenheit)
 celcius = []
 for x in range(lenght):
    num = round(((farenheit[x]-32)*5/9))
    
    celcius.append(num)

 print(farenheit)
 print(celcius)


    

        


        

    
if __name__ == "__main__":
    main()