import imageio.v3 as iio
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

filenames = [
    os.path.join(script_dir, "chicklet1.png"),
    os.path.join(script_dir, "chicklet2.png"),
    os.path.join(script_dir, "chicklet3.png"),
    os.path.join(script_dir, "chicklet4.png")
]
images = [iio.imread(f) for f in filenames]

iio.imwrite('team.gif', images, duration = 500, loop = 0)
