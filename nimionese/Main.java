package nimionese;

import java.util.*;

class Main {
    public static void main(String[] args) {
        HashSet<Character> hardCons = new HashSet<>(
            Arrays.asList('b', 'c',
                                'd', 'g',
                                'k', 'n',
                                'p', 't',
                                'B', 'C',
                                'D', 'G',
                                'K', 'N',
                                'P', 'T'));
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        String result = "";
        boolean isFirst = true;
        boolean isSyllable = true;
        char firstLetter = ' ';
        int nexti = 0;

        for (char x : line.toCharArray()) {
            nexti++;
            if(x == ' '){
                result += x;
                isFirst = true;
                isSyllable = true;
            }else if (isFirst) {
                char nearestHard = findNearestHard(x);
                result += nearestHard;
                firstLetter = nearestHard;
                isFirst = false;
                
                if(nexti >= line.length() || line.charAt(nexti)==' '){
                    if(hardCons.contains(Character.toLowerCase(nearestHard))){
                        result += findNearestSoft(nearestHard);
                    }
                }
            }else if(x == '-'){
                isSyllable = false;
            }else if (!isSyllable && hardCons.contains(Character.toLowerCase(x))) {
                if(Character.isUpperCase(x)){
                    result += Character.toUpperCase(Character.toLowerCase(firstLetter));
                }else{
                    result += Character.toLowerCase(firstLetter);
                }
                
                if(nexti >= line.length() || line.charAt(nexti)==' '){
                    if(hardCons.contains(Character.toLowerCase(firstLetter))){
                        result += findNearestSoft(firstLetter);
                    }
                }
            }else if(nexti >= line.length() || line.charAt(nexti)==' '){
                if(hardCons.contains(Character.toLowerCase(x))){
                    result += x + findNearestSoft(x);
                }else{
                    result += x;
                }
            }else if(x != '-') {
                result += x;
            }
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
        char[] soft = {'a','o','u'};
        char closest = soft[0];
        int best = 26;
        for (int i = 0; i < soft.length; i++){
            char softi = soft[i];
            int diff = Math.abs((int)Character.toLowerCase(a) - (int)softi);
            if(diff < best){
                best = diff;
                closest = softi;
            }
        }
        return "" + closest + "h";
    }
}