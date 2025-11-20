# Q20: Computed vs Stored Properties

## 🎯 The Answer

**Stored**: Hold values in memory
**Computed**: Calculate values on access, no storage

## 📖 Deep Dive

```swift
struct Rectangle {
    // Stored properties
    var width: Double
    var height: Double
    
    // Computed property
    var area: Double {
        width * height
    }
    
    // Computed with getter and setter
    var perimeter: Double {
        get {
            2 * (width + height)
        }
        set {
            // newValue is implicit
            let side = newValue / 4
            width = side
            height = side
        }
    }
}

var rect = Rectangle(width: 10, height: 5)
print(rect.area)  // 50 (calculated)
rect.perimeter = 40  // Sets width and height

// Property observers
struct StepCounter {
    var steps: Int = 0 {
        willSet {
            print("About to set to \(newValue)")
        }
        didSet {
            print("Changed from \(oldValue) to \(steps)")
        }
    }
}

// Lazy stored property
class DataManager {
    lazy var data: [String] = {
        print("Loading data...")
        return ["Item 1", "Item 2"]
    }()
}

let manager = DataManager()
// "Loading data..." not printed yet
print(manager.data)  // Now it loads
```

## ✅ Mastery Checklist

- [ ] Know stored vs computed
- [ ] Understand property observers
- [ ] Can use lazy properties

---

**Congratulations!** You've completed Swift & Language (Q1-20)

**Next Section**: [Q21: Concurrency - GCD →](../concurrency/21-gcd.md)
