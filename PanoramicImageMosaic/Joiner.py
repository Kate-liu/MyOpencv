# -*- coding:utf-8 -*-
import cv2
import numpy as np


class Joiner:

    def show_image(self, winname, mat):
        """
        cv2 show image.
        :param winname:
        :param mat:
        :return:
        """
        cv2.imshow(winname, mat)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def detect_and_describe(self, image):
        # create SIFT
        descriptor = cv2.xfeatures2d.SIFT_create()
        # check point and get desc
        (keypoints, descriptors) = descriptor.detectAndCompute(image, None)
        # converse numpy array
        keypoints = np.float32([kp.pt for kp in keypoints])

        return (keypoints, descriptors)

    def match_keypoints(self, keypoints1, keypoints2, descriptors1, descriptors2, ratio, reprojThresh):
        # bf matcher
        matcher = cv2.BFMatcher()
        # use knn
        knn_matches = matcher.knnMatch(descriptors1, descriptors2, k=2)

        matches = []
        for m in knn_matches:
            # use 0.75, filter the key point
            if len(m) == 2 and m[0].distance < m[1].distance * ratio:
                matches.append((m[0].trainIdx, m[0].queryIdx))
        # use > 4 point value, to find angle of view transformation matrix
        if len(matches) > 4:
            # get match pair point
            points1 = np.float32([keypoints1[i] for (_, i) in matches])
            points2 = np.float32([keypoints2[i] for (i, _) in matches])
            #  view transformation matrix
            # H is 3 * 3 matrix
            (H, status) = cv2.findHomography(points1, points2, cv2.RANSAC, reprojThresh)

            return (matches, H, status)
        # matches < 4
        return None

    def draw_matches(self, image1, image2, keypoints1, keypoints2, matches, status):
        (h1, w1) = image1.shape[:2]
        (h2, w2) = image2.shape[:2]

        # join the image 1 and 2
        join_image = np.zeros((max(h1, h2), w1 + w2, 3), dtype="uint8")
        join_image[0:h1, 0:w1] = image1
        join_image[0:h2, w1:] = image2

        # draw matched
        for ((trainIdx, queryIdx), s) in zip(matches, status):
            # matched
            if s == 1:
                # draw
                pt1 = (int(keypoints1[queryIdx][0]), int(keypoints1[queryIdx][1]))
                pt2 = (int(keypoints2[trainIdx][0]) + w1, int(keypoints2[trainIdx][1]))
                cv2.line(join_image, pt1, pt2, (0, 255, 0), 1)
        return join_image

    def join(self, images, ratio=0.75, reprojThresh=4.0, showMatches=False):
        (image1, image2) = images

        # use SIFT
        (keypoints1, descriptors1) = self.detect_and_describe(image1)
        (keypoints2, descriptors2) = self.detect_and_describe(image2)

        # match points
        M = self.match_keypoints(keypoints1, keypoints2, descriptors1, descriptors2, ratio, reprojThresh)
        if M is None:
            return None
        (matches, H, status) = M

        # wrap perspective image1
        # width = images + image2
        # height = image1
        result = cv2.warpPerspective(image1, H, (image1.shape[1] + image2.shape[1], image1.shape[0]))
        cv2.imshow("image1", image1)
        self.show_image("perspective image1", result)

        # add image2 to wrap image1
        result[0:image2.shape[0], 0:image2.shape[1]] = image2
        self.show_image("finally result", result)

        # show matches
        if showMatches:
            # draw matches
            draw_image = self.draw_matches(image1, image2, keypoints1, keypoints2, matches, status)
            return (result, draw_image)
        return result
