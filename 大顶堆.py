import copy
import heapq


class ReversedList(list):
    def __lt__(self, __x: list) -> bool:
        return super().__gt__(__x)
    def __gt__(self, __x: list) -> bool:
        return super().__lt__(__x)

class ReversedInt(int):
    def __lt__(self, __x: int) -> bool:
        return super().__gt__(__x)
    def __gt__(self, __x: int) -> bool:
        return super().__lt__(__x)

if __name__ == "__main__":
    nums = [2, 5, 1, 3, 4]
    new_nums = []
    for i in nums:
        new_nums.append(ReversedInt(i))

    # 小顶堆
    heapq.heapify(nums)
    print(nums)

    # 大顶堆
    heapq.heapify(new_nums)
    print(new_nums)

   