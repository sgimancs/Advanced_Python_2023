#! python
# coding=utf-8
# **************************************************************
# L_011_007.py
# 011_Рекурсия
# 007.Рекурсивный Проход по Списку
# --------------------------------------------------------------
# Практический Курс по Продвинутому Python (2023)
# https://www.udemy.com/course/avecoder-advanced-python/
# Ave Coder, 2023
# **************************************************************
# Writing by sgiman, May 2025

# Список, который содержит списки с подсписки
colours = [
    "Black",                        # 1
    [                               # 2
        "Gray",
        ["Yellow", "Orange"],
        "Green",
        "Blue"
    ],
    "white",                        # 3
    ["Brown", "Red"],               # 4
    "Pink"                          # 5
]

print('=' * 80)
print(len(colours))

print('=' * 80)
for index, item in enumerate(colours):      # enumerate => index, item (нумератор)
    print(index, item)

###############################################################
### traverse non-recursively (???)
# def count_leaf_items(item_list):
#     count = 0
#     stack = []
#     current_list = item_list
#     i = 0
#
#     while i == len(current_list):
#         if current_list == item_list:   # если элемент из главного списка
#             return count
#         else:
#             current_list, i = stack.pop()
#             i += 1
#             continue
#
#         if isinstance(current_list[i], list):
#             stack.append([current_list, i])
#             current_list = current_list[i]
#             i = 0
#         else:
#             count += 1
#             i += 1


### recursion
def count_leaf_items_rec(item_list):
    print(f"List:{item_list}")
    count = 0
    for item in item_list:
        if isinstance(item, list):
            print('if sublist')
            count += count_leaf_items_rec(item)
        else:
            print(f'leaf "item"')
            count += 1
    print(f"-> count is {count}")
    return count


###############################################################
if __name__ == "__main__":
    # print('=' * 80)
    # print(count_leaf_items(colours)) # ???
    print('=' * 80)
    print(count_leaf_items_rec(colours))
