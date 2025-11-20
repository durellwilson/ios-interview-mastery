# Q24: Race Conditions

## 🎯 The Answer

A race condition occurs when multiple threads access shared data simultaneously, causing unpredictable results. Fixed with synchronization (serial queues, locks, actors).

## 📖 Deep Dive

```swift
// RACE CONDITION
class UnsafeCounter {
    var count = 0
    
    func increment() {
        count += 1  // ❌ Not thread-safe
    }
}

let counter = UnsafeCounter()
DispatchQueue.concurrentPerform(iterations: 1000) { _ in
    counter.increment()
}
print(counter.count)  // Not 1000! Race condition

// FIX 1: Serial Queue
class SafeCounter {
    private var count = 0
    private let queue = DispatchQueue(label: "counter")
    
    func increment() {
        queue.sync {
            count += 1
        }
    }
}

// FIX 2: Actor (Swift 5.5+)
actor ActorCounter {
    var count = 0
    
    func increment() {
        count += 1  // Automatically synchronized
    }
}
```

## ✅ Mastery Checklist

- [ ] Can identify race conditions
- [ ] Know synchronization methods
- [ ] Understand thread safety

---

**Next**: [Q25: Deadlocks →](./25-deadlocks.md)
