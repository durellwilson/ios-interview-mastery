# Q26: DispatchGroup

## 🎯 The Answer

DispatchGroup coordinates multiple async tasks, notifying when all complete.

## 📖 Deep Dive

```swift
let group = DispatchGroup()

// Method 1: enter/leave
group.enter()
fetchUser { user in
    print("Got user")
    group.leave()
}

group.enter()
fetchPosts { posts in
    print("Got posts")
    group.leave()
}

group.notify(queue: .main) {
    print("All done!")
}

// Method 2: Pass to async
let queue = DispatchQueue.global()
queue.async(group: group) {
    // Task 1
}
queue.async(group: group) {
    // Task 2
}

// Wait (blocks)
group.wait()  // Waits until all complete
```

## ✅ Mastery Checklist

- [ ] Can use enter/leave
- [ ] Know notify callback
- [ ] Understand wait blocking

---

**Next**: [Q27: OperationQueue →](./27-operation-queue.md)
