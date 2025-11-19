# Q1: What's the difference between struct and class?

## 🎯 The Answer

**Structs** are **value types** - they're copied when assigned or passed.  
**Classes** are **reference types** - they're shared via references.

## 📖 Deep Dive

### Key Differences

| Feature | Struct | Class |
|---------|--------|-------|
| Type | Value type | Reference type |
| Inheritance | ❌ No | ✅ Yes |
| Deinitializers | ❌ No | ✅ Yes |
| Reference counting | ❌ No | ✅ Yes (ARC) |
| Mutability | Explicit `mutating` | Implicit |
| Thread safety | Safer (copied) | Requires care |

### Code Example

```swift
// STRUCT - Value Type
struct Point {
    var x: Int
    var y: Int
}

var point1 = Point(x: 10, y: 20)
var point2 = point1  // COPY created
point2.x = 30

print(point1.x)  // 10 (unchanged)
print(point2.x)  // 30 (changed)

// CLASS - Reference Type
class Person {
    var name: String
    init(name: String) { self.name = name }
}

var person1 = Person(name: "Alice")
var person2 = person1  // REFERENCE shared
person2.name = "Bob"

print(person1.name)  // "Bob" (changed!)
print(person2.name)  // "Bob" (same reference)
```

## ⚠️ Common Pitfalls

### Pitfall 1: Unexpected Mutations
```swift
class Counter {
    var count = 0
}

let counter = Counter()
counter.count = 10  // ✅ Works! 'let' only makes reference constant
```

### Pitfall 2: Struct Mutation
```swift
struct Counter {
    var count = 0
    
    mutating func increment() {  // Must be 'mutating'
        count += 1
    }
}

let counter = Counter()
// counter.increment()  // ❌ Error: 'let' prevents mutation
```

## 💡 When to Use Each

### Use Struct When:
- Modeling simple data (Point, Size, Color)
- You want value semantics
- Thread safety is important
- No inheritance needed

### Use Class When:
- Need inheritance
- Need deinitializers
- Modeling identity (User, Session)
- Working with Objective-C APIs

## 🎤 Interview Tips

**Interviewer**: "Why does Swift prefer structs?"

**You**: "Swift prefers structs because they're safer by default - no retain cycles, better thread safety, and clearer ownership. The compiler can optimize them better too. But classes are essential when you need inheritance or reference semantics."

**Follow-up**: "Can structs have methods?"

**You**: "Yes! Structs can have methods, computed properties, initializers, and even conform to protocols. They just can't inherit from other structs."

## 🏋️ Practice Challenge

Create a `BankAccount` struct and a `User` class. The User should have a reference to their account. Demonstrate:
1. Copying a BankAccount creates a new account
2. Multiple Users can't share the same account reference
3. Implement a `transfer` method that's safe

<details>
<summary>Solution</summary>

```swift
struct BankAccount {
    var balance: Double
    let accountNumber: String
    
    mutating func deposit(_ amount: Double) {
        balance += amount
    }
    
    mutating func withdraw(_ amount: Double) -> Bool {
        guard balance >= amount else { return false }
        balance -= amount
        return true
    }
}

class User {
    let name: String
    var account: BankAccount
    
    init(name: String, account: BankAccount) {
        self.name = name
        self.account = account
    }
    
    func transfer(to recipient: User, amount: Double) -> Bool {
        guard account.withdraw(amount) else { return false }
        recipient.account.deposit(amount)
        return true
    }
}

// Test
var account1 = BankAccount(balance: 1000, accountNumber: "001")
var account2 = BankAccount(balance: 500, accountNumber: "002")

let alice = User(name: "Alice", account: account1)
let bob = User(name: "Bob", account: account2)

alice.transfer(to: bob, amount: 200)
print(alice.account.balance)  // 800
print(bob.account.balance)    // 700
```

</details>

## ✅ Mastery Checklist

- [ ] Can explain value vs reference types
- [ ] Know when to use struct vs class
- [ ] Understand mutating keyword
- [ ] Can identify copy vs reference behavior
- [ ] Know the performance implications

---

**Next**: [Q2: Value vs Reference Types →](./02-value-vs-reference.md)
