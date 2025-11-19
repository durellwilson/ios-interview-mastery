# Q2: Value Type vs Reference Type

## 🎯 The One-Sentence Answer

**Value types are copied when assigned or passed; reference types share the same instance.**

## 📖 Complete Explanation

### The Core Difference

```swift
// VALUE TYPE - Each variable gets its own copy
var a = 5
var b = a
b = 10
print(a)  // 5 (unchanged)
print(b)  // 10 (changed)

// REFERENCE TYPE - Variables share the same instance
class Box { var value: Int; init(_ v: Int) { value = v } }
var x = Box(5)
var y = x
y.value = 10
print(x.value)  // 10 (changed!)
print(y.value)  // 10 (same instance)
```

### Memory Behavior

| Aspect | Value Type | Reference Type |
|--------|-----------|----------------|
| Storage | Stack (usually) | Heap |
| Assignment | Copy | Reference |
| Mutation | Requires `var` | Can mutate with `let` |
| Thread Safety | Safer | Requires synchronization |
| Performance | Faster for small data | Better for large data |

### Swift Types

**Value Types:**
- `struct`
- `enum`
- `Int`, `Double`, `String`, `Array`, `Dictionary`, `Set`
- Tuples

**Reference Types:**
- `class`
- `function` (closures)
- Actors

## 💡 Visual Mental Model

```
VALUE TYPE (Copy)
┌─────┐      ┌─────┐
│  5  │  →   │  5  │  (Independent copies)
└─────┘      └─────┘
  var a       var b

REFERENCE TYPE (Share)
┌─────┐      
│ Box │  ←─── var x
│  5  │  ←─── var y  (Both point to same box)
└─────┘      
```

## 🔍 Deep Dive: Why This Matters

### 1. Unexpected Mutations
```swift
// Value type - Safe
var numbers1 = [1, 2, 3]
var numbers2 = numbers1
numbers2.append(4)
print(numbers1)  // [1, 2, 3] ✅ Safe

// Reference type - Surprising!
class NumberList {
    var items = [1, 2, 3]
}
var list1 = NumberList()
var list2 = list1
list2.items.append(4)
print(list1.items)  // [1, 2, 3, 4] ⚠️ Changed!
```

### 2. Function Parameters
```swift
func modify(_ value: Int) {
    var value = value
    value += 10
    // Original unchanged
}

func modify(_ object: Box) {
    object.value += 10
    // Original IS changed!
}
```

### 3. Collections
```swift
// Array is value type, but contains reference types
class Person { var name: String; init(_ n: String) { name = n } }

var people1 = [Person("Alice")]
var people2 = people1  // Array copied
people2[0].name = "Bob"  // But Person is reference!

print(people1[0].name)  // "Bob" - Person shared!
```

## ⚠️ Common Pitfalls

### Pitfall 1: Assuming `let` Makes Everything Immutable
```swift
class Counter {
    var count = 0
}

let counter = Counter()
counter.count = 10  // ✅ Works! `let` only makes reference constant
```

### Pitfall 2: Copying Arrays of Classes
```swift
class Item { var value = 0 }
var array1 = [Item()]
var array2 = array1  // Array copied, but Items shared!
array2[0].value = 10
print(array1[0].value)  // 10 (shared!)
```

### Pitfall 3: Dictionary Keys
```swift
class BadKey: Hashable {
    var id: Int
    init(_ id: Int) { self.id = id }
    func hash(into hasher: inout Hasher) { hasher.combine(id) }
    static func == (lhs: BadKey, rhs: BadKey) -> Bool { lhs.id == rhs.id }
}

var dict = [BadKey(1): "value"]
let key = BadKey(1)
dict[key] = "new"
key.id = 2  // ⚠️ Mutated key! Dictionary broken!
```

## 🎤 Interview Answer Template

**Question**: "What's the difference between value and reference types?"

**Your Answer**:
> "Value types like structs are copied when assigned or passed to functions, so each variable has its own independent copy. Reference types like classes share the same instance, so multiple variables can point to the same object.
>
> This affects memory management - value types are typically stored on the stack and don't need ARC, while reference types are on the heap and use reference counting. It also impacts thread safety - value types are inherently safer because each thread gets its own copy.
>
> In Swift, structs, enums, and basic types are value types, while classes and closures are reference types."

