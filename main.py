from PIL import Image
import glob, os
import math
from random import randint, randrange


ratioH = 17
ratioW = 10

input_path = 'inputs'
output_path = 'output'
file_endings = ['jpg', 'jpeg']

if __name__ == "__main__":

    files_found = []
    for ending in file_endings:
        pattern = os.path.join(input_path, f'*.{ending}')
        files_found.extend(glob.glob(pattern))

    for infile in files_found:
        filepath, ext = os.path.splitext(infile)
        filename = os.path.basename(filepath)
        with Image.open(infile) as im:
            w,h = im.size
            sliceH = h
            sliceW = int((h/ratioH)*ratioW)
            nSlices = math.ceil(w/sliceW)
            overlapTotal = (nSlices*sliceW)-w
            overlapEach = overlapTotal/(nSlices-1)

            upper = 0
            lower = h  # or (h-1) ?
            left = 0
            right = sliceW

            # make output fol
            # output_fol = os.path.join(output_path, filename.split('.')[0])
            # os.makedirs(output_fol, exist_ok=True)


            for i in range(nSlices):
                # crop
                islice = im.crop((left, upper, right, lower))

                # save
                randID = randint(0,10000)
                save_as = os.path.join(output_path,
                                       f"{randID}_{filename.split('.')[0]}_{i}.jpeg")
                islice.save(save_as, "JPEG")

                left += (sliceW - overlapEach)
                right += (sliceW - overlapEach)

            #The cropped images must have
            #a height higher than 1800 pixels and
            # a ratio of about 10:17.
            # That is to say that if an image has a width of 10000 pixels,
            # its heigth must be around 17000 pixels (x 1.7).
