# Done by Balloon_356
# Bilibili: https://space.bilibili.com/244384103

from cv2 import cvtColor, matchTemplate, minMaxLoc, line, COLOR_RGB2BGR, TM_SQDIFF, TM_CCOEFF, CV_32F
from utils.grabscreen import grab_screen



def temp_match(template_eye_1, template_eye_2, mask, region=(0, 0, 1919, 1079)):
    '''
    param: template_eye(cv2.imread()), the template used to match the screenshot
    param: mask, the mask used in cv2.matchTemplate
    param: region, the region of screenshot
    return: minVal of matchTemplate result, destX, destY, endereye
    '''

    # screen
    img_screen = grab_screen(region=region)
    img_screen = cvtColor(img_screen, COLOR_RGB2BGR)

    mask_sum = (mask > 0).sum()
    dx = int(mask.shape[0] / 2.0 - 1)
    dy = int(mask.shape[1] / 2.0 - 1)

    # matching
    result_1 = matchTemplate(img_screen, template_eye_1, TM_SQDIFF, mask=mask)
    (minVal_1, _, minLoc_1, _) = minMaxLoc(result_1)  
    minVal_1 = (minVal_1 / mask_sum) ** 0.5

    result_2 = matchTemplate(img_screen, template_eye_2, TM_SQDIFF, mask=mask)
    (minVal_2, _, minLoc_2, _) = minMaxLoc(result_2)  
    minVal_2 = (minVal_2 / mask_sum) ** 0.5

    minVal = minVal_1 if minVal_1 < minVal_2 else minVal_2
    minLoc = minLoc_1 if minVal_1 < minVal_2 else minLoc_2

    if minVal > 6:
        print(minVal)
        return minVal, None, None, None

    else:
        print(minVal, '!')
        (LocY, LocX) = minLoc

        # used to grab screen
        startX = LocX - 5
        startY = LocY - 5
        endX = LocX + 95
        endY = LocY + 25

        endereye = grab_screen(region=(startY, startX, endY, endX))

        # original dest point
        destX = LocX + dx
        destY = LocY + dy

        # draw the line
        color = (255, 224, 47)
        x1 = destX - startX
        y1 = destY - startY
        # cv2.line  point(y1, x1) to point(y2, x2)
        endereye = line(endereye, (y1, x1), (y1, x1+10), color, 1)
        endereye = line(endereye, (y1, x1+20), (y1, x1+30), color, 1)
        endereye = line(endereye, (y1, x1+40), (y1, x1+50), color, 1)
        endereye = line(endereye, (y1, x1+60), (y1, x1+70), color, 1)

        return minVal, destX+50, destY, endereye