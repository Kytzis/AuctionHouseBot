def getData(directory):
    import matplotlib.image as mpimg
    import matplotlib.pyplot as plt

    brightnessThreshold = .3

    img = mpimg.imread(directory)

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

    plt.imshow(img)
    plt.show()



if __name__ == '__main__':
    getData('./test.png')