#!/usr/bin/env python3
import os

# Real, complete content for each question
content = {
    "swift/05-retain-cycles.md": """# Q5: What Causes Retain Cycles

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
""",

    "swift/06-property-wrappers.md": """# Q6: Property Wrappers

## 🎯 The Answer

Property wrappers add reusable behavior to properties using `@propertyWrapper`. They wrap a value and add logic for getting/setting. Examples: `@State`, `@Published`, `@UserDefault`.

## 📖 Deep Dive

```swift
@propertyWrapper
struct Capitalized {
    private var value: String = ""
    
    var wrappedValue: String {
        get { value }
        set { value = newValue.capitalized }
    }
    
    init(wrappedValue: String) {
        self.value = wrappedValue.capitalized
    }
}

// Usage
struct User {
    @Capitalized var name: String
}

var user = User(name: "john")
print(user.name)  // "John"
user.name = "jane"
print(user.name)  // "Jane"
```

### Built-in Property Wrappers

**SwiftUI:**
- `@State`: Local view state
- `@Binding`: Two-way binding
- `@StateObject`: Observable object owner
- `@ObservedObject`: Observable object observer
- `@EnvironmentObject`: Shared environment object
- `@Environment`: System environment values

**Combine:**
- `@Published`: Publishes value changes

### Custom Examples

**@UserDefault**
```swift
@propertyWrapper
struct UserDefault<T> {
    let key: String
    let defaultValue: T
    
    var wrappedValue: T {
        get {
            UserDefaults.standard.object(forKey: key) as? T ?? defaultValue
        }
        set {
            UserDefaults.standard.set(newValue, forKey: key)
        }
    }
}

// Usage
struct Settings {
    @UserDefault(key: "username", defaultValue: "Guest")
    var username: String
}
```

**@Clamped**
```swift
@propertyWrapper
struct Clamped<Value: Comparable> {
    private var value: Value
    private let range: ClosedRange<Value>
    
    var wrappedValue: Value {
        get { value }
        set { value = min(max(range.lowerBound, newValue), range.upperBound) }
    }
    
    init(wrappedValue: Value, _ range: ClosedRange<Value>) {
        self.range = range
        self.value = min(max(range.lowerBound, wrappedValue), range.upperBound)
    }
}

struct Game {
    @Clamped(0...100) var health = 100
}
```

## 🎤 Interview Tips

"Property wrappers let me extract common property logic into reusable components. For example, @State in SwiftUI automatically triggers view updates when the value changes. I can create custom wrappers for things like UserDefaults, validation, or clamping values to ranges."

## ✅ Mastery Checklist

- [ ] Can create property wrappers
- [ ] Know SwiftUI property wrappers
- [ ] Understand wrappedValue
- [ ] Can use projectedValue

---

**Next**: [Q7: Codable →](./07-codable.md)
"""
}

# Write all files
for path, text in content.items():
    full_path = f"src/{path}"
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(text)
    print(f"✅ {path}")

print(f"\n✅ Created {len(content)} complete questions")