**Follow-up**: "When would you choose one over the other?"

**Your Answer**:
> "I use structs for simple data models where I want value semantics - like Point, Size, or User data. They're safer by default and prevent accidental mutations.
>
> I use classes when I need inheritance, when modeling identity (like a User session), or when I need reference semantics - like a view controller or a shared cache. Classes are also necessary for Objective-C interop."

## 🏋️ Practice Challenges

### Challenge 1: Predict the Output
```swift
struct Point {
    var x: Int
    var y: Int
}

class Circle {
    var center: Point
    var radius: Int
    init(center: Point, radius: Int) {
        self.center = center
        self.radius = radius
    }
}

var point = Point(x: 0, y: 0)
var circle1 = Circle(center: point, radius: 5)
var circle2 = circle1

circle2.center.x = 10
circle2.radius = 20

print(circle1.center.x)  // ?
print(circle1.radius)    // ?
print(point.x)           // ?
```

<details>
<summary>Solution</summary>

```
circle1.center.x = 10  (Circle shared, Point copied into Circle)
circle1.radius = 20    (Circle shared)
point.x = 0            (Original Point unchanged)
```

**Explanation**: `circle2` shares the same Circle instance as `circle1`, so changes affect both. But when Point was assigned to Circle, it was copied, so the original `point` is unchanged.
</details>

### Challenge 2: Fix the Bug
```swift
class ViewModel {
    var items: [String] = []
    
    func getItems() -> [String] {
        return items
    }
}

let vm = ViewModel()
vm.items = ["A", "B", "C"]

var myItems = vm.getItems()
myItems.append("D")

// Bug: We don't want to modify vm.items, but...?
```

<details>
<summary>Solution</summary>

**No bug!** Array is a value type, so `myItems` is a copy. `vm.items` is unchanged.

If items were a class:
```swift
class ItemList {
    var items: [String] = []
}

class ViewModel {
    var itemList = ItemList()
    
    func getItems() -> ItemList {
        return itemList  // ⚠️ Shared reference!
    }
}
```

Then you'd need to return a copy or use a struct.
</details>

### Challenge 3: Implement Copy-on-Write
Create a `Buffer` class that behaves like a value type using copy-on-write.

<details>
<summary>Solution</summary>

```swift
final class Storage {
    var data: [Int]
    init(_ data: [Int]) { self.data = data }
}

struct Buffer {
    private var storage: Storage
    
    init(_ data: [Int]) {
        storage = Storage(data)
    }
    
    var data: [Int] {
        get { storage.data }
        set {
            if !isKnownUniquelyReferenced(&storage) {
                storage = Storage(newValue)  // Copy on write
            } else {
                storage.data = newValue
            }
        }
    }
}

// Test
var buffer1 = Buffer([1, 2, 3])
var buffer2 = buffer1  // Shares storage
buffer2.data.append(4)  // Triggers copy
// buffer1 unchanged, buffer2 has copy
```
</details>

## 🧠 Memory Tricks

**Remember**: "**V**alue types **V**ary independently, **R**eference types **R**emain connected"

**Mnemonic**: 
- **S**tructs are **S**eparate (value)
- **C**lasses are **C**onnected (reference)

## ✅ Mastery Checklist

- [ ] Can explain the difference in one sentence
- [ ] Know which Swift types are value vs reference
- [ ] Understand memory implications (stack vs heap)
- [ ] Can predict behavior in code examples
- [ ] Know when to use each type
- [ ] Understand copy-on-write optimization
- [ ] Can identify bugs related to type semantics

## 🎯 Quick Self-Test

1. Is `String` a value or reference type? **Value**
2. What happens when you assign a struct? **Copy created**
3. Can you mutate a class property with `let`? **Yes**
4. Are closures value or reference types? **Reference**
5. What's stored on the heap? **Reference types**

**Score**: 5/5 = Ready | 3-4/5 = Review | <3/5 = Study more

---

**Next**: [Q3: How ARC Works →](./03-arc-basics.md)
