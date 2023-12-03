import org.junit.jupiter.api.Assertions
import org.junit.jupiter.api.DisplayName
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.assertThrows
import org.junit.platform.commons.annotation.Testable
import special_hashmap.exception.SpecialHashMapException
import special_hashmap.special_hashmap.SpecialHashMap

@Testable
class TestSpecialHashMap {

    @Test
    @DisplayName("Regular key access test")
    fun testRegularAccess(){
        val demoSpecialHashMap: SpecialHashMap = SpecialHashMap()
        demoSpecialHashMap["value1"] = 1
        demoSpecialHashMap["2"] = 20
        demoSpecialHashMap["5, 5"] = 200
        Assertions.assertEquals(demoSpecialHashMap["value1"], 1)
        Assertions.assertEquals(demoSpecialHashMap["2"], 20)
        Assertions.assertEquals(demoSpecialHashMap["5, 5"], 200)
    }

    @Test
    @DisplayName("Test alphabet sort")
    fun  testItemsAccess(){
        val demoSpecialHashMap: SpecialHashMap = SpecialHashMap()
        demoSpecialHashMap["value1"] = 1
        demoSpecialHashMap["value2"] = 2
        demoSpecialHashMap["value3"] = 3
        demoSpecialHashMap["1"] = 10
        demoSpecialHashMap["2"] = 20
        demoSpecialHashMap["3"] = 30
        demoSpecialHashMap["1, 5"] = 100
        demoSpecialHashMap["5, 5"] = 200
        demoSpecialHashMap["10, 5"] = 300
        Assertions.assertEquals(demoSpecialHashMap.iloc[0], 10)
        Assertions.assertEquals(demoSpecialHashMap.iloc[2], 300)
        Assertions.assertEquals(demoSpecialHashMap.iloc[5], 200)
        Assertions.assertEquals(demoSpecialHashMap.iloc[8], 3)
    }

    @Test
    @DisplayName("Out of bounce access test")
    fun testOutOfBounceAccess(){
        val demoSpecialHashMap: SpecialHashMap = SpecialHashMap()
        demoSpecialHashMap["value1"] = 1
        demoSpecialHashMap["value2"] = 2
        assertThrows<IndexOutOfBoundsException> {
            val ara = demoSpecialHashMap.iloc[100]
        }
    }

    @Test
    @DisplayName("Single Condition test")
    fun testPlocWithSingleCondition() {
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
        val result = map.ploc[">=1"]
        val expected = SpecialHashMap()
        expected["1"] = 10
        expected["2"] = 20
        expected["3"] = 30
        Assertions.assertEquals(expected, result)
    }

    @Test
    @DisplayName("Two conditions test")
    fun testTwoConditions(){
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
        val result = map.ploc[">0, >0"]
        val expected = SpecialHashMap()
        expected["(1, 5)"] = 100
        expected["(5, 5)"] = 200
        expected["(10, 5)"] = 300
        Assertions.assertEquals(expected, result)

    }

    @Test
    @DisplayName("Several conditions test")
    fun testSeveralConditions(){
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
            val result = map.ploc["<5, >=5, >=3"]
            val expected = SpecialHashMap()
            expected["(1, 5, 3)"] = 400
            Assertions.assertEquals(expected, result)
    }

    @Test
    @DisplayName("Other Separators test")
    fun testOtherSeparators() {
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
        val result = map.ploc["<5 a  >=5 a >=3"]
        val expected = SpecialHashMap()
        expected["(1, 5, 3)"] = 400
        Assertions.assertEquals(expected, result)
    }

    @Test
    @DisplayName("Test exception throw")
    fun testThrowException(){
        assertThrows<SpecialHashMapException> {
            throw  SpecialHashMapException("Test")
        }
    }

    @Test
    @DisplayName("Unsupported operator test")
    fun testUnsupportedOperator(){
        val map = SpecialHashMap()
        map["value1"] = 1
        map["(1, 12)"] = 1
        assertThrows<SpecialHashMapException> {
            println(map.ploc["1 >, > 12"])
        }
    }

    @Test
    @DisplayName("Test Other Operators")
    fun testOtherOperators(){
        val map = SpecialHashMap()
        map["value1"] = 1
        map["(1, 12)"] = 1
        val res = map.ploc["!=0, =12"]
        val res1 = map.ploc["!=0, <=12"]
        val exp = SpecialHashMap()
        exp["(1, 12)"] = 1
        Assertions.assertEquals(res, exp)
        Assertions.assertEquals(res, res1)
    }
}