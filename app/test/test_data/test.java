import java.util.Scanner;
import java.lang.Math;

class solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine(); // reads string
        sc.close();
        String[] arg = str.split(" ");
        double a = Double.parseDouble(arg[0]);
        double b = Double.parseDouble(arg[1]);
        System.out.println(calculate(a, b));
    }

    public static Integer calculate(double a, double b) {
        return (int) Math.pow(a, b);
    }
}