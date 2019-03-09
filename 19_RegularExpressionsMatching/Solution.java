public class Solution {
	/**
	* 判断字符串是否与模式串匹配
	* @param str 字符串
	* @param pattern 模式串
	* @return 是否匹配 
	*/
	public boolean match(char[] str, char[] pattern){
		if (str==null||pattern==null){
			return false;
		}
		return strmatch(str, 0, str.length, pattern, 0, pattern.length);
	}

	public boolean strmatch(char[] str, int i, int len1, char[] pattern, int j, int len2){
		// 正常结束条件1，字符串和模式串都匹配完成
		if (i==len1&&j==len2){
			return true;
		}
		// 正常结束条件2，字符串已经结束，模式串剩余的都是a*
		if (i==len1){
			if (j+1<len2&&pattern[j+1]=='*'){
				return strmatch(str, i, len1, pattern, j+2, len2);
			}
			else {
				return false;
			}

		}
		//错误结束： 模式串已经结束，字符串还没有结束，为了保证下面访问的时候不越界
		if(i<len1&&j==len2){
			return false;
		}

		// 情况一：第二个字符是*
		if(j+1<len2 && pattern[j+1]=="*"){
			if(str[i]==pattern[j] || pattern[j]=='.'){
				return strmatch(str, i+1, len1, pattern, j, len2) || strmatch(str, i, len1, pattern, j+2, len2);
			}
			else{
				return strmatch(str, i, len1, pattern, j+2, len2);
			}
		}
		// 情况二：第二个字符是.
		if(j+1<len2 && pattern[j+1]=="."){
			return strmatch(str, i+1, len1, pattern, j+1, len2);
		}
		// 情况三：其他
		if(str[i]==pattern[j]){
			return strmatch(str, i+1, len1, pattern, j+1, len2);
		}
		return false;
	}
}
