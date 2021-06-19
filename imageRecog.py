import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def getData(directory):

    img = mpimg.imread(directory)

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
    for pixel in range(100, len(img[34])):
        if img[34][pixel][0] == 1:
            numStart = pixel
            break
    numEnd = -1
    for pixel in range(len(img[34])-100, 0, -1):
        if img[34][pixel][0] == 1:
            numEnd = pixel+1
            break

    # Crop down, and offset for parentheses
    cropped = img[16:42, numStart+2:numEnd-2]

    plt.imshow(cropped)
    plt.show()



if __name__ == '__main__':
    getData('./test.png')