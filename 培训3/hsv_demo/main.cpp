#include <opencv2/opencv.hpp>
#include <iostream>
#include <vector>

int main() {
    cv::Mat img = cv::imread("images/armor.jpg");
    if (img.empty()) {
        std::cout << "failed to load image" << std::endl;
        return -1;
    }

    cv::Mat hsv;
    cv::cvtColor(img, hsv, cv::COLOR_BGR2HSV);

    std::vector<cv::Mat> ch;
    cv::split(hsv, ch);
    cv::imshow("H", ch[0]);
    cv::imshow("S", ch[1]);
    cv::imshow("V", ch[2]);

    cv::Mat mask1, mask2, mask;
    cv::inRange(hsv, cv::Scalar(0, 80, 60), cv::Scalar(10, 255, 255), mask1);
    cv::inRange(hsv, cv::Scalar(170, 80, 60), cv::Scalar(180, 255, 255), mask2);
    cv::bitwise_or(mask1, mask2, mask);

    cv::imshow("armor", img);
    cv::imshow("red_mask", mask);
    cv::imwrite("red_mask.png", mask);
    std::cout << "saved red_mask.png" << std::endl;

    cv::waitKey(0);
    return 0;
}
