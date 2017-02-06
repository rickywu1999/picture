#!/usr/bin/env python

pic = open("picture.ppm","w+");

pic.write("P3\n500 500 255\n");

for a in range(500):
    for b in range(500):
        if a == b:
            pic.write("255 255 255 ")
        else:
            pic.write(str((a+b) / 255) + " ")
            pic.write(str((a+b) % 255) + " ")
            pic.write(str((a*b) % 255) + " ")

