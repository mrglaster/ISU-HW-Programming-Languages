package special_hashmap.special_hashmap

import special_hashmap.data_providers.ILocProvider
import special_hashmap.data_providers.PLocProvider


class SpecialHashMap:HashMap<String, Any?>() {

    val iloc: ILocProvider
        get() = ILocProvider(this)

    val ploc: PLocProvider
        get() = PLocProvider(this)
}
