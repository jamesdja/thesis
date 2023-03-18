import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob
hl = 0
start_point = (0, hl)


def imshow(title = "test", image = None, size = 10):
    w, h = image.shape[0], image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize=(size * aspect_ratio,size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()


def region_of_interest(img, vertices):
    """
    Applies an image mask.

    Only keeps the region of the image defined by the polygon
    formed from `vertices`. The rest of the image is set to black.
    `vertices` should be a numpy array of integer points.
    """
    # defining a blank mask to start with
    mask = np.zeros_like(img)

    # defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    if len(img.shape) > 2:
        channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255

    # filling pixels inside the polygon defined by "vertices" with the fill color
    cv2.fillPoly(mask, vertices, ignore_mask_color)

    # returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

image = cv2.imread('distance-4.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use canny edge detection
#sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)
#edges = cv2.Laplacian(gray,cv2.CV_8UC1)
edges = cv2.Canny(gray, 10, 20, apertureSize=3)

vertices = np.array([[(400, image.shape[0]), (600, 50), (600, 50), (850, image.shape[0])]])
print(vertices)
ROI_image = region_of_interest(edges, vertices)

# Apply HoughLinesP method to
# to directly obtain line end points
lines_list = []
lines = cv2.HoughLinesP(
    ROI_image,  # Input edge image
    1,  # Distance resolution in pixels
    np.pi / 180,  # Angle resolution in radians
    threshold=90,  # Min number of votes for valid line
    minLineLength=20,  # Min allowed length of line
    maxLineGap=40 # Max allowed gap between line for joining them
)

# Iterate over points
for points in lines:
    # Extracted points nested in the list
    x1, y1, x2, y2 = points[0]
    #print(lines)
    # Draw the lines joing the points
    # On the original image
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    # Maintain a simples lookup list for points
    lines_list.append([(x1, y1), (x2, y2)])
#
# # Save the result image
# #cv2.imwrite('detectedLines.png', image)


imshow("test",ROI_image)
#imshow("test",edges)
imshow("test",image)