// v-0.0
public class Solution {
    public String replaceSpace(StringBuffer str) {
    	// boundary condition
        if (str == null || str.length()==0){
            return str.toString();
        }
        
        StringBuffer ss = new StringBuffer();
        
        int len = str.length();
        for(int i=0;i<len; ++i){
            char ch = str.charAt(i);
            ss.append(ch == ' ' ? "%20": ch);
        }
        return ss.toString();
            
    }
}