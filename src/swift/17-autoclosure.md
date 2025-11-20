# Q17: Autoclosure

## 🎯 The Answer

@autoclosure automatically wraps an expression in a closure, delaying its evaluation. Used for short-circuit evaluation and lazy execution.

## 📖 Deep Dive

```swift
// Without autoclosure
func assert(_ condition: () -> Bool, message: String) {
    if !condition() {
        print(message)
    }
}

assert({ 2 + 2 == 4 }, message: "Math broken")  // Verbose

// With autoclosure
func assert(_ condition: @autoclosure () -> Bool, message: String) {
    if !condition() {
        print(message)
    }
}

assert(2 + 2 == 4, message: "Math broken")  // Clean!

// Real-world: Optional coalescing
func ?? <T>(optional: T?, defaultValue: @autoclosure () -> T) -> T {
    if let value = optional {
        return value
    }
    return defaultValue()  // Only evaluated if needed
}

let name: String? = nil
let result = name ?? expensiveOperation()  // Only called if name is nil
```

## ✅ Mastery Checklist

- [ ] Understand @autoclosure
- [ ] Know lazy evaluation
- [ ] Can use appropriately

---

**Next**: [Q18: Inout →](./18-inout.md)
