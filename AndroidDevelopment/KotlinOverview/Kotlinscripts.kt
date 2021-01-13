//Nisarg Patel CS-388 HW-1
import org.jsoup.Jsoup
import java.util.Scanner
import com.squareup.okhttp.OkHttpClient
import com.squareup.okhttp.Request
import org.json.JSONObject
fun main(args: Array<String>) {

    // Creates an instance which takes input from standard input (keyboard)
    intReview()
    senCount()
    stringDate()
    leapYear()
    RomanNum()
    isPrime()
    covidNJIT()
    covidCompare()

}

fun intReview(){

    val reader = Scanner(System.`in`)
    print("Enter the first integer: ")

    // nextInt() reads the next integer from the keyboard
    var integer:Int = reader.nextInt()

    print("Enter the second integer: ")

    // nextInt() reads the next integer from the keyboard
    var integer2:Int = reader.nextInt()

    println("You entered: $integer and $integer2")

    var sum = integer + integer2

    var product = integer * integer2

    var boolean_check = false

    if (sum % 2 == 0){
        boolean_check=true
        println("sum: $sum, product: $product, $boolean_check")
    }
    else {

        println("sum: $sum, product: $product, $boolean_check")
    }


}

fun senCount (){
    print("Write your sentence: ")

    val enteredString = readLine()

    println("You have entered this: $enteredString")
    var vcount=0
    var ccount=0

    if (enteredString != null)
    {
        for (item in enteredString){
            //println(item)

            if (item in "aeiou" )
            {
                vcount ++
            }
            else if (item in 'a'..'z' || item in 'A'..'Z'){
                ccount ++
            }
        }

        println(" $vcount Vowels and $ccount consonants ")
    }

}

fun stringDate (){

    print("Enter the date: ")

    val strDate: String = readLine().toString()

    println("You have entered this: $strDate")

    var ListDate = strDate.split(" ")

    //println(" $ListDate")
    //println(ListDate[1])

    var count = ListDate[1].length
    //println(count)

    if ( count > 1){

        var ListDates =""

        if ("th" in ListDate[1]){

            ListDates=ListDate[1].slice(0..1)
            //val day: Int = ListDates.toInt()
        }

        while (ListDate[0]!= "January" && ListDate[0]!= "February" && ListDate[0]!= "March" && ListDate[0]!= "April" && ListDate[0]!= "May" && ListDate[0]!= "June" && ListDate[0]!= "July" && ListDate[0]!= "August" && ListDate[0]!= "September" && ListDate[0]!= "October" && ListDate[0]!= "November" && ListDate[0]!= "December" && ListDate[1]!in "0..31" && "th" !in ListDate[1] && count <= 2)
        {
            println("invalid input")
            break

        }

        var month_counter = hashMapOf<String, Int>()
        month_counter.put("January", 1)
        month_counter.put("February", 2)
        month_counter.put("March", 3)
        month_counter.put("April", 4)
        month_counter.put("May", 5)
        month_counter.put("June", 6)
        month_counter.put("July", 7)
        month_counter.put("August", 8)
        month_counter.put("September", 9)
        month_counter.put("October", 10)
        month_counter.put("November", 11)
        month_counter.put("December", 12)

        if ("th" in ListDate[1]){

            val day: String = ListDates.toString()
            //println(ListDates)

            // val day: Int = ListDate[1].toInt()

            val year = ListDate[2].toInt()
            val month: String = ListDate[0].toString()

            val output = month_counter.toList().toMap()

            for (i in output) {
                if (month == i.key)
                {
                    var data: Int= i.value

                    println("0$data/$day/$year")
                    break
                }

            }
        }else {



            val days: String = ListDate[1]

            val year_date: String = ListDate[2].slice(2..3)

            val year: String = year_date
            val month: String = ListDate[0].toString()

            val output = month_counter.toList().toMap()

            for (j in output) {
                if (month == j.key)
                {
                    var data1: Int= j.value

                    println("0$data1/$days/$year")
                    break
                }

            }
        }

    }else{
        println("invalid input")
    }
/*
    var delimiter = " "
    val emptyStringArray = arrayOf<String>()

    for (item in enteredString){
   if (enteredString != null){
    var parts = enteredString.split(delimiter)
      parts= emptyStringArray[i]
      i++
    print(parts)

 */
}

