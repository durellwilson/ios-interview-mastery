# Q29: Actors

## 🎯 The Answer

Actors are reference types that protect mutable state from data races. Only one task can access actor state at a time.

## 📖 Deep Dive

```swift
actor Counter {
    var value = 0
    
    func increment() {
        value += 1  // Thread-safe automatically
    }
    
    func getValue() -> Int {
        value
    }
}

// Usage
let counter = Counter()

Task {
    await counter.increment()  // Must use await
    let value = await counter.getValue()
}

// Nonisolated for synchronous access
actor DataStore {
    private var data: [String] = []
    
    nonisolated let id: String  // Can access without await
    
    init(id: String) {
        self.id = id
    }
}
```

## ✅ Mastery Checklist

- [ ] Understand actor isolation
- [ ] Know await requirement
- [ ] Can use nonisolated

---

**Next**: [Q30: MainActor →](./30-main-actor.md)
