# Q19: Optional Chaining

## 🎯 The Answer

Optional chaining queries optional properties, methods, and subscripts with ?. Returns nil if any part of the chain is nil.

## 📖 Deep Dive

```swift
struct Address {
    var street: String
}

struct Person {
    var address: Address?
}

let person = Person(address: nil)

// Optional chaining
let street = person.address?.street  // nil (String?)

// vs Forced unwrapping
// let street = person.address!.street  // ❌ Crash!

// Chaining multiple levels
struct Company {
    var ceo: Person?
}

let company = Company(ceo: Person(address: Address(street: "Main St")))
let ceoStreet = company.ceo?.address?.street  // Optional("Main St")

// Method calls
class Counter {
    var count = 0
    func increment() { count += 1 }
}

var counter: Counter? = Counter()
counter?.increment()  // Calls if not nil
```

## ✅ Mastery Checklist

- [ ] Understand ? operator
- [ ] Know nil propagation
- [ ] Can chain multiple levels

---

**Next**: [Q20: Computed vs Stored Properties →](./20-properties.md)