fun leapYear (){
    val reader = Scanner(System.`in`)
    print("Enter the first integer: ")
    // nextInt() reads the next integer from the keyboard
    var year:Int = reader.nextInt()
    println("You entered: $year ")
    var leap = false
    if (year % 4 == 0) {
        if (year % 100 == 0) {
            // year is divisible by 400, hence the year is a leap year
            if (year % 400 == 0){
                leap = true
                println(leap)
            }
            else{
                leap = false
                println(leap)
            }
        }
        else
        {
            //println(year)
            leap = false
            println(leap)
        }
    } else{
        //println(year)
        leap = false
        println(leap)
    }
}

fun RomanNum ()
{

    val reader = Scanner(System.`in`)
    print("Enter the first integer: ")
    // nextInt() reads the next integer from the keyboard
    var num:Int = reader.nextInt()
    println("You entered: $num ")

    if (num > 0 && num < 5001){

        val number: IntArray = intArrayOf(1,4,5,9,10,40,50,90,100,400,500,900,1000)
        val roman_letter = arrayOf<String>("I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M")

        var index: Int = 12
        var n: Int = num

        while (n > 0){

            var b: Int = n/number[index]
            n = n % number[index]
            while ( b > 0){
                b = b - 1
                print (roman_letter[index])
            }
            index--
        }
        println()

    } else {
        println("invalid input")
    }

}

fun isPrime(){

    val reader = Scanner(System.`in`)
    print("Enter the first integer: ")

// nextInt() reads the next integer from the keyboard
    var num:Int = reader.nextInt()
    println("You entered: $num ")

    var flag = false

    if (num != 1) {

        for (i in 2..num / 2) {
            // condition for nonprime number
            if (num % i == 0 ) {
                //println(flag)
                flag = true
                //println(flag)
                break
            }
        }

        if (!flag){
            println(true)
        }
        else{
            println(false)

        }
    }
    else {
        println(flag)
    }
}

fun covidNJIT(){

    val data  = Jsoup.connect("https://www.njit.edu/pandemicrecovery/#tab-2").get()

    val bc = data.select("td h2 strong").text()

    val cd = bc.split(" ")

    println("Total Statistics: ")
    println("New cases ${cd[0]}")

    println("Total ${cd[1]}")

    println("recovery ${cd[2]}")

}


fun covidCompare(){
    val reader = Scanner(System.`in`)
    print("Enter the first country: ")
    var string1 = reader.nextLine()
    print("Enter the second country: ")
    var string2 = reader.nextLine()

    val client = OkHttpClient()
    var url:String = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total?country=$string1"
    val request = Request.Builder().url(url).get()
        .addHeader("x-rapidapi-host", "covid-19-coronavirus-statistics.p.rapidapi.com")
        .addHeader("x-rapidapi-key", "87adc4d21cmshd3a7b3db3027f58p169fc9jsn7409e72bbe79  ")
        .build()
    val response = client.newCall(request).execute()
    val temp = response.body().string()

    var json = JSONObject(temp)
    var obj = json["data"] as JSONObject
    val case1 = obj["confirmed"].toString().toInt()
    println("$string1 has $case1 confirmed cases")


    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total?country=$string2"
    val request1 = Request.Builder().url(url).get()
        .addHeader("x-rapidapi-host", "covid-19-coronavirus-statistics.p.rapidapi.com")
        .addHeader("x-rapidapi-key", " 87adc4d21cmshd3a7b3db3027f58p169fc9jsn7409e72bbe79").build()
    val response2 = client.newCall(request1).execute()
    val temp2 = response2.body().string()
    json = JSONObject(temp2)
    obj = json["data"] as JSONObject
    val case2 = obj["confirmed"].toString().toInt()
    println("$string2 has $case2 confirmed cases")

    if (case1 > case2){
        println("$string1 has higher number of cases")
    }else{
        println("$string2 has higher number of cases")
    }


}