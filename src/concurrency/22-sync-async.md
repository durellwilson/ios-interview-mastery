# Q22: Sync vs Async

## 🎯 The Answer

**sync**: Blocks current thread until task completes
**async**: Returns immediately, task runs in background

## 📖 Deep Dive

```swift
let queue = DispatchQueue(label: "com.app.queue")

// ASYNC - Non-blocking
print("1")
queue.async {
    print("2")
}
print("3")
// Output: 1, 3, 2

// SYNC - Blocking
print("1")
queue.sync {
    print("2")
}
print("3")
// Output: 1, 2, 3

// Real-world: Network call
func fetchData(completion: @escaping (Data?) -> Void) {
    DispatchQueue.global().async {
        // Network request
        let data = downloadData()
        
        DispatchQueue.main.async {
            completion(data)
        }
    }
}

// Barrier for thread-safe writes
let concurrent = DispatchQueue(label: "queue", attributes: .concurrent)

concurrent.async {
    // Read operation
}

concurrent.async(flags: .barrier) {
    // Write operation - waits for reads, blocks new reads
}
```

## ✅ Mastery Checklist

- [ ] Know sync blocks
- [ ] Understand async returns immediately
- [ ] Can use barriers

---

**Next**: [Q23: Serial vs Concurrent Queues →](./23-queues.md)
