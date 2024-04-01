#정렬 3종
## 선택정렬
# input_list = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# for i in range(len(input_list)):
#     min_index = i
#     for j in range(i + 1, len(input_list)):
#         if input_list[min_index] > input_list[j]:
#             min_index = j
#     input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
# print(input_list)

## 거품 정렬
# input_list = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# for i in range(len(input_list) - 1):
#     for j in range(len(input_list) - i - 1):
#         if input_list[j] > input_list[j+1]:
#             input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
# print(input_list)

## 삽입 정렬
input_list = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(input_list)):
    for j in range(i, 0, -1):
        if input_list[j] < input_list[j-1]:
            input_list[j], input_list[j-1] = input_list[j-1], input_list[j]
print(input_list)