# Swift & Language Quiz

Test your mastery of Swift fundamentals (Q1-Q20)

## 📝 Multiple Choice

### Question 1
What happens when you assign a struct to another variable?

A) A reference is shared  
B) A copy is created  
C) A pointer is created  
D) Compiler error  

<details>
<summary>Answer</summary>

**B) A copy is created**

Structs are value types, so assignment creates a complete copy.
</details>

---

### Question 2
Which is true about ARC?

A) Works at runtime like garbage collection  
B) Only works with structs  
C) Inserts retain/release at compile time  
D) Requires manual memory management  

<details>
<summary>Answer</summary>

**C) Inserts retain/release at compile time**

ARC is a compile-time feature that automatically manages reference counting.
</details>

---

### Question 3
What's the output?

```swift
class Box {
    var value: Int
    init(value: Int) { self.value = value }
}

let box = Box(value: 10)
box.value = 20
print(box.value)
```

A) Compiler error  
B) 10  
C) 20  
D) nil  

<details>
<summary>Answer</summary>

**C) 20**

`let` makes the reference constant, not the object's properties.
</details>

---

## 💻 Code Challenges

### Challenge 1: Fix the Retain Cycle

```swift
class Parent {
    var child: Child?
    deinit { print("Parent gone") }
}

class Child {
    var parent: Parent?
    deinit { print("Child gone") }
}

var p: Parent? = Parent()
var c: Child? = Child()
p?.child = c
c?.parent = p
p = nil
c = nil
// Nothing prints! Fix it.
```

<details>
<summary>Solution</summary>

```swift
class Parent {
    var child: Child?
    deinit { print("Parent gone") }
}

class Child {
    weak var parent: Parent?  // ✅ Use weak
    deinit { print("Child gone") }
}
```

</details>

---

### Challenge 2: Implement a Generic Stack

Create a generic `Stack<T>` with:
- `push(_ item: T)`
- `pop() -> T?`
- `peek() -> T?`
- `isEmpty: Bool`

<details>
<summary>Solution</summary>

```swift
struct Stack<T> {
    private var items: [T] = []
    
    mutating func push(_ item: T) {
        items.append(item)
    }
    
    mutating func pop() -> T? {
        items.popLast()
    }
    
    func peek() -> T? {
        items.last
    }
    
    var isEmpty: Bool {
        items.isEmpty
    }
}

// Test
var stack = Stack<Int>()
stack.push(1)
stack.push(2)
print(stack.pop())  // Optional(2)
print(stack.peek()) // Optional(1)
```

</details>

---

### Challenge 3: Protocol with Associated Type

Create a `Container` protocol with:
- Associated type `Item`
- `add(_ item: Item)`
- `count: Int`

Implement it for an `IntContainer`.

<details>
<summary>Solution</summary>

```swift
protocol Container {
    associatedtype Item
    mutating func add(_ item: Item)
    var count: Int { get }
}

struct IntContainer: Container {
    typealias Item = Int
    private var items: [Int] = []
    
    mutating func add(_ item: Int) {
        items.append(item)
    }
    
    var count: Int {
        items.count
    }
}
```

</details>

---

## 🎯 Scenario Questions

### Scenario 1: Memory Leak Detective

You have a view controller that never deallocates. The code:

```swift
class ProfileVC: UIViewController {
    var user: User?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        NetworkManager.shared.fetchUser { user in
            self.user = user
            self.updateUI()
        }
    }
    
    func updateUI() {
        // Update UI
    }
}
```

**Question**: What's causing the leak and how do you fix it?

<details>
<summary>Answer</summary>

The closure captures `self` strongly. If `NetworkManager` holds onto the closure, it creates a retain cycle.

**Fix**:
```swift
NetworkManager.shared.fetchUser { [weak self] user in
    self?.user = user
    self?.updateUI()
}
```

</details>

---

## 📊 Score Yourself

- **0-5 correct**: Review the Swift fundamentals section
- **6-10 correct**: Good foundation, practice more
- **11-15 correct**: Strong understanding
- **16+ correct**: Interview ready! 🎉

---

**Next**: [Concurrency Quiz →](./concurrency-quiz.md)
