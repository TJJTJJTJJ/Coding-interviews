public class Solution {
	class ListNode {
		int val;
		ListNode next;
	}

	public ListNode deleteNode(ListNode head, ListNode tobeDelete){
		if (head==null||tobeDelete==null){
			return head;
		}

		// 删除的不是尾节点
		if(tobeDelete.next != null){
			tobeDelete.val = tobeDelete.next.val;
			tobeDelete.next = tobeDelete.next.next;
		}
		// 删除的是尾节点
		// 只有一个节点时
		else if (head==tobeDelete){
			head = null;
		}
		// 有多个节点
		// 这里作者直接用的是令尾节点为null
		/*
		node1.next = node2;
		node2 = null;
		<==>
		nodel.next = null;
		*/
		else{
			tobeDelete = null;
		}

		return head;
	}
}