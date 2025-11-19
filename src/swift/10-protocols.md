# Q10: Protocols

## 🎯 The Answer

A protocol defines a blueprint of methods, properties, and requirements that types must implement. It specifies "what" without "how" - enabling polymorphism, composition, and testability.

## 📖 Deep Dive

### Basic Protocol

```swift
protocol Drawable {
    var color: String { get set }
    var lineWidth: Double { get }
    func draw()
}

struct Circle: Drawable {
    var color: String
    let lineWidth: Double = 2.0
    
    func draw() {
        print("Drawing \(color) circle with width \(lineWidth)")
    }
}

struct Rectangle: Drawable {
    var color: String
    var lineWidth: Double
    
    func draw() {
        print("Drawing \(color) rectangle")
    }
}

// Polymorphism
let shapes: [Drawable] = [
    Circle(color: "red"),
    Rectangle(color: "blue", lineWidth: 3.0)
]

shapes.forEach { $0.draw() }
```

### Property Requirements

```swift
protocol Vehicle {
    var speed: Double { get set }  // Read-write
    var maxSpeed: Double { get }   // Read-only
    static var wheelCount: Int { get }  // Type property
}

struct Car: Vehicle {
    var speed: Double
    let maxSpeed: Double = 200.0  // Can be let for get-only
    static let wheelCount = 4
}
```

### Method Requirements

```swift
protocol Resettable {
    mutating func reset()  // mutating for value types
    func configure()
}

struct Counter: Resettable {
    var count = 0
    
    mutating func reset() {  // Must be mutating
        count = 0
    }
    
    func configure() {
        print("Configured")
    }
}

class Timer: Resettable {
    var seconds = 0
    
    func reset() {  // No mutating needed for classes
        seconds = 0
    }
    
    func configure() {
        print("Timer configured")
    }
}
```

### Initializer Requirements

```swift
protocol Identifiable {
    var id: String { get }
    init(id: String)
}

struct User: Identifiable {
    let id: String
    // Initializer automatically satisfies requirement
}

class Product: Identifiable {
    let id: String
    required init(id: String) {  // required for classes
        self.id = id
    }
}

class SpecialProduct: Product {
    let name: String
    
    required init(id: String) {  // Must override with required
        self.name = "Special"
        super.init(id: id)
    }
}
```

### Protocol Inheritance

```swift
protocol Identifiable {
    var id: String { get }
}

protocol Nameable {
    var name: String { get }
}

protocol Timestamped {
    var createdAt: Date { get }
}

protocol Entity: Identifiable, Nameable, Timestamped {
    // Inherits all requirements
}

struct User: Entity {
    let id: String
    let name: String
    let createdAt: Date
}
```

### Class-Only Protocols

```swift
protocol Delegate: AnyObject {  // Only classes can conform
    func didUpdate()
}

class Manager {
    weak var delegate: Delegate?  // Can use weak
}
```

### Protocol Extensions

```swift
protocol Greetable {
    var name: String { get }
    func greet()
    func farewell()
}

extension Greetable {
    // Default implementation
    func greet() {
        print("Hello, \(name)!")
    }
    
    func farewell() {
        print("Goodbye, \(name)!")
    }
}

struct Person: Greetable {
    let name: String
    // greet() and farewell() provided by extension
}

struct Robot: Greetable {
    let name: String
    
    // Can override default
    func greet() {
        print("BEEP BOOP. I AM \(name.uppercased())")
    }
}
```

### Protocol Composition

```swift
protocol Codable: Encodable, Decodable {}  // Type alias

func save<T: Codable & Identifiable>(_ item: T) {
    // T must conform to both Codable and Identifiable
}

// Using typealias
typealias Saveable = Codable & Identifiable
func save<T: Saveable>(_ item: T) {
    // Same as above
}

// Inline composition
func process(_ item: Codable & Equatable & Hashable) {
    // Multiple protocol requirements
}
```

### Conditional Conformance

```swift
extension Array: Equatable where Element: Equatable {
    // Array is Equatable only if Element is Equatable
}

let numbers = [1, 2, 3]
let sameNumbers = [1, 2, 3]
print(numbers == sameNumbers)  // true

extension Optional: Encodable where Wrapped: Encodable {
    // Optional is Encodable if Wrapped is Encodable
}
```

### Protocol with Associated Types (Preview)

```swift
protocol Container {
    associatedtype Item
    var count: Int { get }
    mutating func append(_ item: Item)
}

struct IntStack: Container {
    typealias Item = Int  // Can be inferred
    private var items: [Int] = []
    
    var count: Int { items.count }
    
    mutating func append(_ item: Int) {
        items.append(item)
    }
}
```

