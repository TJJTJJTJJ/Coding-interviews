// 第一种解法
public class Solution {
	/**
	 * 判断是否是数字
	 * @param str
	 * @return
	**/
	public boolean isNumeric(char[] str){
		return str != null && str.length != 0 && new String(str).matches("[+-]?\\d*(\\.\\d+)?([eE][+-]\\d+)?"); 
	}
}

// 第二种解法
public class Solution {
	private int index = 0;
	/**
	 * 判断是否是数字
	 * @param str
	 * @return
	**/
	public boolean isNumeric(char[] str){
		if (str=== null || str.length==0){
			return false;
		}
		// 判断是否存在整数部分
		boolean flag = scanInteger(str)

		// 判断是否存在小数部分，特殊情况 .333
		if(index<str.length&&str[index]=='.'){
			index++;
			flag = scanUnsignedInteger(str)
		}
		// 判断有没有指数
		if(index<str.length&&(str[index]=='e' || str[index]=='E')){
			index++;
			flag = scanInteger(str) && flag;
		}

		return flag && index==str.length;
	}
	



	private boolean scanInteger(char[] str){
		while (index<str.length && str[index]=='+' || str[index]=='-'){
			index++;
		}

		return scanUnsignedInteger()
	}

	private boolean scanUnsignedInteger(char[] str){
		int start = index;
		while(index<str.length&&str[index]>='0'&&str[index]<='9'){
			index++;
		}
		return start < index;
	}
}