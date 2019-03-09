public class Solution {
    public double Power(double base, int exponent) {
        final double eps = 0.00001;
        // 0的0次方是错误的
        if ((base-0.0) < eps && exponent == 0){
            return 0;
        }
        int absexponent=exponent;
        if(exponent<0){
            absexponent = -1*exponent;
        }
        double result;
        result = Power2(base, absexponent);
        if(exponent<0){
            result = 1/result;
        }
        return result;
    }
    public double Power2(double base, int absexponent){
        int a = absexponent;
        if (absexponent==0){
            return 1;
        }
        if (absexponent==1){
            return base;
        }
        double result;
        result = Power2(base, absexponent>>1);
        if ((absexponent & 0x1)==1){
            result = result * base * result;
        }
        else{
            result = result * result;
        }
        return result;
    }
}