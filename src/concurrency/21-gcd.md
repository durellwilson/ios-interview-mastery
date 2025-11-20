# Q21: GCD (Grand Central Dispatch)

## 🎯 The Answer

GCD is Apple's low-level API for managing concurrent operations using dispatch queues. It abstracts thread management and optimizes task execution.

## 📖 Deep Dive

```swift
// Main queue - UI updates
DispatchQueue.main.async {
    self.label.text = "Updated"
}

// Global queues - background work
DispatchQueue.global(qos: .userInitiated).async {
    // Heavy computation
    let result = processData()
    
    DispatchQueue.main.async {
        self.updateUI(with: result)
    }
}

// Quality of Service levels
DispatchQueue.global(qos: .userInteractive).async { }  // Highest priority
DispatchQueue.global(qos: .userInitiated).async { }    // High priority
DispatchQueue.global(qos: .default).async { }          // Default
DispatchQueue.global(qos: .utility).async { }          // Low priority
DispatchQueue.global(qos: .background).async { }       // Lowest priority

// Custom queue
let queue = DispatchQueue(label: "com.app.myqueue")
queue.async {
    print("Custom queue work")
}

// Concurrent queue
let concurrent = DispatchQueue(label: "com.app.concurrent", attributes: .concurrent)
concurrent.async { print("Task 1") }
concurrent.async { print("Task 2") }  // Can run simultaneously
```

## 🎤 Interview Tips

"GCD manages concurrent execution using queues. Main queue for UI, global queues for background work. I choose QoS based on task priority - userInteractive for UI-related, background for non-urgent tasks."

## ✅ Mastery Checklist

- [ ] Understand dispatch queues
- [ ] Know QoS levels
- [ ] Can switch between queues

---

**Next**: [Q22: Sync vs Async →](./22-sync-async.md)
