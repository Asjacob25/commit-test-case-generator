import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.mockito.MockitoAnnotations;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.Assert.assertEquals;
import static org.mockito.Mockito.*;

public class RockPaperScissorsTest {

    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;

    @Before
    public void setUp() {
        System.setOut(new PrintStream(outContent));
        MockitoAnnotations.initMocks(this);
    }

    @After
    public void tearDown() {
        System.setOut(originalOut);
    }

    @Test
    public void testDetermineWinner_UserWins() {
        String result = RockPaperScissors.determineWinner("rock", "scissors");
        assertEquals("You win!", result);
    }

    @Test
    public void testDetermineWinner_ComputerWins() {
        String result = RockPaperScissors.determineWinner("paper", "scissors");
        assertEquals("Computer wins!", result);
    }

    @Test
    public void testDetermineWinner_Tie() {
        String result = RockPaperScissors.determineWinner("rock", "rock");
        assertEquals("It's a tie!", result);
    }

    @Test
    public void testGetComputerChoice_ValidChoices() {
        String choice = RockPaperScissors.getComputerChoice();
        boolean isValid = choice.equals("rock") || choice.equals("paper") || choice.equals("scissors");
        assertEquals(true, isValid);
    }

    @Test
    public void testDetermineWinner_InvalidUserInput() {
        String result = RockPaperScissors.determineWinner("lizard", "scissors");
        assertEquals("Invalid input. Please enter rock, paper, or scissors.", result);
    }

    @Test
    public void testDetermineWinner_InvalidComputerInput() {
        // As determineWinner method doesn't validate computer choice, this test ensures future implementation handles invalid inputs.
        String result = RockPaperScissors.determineWinner("rock", "lizard");
        assertEquals("Error: Computer choice is invalid.", result);
    }

    // Test getUserChoice method - assuming redesign for dependency injection or input/output abstraction for testing.
    @Test
    public void testGetUserChoice_ValidInput() {
        ByteArrayInputStream in = new ByteArrayInputStream("rock".getBytes());
        System.setIn(in);
        // Assuming getUserChoice now returns a String for the sake of testing
        String userChoice = RockPaperScissors.getUserChoice();
        assertEquals("rock", userChoice);
    }

    @Test
    public void testGetUserChoice_InvalidInput() {
        // Assuming functionality to handle invalid inputs is added
        ByteArrayInputStream in = new ByteArrayInputStream("gun".getBytes());
        System.setIn(in);
        // Assuming getUserChoice now returns a String or uses a mechanism to retry until a valid input is provided
        String userChoice = RockPaperScissors.getUserChoice();
        assertEquals("Invalid input. Please enter rock, paper, or scissors.", userChoice);
    }

    // Ensure cleanup
    @After
    public void restoreStreams() {
        System.setOut(originalOut);
        System.setIn(System.in);
    }
}