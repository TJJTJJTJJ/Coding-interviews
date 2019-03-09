# 旋转数组的最小数字

____

## 题目描述

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组 {3,4,5,1,2} 为 {1,2,3,4,5} 的一个旋转，该数组的最小值为 1。
____

## 解法

### v-1 顺序查找

直观想法，从前到后遍历，一直到一个下降的元素，时间复杂度为O(n).

### v-2 二分法

作者的提示，先讨论一般的情况，即数组一定可以前后分成两个递增数组，最小元素一定在两个递增数组的交界处，用二分法，每次找中间的元素，判断中间元素的位置。

**备注：二分法的最后一定会出现前后两个指针相邻以及下一步两个指针重叠到前一个指针的情况**。

流程：

* array[mid] > array[p], p = mid
* array[mid] < array[q], q = mid
* **上述的过程保证了p总是指向前面的递增数组，q总是指向后面的递增数组**。
* q=p+1, return array[q]

特殊情况：

1. 数组没有发生旋转，此时array[p] < array[q]
2. 数组内有相同的数字array[p] = array[q] = array[mid]（根据参考代码发现还需要mid），此时mid的值不能证明其在前后哪个数组中，只能顺序查找，如果顺序查找过程中又出现array[p] > array[q]，则可以继续二分查找。{1,1,0,1,1}, {1,2,0,1,1}
3. {2,2,0,1,1,1}，从这个特例可以看出来，递增数组是不是严格递增不重要，重要的是array[start]>array[end]
4. 只有一个值

异常情况：

1. 输入为空

____

## 测试用例


## 其他

查找： 顺序查找、二分查找、哈希表查找、二叉排序树
排序： 插入排序、冒泡排序、归并排序、快速排序

哈希表：O(1)时间内查找某一元素