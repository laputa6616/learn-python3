#!/usr/bin/env python3
#coding:utf-8

1 字典(dict)：使用 键-值(key-value)对 储存，但是不区分「存放顺序」

	1.1 字典的创建和访问(或添加)

		e.g.
		dic = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

		dic[key_name]				//访问

		dic[new_key] = value 		//添加新值

		注意：
		(1) 一个 key 只能对应一个 value，多次对一个 key 存放 value，后面的值会把前面的值冲掉；
		(2) 对不存在的 key 进行访问，会报「KeyError」错误，可以通过以下两种方法避免这种错误：

			(i) 通过 in 判断 key 是否存在：
				'Thomas' in dic  ->  False

			(ii) 通过 dict 提供的 get 方法，如果 key 不存在，可以返回 None，或者自己指定的值：
				dic.get('Thomas', -1)  ->  -1

		(3) 可以通过 dict 的 pop 方法删除某一 key-value 对：

			dic.pop(key_name)

		(4) 其实，在新 key-value对 存放进去的时候，dict 已经用「哈希算法(hash)」根据 key 计算出了 value 的存放位置，以后访问的时候就可以直接通过 key值 拿到 value值，不需要一个个查找，这也是 dict 具有「极快查找速度」的原因；
			为了保证 hash 的正确性，key 必须是「不可变对象」！！如字符串、整数，但 list 类型则是「可变对象」，因而不能作为 dict 的 key (unhashable type)；

		(5)	dict 和 list 比较：

			dict ：查找和插入的速度极快，不会随着key的增加而变慢；需要占用大量的内存，内存浪费多。
		
			而 list 相反：查找和插入的时间随着元素的增加而增加；占用空间小，浪费内存很少。

			所以，dict是用空间来换取时间的一种方法



2 集合(set)：和字典类似，只是 key 的「无序」集合，不存放 value

	2.1 集合的创建

		s = set(list)		//创建 set 需要提供 list 作为输入集合

		e.g.
		>>s = set([1, 2, 3])
		>>s
		{1, 2, 3}			//显示顺序不代表 set 有存放顺序！

		注意：
		(1) 重复元素在 set 里面会被自动过滤：s = set([1, 2, 2, 3]) = {1, 2, 3}；
		(2) set 和 dict 的唯一区别仅在于没有存储对应的 value，但是，set 的原理和dict一样，所以，同样不可以放入可变对象

	
	2.2 set 里面 key 的 添加 和 删除：

		>>s.add(4)
		>>s.remove(4)
	

	2.3 set 数学意义上的 交集、并集 运算

		>>> s1 = set([1, 2, 3])
		>>> s2 = set([2, 3, 4])
		>>> s1 & s2
		{2, 3}
		>>> s1 | s2
		{1, 2, 3, 4}
