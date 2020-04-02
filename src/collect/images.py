import os
import math
import numpy
import PIL.Image
from sklearn.cluster import MiniBatchKMeans
from operator import itemgetter

def is_picture(path: str) -> bool:
    return path.endswith(".png") or path.endswith(".jpg") or path.endswith(".jpeg")

def list_images(path: str) -> list:
    file_list = os.listdir(path)
    filtered_list = filter(is_picture, file_list)
    return list(filtered_list)

def get_image_colors(path: str) -> list:
    n_clusters = 4

    imgfile = PIL.Image.open(path).convert("RGBA")
    numarray = numpy.array(imgfile.getdata(), numpy.uint8)

    clusters = MiniBatchKMeans(n_clusters=n_clusters)
    clusters.fit(numarray)

    npbins = numpy.arange(0, n_clusters + 1)
    histogram = numpy.histogram(clusters.labels_, bins=npbins)

    # Sort histogram
    pairs = sorted(zip(histogram[0], histogram[1]), key=itemgetter(0))
    histogram = (numpy.array([v for v, i in pairs]),
                 numpy.array([i for v, i in pairs]))

    colors = []

    for i in range(n_clusters):
        j = histogram[1][i]

        red = math.ceil(clusters.cluster_centers_[j][0])
        green = math.ceil(clusters.cluster_centers_[j][1])
        blue = math.ceil(clusters.cluster_centers_[j][2])

        rgb = red
        rgb = (rgb << 8) + green
        rgb = (rgb << 8) + blue

        colors.append(rgb)

    return colors