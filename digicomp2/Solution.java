import java.util.*;

public class Solution {
    static class Orientation {
        String state;
        int left;
        int right;
        
        Orientation(String state, int left, int right) {
            this.state = state;
            this.left = left;
            this.right = right;
        }
    }
    
    static Orientation[] orientations;
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long balls = sc.nextLong();
        int paddles = sc.nextInt();
        
        orientations = new Orientation[paddles];
        for (int paddle = 0; paddle < paddles; paddle++) {
            String isLeft = sc.next();
            int leftnum = sc.nextInt();
            int rightnum = sc.nextInt();
            orientations[paddle] = new Orientation(isLeft, leftnum - 1, rightnum - 1);
        }
        
        flip(0, balls);
        
        StringBuilder result = new StringBuilder();
        for (Orientation orientation : orientations) {
            result.append(orientation.state);
        }
        System.out.println(result.toString());
    }
    
    static void flip(int switchIndex, long b) {
        Orientation current = orientations[switchIndex];
        if (current.state.equals("L")) {
            if (b % 2 == 1) {
                orientations[switchIndex] = new Orientation("R", current.left, current.right);
                if (current.left != -1) {
                    flip(current.left, b / 2 + 1);
                }
            } else {
                if (current.left != -1) {
                    flip(current.left, b / 2);
                }
            }
            if (current.right != -1) {
                flip(current.right, b / 2);
            }
        } else if (current.state.equals("R")) {
            if (b % 2 == 1) {
                orientations[switchIndex] = new Orientation("L", current.left, current.right);
                if (current.right != -1) {
                    flip(current.right, b / 2 + 1);
                }
            } else {
                if (current.right != -1) {
                    flip(current.right, b / 2);
                }
            }
            if (current.left != -1) {
                flip(current.left, b / 2);
            }
        }
    }
}