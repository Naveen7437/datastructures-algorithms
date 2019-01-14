import java.util.Arrays;

class Pallindrome{
    public static void main(String [] args){
        String string = new String("malayalam");
        if (CheckPallindrome(string)){
            System.out.println("Yes, it is  pallindrome");
        }else{
            System.out.println("Not Pallindrome");
        }
    }

    public static boolean CheckPallindrome(String string){
        int high = string.length()-1;
        int low = 0;
        while (low < high){
            if (string.charAt(low) != string.charAt(high)){
                return false;
            }
            low ++;
            high --;
        }
        return true;
    }
}