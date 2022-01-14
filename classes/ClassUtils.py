import os, time


def getBasepath():
    basepath = os.path.dirname(os.path.realpath(__file__))
    return basepath


def getTakePicturePath():
    """ 取得拍照後要存檔的路徑。 """
    basepath = getBasepath()
    jpgimagepath = os.path.join(
        basepath,
        "takepictures",
        f'HeadPose_{time.strftime("%Y%m%d_%H%M%S", time.localtime())}.jpg',
    )

    if not os.path.exists(os.path.dirname(jpgimagepath)):
        os.makedirs(os.path.dirname(jpgimagepath))
    return jpgimagepath