## ⚠️ Common Pitfalls

### Pitfall 1: Forgetting `mutating` for Value Types

```swift
protocol Resettable {
    func reset()  // ❌ Won't work for structs that modify self
}

struct Counter: Resettable {
    var count = 0
    func reset() {  // ❌ Error: cannot assign to property
        count = 0
    }
}

// Fix:
protocol Resettable {
    mutating func reset()  // ✅
}
```

### Pitfall 2: Strong Delegate References

```swift
protocol Delegate {  // ❌ Not class-only
    func didUpdate()
}

class Manager {
    var delegate: Delegate?  // ❌ Can't use weak
}

// Fix:
protocol Delegate: AnyObject {  // ✅ Class-only
    func didUpdate()
}

class Manager {
    weak var delegate: Delegate?  // ✅ Can use weak
}
```

### Pitfall 3: Protocol Extension vs Requirement

```swift
protocol Greetable {
    func greet()
}

extension Greetable {
    func greet() {
        print("Hello")
    }
}

struct Person: Greetable {
    func greet() {
        print("Hi there!")
    }
}

let person: Greetable = Person()
person.greet()  // "Hi there!" - uses Person's implementation

// But watch out:
extension Greetable {
    func wave() {  // Not in protocol requirement
        print("👋")
    }
}

struct Robot: Greetable {
    func greet() { print("BEEP") }
    func wave() { print("🤖") }
}

let robot: Greetable = Robot()
robot.wave()  // "👋" - uses extension, not Robot's implementation!
```

## 🎤 Interview Tips

**Question**: "What are protocols and why use them?"

**Answer**:
> "Protocols define contracts that types must fulfill - they specify what methods and properties a type must have without dictating how to implement them. This enables polymorphism, where I can treat different types uniformly if they conform to the same protocol.
>
> I use protocols for dependency injection, making code testable, and enabling composition over inheritance. For example, instead of inheriting from a base class, I can have a struct conform to multiple protocols. Protocol extensions let me provide default implementations, reducing boilerplate."

**Follow-up**: "Protocol vs abstract class?"

**Answer**:
> "Swift doesn't have abstract classes, but protocols are more powerful anyway. Protocols support multiple conformance while classes only support single inheritance. Protocols work with structs, enums, and classes, while abstract classes would only work with classes. And protocol extensions provide default implementations similar to abstract class methods."

## 🏋️ Practice Challenge

Create a `DataStore` protocol that:
1. Has an associated type `Item`
2. Requires `save(_:)`, `fetch(id:)`, and `delete(id:)` methods
3. Provides a default `fetchAll()` implementation
4. Implement it for `UserStore` and `ProductStore`

<details>
<summary>Solution</summary>

```swift
protocol DataStore {
    associatedtype Item: Identifiable
    
    func save(_ item: Item)
    func fetch(id: String) -> Item?
    func delete(id: String)
}

extension DataStore {
    // Default implementation
    func fetchAll() -> [Item] {
        // Would need storage mechanism
        []
    }
}

struct User: Identifiable {
    let id: String
    let name: String
}

struct UserStore: DataStore {
    typealias Item = User
    private var storage: [String: User] = [:]
    
    mutating func save(_ item: User) {
        storage[item.id] = item
    }
    
    func fetch(id: String) -> User? {
        storage[id]
    }
    
    mutating func delete(id: String) {
        storage.removeValue(forKey: id)
    }
}

struct Product: Identifiable {
    let id: String
    let name: String
    let price: Double
}

struct ProductStore: DataStore {
    private var storage: [String: Product] = [:]
    
    mutating func save(_ item: Product) {
        storage[item.id] = item
    }
    
    func fetch(id: String) -> Product? {
        storage[id]
    }
    
    mutating func delete(id: String) {
        storage.removeValue(forKey: id)
    }
}
```

</details>

## ✅ Mastery Checklist

- [ ] Can define protocols with properties and methods
- [ ] Understand protocol inheritance
- [ ] Know when to use `mutating`
- [ ] Can create protocol extensions
- [ ] Understand protocol composition
- [ ] Know class-only protocols (AnyObject)
- [ ] Can use protocols for polymorphism

## 🧠 Quick Self-Test

1. Can structs conform to protocols? **Yes**
2. Can protocols have default implementations? **Yes, via extensions**
3. What's `AnyObject` for? **Class-only protocols**
4. Can protocols inherit from multiple protocols? **Yes**
5. Do classes need `mutating`? **No**

---

**Next**: [Q11: Protocol vs Class Inheritance →](./11-protocol-vs-class.md)
