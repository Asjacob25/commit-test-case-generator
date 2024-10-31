import java.util.Random;
import java.util.Scanner;

public class RockPaperScissors {

    // Variables to track scores
    private static int userScore = 0;
    private static int computerScore = 0;
    private static int tieScore = 0;

    // Function to get the user's choice
    public static String getUserChoice() {
        Scanner scanner = new Scanner(System.in);
        String choice;
        while (true) {
            System.out.print("Enter your choice (rock, paper, scissors): ");
            choice = scanner.nextLine().toLowerCase();
            if (choice.equals("rock") || choice.equals("paper") || choice.equals("scissors")) {
                break; // valid choice
            }
            System.out.println("Invalid choice. Please try again.");
        }
        return choice;
    }

    // Function to get the computer's choice
    public static String getComputerChoice() {
        String[] choices = {"rock", "paper", "scissors"};
        Random random = new Random();
        return choices[random.nextInt(choices.length)];
    }

    // Function to determine the winner and update scores
    public static String determineWinner(String userChoice, String computerChoice) {
        if (userChoice.equals(computerChoice)) {
            tieScore++;
            return "It's a tie!";
        } else if ((userChoice.equals("rock") && computerChoice.equals("scissors")) ||
                   (userChoice.equals("paper") && computerChoice.equals("rock")) ||
                   (userChoice.equals("scissors") && computerChoice.equals("paper"))) {
            userScore++;
            return "You win!";
        } else {
            computerScore++;
            return "Computer wins!";
        }
    }

    // Function to display the current score
    public static void displayScore() {
        System.out.println("Score:");
        System.out.println("You: " + userScore);
        System.out.println("Computer: " + computerScore);
        System.out.println("Ties: " + tieScore);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String playAgain;

        do {
            String userChoice = getUserChoice();
            String computerChoice = getComputerChoice();

            System.out.println("Your choice: " + userChoice);
            System.out.println("Computer's choice: " + computerChoice);

            String result = determineWinner(userChoice, computerChoice);
            System.out.println(result);

            // Display the current score after each round
            displayScore();

            System.out.print("Do you want to play again? (yes/no): ");
            playAgain = scanner.nextLine().toLowerCase();
        } while (playAgain.equals("yes"));

        // Close the scanner
        scanner.close();
        System.out.println("Thank you for playing!");
    }
}
