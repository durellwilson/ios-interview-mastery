# Q27: OperationQueue

## 🎯 The Answer

OperationQueue is higher-level than GCD, supporting dependencies, cancellation, and priorities.

## 📖 Deep Dive

```swift
let queue = OperationQueue()

// Block operation
queue.addOperation {
    print("Task")
}

// Dependencies
let op1 = BlockOperation { print("First") }
let op2 = BlockOperation { print("Second") }
op2.addDependency(op1)  // op2 waits for op1

queue.addOperations([op1, op2], waitUntilFinished: false)

// Cancellation
let operation = BlockOperation {
    for i in 1...100 {
        if operation.isCancelled { return }
        print(i)
    }
}
queue.addOperation(operation)
operation.cancel()

// Max concurrent
queue.maxConcurrentOperationCount = 2
```

## ✅ Mastery Checklist

- [ ] Know dependencies
- [ ] Can cancel operations
- [ ] Understand vs GCD

---

**Next**: [Q28: Async-Await →](./28-async-await.md)
