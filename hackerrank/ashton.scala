import scala.collection.mutable
// import
object what {

    def ashtonString(s: String, k: Int): Char = {
        val len: Int = s.length()
        val set = mutable.HashSet[String]()
        for (i <- 0 to len; j <- i to len) {
            val slice = s.slice(i, j)
            if (slice.nonEmpty) set += slice
        }
        val clean = set.toVector.sorted
        var idx: Int = 0
        var i = 0
        var res = 0

        while (idx < k) {
            val next = clean(i)
            val size = next.size            
            if (idx + size >= k - 1) { res = idx }
            i += 1
            idx += size
        }
        clean(i - 1)(k - 1 - res)
    }

    def main(args: Array[String]): Unit = {

        val s = "zsbhetzecbhhepbqrrxwoipsrnqfaplbjmiqgkwklesrvvhmpeidnzxgopnphyqqnbitlfdwlxpgtxtibblqdlyramihkzazcisppynaxchqzcadfotizuazgihsjhsnrmchmphksqcruduatqkskktsvcmgjeudtwkfmtrgmuxgzugsmrmwdfqyichtjbwexijlcdtoxtuyndqzwcxbhnarrhlckjgjssvuvokuhgswjixhmujvjlnduafejmnbgkxbzhviophzzehlbsgkdvpxxvdhjqkpdiscrpmhethdaqqbkynnudmrapalhlckvuooldwryfuyxmzhknugsiaszafinhtkdjzqoxhncdlzpngbaciumimlkttyaokfylvoicbmhpnwctxcxhyjpmwafqahemmeyjtinwvulisneprdxppoblqgdsnkfbodmjlziittrlhxdaacqpstdjcgbrqgthlfqzhyhcuaodztdaxvrppuarbcitkdawltxstewnhmqgfwieraugwuzzyktjnthaoeuikrxtdoclkkpdmlklilkivdtlzanpgixtbvmglqrxbjapwmaeylpvqiirlwhrggmhbzpophlssoioakvavkyoughfcozkvlrymhpeqawkqgatrvvohteecmjeairxuiygrnkjpjvgpwzitwzbqdfspqyszprvapbteofuxacowdzqzytpbajtqilpzckzuovycasbaupzzopzmiqqiajakwqjyclsqiruilvkiljhbagqkzguzrvlnlunphggpzazkykujvcmwkcgjkbkdwvsjsgyzogrnjqzhauswweuijcsvdczbarksxlrlriaabahbubzsgvaryumbzlfzfprcckquvqwwqgzmhzepuhgubtwagbzlssovfgrawnwptxddykstrzpsslvyowkjpaguizwgmuvirbnqlflceawyorzeolnflvbvuxbjtztkagcllnpsqlqgfrkvcaapvdksambvlwfnckypzphpca"
        // val s = "dbac"
        // println(s.size)
        // val s = "dbacdbacdbacdbacdbacdbacdbacdbacdbacdbacdbacdbacdbac"
        val k = 3
        println(ashtonString(s, k))

    }

}