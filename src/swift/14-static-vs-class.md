# Q14: Static vs Class Methods

## 🎯 The Answer

**static**: Cannot be overridden in subclasses
**class**: Can be overridden in subclasses (classes only)

## 📖 Deep Dive

```swift
class Vehicle {
    static func staticMethod() {
        print("Vehicle static")
    }
    
    class func classMethod() {
        print("Vehicle class")
    }
}

class Car: Vehicle {
    // Can't override static
    // override static func staticMethod() { }  // ❌ Error
    
    // Can override class
    override class func classMethod() {
        print("Car class")
    }
}

Vehicle.staticMethod()  // "Vehicle static"
Car.staticMethod()      // "Vehicle static" (inherited)

Vehicle.classMethod()   // "Vehicle class"
Car.classMethod()       // "Car class" (overridden)

// Static properties
struct Config {
    static let apiKey = "abc123"
    static var baseURL = "https://api.example.com"
}

Config.apiKey  // "abc123"
```

## 🎤 Interview Tips

"Static methods and properties belong to the type, not instances. Static can't be overridden, while class methods can be overridden in subclasses. I use static for utility functions and constants, class for factory methods that subclasses might customize."

## ✅ Mastery Checklist

- [ ] Know static vs class difference
- [ ] Understand override capability
- [ ] Can use type properties

---

**Next**: [Q15: Closures →](./15-closures.md)
