import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static ArrayList<Integer> A = new ArrayList<>();
    static int N = 0;
    static int LB = 0;
    static int Size = 7;
    static int operations = 5;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < operations; i++) {
            System.out.println("Select one Operation in given below");
            System.out.println("For Traversing press 1");
            System.out.println("For Insertion press 2");
            System.out.println("For Searching press 3");
            System.out.println("For Deletion press 4");
            System.out.println("For Exit press 5");
            System.out.println("...........................");
            int OP = scanner.nextInt();

            switch (OP) {
                case 1:
                    System.out.println(OP + ": Traverse Selected");
                    Traverse();
                    break;
                case 2:
                    System.out.println(OP + ": Insetion Selected");
                    Insertion();
                    break;
                case 3:
                    System.out.println(OP + ": Searching Selected");
                    Searching();
                    break;
                case 4:
                    System.out.println(OP + ": Deletion Selected");
                    Deletion();
                    break;
                case 5:
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Invalid Option");
            }
        }
    }

    // Traversing Program
    static void Traverse() {
        for (int i = LB; i < N + LB; i++) {
            System.out.print(A.get(i) + ",");
        }
        System.out.println("...........................");
    }

    // Insertion Program
    static void Insertion() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the element you want to insert:");
        int Item = scanner.nextInt();
        System.out.println("Enter the index where you want insertion");
        int K = scanner.nextInt();

        if (N == Size) {
            System.out.println("Overflow");
        } else {
            if (K < LB || K > N + LB) {
                System.out.println("K is Invalid");
            } else {
                A.add(K, Item);
                N++;
                System.out.println("Now the array elements are ");
                for (int i = 0; i < N; i++) {
                    System.out.print(A.get(i) + ",");
                }
                System.out.println("...........................");
            }
        }
    }

    // Deletion Program
    static void Deletion() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the index where you want deletion");  // position to delete
        int K = scanner.nextInt();

        if (N == 0) {
            System.out.println("Underflow");
        } else {
            if (K < LB || K > N + LB - 1) {
                System.out.println("K is Invalid");
            } else {
                A.remove(K);
                N--;
                System.out.println("Now the array elements are ");
                for (int i = 0; i < N; i++) {
                    System.out.print(A.get(i) + ",");
                }
                System.out.println("...........................");
            }
        }
    }

    // Searching Program
    static void Searching() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Select one Operation in given below");
        System.out.println("For Single Binary Search press 1");
        System.out.println("For Multi Binary Search press 2");
        System.out.println("For Single Linear Search press 3");
        System.out.println("For Multi Linear Search press 4");
        System.out.println("...........................");
        int OP = scanner.nextInt();

        switch (OP) {
            case 1:
                System.out.println(OP + ": Binary Single Search.....");
                System.out.println("Enter the item you want to search: ");
                int Item = scanner.nextInt();
                BinarySearch(Item);
                break;
            case 2:
                System.out.println(OP + ": Binary Multi Search.....");
                System.out.println("Enter the items you want to search, separated by space: ");
                String[] items = scanner.nextLine().split(" ");
                MultiBinarySearch(items);
                break;
            case 3:
                System.out.println(OP + ": Linear Single Search.....");
                System.out.println("Enter the item you want to search: ");
                Item = scanner.nextInt();
                LinearSearch(Item);
                break;
            case 4:
                System.out.println(OP + ": Linear Multi Search.....");
                System.out.println("Enter the items you want to search, separated by space: ");
                items = scanner.nextLine().split(" ");
                MultiLinearSearch(items);
                break;
            default:
                System.out.println("Invalid Option");
        }
    }

    static void BinarySearch(int Item) {
        int low = LB;
        int high = N + LB - 1;

        while (low <= high) {
            int mid = (low + high) / 2;
            if (A.get(mid) < Item) {
                low = mid + 1;
            } else if (A.get(mid) > Item) {
                high = mid - 1;
            } else {
                System.out.println("Item " + Item + " found at position " + mid);
                return;
            }
        }
        System.out.println("Item " + Item + " not found");
    }

    static void MultiBinarySearch(String[] items) {
        for (String item : items) {
            BinarySearch(Integer.parseInt(item));
        }
    }

    static void LinearSearch(int Item) {
        for (int i = LB; i < N + LB; i++) {
            if (A.get(i) == Item) {
                System.out.println("Item " + Item + " found at position " + i);
                return;
            }
        }
        System.out.println("Item " + Item + " not found");
    }

    static void MultiLinearSearch(String[] items) {
        for (String item : items) {
            LinearSearch(Integer.parseInt(item));
        }
    }
}
