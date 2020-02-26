import math
import numpy
import PIL.Image
from sklearn.cluster import MiniBatchKMeans
from model.image import Image as Image
from operator import itemgetter


def get_image_data(path: str) -> Image:
    n_clusters = 4

    imgfile = PIL.Image.open(path).convert('RGBA')
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
        colors.append(
            (
                math.ceil(clusters.cluster_centers_[j][0]),
                math.ceil(clusters.cluster_centers_[j][1]),
                math.ceil(clusters.cluster_centers_[j][2])
            )
        )

    return Image(colors)
