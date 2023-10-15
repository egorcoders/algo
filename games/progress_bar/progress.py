# Программа должна вывести единственное число – номер буквы в строке,
# при удалении которой слово становится палиндромом. Если при удалении
# любой буквы слово не станет палиндромом, программа должна вывести число 0.
#
# ПРИМЕРЫ
#
# ВВОД
# raceczcar
#
# ВЫВОД
# 6
# #
# # ВВОД
# # car
# #
# # ВЫВОД
# # 0
# from random import sample
#
# ls = list(range(1_000))
# ls = sample(ls, 500)
#
# ls.sort()
# print(ls)
# def fn(ls, n):
#     start = 0
#     end = len(ls) - 1
#     for i in range(len(ls)):
#         mid = (start + end) // 2
#         c = ls[mid]
#         a = ls[start]
#         b = ls[end]
#         if ls[mid] == n:
#             return True
#
#         if ls[mid] > n:
#             end = mid
#         elif ls[mid] < n:
#             start = mid
#     return False
#
#
# t = 188
# print(fn(ls, t))
from collections import defaultdict

# print(_max, ls[start], ls[end])

# def fn(a):
#     if abs(len(a) - len(b)) > 1:
#         return False
#
#     if len(a) > len(b):
#         a, b = b, a
#
#     if b[1:] == a or b[:-1] == a:
#         return True
#
#     for i in range(len(b)):
#         ans = b[:i] + b[i + 1:]
#         if ans == a:
#             return True
#
#     return False
#
#
# s1 = '111ab111'
# print(fn(s1))
# from json import loads, dumps

# import queue
#
# q = queue.PriorityQueue()
# q.put((1, "Daniel Wilson"))
# q.put((2, "Liam Walker"))
# q.put((3, "Sarah Johnson"))
#
# print(q.get())

from pympler import asizeof


aa = [a for a in range(1_000_000)]

def humanize_bytes(bytes, precision=2):
    abbrevs = (
        (1 << 50, 'PB'),
        (1 << 40, 'TB'),
        (1 << 30, 'GB'),
        (1 << 20, 'MB'),
        (1 << 10, 'KB'),
        (1, 'bytes')
    )

    if bytes == 1:
        return '1 byte'
    for factor, suffix in abbrevs:
        if bytes >= factor:
            break
    return f"{bytes / factor:.{precision}f} {suffix}"

# # Example usage
# size_in_bytes = 1024000  # 1 megabyte
# human_readable_size = humanize_bytes(size_in_bytes)
print(humanize_bytes(asizeof.asizeof(aa)))  # Output: "1000.00 KB"
# In this example, the humanize_bytes function takes a size in bytes and an optional precision argument for formatting floating-point numbers. It converts the size into a human-readable format using common size units like kilobytes, megabytes, etc.
#
# You can adjust the units and their corresponding abbreviations in the abbrevs tuple to match your specific needs or localization requirements.





