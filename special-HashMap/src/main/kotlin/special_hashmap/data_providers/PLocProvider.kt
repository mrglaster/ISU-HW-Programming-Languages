package special_hashmap.data_providers

import special_hashmap.exception.SpecialHashMapException
import special_hashmap.special_hashmap.SpecialHashMap

class PLocProvider(private val map: SpecialHashMap) {

    private fun unifySeparator(condition: String):String{
        val allowedChars = listOf('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '>', '<', '=', ' ', '!')
        val regex = "[^${allowedChars.joinToString("")}]".toRegex()
        return regex.replace(condition, ",")
    }


    private fun parseCondition(condition: String): Pair<String, Double> {
        val operators = setOf("<>", ">=", "<=", ">", "<", "!=", "=", )
        val operator = operators.find { condition.trim().startsWith(it) }
            ?: throw SpecialHashMapException("Unsupported operator: $condition")
        val value =  condition.replace(operator, "").trim().toDouble()
        return Pair(operator, value)

    }

    private fun checkSingleCondition(keyValue: Double, operator: String, value: Double): Boolean {
        return when (operator) {
            ">" -> keyValue > value
            "<" -> keyValue < value
            ">=" -> keyValue >= value
            "<=" -> keyValue <= value
            "=" -> keyValue == value
            "!=" -> keyValue != value
            else -> throw SpecialHashMapException("Something went wrong during operator parsing...")
        }
    }

    operator fun get(conditionSource: String): Map<String, Any?> {
        val condition = unifySeparator(conditionSource)
        val comaCount = condition.count { it == ',' }
        val result = SpecialHashMap()
        val conditionsList: List<String> = condition.split(",")

        for (item in map.keys.toSortedSet()) {
            if (item.count { it == ',' } == comaCount && (item.toIntOrNull() != null || item.count { it == ',' } > 0)) {
                val preparedElements: List<String> = item.replace("(", "").replace(")", "").split(",")
                var passedCounter = 0
                for (i in conditionsList.indices) {
                    val (operator, value) = parseCondition(conditionsList[i])
                    val keyVa =  preparedElements[i].trim().toDouble()

                    val conditionResult = checkSingleCondition(keyVa, operator, value)
                    if (!conditionResult) {
                        break
                    }
                    passedCounter++
                }

                if (passedCounter == conditionsList.size) {
                    result[item] = map[item]
                }
            }
        }
        return result
    }
}
