from pyreproj import Reprojector


def decdeg2dms(dd):
    mnt, sec = divmod(dd * 3600, 60)
    deg, mnt = divmod(mnt, 60)
    return deg, mnt, sec


rp = Reprojector()
transform = rp.get_transformation_function(from_srs=2180, to_srs='epsg:4326')
print(decdeg2dms(transform(204972.8521, 567573.1002)[0]), decdeg2dms(transform(204972.8521, 567573.1002)[1]))
