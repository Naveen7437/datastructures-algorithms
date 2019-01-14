
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.Stream;


class NumberGame{
    public static void main(String[] args){
        Integer num = GetMinOpertaions( 90);
        System.out.println(num);
    }
    public  static Integer GetMinOpertaions(Integer number){
        String binaryFormat = Integer.toBinaryString(number);
        List <String> binaryFormatList = Arrays.asList(binaryFormat.split(""));
        List<Integer> binaryIntergerList = binaryFormatList.stream()
                .map(s->Integer.parseInt(s))
                .collect(Collectors.toList());

        List<Double> operations = new ArrayList<>();
        int listSize = binaryIntergerList.size();

        for (int i=0; i<listSize; i++){
            if (binaryIntergerList.get(i) != 0){
                operations.add(Math.pow(2, listSize - i) -1);
            }
        }
        for (int i=listSize-2 ; i>=0; i--){
            try {
                operations.set(i, operations.get(i)- operations.get(i+1));
            }catch (Exception e){
                e.printStackTrace();
            }
        }
        return operations.get(0).intValue();
    }
}