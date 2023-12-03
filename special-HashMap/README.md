## Special HashMap

### Description


Develop an extension class for HashMap (Kotlin, Rust) or dict (Python) to organize additional ways to obtain elements.

First access method: access by key number, the keys must be sorted (toSortedSet method)

***Example:***
```
val map = SpecialHashMap()
map["value1"] = 1
map["value2"] = 2
map["value3"] = 3
map["1"] = 10
map["2"] = 20
map["3"] = 30
map["1, 5"] = 100
map["5, 5"] = 200
map["10, 5"] = 300

println(map.iloc[0])  // >>> 10
println(map.iloc[2])  // >>> 300
println(map.iloc[5])  // >>> 200
println(map.iloc[8])  // >>> 3
```

The second access method: selecting all key:value pairs based on a specific condition.

***Example:***

```
val map = SpecialHashMap()
map["value1"] = 1
map["value2"] = 2
map["value3"] = 3
map["1"] = 10
map["2"] = 20
map["3"] = 30
map["(1, 5)"] = 100
map["(5, 5)"] = 200
map["(10, 5)"] = 300
map["(1, 5, 3)"] = 400
map["(5, 5, 4)"] = 500
map["(10, 5, 5)"] = 600

println(map.ploc[">=1"]) // >>> {1=10, 2=20, 3=30}
println(map.ploc["<3"]) // >>> {1=10, 2=20}

println(map.ploc[">0, >0"]) // >>> {(1, 5)=100, (5, 5)=200, (10, 5)=300}
println(map.ploc[">=10, >0"]) // >>> {(10, 5)=300}

println(map.ploc["<5, >=5, >=3"]) // >>> {(1, 5, 3)=400}
```

***For second access:***

1) ​The following symbols are used for conditions: <. >, = and their combinations, for not equal the combination <> is used
2) The condition can contain any number of spaces
3) The condition uses only integer and real numbers
4) The separator can be any symbol except condition symbols and numbers.
5) The keys must match the number of conditions, i.e. if there are two numbers in the key and three in the condition, then such a key is ignored
6) Parentheses are optional and are ignored when selecting


***General requirements:***

1) Additional methods should be available via the iloc and ploc fields
2) An exception must be defined for invalid conditions
3) Tests must be written to test all code
4) The code can be implemented in one of the languages: Kotlin, Rust or Python.



### Tests coverage 

![изображение](https://github.com/mrglaster/ISU-HW-Programming-Languages/assets/50916604/d60158aa-2678-4e0d-b3da-e95309c485f9)
