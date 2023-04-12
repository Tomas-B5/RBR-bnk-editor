
from matplotlib import pyplot as plt
from bank_names import bank_names
def render(coords):
    # plot each box
    for i, box in enumerate(coords):
        # extract corner coordinates
        x1, x2, x3, x4, y1, y2, y3, y4 = box[1:]
        y1=abs(y1 -1)
        y2=abs(y2 - 1)
        y3=abs(y3 - 1)
        y4=abs(y4 - 1)
        # create box polygon
        #(x1, y1)--------(x2, y2)
        #
        #
        #
        #(x3, y3)--------(x4, y4)
        poly = plt.Polygon([(x1, y1), (x2, y2), (x4, y4), (x3, y3)], fill=None, edgecolor='r')

        # add box polygon to plot
        plt.gca().add_patch(poly)
        plt.text(x1, (y2+y4)/2, bank_names[i], color='black', fontsize=7)

    # show plot
    plt.axis('scaled')
    plt.show()
    