#coding= UTF-8
'''
题目：  给定一个字符 找出不含有重复字符的最长子串长度

示例： 给定 ‘abcabcbb’ 没有重字符的的最长子串的 ‘abc’ 最长的子串长度为 3
 给定 ‘bbbb' 最长子串的长度为‘b'  长度为1

'''
'''
a = input("请输入一个字符串")
d ={ }

for index,item in enumerate(a):
    
    if item not in d:
        d = d.append(item)
    else :
	print(index,item)
'''
def find_longest_no_repeat_substr(one_str):  
    ''''' 
    找出来一个字符串中最长不重复子串 
    '''  
    res_list=[]  
    length=len(one_str)  
    for i in range(length):  
        tmp=one_str[i]  
        for j in range(i+1, length):  
            if one_str[j] not in tmp:  
                tmp+=one_str[j]  
            else:  
                break  
        res_list.append(tmp)  
    #res_list.sort(lambda x,y:cmp(len(x),len(y)))  
    l = 0
    for i in res_list:
	    length = len(i)
	    if length > l:
		    l = length
		    d = []
		    d += i
	    else:
		    continue
    return (l,d)


s = "eeydgwdykpv"
print(find_longest_no_repeat_substr(s))
