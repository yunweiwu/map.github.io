import cv2
import numpy as np
from bfs import bfs

def process_image(image_path):
    # 读取图片
    image = cv2.imread(image_path)

    # 将图片转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 二值化处理，黑色为1，白色为0
    _, binary = cv2.threshold(gray, 127, 1, cv2.THRESH_BINARY_INV)

    # 初始化绿色和红色点的中心数组
    start_pos = []
    end_pos = []

    # 遍历图片的每个像素
    for i in range(binary.shape[0]):
        for j in range(binary.shape[1]):
            # 如果像素值为1（黑色），则检查其颜色
            if binary[i, j] == 1:
                color = image[i, j]
                if color[1] > color[2]:  # 绿色点的中心
                    start_pos.append((i, j))
                    binary[i, j] = 0
                elif color[2] > color[1]:  # 红色点的中心
                    end_pos.append((i, j))
                    binary[i, j] = 0

    # 输出结果
    print("Start positions:", start_pos)
    print("End positions:", end_pos)
    print("Array representation of the map:")
    output_row = [row.tolist() for row in binary]
    return output_row, list(start_pos[0]), list(end_pos[0])

# 调用函数处理图片

row, start_pos, end_pos = process_image(r"C:\Users\lu\Desktop\map\small_map.png")
path, dir_list = bfs(row, start_pos, end_pos)
direction = {0: "←", 1: "↑", 2: "→", 3: "↓"}
for i in range(len(row)):
    for j in range(len(row[i])):
        if row[i][j] == 1:
            print("#", end="")
        elif [i, j] == start_pos:
            print("S", end="")
        elif [i, j] == end_pos:
            print("E", end="")
        elif [i, j] in path:
            print(direction[dir_list[path.index([i, j])]], end="")
        else:
            print(" ", end="")
    print()
