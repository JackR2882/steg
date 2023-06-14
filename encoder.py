# ENCODER - hides message by means of lsb modification within an image file

import cv2
import bitarray

original_img = cv2.imread('original.png')
(h, w, d) = original_img.shape

print("max bits: " + str(h*w*d))

message = "Hello!"

ba = bitarray.bitarray() # convert message to bit-array
ba.frombytes(message.encode('utf-8'))
#print(ba)

x, y, z = -1, 0, 0 # use as pointers for where to insert message bits (height / width / depth, respectively)
modified_img = original_img.copy()
i = 0

# overwrite lsb of each pixel with message bits
for i in range(0, len(ba)):
    x += 1
    if x == h:
        x = 0 # reset x
        y += 1
        if y >= w:
            y = 0 # reset y
            z+=1

    curr_val = modified_img[x][y][z]
    msg_val = ba[i]

    if curr_val % 2 == msg_val % 2:
        # do nothing
        curr_val = curr_val
    else:
        if curr_val != 0:
            curr_val -= 1
        else:
            curr_val += 1
        modified_img[x][y][z] = curr_val

# write to new image
cv2.imwrite('modified1.png', modified_img)