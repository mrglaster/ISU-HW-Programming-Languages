package special_hashmap.data_providers

import special_hashmap.special_hashmap.SpecialHashMap

class ILocProvider(private val map: SpecialHashMap){
    operator fun get(index: Int): Any {
        val sortedKeys = map.keys.toSortedSet()
        return map[sortedKeys.elementAt(index)] ?: throw ArrayIndexOutOfBoundsException("Index $index out of bounds")
    }
}