#!/usr/bin/env python3
#coding:utf-8

1 列表(list)：一种可变的有序集合

	1.1 列表的创建和列表元素的访问
		
		e.g.
			classmates = ['hhqy', 'Nauh', 'laputa']
			
			classmates[index_num]
			
		注意：
		(1) Python 的索引号都是从 0 开始的；
		(2) index_num 的取值范围为 [-len(classmates), len(classmates)-1]；
		(3) 列表中元素可以是不同的数据类型；
		(4) 空列表：void = []；
		(5) 列表中的元素也可以是列表，可以用索引递归访问，如：list[3][2] = (list[3])[2]

	1.2 列表操作：

		list.append(new_value)					// 追加新元素至末尾
		list.insert(index_num, new_value)		// 把新元素插入指定索引位置 
		list.pop(index_num)/list.pop()			// 删除置顶索引位置元素或直接删除最后一个元素
		
		list[index_num] = new_value				// 用新值替换指定索引值

	1.3 列表切片：
	
			list[n:m:s]
	
		表示取列表list中索引号从 n 开始，步长为 s，到（m-1）结束的元素所构成的list。
	
		注意：
		(1) 负数切片 list[-n:] 表示依次取列表list后 n 位元素所构成的list，此时步长仍为1；
		(2) 其他比较特殊、需要注意的切片：

			  list[:]     原样复制list；
			  list[::2]   从原list中「第一个元素」开始，以步长为2截取切片，即「偶数」索引切片，类似的「奇数」索引切片：list[1::2]；
			  list[::-1]  反向复制list (原list「倒序」排列);
		
		(3) tuple 和 字符串 也可以用切片操作，结果仍为 tuple 和 字符串，操作方法与列表类似:
		e.g. (0, 1, 2, 3)[:2] = (0, 1)
		     'ABCD'[:2] = 'AB'

2 元组(tuple)：一种「不」可变的有序集合，和列表类似，只是一旦确定下来就无法更改

	2.1 元组的创建
	
		e.g.
			classmates = ('hhqy', 'Nauh', 'laputa')

		注意：
		(1) 只含一个元素的元组：(1,)，切忌省略掉逗号的写法 (1) = 1；
		(2) 元组的访问与列表相同，但是「没有」列表类似的操作方式(1.2)；
		(3) 元组的「不可变性」：元组元素的指向不可变，元组元素本身肯能会变，如元组元素是列表，该列表的值是可以变化的：
			>>> t = ('a', 'b', ['A', 'B'])
			>>> t[2][0] = 'X'
			>>> t[2][1] = 'Y'
			>>> t
			('a', 'b', ['X', 'Y'])