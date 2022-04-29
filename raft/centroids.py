from argparse import ArgumentParser
from sklearn.cluster import MeanShift
import cv2
import matplotlib.pyplot as plt


def place_centroids(img):

    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = len(grayscale), len(grayscale[0])

    intensity_weighted_pixels = []

    [
        intensity_weighted_pixels.append([r, c] * grayscale[r][c])
        for r in range(h)
        for c in range(w)
    ]

    X = chain(*intensity_weighted_pixels)

    # --> only for debugging purposes
    fig = plt.figure()

    ax = fig.add_subplot(111)

    ax.scatter(X[:, 0], X[:, 1], marker="o", alpha=0.1)

    plt.show()

    assert 1 == 0
    # --> only for debugging purposes

    ms = MeanShift()
    ms.fit(X)


cluster_centers = ms.cluster_centers_


def main(args):
    # os.system(f"python run_inference.py")
    data_path = args.path

    img_flo_path = data_path + "/FlowImages_gap-1"  # path to the dataset
    superfolder = gb.glob(os.path.join(img_flo_path, "*"))

    outroot = data_path + f"/Centroids/"

    for folder in superfolder:
        img_path1 = os.path.join(args.path, "*.png")
        img_path2 = os.path.join(args.path, "*.jpg")
        images = glob.glob(img_path1) + glob.glob(img_path2)

        floout = os.path.join(outroot, folder)

        if args.clear and os.path.exists(floout):
            shutil.rmtree(floout)
        os.makedirs(floout, exist_ok=True)

        images = sorted(images)

        for index, imfile1 in enumerate(images_):
            image1 = load_image(imfile1)
            svfile = imfile1

            flopath = os.path.join(floout, os.path.basename(svfile))

            processed_img = place_centroids(image1)

            cv2.imwrite(flopath[:-4] + ".png", processed_img)


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("--path", type=str, default="../data/custom")
    parser.add_argument("--clear", action=BooleanOptionalAction)

    args = parser.parse_args()

    main(args)
