# Q12: Associated Types in Protocols

## 🎯 The Answer

Associated types are placeholder types in protocols, defined by conforming types. They're like generics for protocols, enabling type-safe, flexible protocol definitions.

## 📖 Deep Dive

```swift
protocol Container {
    associatedtype Item  // Placeholder type
    
    var count: Int { get }
    mutating func append(_ item: Item)
    subscript(i: Int) -> Item { get }
}

struct IntStack: Container {
    typealias Item = Int  // Define the associated type
    
    private var items: [Int] = []
    
    var count: Int {
        items.count
    }
    
    mutating func append(_ item: Int) {
        items.append(item)
    }
    
    subscript(i: Int) -> Int {
        items[i]
    }
}

struct StringStack: Container {
    // Item inferred as String
    private var items: [String] = []
    
    var count: Int { items.count }
    
    mutating func append(_ item: String) {
        items.append(item)
    }
    
    subscript(i: Int) -> String {
        items[i]
    }
}
```

### Type Inference

```swift
protocol Container {
    associatedtype Item
    mutating func append(_ item: Item)
}

struct Stack: Container {
    private var items: [Int] = []
    
    mutating func append(_ item: Int) {  // Item inferred as Int
        items.append(item)
    }
}
```

### Constraints on Associated Types

```swift
protocol SortableContainer {
    associatedtype Item: Comparable  // Item must be Comparable
    var items: [Item] { get }
    func sorted() -> [Item]
}

struct NumberContainer: SortableContainer {
    let items: [Int]
    
    func sorted() -> [Int] {
        items.sorted()
    }
}
```

### Using Associated Types in Functions

```swift
// Can't use protocol with associated type directly
// func process(_ container: Container) { }  // ❌ Error

// Use generics instead
func process<C: Container>(_ container: C) where C.Item == Int {
    // C is any Container where Item is Int
}

// Or use type erasure
struct AnyContainer<T>: Container {
    typealias Item = T
    
    private let _count: () -> Int
    private let _append: (T) -> Void
    private let _subscript: (Int) -> T
    
    init<C: Container>(_ container: C) where C.Item == T {
        var mutableContainer = container
        _count = { container.count }
        _append = { mutableContainer.append($0) }
        _subscript = { container[$0] }
    }
    
    var count: Int { _count() }
    mutating func append(_ item: T) { _append(item) }
    subscript(i: Int) -> T { _subscript(i) }
}
```

## 🎤 Interview Tips

"Associated types let protocols work with different types while maintaining type safety. They're like generics for protocols. For example, Array's Element is an associated type. I use them when a protocol needs to work with a type that conforming types will define."

## ✅ Mastery Checklist

- [ ] Understand associated types
- [ ] Can constrain associated types
- [ ] Know type inference
- [ ] Understand generic constraints

---

**Next**: [Q13: Extensions →](./13-extensions.md)
