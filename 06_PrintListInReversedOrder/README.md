# 从尾到头打印链表

____

## 题目描述

输入一个链表，按链表值从尾到头的顺序返回一个 ArrayList。
____

## 解法

因为链表只能正向访问，所以，基本就是两个过程，从前到后依次访问，将访问的元素按照能够倒着访问的形式保存下来，然后再访问依次。

**栈：能够实现正着访问一次，再倒着访问的目的**。

## 其他

在java中，显示利用里栈，在python中，用list的insert(0)直接完成了存储+访问。
____

## 2.3.3 链表

* \**pHead: 指向链表第一个节点指针的指针，可以为NULL，表示为空
* \*pHead: 指向链表第一个节点的指针
* pNew: 指向链表节点的指针
* *pHead = pNew
* pNode = *pHead
* pNode->m_pNext = pNew
* 链表为空：pHead == NULL(指向链表第一个节点指针的指针为空) or *pHead == NULL(链表的第一个节点为空)

需要遵守**同级赋值**的性质：*pHead和pNew同级，pNode->m_pNext和pNew同级

### 2.3.3.1 链表定义

```c++
struct ListNode {
    int m_nValue;
    struct ListNode *m_pNext;
};
```

**空链表**:

```c++
ListNode **pHead;
if (pHead == NULL || *pHead == NULL)
```

### 2.3.3.2 链表末尾添加一个结点

```c++
void AddToTail(ListNode **pHead, int value)
{
    ListNode *pNew = new ListNode();
    pNew->m_nValue = value;
    pNew->m_pNext = NULL;

    // 链表为空
    if(pHead==NULL || *pHead==NULL){
        *pHead = pNew;
    }
    else
    {
        ListNode *pNode = *pHead;
        while(pNode->m_pNext!=NULL):{
            pNode = pNode->m_pNext;
        }
        pNode->m_pNext = pNew;
    }
}
```

### 2.3.3.3 在链表中删除第一个指定值的结点

```c++
void RemoveNode(ListNode **pHead, int value){
    // 链表为空
    if(pHead==NULL||*pHead==NULL){
        return;
    }
    // 第一个结点
    ListNode *pToBeDeleted = NULL;
    ListNode *pNode = *pHead;
    if (pNode->m_nValue==value){
        *pHead = pNode->m_pNext;
        pToBeDeleted = pNode;
    }
    // 下一个结点
    else{
        int flag = 1;
        while(pNode->m_pNext!=NULL){
            if (pNode->m_pNext->m_nValue==value){
                pToBeDeleted = pNode->m_pNext;
                pNode->m_pNext = pNode->m_pNext->m_pNext;
                flag = 0;
                break;
            }
            pNode = pNode->m_pNext;
        }
    }

    if(pToBeDeleted !=NULL){
        delete pToBeDeleted;
        pToBeDeleted = NULL;
    }
}
```

## 补充1：结构体

1.一般形式的定义

```python
struct student
{
    char name[10];
    char sex;
    int age;
    float score;
};
```

2.定义结构体类型的变量、指针变量和数组

```python
# 方法一：定义结构体类型时，同时定义该类型的变量
struct [student] /* [ ]表示结构体名是可选的 */
{
    char name[10];
    char sex;
    int age;
    float score;
}stu1, *ps, stu[5]; /* 定义结构体类型的普通变量、指针变量和数组 */

# 方法二：先定义结构体类型，再定义该类型的变量
struct student
{
    char name[10];
    char sex;
    int age;
    float score;
};
struct student stu1, *ps, stu[5]; /* 定义结构体类型的普通变量、指针变量和数组 */

# 方法三：用类型定义符typedef先给结构体类型命别名，再用别名定义变量
typedef struct [student]
{
    char name[10];
    char sex;
    int age;
    float score;
}STU;

STU stu1, *ps, stu[5]; /* 用别名定义结构体类型的普通变量、指针变量和数组 */
```

3.给结构体变量赋初值

```python
struct [student]
{
    char name[10];
    char sex;
    int age;
    float score;
}stu1, *ps, stu[2]={{"Li", 'F', 22, 90.5}, {"Su", 'M', 20, 88.5}};
ps = &stu1;
```

4.引用结构体变量中的成员

```python
1) 结构体变量名. 成员名：      stu1.name
2) 结构体指针变量à成员名：     p->name
3) (*结构体指针变量). 成员名： (*ps).name
4) 结构体变量数组名. 成员名：  stu[0].name
```

5.结构体的大小与内存对齐

<http://www.cnblogs.com/zhengfa-af/p/8144786.html>

6.空指针

```c++
int *p
p = NULL;
printf("%d", p ); # 0，即p的值为0，而且地址为0的位置没有值。
printf("%d", *p): # 什么也不显示
```