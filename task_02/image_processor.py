import numpy as np
import cv2
import os


class ImageProcessor:
    def __init__(self, input_file_name=None, output_file_name=None, coefficient=None):
        self.__image_with_points = np.ndarray(shape=10)
        self.__image_without_points = np.ndarray(shape=10)
        self.__input_file_name = input_file_name
        self.__approx_poly_dp_coefficient = 0.01 if coefficient is None else coefficient

    def find_points(self):
        img = self.__image_without_points
        width = int(img.shape[1])
        height = int(img.shape[0])
        resize = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

        # Обесцвечиваем изображение
        gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

        blur = cv2.medianBlur(gray, 21)
        ret, thresh1 = cv2.threshold(blur, 30, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        drawing = np.zeros(img.shape, np.uint8)

        max_area = 0

        for i in range(len(contours)):
            cnt = contours[i]
            area = cv2.contourArea(cnt)
            if area > max_area:
                max_area = area
                ci = i
                cnt = contours[ci]
                hull = cv2.convexHull(cnt)
                moments = cv2.moments(cnt)
                if moments['m00'] != 0:
                    cx = int(moments['m10'] / moments['m00'])  # cx = M10/M00
                    cy = int(moments['m01'] / moments['m00'])  # cy = M01/M00

                    central = (cx, cy)
                    cv2.circle(img, central, 5, [0, 0, 255], 1)
                    cv2.drawContours(drawing, [cnt], 0, (0, 255, 0), 1)
                    cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 1)
                    cnt = cv2.approxPolyDP(cnt, self.__approx_poly_dp_coefficient * cv2.arcLength(cnt, True), True)
                    hull = cv2.convexHull(cnt, returnPoints=False)

                    defects = cv2.convexityDefects(cnt, hull)
                    for j in range(defects.shape[0]):
                        s, e, f, d = defects[j, 0]
                        start = tuple(cnt[s][0])
                        end = tuple(cnt[e][0])
                        far = tuple(cnt[f][0])
                        cv2.circle(img, far, 3, [0, 0, 255], -1)
                        cv2.circle(img, end, 3, [0, 0, 255], -1)
                        cv2.circle(img, start, 3, [0, 0, 255], -1)
                        cv2.line(img, start, far, [0, 255, 0], 1)
                        cv2.line(img, end, far, [0, 255, 0], 1)

        self.__image_with_points = img

    def show_processed_image(self):
        cv2.imshow('Image with points on fingers', self.__image_with_points)
        cv2.waitKey(0)

    def load_image_from_file(self, input_file_name=None):
        if input_file_name is None:
            input_file_name = self.__input_file_name
        else:
            self.__input_file_name = input_file_name
        self.__image_without_points = cv2.imread(input_file_name)

    def save_image_to_file(self, output_file_name=None):
        if output_file_name is None:
            output_file_name = f"./training/test/{os.path.basename(self.__input_file_name)}"
        cv2.imwrite(output_file_name, self.__image_with_points)
