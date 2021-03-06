# 调整数组顺序使奇数位于偶数前面

____

## 题目描述

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
____

## 解法

### v-1.0

前后两个指针，从前到后遍历，然后交换

牛客网不支持这种做法，因为要求排序后的数组保序。

### v-2.0

这个思路有点奇思妙想了，**定义一个新的比较大小规则**：同为奇数或者同为偶数记为一样大，奇数比偶数小，然后按照这个规则对数组从到大排序。说实话，我觉得这种效率应该挺低的，因为需要两两比较，而且需要换多次位置，但是思路倒是很奇特，并且是稳定的。

(x,y)->(y&1)-(x&1)

### v-3.0

因为需要保序，所以原地操作是不行了，可以采用新建数组的方法。
____

## 测试用例

___

