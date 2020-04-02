from soma import aims
import numpy as np

t=0.8

def projectOnSurface(myelin, surface):
    norm=surface.normal()
    vert=surface.vertex()
    Nv=vert.size

    surfMap=aims.TimeTexture('float')
    surfMap[0].resize(Nv)

    for i in range(Nv):
        v=vert[i]+t*norm[i]
        val=myelin(v)
        surfMap[0][i]=val
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
