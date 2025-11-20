# Q23: Serial vs Concurrent Queues

## 🎯 The Answer

**Serial**: Executes one task at a time, in order
**Concurrent**: Executes multiple tasks simultaneously

## 📖 Deep Dive

```swift
// Serial queue (default)
let serial = DispatchQueue(label: "com.app.serial")
serial.async { print("Task 1") }
serial.async { print("Task 2") }
serial.async { print("Task 3") }
// Output: Task 1, Task 2, Task 3 (in order)

// Concurrent queue
let concurrent = DispatchQueue(label: "com.app.concurrent", attributes: .concurrent)
concurrent.async { print("Task 1") }
concurrent.async { print("Task 2") }
concurrent.async { print("Task 3") }
// Output: Order not guaranteed

// Thread-safe counter with serial queue
class Counter {
    private var value = 0
    private let queue = DispatchQueue(label: "counter")
    
    func increment() {
        queue.async {
            self.value += 1
        }
    }
    
    func getValue() -> Int {
        queue.sync {
            return value
        }
    }
}
```

## ✅ Mastery Checklist

- [ ] Know serial executes in order
- [ ] Understand concurrent parallelism
- [ ] Can choose appropriate queue

---

**Next**: [Q24: Race Conditions →](./24-race-conditions.md)
