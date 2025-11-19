# Q4: Strong, Weak, Unowned

## 🎯 The Answer

- **Strong** (default): Increases reference count, keeps object alive
- **Weak**: Optional, doesn't increase count, becomes `nil` when object deallocated
- **Unowned**: Non-optional, doesn't increase count, crashes if accessed after deallocation

## 📖 Deep Dive

```swift
class Person {
    let name: String
    var apartment: Apartment?
    
    init(name: String) {
        self.name = name
        print("\(name) is initialized")
    }
    
    deinit {
        print("\(name) is deallocated")
    }
}

class Apartment {
    let unit: String
    weak var tenant: Person?  // ✅ weak prevents retain cycle
    
    init(unit: String) {
        self.unit = unit
    }
    
    deinit {
        print("Apartment \(unit) is deallocated")
    }
}

// Usage
var john: Person? = Person(name: "John")
var unit4A: Apartment? = Apartment(unit: "4A")

john?.apartment = unit4A
unit4A?.tenant = john

john = nil  // Both deallocated because weak broke the cycle
unit4A = nil
```

### When to Use Each

| Type | Use When | Example |
|------|----------|---------|
| **Strong** | Default ownership | Properties, variables |
| **Weak** | Optional relationship, might be nil | Delegates, parent references |
| **Unowned** | Non-optional, guaranteed to exist | Child to parent (parent owns child) |

### Unowned Example

```swift
class Customer {
    let name: String
    var card: CreditCard?
    
    init(name: String) {
        self.name = name
    }
    
    deinit { print("\(name) is deallocated") }
}

class CreditCard {
    let number: UInt64
    unowned let customer: Customer  // ✅ Card can't exist without customer
    
    init(number: UInt64, customer: Customer) {
        self.number = number
        self.customer = customer
    }
    
    deinit { print("Card #\(number) is deallocated") }
}

var john: Customer? = Customer(name: "John")
john?.card = CreditCard(number: 1234_5678_9012_3456, customer: john!)
john = nil  // Both deallocated
```

## ⚠️ Common Pitfalls

### Pitfall 1: Using Unowned When Object Might Be Deallocated

```swift
class ViewController {
    unowned let delegate: MyDelegate  // ❌ Crashes if delegate deallocated first
}

// Fix: Use weak
class ViewController {
    weak var delegate: MyDelegate?  // ✅ Safe
}
```

### Pitfall 2: Strong Delegate References

```swift
protocol DataSourceDelegate: AnyObject {
    func didUpdate()
}

class DataSource {
    var delegate: DataSourceDelegate?  // ❌ Should be weak!
}

// Fix:
class DataSource {
    weak var delegate: DataSourceDelegate?  // ✅ Correct
}
```

### Pitfall 3: Closures Capturing Self

```swift
class ViewController {
    var name = "VC"
    
    func setup() {
        someAsyncCall {
            print(self.name)  // ❌ Strong capture
        }
    }
}

// Fix:
func setup() {
    someAsyncCall { [weak self] in
        print(self?.name ?? "")  // ✅ Weak capture
    }
}
```

## 🎤 Interview Tips

**Question**: "What's the difference between weak and unowned?"

**Answer**: 
> "Both weak and unowned don't increase the reference count, preventing retain cycles. The key difference is that weak is optional and automatically becomes nil when the object is deallocated, while unowned is non-optional and will crash if you try to access it after deallocation.
>
> I use weak for delegates and optional relationships where the object might not exist. I use unowned when I'm certain the object will outlive the reference, like a child object referencing its parent that owns it."

## 🏋️ Practice Challenge

Create a `Node` class for a linked list where each node has a `next` (strong) and `previous` (weak) reference. Demonstrate that nodes are properly deallocated.

<details>
<summary>Solution</summary>

```swift
class Node {
    let value: Int
    var next: Node?
    weak var previous: Node?
    
    init(value: Int) {
        self.value = value
        print("Node \(value) created")
    }
    
    deinit {
        print("Node \(value) deallocated")
    }
}

// Test
var head: Node? = Node(value: 1)
var second: Node? = Node(value: 2)
var third: Node? = Node(value: 3)

head?.next = second
second?.previous = head
second?.next = third
third?.previous = second

// Break the chain
head = nil
second = nil
third = nil
// All nodes deallocated properly
```

</details>

## ✅ Mastery Checklist

- [ ] Know when to use strong, weak, unowned
- [ ] Understand reference counting impact
- [ ] Can prevent retain cycles
- [ ] Know weak is optional, unowned is not
- [ ] Can identify when to use each in code

---

**Next**: [Q5: Retain Cycles →](./05-retain-cycles.md)
