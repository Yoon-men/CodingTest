import java.util.Scanner;

public class _18301 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int shit, bullShit, holyShit;
        shit = sc.nextInt();
        bullShit = sc.nextInt();
        holyShit = sc.nextInt();

        System.out.println((shit + 1)*(bullShit + 1)/(holyShit + 1) - 1);
    }
}
