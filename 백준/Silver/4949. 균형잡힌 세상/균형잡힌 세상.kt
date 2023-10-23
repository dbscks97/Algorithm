import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val sb = StringBuilder()

    while (true) {
        val sentence = br.readLine()
        val stack = Stack<Char>()

        if (sentence == ".") {
            break
        } else {
            for (char in sentence) {
                when (char) {
                    '(', '[' -> stack.push(char)
                    ')' -> {
                        if (stack.isNotEmpty() && stack.peek() == '(') {
                            stack.pop()
                        } else {
                            stack.push(char) // Mismatched closing bracket
                            break
                        }
                    }
                    ']' -> {
                        if (stack.isNotEmpty() && stack.peek() == '[') {
                            stack.pop()
                        } else {
                            stack.push(char) // Mismatched closing bracket
                            break
                        }
                    }
                }
            }
        }

        if (stack.isEmpty()) {
            sb.append("yes\n")
        } else {
            sb.append("no\n")
        }
    }

    println(sb)
}