from soma import aims
import numpy as np
import sys

t=0.8

def projectOnSurface(myelin, surface):
    norm=surface.normal()
    vert=surface.vertex()
    Nv=vert.size()

    surfMap=aims.TimeTexture('FLOAT')
    surfMap[0].resize(Nv)
    dx, dy, dz, dt=myelin.getVoxelSize()
    volVox=aims.Volume(myelin.getSizeX(), myelin.getSizeY(), myelin.getSizeZ(), myelin.getSizeT(), 'FLOAT')
    volVox.header().update(myelin.header())
    volVox.fill(0.0)

    print dx, dy, dz

    for i in range(Nv):
        v=vert[i]+t*norm[i]
        x=int(round(v[0]/dx))
        y=int(round(v[1]/dy))
        z=int(round(v[2]/dz))

        val=myelin.value(x,y,z)
        volVox.setValue(val, x,y,z)
        surfMap[0][i]=val
    return surfMap, volVox


def main(arguments):
    if len(arguments)==4:
        myelinN=arguments[1]
        surfaceN=arguments[2]
        surfMapN=arguments[3]

        r=aims.Reader()
        myelin=r.read(myelinN)
        surface=r.read(surfaceN)

        surfMap,volOut=projectOnSurface(myelin, surface)

        w=aims.Writer()
        w.write(surfMap, surfMapN)
        #w.write(volOut, 'midVoxels.nii')
    else:
        print 'Usage:'
        print 'python projectT1T2onSurface.py myelinImage surface map'

if __name__ == "__main__":
     arguments=sys.argv
     main(arguments)
