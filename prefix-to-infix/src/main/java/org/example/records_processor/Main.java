package org.example.records_processor;
import java.util.Scanner;
import org.example.records_processor.InfixConverter;

public class Main {
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    String input = sc.nextLine();
    System.out.println(InfixConverter.convertPrefixToInfix(input));    
  }
}
