import org.example.records_processor.InfixConverter;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.platform.commons.annotation.Testable;

@Testable
public class TestInfixConverter {

    @Test
    @DisplayName("Regular Work Test #1")
    void testRegularWork() throws Exception {
        String inputData = "+ - 13 4 55";
        String expectedResult = "13 - 4 + 55";
        Assertions.assertEquals(expectedResult, InfixConverter.convertPrefixToInfix(inputData));
    }

    @Test
    @DisplayName("Check too many strings in input")
    void testTooManyEmptyStrings(){
        String inputData = "+ 33         44            ";
        Assertions.assertThrows(IllegalArgumentException.class,
                ()->{
                    InfixConverter.convertPrefixToInfix(inputData);
                },
                "Error! Empty string got as a value!");

    }

    @Test
    @DisplayName("Unknown operator test")
    void testUnknownOperator(){
        String inputData = "++ 1 24 15 115";
        Assertions.assertThrows(IllegalArgumentException.class,
                ()->{
                    InfixConverter.convertPrefixToInfix(inputData);
                },
                "Unknown operator! We cant continue. Number or math operator expected. Got: ++");
    }

    @Test
    @DisplayName("Same amount of math operators and numbers")
    void testSameCount(){
        String inputData = "+ + 1 24";
        Assertions.assertThrows(IllegalArgumentException.class,
                ()->{
                    InfixConverter.convertPrefixToInfix(inputData);
                },
                "Same number of numbers and operators got! The input string should have at least N math operators and N+1 numbers!");
    }

    @Test
    @DisplayName("Too many numbers test")
    void testTooManyNumbers(){
        String inputData = "+ 24 24 24 24";
        Assertions.assertThrows(IllegalArgumentException.class,
                ()->{
                    InfixConverter.convertPrefixToInfix(inputData);
                },
                "You have too many numbers in your input string! The input string should have at least N math operators and N+1 numbers!");
    }

    @Test
    @DisplayName("Too many operators test")
    void testTooManyOperators(){
        String inputData = "+ + + + 12 24";
        Assertions.assertThrows(IllegalArgumentException.class,
                ()->{
                    InfixConverter.convertPrefixToInfix(inputData);
                },
                "You have too many math operators in your input string! The input string should have at least N math operators and N+1 numbers!");
    }

    @Test
    @DisplayName("Null input string")
    void testNullInputString(){
        String inputData = null;
        Assertions.assertThrows(NullPointerException.class,
                ()->{
                    InfixConverter.convertPrefixToInfix(inputData);
                },
                "A string expected! Got: null");
    }

    @Test
    @DisplayName("Zero length input string test")
    void testZeroLengthInputString(){
        String inputData = "";
        Assertions.assertThrows(IllegalArgumentException.class,
                ()->{
                    InfixConverter.convertPrefixToInfix(inputData);
                },
                "Input string should have length greater than 0 !");
    }

    @Test
    @DisplayName("Single number test")
    void testSingleNumber(){
        String inputData = "42";
        Assertions.assertThrows(IllegalArgumentException.class,
                ()->{
                    InfixConverter.convertPrefixToInfix(inputData);
                },
                "At least 3 space-divided string expected! Got: " + 1);

    }

    @Test
    @DisplayName("Single number test")
    void testSingleOperator(){
        String inputData = "+";
        Assertions.assertThrows(IllegalArgumentException.class,
                ()->{
                    InfixConverter.convertPrefixToInfix(inputData);
                },
                "At least 3 space-divided string expected! Got: " + 1);

    }
}
