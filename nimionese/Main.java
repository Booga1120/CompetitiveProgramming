package nimionese;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        HashSet<Character> hardCons = new HashSet<>(
            Arrays.asList('b', 'c', 'd', 'g', 'k', 'n', 'p', 't',
                          'B', 'C', 'D', 'G', 'K', 'N', 'P', 'T'));
        HashSet<Character> vowels = new HashSet<>(
            Arrays.asList('a', 'e', 'i', 'o', 'u',
                          'A', 'E', 'I', 'O', 'U'));
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        String result = "";
        boolean isFirst = true;
        char firstLetter = ' ';
        boolean isMiddleSyllable = false;
        int nexti = 0;

        for (char x : line.toCharArray()) {
            nexti++;
            if(x == ' '){//deal with first letter of new word
                result += x;
                isFirst = true;
            }else if (isFirst) {
                char nearestHard = findNearestHard(x);
                result += nearestHard;
                firstLetter = line.charAt(nexti - 1);
                //System.out.println("First Letter is now: "+firstLetter);
                isFirst = false;
                
                if(nexti >= line.length() || line.charAt(nexti)==' '){//deal with single letter words
                    if(hardCons.contains(nearestHard)){
                        result += findNearestSoft(x);
                    }
                }
            }else if (x == '-') {//deal with syllables
                isMiddleSyllable = true;
            } else if (isMiddleSyllable) {
                boolean isUpperCase = Character.isUpperCase(x);
                boolean isSoft = !(hardCons.contains(x));
                if(vowels.contains(x) || isSoft){
                    result += x;
                }else if(isUpperCase){
                    result += Character.toUpperCase(firstLetter);
                }else{
                    result += Character.toLowerCase(firstLetter);
                }
                isMiddleSyllable = false;
            }else if(nexti >= line.length() || line.charAt(nexti)==' '){//deal with last letter of word
                if(hardCons.contains(x)){
                    result += findNearestSoft(x);
                }else{
                    result += x;
                }
            }else result += x;//else
        }
        System.out.println(result);
    }

    public static char findNearestHard(char a) {
        boolean isUpperCase = Character.isUpperCase(a);
        if(isUpperCase){
            a = Character.toLowerCase(a);
        }
        char[] hard = {
            'b', 'c',
            'd', 'g',
            'k', 'n',
            'p', 't'
        };

        char closest = hard[0];
        int best = 26;
        for (int i = 0; i < hard.length; i++) {
            int diff = Math.abs((int) a - (int)hard[i]);
            //System.out.println("a: "+a+","+(int)a+" hardi: "+hard[i]+","+(int)hard[i] + " diff:" + diff+" inta: "+ (int)a);
            if (diff < best) {
                best = diff;
                closest = hard[i];
            }
        }

        if (isUpperCase) {
            closest = Character.toUpperCase(closest);
        }
        return closest;
    }

    public static String findNearestSoft(char a){
        int[] hard = {
            (int) 'a',(int) 'o',
            (int) 'u'};
        char closest = (char)hard[0];
        int best = 26;
        for (int i = 0; i<hard.length; i++){
            char hardi = (char)hard[i];
            hard[i] = Math.abs((int)a - (int)hardi);
            if(hard[i]<best){
                best = hard[i];
                closest = hardi;
            }
        }
        return ""+closest+"h";
    }
}