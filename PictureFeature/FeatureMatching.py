# Feature matching

import cv2


def show_image(winname, mat):
    cv2.imshow(winname, mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


book = cv2.imread('../Data/box.png')
books = cv2.imread('../Data/box_in_scene.png')

show_image("book", book)
show_image("books", books)

# create SIFT
sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(book, None)
kp2, des2 = sift.detectAndCompute(books, None)

##################################### one to one #####################################
# create Brute-Force (暴力匹配)
# def create(self, normType=None, crossCheck=None)
# crossChec: k表示两个特征点要互相匹，例如A中的第i个特征点与B中的第j个特征点最近的，并且B中的第j个特征点到A中的第i个特征点也是
# NORM_L2: 归一化数组的(欧几里德距离)，如果其他特征计算方法需要考虑不同的匹配计算方式
bf = cv2.BFMatcher(crossCheck=True)

# use match, the one to one
matches = bf.match(des1, des2)
# sorted the result
matches = sorted(matches, key=lambda x: x.distance)
# draw matches 10
img = cv2.drawMatches(book, kp1, books, kp2, matches[:10], None, flags=2)
show_image('img', img)

##################################### k best matches #####################################
bf_matcher = cv2.BFMatcher()
knn_matches = bf_matcher.knnMatch(des1, des2, k=2)

best = []
for m, n in knn_matches:
    if m.distance < 0.75 * n.distance:  # filter the key point
        best.append([m])

best_image = cv2.drawMatchesKnn(book, kp1, books, kp2, best, None, flags=2)
show_image('best_image', best_image)

##################################### Use the fast Matcher: FlannBasedMatcher #####################################
flann_matcher = cv2.FlannBasedMatcher()
# use match, the one to one
matches = flann_matcher.match(des1, des2)
# sorted the result
matches = sorted(matches, key=lambda x: x.distance)
# draw matches 10
img = cv2.drawMatches(book, kp1, books, kp2, matches[:10], None, flags=2)
show_image('img', img)
