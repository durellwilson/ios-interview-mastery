# Q3: How ARC Works

## 🎯 The Answer

**ARC (Automatic Reference Counting)** automatically manages memory by tracking how many strong references point to each class instance. When the count reaches zero, the instance is deallocated.

## 📖 Deep Dive

### The Three Rules of ARC

1. **Strong reference created** → Reference count +1
2. **Strong reference removed** → Reference count -1
3. **Count reaches 0** → Instance deallocated

### Code Example

```swift
class Person {
    let name: String
    
    init(name: String) {
        self.name = name
        print("\(name) is initialized")
    }
    
    deinit {
        print("\(name) is deallocated")
    }
}

// Reference count: 0
var person1: Person? = Person(name: "Alice")  // RC: 1
var person2 = person1                          // RC: 2
var person3 = person1                          // RC: 3

person1 = nil  // RC: 2
person2 = nil  // RC: 1
person3 = nil  // RC: 0 → deinit called!
```

### Output:
```
Alice is initialized
Alice is deallocated
```

## 🔍 How It Works Under the Hood

```swift
class Node {
    var value: Int
    var next: Node?
    
    init(value: Int) {
        self.value = value
    }
    
    deinit {
        print("Node \(value) deallocated")
    }
}

var head: Node? = Node(value: 1)  // RC: 1
head?.next = Node(value: 2)        // RC: 1 for node 2
head?.next?.next = Node(value: 3)  // RC: 1 for node 3

head = nil  // All nodes deallocated in order
```

## ⚠️ Common Pitfalls

### Pitfall 1: Retain Cycles
```swift
class Parent {
    var child: Child?
    deinit { print("Parent deallocated") }
}

class Child {
    var parent: Parent?  // ⚠️ Strong reference!
    deinit { print("Child deallocated") }
}

var parent: Parent? = Parent()
var child: Child? = Child()
parent?.child = child
child?.parent = parent

parent = nil
child = nil
// ❌ Nothing deallocated! Retain cycle!
```

### Pitfall 2: Closures Capturing Self
```swift
class ViewController {
    var name = "VC"
    
    func setupHandler() {
        someAsyncCall {
            print(self.name)  // ⚠️ Strong capture!
        }
    }
    
    deinit { print("VC deallocated") }
}
```

## 💡 ARC vs Garbage Collection

| ARC | Garbage Collection |
|-----|-------------------|
| Compile-time | Runtime |
| Deterministic | Non-deterministic |
| No pause | Can pause app |
| Manual cycle breaking | Automatic |
| iOS/Swift | Java/C# |

## 🎤 Interview Tips

**Interviewer**: "How does ARC differ from manual memory management?"

**You**: "ARC automatically inserts retain and release calls at compile time, so we don't have to manually manage memory like in C. But we still need to understand ownership to avoid retain cycles."

**Follow-up**: "When does ARC not work?"

**You**: "ARC only works with reference types (classes). Value types like structs don't need it. Also, ARC can't automatically break retain cycles - we need weak or unowned references for that."

## 🏋️ Practice Challenge

Create a `Task` and `TaskManager` system where:
1. TaskManager holds an array of tasks
2. Each Task has a completion handler
3. Prove that tasks are properly deallocated
4. Show what happens with a retain cycle

<details>
<summary>Solution</summary>

```swift
class Task {
    let id: Int
    var onComplete: (() -> Void)?
    
    init(id: Int) {
        self.id = id
        print("Task \(id) created")
    }
    
    func execute() {
        print("Task \(id) executing")
        onComplete?()
    }
    
    deinit {
        print("Task \(id) deallocated")
    }
}

class TaskManager {
    var tasks: [Task] = []
    
    func addTask(_ task: Task) {
        tasks.append(task)
        
        // ✅ Correct: weak self
        task.onComplete = { [weak self] in
            self?.removeTask(task)
        }
        
        // ❌ Wrong: creates retain cycle
        // task.onComplete = {
        //     self.removeTask(task)
        // }
    }
    
    func removeTask(_ task: Task) {
        tasks.removeAll { $0 === task }
        print("Task removed from manager")
    }
    
    deinit {
        print("TaskManager deallocated")
    }
}

// Test
var manager: TaskManager? = TaskManager()
let task = Task(id: 1)
manager?.addTask(task)
task.execute()
manager = nil  // Should deallocate everything
```

</details>

## ✅ Mastery Checklist

- [ ] Understand reference counting
- [ ] Know when objects are deallocated
- [ ] Can identify retain cycles
- [ ] Understand ARC vs GC differences
- [ ] Know ARC limitations

---

**Next**: [Q4: Strong, Weak, Unowned →](./04-reference-types.md)
