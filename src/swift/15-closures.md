# Q15: Closures

## 🎯 The Answer

Closures are self-contained blocks of code that can capture and store references to variables and constants from their surrounding context.

## 📖 Deep Dive

```swift
// Closure syntax
let greet = { (name: String) -> String in
    return "Hello, \(name)"
}

greet("Alice")  // "Hello, Alice"

// Trailing closure
[1, 2, 3].map { $0 * 2 }  // [2, 4, 6]

// Capturing values
func makeIncrementer(amount: Int) -> () -> Int {
    var total = 0
    return {
        total += amount
        return total
    }
}

let incrementByTwo = makeIncrementer(amount: 2)
incrementByTwo()  // 2
incrementByTwo()  // 4

// Closure as parameter
func performOperation(_ operation: (Int, Int) -> Int) {
    let result = operation(5, 3)
    print(result)
}

performOperation { $0 + $1 }  // 8
```

## 🎤 Interview Tips

"Closures are like anonymous functions that can capture values from their context. They're used for callbacks, completion handlers, and functional programming. Swift has three types: global functions, nested functions, and closure expressions."

## ✅ Mastery Checklist

- [ ] Understand closure syntax
- [ ] Know value capturing
- [ ] Can use trailing closures

---

**Next**: [Q16: Escaping vs Non-Escaping →](./16-escaping-closures.md)
