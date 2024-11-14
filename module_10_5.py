import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data


filenames = [f'./file {number}.txt' for number in range(1, 5)]
start_time = time.time()
for file in filenames:
    read_info(file)
end_time = time.time()
print(f"Время выполнения линейного вызова: {end_time - start_time:.4f} секунд")

# if __name__ == '__main__':
#     start_time = time.time()
#     with Pool() as pool:
#         results = pool.map(read_info, filenames)
#
#     end_time = time.time()
#     print(f"Время выполнения многопроцессного вызова: {end_time - start_time:.4f} секунд")
