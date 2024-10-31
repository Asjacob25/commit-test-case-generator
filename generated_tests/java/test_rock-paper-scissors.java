import static org.junit.Assert.assertEquals;
import static org.mockito.Mockito.*;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

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
        // This test cannot mock Random's behavior without altering the method's access to Random.
        // However, it will call the method to ensure it doesn't throw an exception and returns a valid choice.
        String choice = RockPaperScissors.getComputerChoice();
        boolean isValid = choice.equals("rock") || choice.equals("paper") || choice.equals("scissors");
        assertEquals(true, isValid);
    }

    // Testing getUserChoice is difficult due to its reliance on System.in and System.out.
    // An alternative approach involves redesigning the method to support dependency injection for testing.

    // This demonstrates basic tests for the static methods. Ideally, the class should be refactored for better testability,
    // including not using static methods, which would allow for more effective use of mocking frameworks like Mockito.
}