# Q13: Extensions

## 🎯 The Answer

Extensions add functionality to existing types without subclassing or modifying source code. Can add methods, computed properties, initializers, and protocol conformance.

## 📖 Deep Dive

```swift
// Add methods to existing types
extension String {
    func trimmed() -> String {
        trimmingCharacters(in: .whitespacesAndNewlines)
    }
    
    var isEmail: Bool {
        contains("@") && contains(".")
    }
}

"  hello  ".trimmed()  // "hello"
"test@example.com".isEmail  // true

// Add computed properties
extension Int {
    var squared: Int {
        self * self
    }
    
    var isEven: Bool {
        self % 2 == 0
    }
}

5.squared  // 25
4.isEven   // true

// Add initializers
extension UIColor {
    convenience init(hex: String) {
        // Parse hex string
        self.init(red: 1, green: 0, blue: 0, alpha: 1)
    }
}

// Protocol conformance
extension Array: Identifiable where Element: Identifiable {
    var id: String {
        map { $0.id }.joined()
    }
}

// Conditional extensions
extension Array where Element: Numeric {
    func sum() -> Element {
        reduce(0, +)
    }
}

[1, 2, 3].sum()  // 6
```

## 🎤 Interview Tips

"Extensions let me add functionality to types I don't own, like String or Int. I use them to organize code, add protocol conformance, and provide convenience methods. They can't add stored properties or override existing methods."

## ✅ Mastery Checklist

- [ ] Can create extensions
- [ ] Know limitations (no stored properties)
- [ ] Understand conditional extensions
- [ ] Can add protocol conformance

---

**Next**: [Q14: Static vs Class Methods →](./14-static-vs-class.md)
