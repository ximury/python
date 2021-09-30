# 可利用回溯法的设计思想来解决背包问题。
# 首先将 n 件物品排成一列，依次选取；若装入某件物品后，背包内物品的总质量不超过背包最大装载质量时，则装入（进栈）；
# 否则放弃这件物品的选择，选择下一件物品试探，直至装入的物品总和正好是背包的最大转载质量为止。这时我们称背包装满。
# 若装入若干物品的背包没有满，而且又无其他物品可以选入背包，说明已装入背包的物品中有不合格者，需从背包中取出最后装入的物品（退栈）
# 然后在未装入的物品中挑选，重复此过程，直至装满背包（有解），或无物品可选（无解）为止。
from leet.栈 import SStack


def knapstack(weight, wlist):
    n = len(wlist)  # 可选的物品数量
    stack = SStack()  # 创建一个栈
    k = 0  # 当前所选择的物品游标
    while stack.is_empty() is not True or k < n:  # 栈不为空或者k<n
        while weight > 0 and k < n:  # 还有剩余空间并且有物品可装
            if weight >= wlist[k]:  # 剩余空间大于等于当前物品重量
                print(wlist[k])
                stack.push(k)  # 把物品装备背包
                weight -= wlist[k]  # 背包空间减少
            k += 1  # 继续向后找
        if weight == 0:  # 找到解
            print(stack._elems, end='----')
            # return True
        # 回退过程
        k = stack.pop()  # 把最后一个物品拿出来
        print(wlist[k])
        weight += wlist[k]  # 背包总容量加上w[k]
        print(weight)
        k += 1  # 装入下一个物品


if __name__ == '__main__':
    assert knapstack(100, [90, 40, 20, 10, 50]) is True
