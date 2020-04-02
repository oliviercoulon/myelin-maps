from soma import aims
import numpy as np


def projectOnSurface(myelin, surface):

    return surfMap


def main(arguments):
    if len(arguments)==4:
        myelinN=arguments[1]
        surfaceN=arguments[2]
        surfMapN=arguments[3]

        r=aims.Reader()
        myelin=r.read(myelinN)
        surface=r.read(surfaceN)

        surfMap=projectOnSurface(myelin, surface)

        w=aims.Writer()
        w.write(surfMap, surfMapN)
    else:
        print 'Usage:'
        print 'python projectT1T2onSurface.py myelinImage surface map'

if __name__ == "__main__":
     arguments=sys.argv
     main(arguments)
