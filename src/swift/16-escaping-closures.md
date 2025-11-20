# Q16: Escaping vs Non-Escaping

## 🎯 The Answer

**Non-escaping** (default): Closure executed before function returns
**Escaping** (@escaping): Closure can outlive the function, stored or called later

## 📖 Deep Dive

```swift
// Non-escaping (default)
func performSync(completion: () -> Void) {
    completion()  // Called immediately
}  // completion can't be used after return

// Escaping
func performAsync(completion: @escaping () -> Void) {
    DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
        completion()  // Called after function returns
    }
}

// Stored closure must be escaping
class ViewController {
    var completion: (() -> Void)?
    
    func setup(completion: @escaping () -> Void) {
        self.completion = completion  // Stored
    }
}

// Escaping requires explicit self
class Manager {
    var name = "Manager"
    
    func start(completion: @escaping () -> Void) {
        DispatchQueue.main.async {
            print(self.name)  // Must use self
            completion()
        }
    }
}
```

## 🎤 Interview Tips

"Non-escaping closures are executed before the function returns, so they're safer and more efficient. Escaping closures can outlive the function - used for async operations, stored properties, or callbacks. Escaping closures require explicit self to avoid accidental retain cycles."

## ✅ Mastery Checklist

- [ ] Know default is non-escaping
- [ ] Understand when to use @escaping
- [ ] Know self requirement

---

**Next**: [Q17: Autoclosure →](./17-autoclosure.md)
