# DECODER - recovers message by decoding least significant bit of a target file

import cv2
import bitarray

target_img = cv2.imread('modified1.png')

(h, w, d) = target_img.shape

x, y, z = -1, 0, 0

msg = bitarray.bitarray(0)
print(msg)
#msg = bytearray()

for i in range(0, 48):
    x += 1
    if x == h:
        x = 0 # reset x
        y += 1
        if y >= w:
            y = 0 # reset y
            z+=1

    curr_val = target_img[x][y][z]

    msg.append(curr_val%2)

print(msg)
recovered = msg.tobytes().decode('utf-8')
print(recovered)