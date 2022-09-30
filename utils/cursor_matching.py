# Done by Balloon_356
# Bilibili: https://space.bilibili.com/244384103

from cv2 import matchTemplate, cvtColor, minMaxLoc, rectangle, COLOR_BGR2HSV, TM_CCOEFF_NORMED
from utils.grabscreen import grab_screen

import cv2
from collections import Counter


class LocQueue():
    def __init__(self, maxsize=9):
        self.queue = []
        self.maxsize = maxsize
        self.ptr = 0

    def put(self, elem):
        if self.full():
            self.queue[self.ptr] = elem
            self.ptr = (self.ptr + 1) % self.maxsize
        else:
            self.queue.append(elem)
    
    def full(self):
        return len(self.queue) == self.maxsize

    def major(self):
        return Counter(self.queue).most_common(1)  # a list of (key, value)


Loc_Q = LocQueue(maxsize=100)

def cursor_match(template_cursor, resolution, region=(0, 0, 1920-1, 1080-1)):

    # screen
    img = grab_screen(region=region)
    img_H = cvtColor(img, COLOR_BGR2HSV)[:, :,0]
    # template
    
    template_cursor_H = cvtColor(template_cursor, COLOR_BGR2HSV)[:, :, 0]

    # matching by NCC
    result = matchTemplate(img_H, template_cursor_H, TM_CCOEFF_NORMED)
    (minVal, maxVal, minLoc, maxLoc) = minMaxLoc(result)

    # majority voting
    Loc_Q.put(maxLoc if abs(maxVal)>abs(minVal) else minLoc)
    Loc = Loc_Q.major()[0][0]

    dict_dy = {'1080': 14, '2k': 14, '4k': 14}

    return Loc[1], Loc[0] + dict_dy[resolution]