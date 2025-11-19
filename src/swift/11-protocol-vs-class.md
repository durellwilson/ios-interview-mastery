# Q11: Protocol vs Class Inheritance

## 🎯 The Answer

**Protocols**: Multiple adoption, no default implementation (unless extension), works with all types
**Classes**: Single inheritance, provides implementation, classes only

## 📖 Deep Dive

```swift
// PROTOCOLS - Multiple Adoption
protocol Flyable {
    func fly()
}

protocol Swimmable {
    func swim()
}

struct Duck: Flyable, Swimmable {  // ✅ Multiple protocols
    func fly() { print("Duck flying") }
    func swim() { print("Duck swimming") }
}

// CLASSES - Single Inheritance
class Animal {
    func breathe() { print("Breathing") }
}

class Mammal: Animal {
    func nurse() { print("Nursing") }
}

class Dog: Mammal {  // ✅ Inherits from Mammal (and Animal)
    func bark() { print("Barking") }
}

// class Cat: Mammal, Animal { }  // ❌ Can't inherit from multiple classes
```

### Key Differences

| Feature | Protocol | Class Inheritance |
|---------|----------|-------------------|
| Multiple | ✅ Yes | ❌ No (single only) |
| Value Types | ✅ Yes | ❌ No |
| Implementation | Extension only | ✅ Yes |
| Override | No concept | ✅ Yes |
| Polymorphism | ✅ Yes | ✅ Yes |

### When to Use Protocols

```swift
// Composition over inheritance
protocol Purchasable {
    var price: Double { get }
}

protocol Downloadable {
    func download()
}

protocol Streamable {
    func stream()
}

struct Movie: Purchasable, Downloadable, Streamable {
    let price: Double
    func download() { }
    func stream() { }
}

struct Song: Purchasable, Downloadable, Streamable {
    let price: Double
    func download() { }
    func stream() { }
}
```

### When to Use Class Inheritance

```swift
// Shared implementation
class UIView {
    var frame: CGRect
    func draw() { /* complex drawing */ }
}

class UIButton: UIView {
    var title: String
    // Inherits frame and draw()
}

class UILabel: UIView {
    var text: String
    // Inherits frame and draw()
}
```

## 🎤 Interview Tips

"Protocols enable multiple conformance and work with value types, making them more flexible than class inheritance. I use protocols for capabilities and behaviors, and class inheritance when I need to share implementation. Swift favors protocol-oriented programming because it's more composable and testable."

## ✅ Mastery Checklist

- [ ] Know protocols allow multiple adoption
- [ ] Understand single inheritance limitation
- [ ] Can choose appropriate approach
- [ ] Know composition over inheritance

---

**Next**: [Q12: Associated Types →](./12-associated-types.md)
