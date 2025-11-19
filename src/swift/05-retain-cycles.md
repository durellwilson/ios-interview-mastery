# Q5: What Causes Retain Cycles

## 🎯 The Answer

A retain cycle occurs when two or more objects hold strong references to each other, preventing ARC from deallocating them. Common causes: parent-child relationships, closures capturing self, delegates with strong references.

## 📖 Deep Dive

```swift
// RETAIN CYCLE EXAMPLE
class Parent {
    var child: Child?
    deinit { print("Parent deallocated") }
}

class Child {
    var parent: Parent?  // ❌ Strong reference creates cycle
    deinit { print("Child deallocated") }
}

var parent: Parent? = Parent()
var child: Child? = Child()
parent?.child = child
child?.parent = parent

parent = nil
child = nil
// ❌ Nothing prints - memory leak!

// FIX: Use weak
class Child {
    weak var parent: Parent?  // ✅ Breaks the cycle
}
```

### Common Scenarios

**1. Closure Retain Cycles**
```swift
class ViewController {
    var completion: (() -> Void)?
    
    func setup() {
        completion = {
            self.view.backgroundColor = .red  // ❌ Captures self strongly
        }
    }
}

// Fix:
completion = { [weak self] in
    self?.view.backgroundColor = .red  // ✅
}
```

**2. Delegate Retain Cycles**
```swift
protocol Delegate: AnyObject {}

class Manager {
    var delegate: Delegate?  // ❌ Should be weak
}

// Fix:
weak var delegate: Delegate?  // ✅
```

**3. Timer Retain Cycles**
```swift
class ViewController {
    var timer: Timer?
    
    func startTimer() {
        timer = Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { _ in
            self.update()  // ❌ Timer retains self
        }
    }
}

// Fix:
timer = Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { [weak self] _ in
    self?.update()  // ✅
}
```

## ⚠️ Common Pitfalls

**Pitfall**: Forgetting to invalidate timers
```swift
deinit {
    timer?.invalidate()  // ✅ Must invalidate
}
```

## 🎤 Interview Tips

"Retain cycles happen when objects hold strong references to each other. The most common cases are closures capturing self, delegates, and parent-child relationships. I prevent them by using weak or unowned references, and always use [weak self] in closures that might outlive the object."

## ✅ Mastery Checklist

- [ ] Can identify retain cycles
- [ ] Know how to break cycles
- [ ] Understand closure capture
- [ ] Know delegate best practices

---

**Next**: [Q6: Property Wrappers →](./06-property-wrappers.md)
