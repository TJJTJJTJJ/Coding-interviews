public class Solution {
	/** 
	* 打印从1到最大的n位数
	* @param n n位
	*/
	public void print1ToMaxOfNDigits(int n){
		if (n<1){
			return;
		}

		char[] chars = new char[n+1];
		for(int i=0; i<chars.length; i++){
			chars[i]='0';
		}
		
		while(!increment(chars)){
			printNumber(chars);
		}
	}

	/**
     * 数字加1
     * @param chars 数字数组
     * @return 是否溢出
     */
    private boolean increment(char[] chars){
		boolean isOverflow = false;
		int n = chars.length;
		int nTakeOver = 1;
		// 这里用参考给的代码，每次都是加1.

		for (int i=n-1; i>=0; i--){
			int num = chars[i]-'0'+nTakeOver;
			if(num>9){
				chars[i]='0';
			}
			else {
				++chars[i];
				break;
			}
		}

		// 判断是否超出
		if(chars[0]=='1'){
			isOverflow = true;
		}

		return isOverflow;
	}

	private void printNumber(char[] chars){
		boolean isBeginning0 = true;
		int n = chars.length;
		for (int i=0; i<n; i++){
			if (isBeginning0 && chars[i]!='0'){
				isBeginning0 = false;
			}
			if (!isBeginning0){
				System.out.print(chars[i]);	
			}
		}
		System.out.println();
	}
}