import cv2
import numpy as np
import math
import argparse


class MissingArgumentError(ValueError):
    pass

input_path = ''

# argument parsing
parser = argparse.ArgumentParser(description='Convert image file to High-Color bitmap to be integrated in C code.')
parser.add_argument("-f", "--file", help = "input image file")
parser.add_argument("-o", "--output", help = "output text file (OPTIONAL)", default=None)
parser.add_argument("-r", "--rows", help = "set length of output rows (OPTIONAL, default = 16)", type = int, default=16)
args = parser.parse_args()

output_path = args.output
row_length = args.rows
if not args.file:
    raise MissingArgumentError("Path to file must be given as argument.")
else:
    input_path = args.file

#colors are coded as 1 byte [0,255]
#stored in BGR order
img = cv2.imread(input_path)
rows,cols,_ = img.shape

output_file = None

if output_path is not None:
    output_file = open(output_path, "w")

for i in range(rows):
    for j in range(cols):
        #convert
        dat = img[i,j]
        R = math.floor(dat[2]/255*31)
        G = math.floor(dat[1]/255*63)
        B = math.floor(dat[0]/255*31)
        res = R<<11 | G<<5 | B
        #print
        res_padded = '0x' + hex(res)[2:].zfill(4)
        print(res_padded + ",", end='')
        if output_file is not None:
            output_file.write(res_padded + ",")
        if (i*cols+j)%row_length==row_length-1:
            print("")
            if output_file is not None:
                output_file.write("\n")
print("\nImage size is: " + str(rows) + ", " + str(cols))

if output_file is not None:
    output_file.close()