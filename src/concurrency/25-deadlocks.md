# Q25: Deadlocks

## 🎯 The Answer

A deadlock occurs when two or more threads wait for each other indefinitely. Common cause: nested sync calls on same queue.

## 📖 Deep Dive

```swift
// DEADLOCK EXAMPLE
let queue = DispatchQueue(label: "queue")

queue.sync {
    print("Outer")
    queue.sync {  // ❌ DEADLOCK!
        print("Inner")
    }
}

// FIX: Use async or different queue
queue.async {
    print("Outer")
    queue.async {  // ✅ Works
        print("Inner")
    }
}

// Avoid on main queue
DispatchQueue.main.sync {  // ❌ Deadlock if called from main
    print("This will hang")
}
```

## ✅ Mastery Checklist

- [ ] Understand deadlock causes
- [ ] Can avoid nested sync
- [ ] Know prevention strategies

---

**Next**: [Q26: DispatchGroup →](./26-dispatch-group.md)
