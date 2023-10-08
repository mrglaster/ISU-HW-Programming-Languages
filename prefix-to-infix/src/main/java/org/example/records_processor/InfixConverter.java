package org.example.records_processor;
import java.util.Stack;

public class InfixConverter {

    /**List of all supported operators*/
    private static final String supportedOperators = "+-*/";

    /**Checks if current symbol is an operator*/
    private static boolean isOperator(String symbol){
        return supportedOperators.contains(symbol);
    }

    /**Checks if the String is numeric one*/
    private static boolean isNumericString(String inputData){
        return inputData.chars().allMatch( Character::isDigit );
    }

    /**Checks ratio of numbers and math operators in the input string*/
    private static void checkOperatorsRatio(String[] tokens){
        if (tokens.length < 3){
            throw new IllegalArgumentException("At least 3 space-divided string expected! Got: " + tokens.length);
        }
        int numbersCount = 0;
        int operatorsCount = 0;
        for (String i : tokens){
            if (i.length() == 0){
                throw new IllegalArgumentException("Error! Empty string got as a value!");
            }
            if (isOperator(i) && i.length() == 1) {
                operatorsCount++;
            } else if (isNumericString(i)){
                numbersCount++;
            } else {
                throw new IllegalArgumentException("Unknown operator! We cant continue. Number or math operator expected. Got: " + i);
            }
        }
        if (numbersCount == operatorsCount){
            throw new IllegalArgumentException("Same number of numbers and operators got! The input string should have at least N math operators and N+1 numbers!");
        }
        if (numbersCount > operatorsCount + 1){
            throw new IllegalArgumentException("You have too many numbers in your input string! The input string should have at least N math operators and N+1 numbers!");
        } else if (numbersCount < operatorsCount + 1){
            throw new IllegalArgumentException("You have too many math operators in your input string! The input string should have at least N math operators and N+1 numbers!");
        }

    }

    /** Converts prefix notation to the infix one */
    public static String convertPrefixToInfix(String record){

        if (record == null){
            throw new NullPointerException("A string expected! Got: null");
        }

        if (record.length() == 0){
            throw new IllegalArgumentException("Input string should have length greater than 0 !");
        }

        Stack<String> stack = new Stack<>();
        String[] tokens = record.split(" ");
        checkOperatorsRatio(tokens);

        for (int i = tokens.length - 1; i >= 0; i--) {
            String token = tokens[i];
            if (isOperator(token)) {
                String operand1 = stack.pop();
                String operand2 = stack.pop();
                String infixExpression = operand1 + " " + token + " " + operand2;
                stack.push(infixExpression);
            }
            else {
                stack.push(token);
            }
        }
        return stack.pop();
    }
}
