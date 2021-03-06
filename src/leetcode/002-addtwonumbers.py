# https://leetcode.com/problems/add-two-numbers/description/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def append(self, listNode, x):
        """
        给ListNode追加元素

        :param listNode:
        :param x:
        :return:
        """
        while listNode.next != None:
            listNode = listNode.next
        listNode.next = ListNode(x)


    def addTwoNumbers(self, l1, l2):
        head = None

        self.carry = 0  # 进位项

        # 以l1为主表进行遍历加和
        while l1 != None:

            # 累加
            if l2 != None:
                sum = l1.val + l2.val + self.carry
                l2 = l2.next # 当l2的next不为空时，l2向后移动
            else:
                sum = l1.val + self.carry

            # 保存 并 计算下一次进位
            head = self.add(head, sum)

            l1 = l1.next

        while l2 != None:
            # 累加
            if self.carry == 1:
                sum = l2.val + 1
            else:
                sum = l2.val

            # 保存 并 计算下一次进位
            self.add(head, sum)

            l2 = l2.next

        if self.carry == 1:
            self.append(head,1)

        return head

    def add(self, head, sum):
        """
        计算当前的元素和

        :param head:
        :param sum:
        :return:
        """
        self.carry = 0

        if sum > 9:
            self.carry = 1
            sum = sum % 10

        if head == None:
            head = ListNode(sum)
        else:
            self.append(head, sum)

        return head


solution = Solution()

def print_list_node(listNode):
    while listNode != None:
        print(listNode.val)
        listNode = listNode.next

l1 = ListNode(2)
solution.append(l1, 4)
solution.append(l1, 3)

l2 = ListNode(5)
solution.append(l2, 6)
#solution.append(l2, 4)

print_list_node(solution.addTwoNumbers(l1,l2))
