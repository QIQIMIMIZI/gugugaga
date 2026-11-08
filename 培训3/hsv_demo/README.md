# 培训3 - OpenCV 作业

## 环境
- Windows 11 + Visual Studio 2026 (MSVC) + CMake
- OpenCV 4.10.0（Windows 预编译包，OpenCV_DIR = C:/opencv/build/x64/vc16/lib）

## 目录
- src/main.cpp ：任务1，读图 -> 转 HSV -> 分离 H/S/V 三个通道并分别显示 -> inRange 提取红色掩膜 -> 保存 red_mask.png
- src/video.cpp：任务2，视频逐帧识别灯条，minAreaRect 画出灯条外接矩形，连接装甲板四个角点 P1~P4
- images/armor.jpg ：测试图片

## 编译运行
cmake -S . -B build -G "Visual Studio 18 2026" -A x64
cmake --build build --config Release
.\build\Release\hw1_image.exe
.\build\Release\hw2_video.exe

## 结果
- 任务1：red_mask.png（红色灯条被提取为白色区域）
- 任务2：视频窗口显示黄色灯条矩形 + 绿色装甲板四边形和 P1~P4 角点
