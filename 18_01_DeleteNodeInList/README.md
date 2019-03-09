# 在O(1)时间内删除链表节点

____

## 题目描述

给定单向链表的头指针和一个节点指针，定义一个函数在 O(1) 时间内删除该节点。
____

## 解法

删除链表节点必须知道该节点的前置节点，一般情况是从前到后遍历，遍历到删除节点，这种方法是最基本的，复杂度是O(N)，但是换一种思路，只是需要一个前置节点和删除节点就可以，那不妨令已知节点为前置节点，后一个节点为删除节点，具体方法就是调换两者的位置。

对于首节点和尾节点，需要特殊处理。

____

## 测试用例

1. 功能测试（从有多个节点的链表的中间/头部/尾部删除一个节点；从只有一个节点的链表中删除唯一的节点）；
2. 特殊输入测试（指向链表头节点的为空指针；指向要删除节点的为空指针）。

___
