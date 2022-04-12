import java.util.Scanner;

public class _20254 {
    public static void main(String[] shit) {
        Scanner sc = new Scanner(System.in);

        int U_R, T_R, U_O, T_O;
        U_R = sc.nextInt();
        T_R = sc.nextInt();
        U_O = sc.nextInt();
        T_O = sc.nextInt();

        System.out.println(56*U_R + 24*T_R + 14*U_O + 6*T_O);
    }
}
