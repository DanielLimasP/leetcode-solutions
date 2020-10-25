def rotate_image(image):
    l = len(image) 
    for i in range(l // 2):  # layer
        k = l - i - 1
        for r in range(i, l - i - 1):  # offset in layer
            j = l - r - 1
            image[r][i], image[k][r] = image[k][r], image[r][i]
            image[k][r], image[j][k] = image[j][k], image[k][r]
            image[j][k], image[i][j] = image[i][j], image[j][k]

if __name__ == "__main__":
    image = [[1,2,3],[4,5,6],[7,8,9]]
    rotate_image(image)
    for i in image:
        print(i)
    
    image = [[1]]
    rotate_image(image)
    for i in image:
            print(i)

    image = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    rotate_image(image)
    for i in image:
        print(i)

