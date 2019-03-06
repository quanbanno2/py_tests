import unittest


def insertsort(arr):
    for i in range(1, len(arr)):
        # 设置当前值前一个元素的标识
        j = i - 1
        # 如果当前值小于前一个元素,则将当前值作为一个临时变量存储,
        # 将前一个元素后移一位
        # [5,6,4,3,2,1]
        if (arr[i] < arr[j]):

            # [5, ,6,3,2,1,]  j=1  将小的数放到缓存中
            temp = arr[i]
            arr[i] = arr[j]

            # 继续往前寻找,如果有比临时变量大的数字,则后移一位,
            # 直到找到比临时变量小的元素或者达到列表第一个元素

            # [5, ,6,3,2,1,]   j=0  arr[j]=5
            j = j - 1

            # 条件成立
            while j >= 0 and arr[j] > temp:
                # arr[1] = arr[0]
                # j= -1 时跳出循环
                arr[j + 1] = arr[j]
                j = j - 1

            # 将临时变量赋值给合适位置
            # arr[-1+1] = 4
            arr[j + 1] = temp


class test_sort(unittest.TestCase):
    def test_insertsort(self):
        data_1 = [5, 6, 4, 3, 2, 1]
        data_2 = [1, 3, 4, 5, 2]

        copy_date1 = data_1
        copy_date2 = data_2

        insertsort(data_1)
        insertsort(data_2)

        copy_date1.sort()
        copy_date2.sort()

        self.assertEqual(copy_date1, data_1)
        self.assertEqual(copy_date2, data_2)


if __name__ == '__main__':
    unittest.main()
