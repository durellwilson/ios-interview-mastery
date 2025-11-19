# Q6: Property Wrappers

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
