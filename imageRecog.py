import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pyautogui
from os import remove

from mapleFont import *


def saveWindow(directory):
    pyautogui.screenshot(directory, region=pyautogui.locateOnScreen('image\AHWindow.png', confidence=0.8))


def splitImage(directory):
    images = []

    raw = mpimg.imread(directory)
    remove(directory)

    for i in range(9):
        images.append(raw[204+55*i:258+55*i, 276:1007])

    return images



def getData(img):

    # Apply black/white filter for ease of read
    brightnessThreshold = .25
    for row in img:
        for pixel in row:
            if ((pixel[0] + pixel[1] + pixel[2])/3 < brightnessThreshold):
                pixel[0] = 0
                pixel[1] = 0
                pixel[2] = 0
            else:
                pixel[0] = 1
                pixel[1] = 1
                pixel[2] = 1


    # Crop down image to only the area with price (given by where parentheses are)
    numStart = -1
    for pixel in range(200, len(img[35])):
        if img[35][pixel][0] == 1:
            numStart = pixel
            break
    numEnd = -1
    for pixel in range(len(img[35])-150, 0, -1):
        if img[35][pixel][0] == 1:
            numEnd = pixel+1
            break
        

    # Crop down, and offset for parentheses
    cropped = img[18:43, numStart+4:numEnd-4]


    # Loop through first number
    black = False
    xOffset = 0
    totPrice = ''

    while not black:
        black = True

        # Skip over commas
        if cropped[9][xOffset][0] == 1:
            xOffset += 3

        # Find which number current position matches and add it to a string
        for num in range(10):
            correct = True
            for y in range(9):
                for x in range(5):
                    
                    # If it doesn't match the numbers in font
                    if not cropped[y][xOffset+x][0] == numbers[num][y][x]:  
                        correct = False
                    # If image isn't all black
                    if cropped[y][xOffset+x][0] == 1:
                        black = False
                
                # Exit loop if we already found a mistake
                if not correct:         
                    break
            
            # Append the correct digit to the answer
            if correct:                 
                totPrice += str(num)
                break

        # Move to next number
        xOffset += 7    


    # Loop through second number
    black = False
    xOffset = 4
    price = ''
    width = len(cropped[0])-1

    while not black:
        black = True

        # Skip over commas
        if cropped[9][width-xOffset+4][0] == 1:
            xOffset += 3

        # Find which number current position matches and add it to a string
        for num in range(10):
            correct = True
            for y in range(9):
                for x in range(5):
                    
                    # If it doesn't match the numbers in font
                    if not cropped[y][width-xOffset+x][0] == numbers[num][y][x]:  
                        correct = False
                    # If image isn't all black
                    if cropped[y][width-xOffset+x][0] == 1:
                        black = False
                
                # Exit loop if we already found a mistake
                if not correct:         
                    break
            
            # Append the correct digit to the answer
            if correct:                 
                price = str(num) + price
                break

        # Move to next number
        xOffset += 7


    print('Total price: ' + totPrice)
    print('Price per item: ' + price)
    print('Items for sale: ' + str(int(totPrice)//int(price)))



if __name__ == '__main__':
    # getData('./test3.png')
    saveWindow('image\scrnsht.png')
    images = splitImage('image\scrnsht.png')

    for image in images:
        getData(image)