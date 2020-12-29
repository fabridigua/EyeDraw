import cv2
import numpy as np


class Homography:
    def __init__(self, move_thresh=2):
        self.calibration_circle_pos = np.empty((0, 2), np.float32)
        self.calibration_eye_pos = np.empty((0, 2), np.float32)
        self.homography = None
        self.calibration_counter = 0
        self.current_screen_pont = [0, 0]
        self.move_thresh = move_thresh

    def save_calibration_position(self, eyes_pos, position, pos_counter):
        eyes_point = self.get_middle_point(eyes_pos)
        eyes_point = [[list(eyes_point)[0], list(eyes_point)[1]]]
        c_pos = [[list(position)[0], list(position)[1]]]
        if self.calibration_counter < pos_counter:
            self.calibration_counter += 1
            self.calibration_circle_pos = np.append(self.calibration_circle_pos, np.array(c_pos), axis=0)
            self.calibration_eye_pos = np.append(self.calibration_eye_pos, np.array(eyes_point), axis=0)

    def get_middle_point(self, eyes):
        left_eye = eyes[0]
        right_eye = eyes[1]
        return [(left_eye[0] + right_eye[0]) / 2, (left_eye[1] + right_eye[1]) / 2]

    def calculate_homography(self):
        self.homography, _ = cv2.findHomography(self.calibration_eye_pos, self.calibration_circle_pos)

    def get_cursor_pos(self, eyes_pos):
        eyes_point = np.empty((0, 2), np.float32)
        eyes_point = np.append(eyes_point, np.array([self.get_middle_point(eyes_pos)]), axis=0)
        eyes_point = np.append(eyes_point, 1)
        eyes_point_homogenous = np.dot(self.homography, eyes_point)
        screen_point = [eyes_point_homogenous[0] / eyes_point_homogenous[2],
                        eyes_point_homogenous[1] / eyes_point_homogenous[2]]
        if cv2.norm(np.array(screen_point, np.int32), np.array(self.current_screen_pont, np.int32)) <= self.move_thresh:
            screen_point = self.current_screen_pont

        self.current_screen_pont = screen_point
        return screen_point
