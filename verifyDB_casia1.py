
from utils.extractandenconding import extractFeature, matchingTemplate
from time import time
import argparse
import cv2


# args
parser = argparse.ArgumentParser()
parser.add_argument("--filename", type=str, default="../CASIA1/110/110_1_1.jpg",
                    help="../CASIA1/1/110_1_1.jpg")
parser.add_argument("--template_dir", type=str, default="./templates/CASIA1/",
                    help="./templates/CASIA1/")
parser.add_argument("--threshold", type=float, default=0.37,
                    help="Threshold for matching.")
args = parser.parse_args()






if __name__ == '__main__':
    # timing
    start = time()
    if 0:
        key = cv2.waitKey(1)
        webcam = cv2.VideoCapture(0)
        while True:
            try:
                check, frame = webcam.read()
                print(check)  # prints true as long as the webcam is running
                print(frame)  # prints matrix values of each framecd
                cv2.imshow("Capturing", frame)
                key = cv2.waitKey(1)
                if key == ord('s'):
                    cv2.imwrite(filename='./CamTemp/saved_img.jpg', img=frame)
                    webcam.release()
                    img_new = cv2.imread('./CamTemp/saved_img.jpg')
                    # img_new = cv2.imshow("Captured Image", img_new)
                    # cv2.waitKey(1650)
                    # cv2.destroyAllWindows()
                    # print("Processing image...")
                    # img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                    # print("Converting RGB image to grayscale...")
                    # gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                    # print("Converted RGB image to grayscale...")
                    # print("Resizing image to 28x28 scale...")
                    img_ = cv2.resize(img_new, (320, 280),interpolation= cv2.INTER_LINEAR)
                    print("Resized...")
                    img_resized = cv2.imwrite(filename='./CamTemp/saved_img-final.jpg', img=img_)
                    print("Image saved!")
                    fileCamName = './CamTemp/saved_img-final.jpg'
                    break
                elif key == ord('q'):
                    print("Turning off camera.")
                    webcam.release()
                    print("Camera off.")
                    print("Program ended.")
                    cv2.destroyAllWindows()
                    break

            except(KeyboardInterrupt):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break
    else:
        fileCamName = args.filename;
    print('\tStart verifying {}\n'.format(fileCamName))
    template, mask, filename = extractFeature(args.filename)
    result = matchingTemplate(template, mask, args.template_dir, args.threshold)

    # results
    if result == -1:
        print('\tNo registered sample.')
    elif result == 0:
        print('\tOops..No sample found..Attendance cannot be Captured. Try Again')
    else:
        print('\tsamples found ..Attendance Captured for the ID:'.format(len(result)))
        for res in result:
            print("\t", res.split("_")[0])
    # total time
    end = time()
    print('\n\tTotal time: {} [s]\n'.format(end - start))