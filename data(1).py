import numpy as np
import tqdm

file1 = open("D:\\硕士课题\\光谱混叠任务资料\\20210111\\20210227\\data0006.csv", 'r', encoding='UTF8')
# file1 = open("C:\\Users\\mate\\Desktop\\light_detect\\20210825\\data0001.csv", 'r', encoding='UTF8')
RAR_data = np.zeros([10000, 3, 2001])
# RAR_data = np.zeros([10000, 1, 1498])

lines = file1.readlines()
zip_line = zip(lines[0::3], lines[1::3], lines[2::3])
# zip_line = zip(lines[0::])

count = 0

def make_line(line):
    line = line.replace('\ufeff', '')
    line = line.strip().split(',')
    line = np.asarray(line, dtype=np.float64)
    return line

for line1, line2, line3 in tqdm.tqdm(zip_line):
    try:
        line1 = make_line(line1)
        line2 = make_line(line2)
        line3 = make_line(line3)

        RAR_data[count][0] = np.asarray(line1[2:], dtype=np.float64)
        RAR_data[count][1] = np.asarray(line2[2:], dtype=np.float64)
        RAR_data[count][2] = np.asarray(line3[2:], dtype=np.float64)

        count += 1
    except:
        pass
#
#
# for line1 in tqdm.tqdm(zip_line):
#     try:
#         line1 = make_line(line1)
#
#         RAR_data[count][0] = np.asarray(line1[2:], dtype=np.float64)
#         count += 1
#     except:
#         pass
RAR_data = RAR_data[:count]

for i in tqdm.trange(count):
    RAR_data[i][0:2] /= np.max(RAR_data[i][0:2])
    RAR_data[i][2] /= np.max(RAR_data[i][2])

np.save("RAR_data009.npy", RAR_data)