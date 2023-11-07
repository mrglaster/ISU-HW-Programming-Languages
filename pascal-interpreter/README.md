##  Simplified Pascal Interpreter

### Description 

Based on the code from practical classes, develop an interpreter for a simplified version of the Pascal language.
The interpreter must output the values ​​of all variables used in the program, for example, in the form of a dictionary.
You can use the following code blocks to check functionality: 

1)

```
BEGIN
END.
```

2) 

```
BEGIN
	x:= 2 + 3 * (2 + 3);
        y:= 2 / 2 - 2 + 3 * ((1 + 1) + (1 + 1));
END.
```

3) 

```
BEGIN
    y: = 2;
    BEGIN
        a := 3;
        a := a;
        b := 10 + a + 10 * y / 4;
        c := a - b;
    END;
    x := 11;
END.
```

General requirements:

1) Tests must be written to test all code
2) The code can be implemented in one of the languages: Kotlin, Rust or Python.


### Coverage Report 

![изображение](https://github.com/mrglaster/ISU-HW-Programming-Languages/assets/50916604/6a9948a1-6667-4dc4-ac47-74426515895c)


