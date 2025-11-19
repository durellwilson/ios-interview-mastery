# 🎴 Flashcards - All 70 Questions

Use these flashcards for quick review and memorization. Click to reveal answers.

## Swift & Language (1-20)

<details>
<summary><strong>Q1: What's the difference between struct and class?</strong></summary>

**Answer**: Structs are value types (copied), classes are reference types (shared). Classes support inheritance and deinitializers, structs don't.

**Key Point**: `let` on struct = immutable. `let` on class = constant reference, mutable properties.
</details>

<details>
<summary><strong>Q2: Value type vs reference type?</strong></summary>

**Answer**: Value types (struct, enum) are copied on assignment. Reference types (class) share the same instance.

**Memory**: Value types on stack (usually), reference types on heap.
</details>

<details>
<summary><strong>Q3: How does ARC work?</strong></summary>

**Answer**: Automatic Reference Counting tracks strong references. When count reaches 0, instance is deallocated. Works at compile-time.

**Formula**: +1 on create, -1 on remove, 0 = dealloc
</details>

<details>
<summary><strong>Q4: Strong, weak, unowned?</strong></summary>

**Answer**: 
- **Strong**: Default, increases reference count
- **Weak**: Optional, doesn't increase count, becomes nil when deallocated
- **Unowned**: Non-optional, doesn't increase count, crashes if accessed after dealloc
</details>

<details>
<summary><strong>Q5: What causes retain cycles?</strong></summary>

**Answer**: Two objects holding strong references to each other. Common in: closures capturing self, parent-child relationships, delegates.

**Fix**: Use `weak` or `unowned` to break the cycle.
</details>

<details>
<summary><strong>Q6: What are property wrappers?</strong></summary>

**Answer**: Reusable code that adds behavior to properties. Examples: `@State`, `@Published`, `@UserDefault`.

**Syntax**: `@propertyWrapper struct Wrapper { var wrappedValue: T }`
</details>

<details>
<summary><strong>Q7: What is Codable?</strong></summary>

**Answer**: Protocol for encoding/decoding. Combines `Encodable` + `Decodable`. Auto-synthesized for simple types.

**Usage**: `struct User: Codable { let name: String }`
</details>

<details>
<summary><strong>Q8: map, flatMap, compactMap?</strong></summary>

**Answer**:
- **map**: Transform each element
- **flatMap**: Transform + flatten nested arrays
- **compactMap**: Transform + remove nils
</details>

<details>
<summary><strong>Q9: What are generics?</strong></summary>

**Answer**: Write flexible, reusable code that works with any type. Provides type safety without duplication.

**Example**: `func swap<T>(_ a: inout T, _ b: inout T)`
</details>

<details>
<summary><strong>Q10: What is a protocol?</strong></summary>

**Answer**: Blueprint of methods, properties, and requirements. Defines "what" not "how". Enables polymorphism.

**Key**: Can be adopted by classes, structs, and enums.
</details>

<details>
<summary><strong>Q11: Protocol vs class inheritance?</strong></summary>

**Answer**: 
- **Protocol**: Multiple adoption, no implementation (unless extension)
- **Class**: Single inheritance, provides implementation
</details>

<details>
<summary><strong>Q12: Associated types in protocols?</strong></summary>

**Answer**: Placeholder type in protocol, defined by conforming type. Like generics for protocols.

**Syntax**: `associatedtype Item`
</details>

<details>
<summary><strong>Q13: What are extensions for?</strong></summary>

**Answer**: Add functionality to existing types without subclassing. Can add methods, computed properties, initializers, protocol conformance.

**Cannot**: Add stored properties or override existing methods.
</details>

<details>
<summary><strong>Q14: Static vs class methods?</strong></summary>

**Answer**:
- **static**: Cannot be overridden
- **class**: Can be overridden in subclasses (classes only)
</details>

<details>
<summary><strong>Q15: What is a closure?</strong></summary>

**Answer**: Self-contained block of code that can be passed around. Can capture values from surrounding context.

**Types**: Global functions, nested functions, closure expressions.
</details>

<details>
<summary><strong>Q16: Escaping vs non-escaping?</strong></summary>

**Answer**:
- **Non-escaping** (default): Executed before function returns
- **Escaping** (`@escaping`): Can outlive function, stored or called later
</details>

<details>
<summary><strong>Q17: What is @autoclosure?</strong></summary>

**Answer**: Automatically wraps expression in closure. Delays evaluation. Used for short-circuit evaluation.

**Example**: `func assert(_ condition: @autoclosure () -> Bool)`
</details>

<details>
<summary><strong>Q18: What is inout?</strong></summary>

**Answer**: Pass parameter by reference, allowing function to modify original value. Creates copy-in, copy-out behavior.

**Syntax**: `func increment(_ value: inout Int)`
</details>

<details>
<summary><strong>Q19: What is optional chaining?</strong></summary>

**Answer**: Query optional properties/methods with `?`. Returns nil if any part is nil. Alternative to forced unwrapping.

**Example**: `user?.address?.street`
</details>

<details>
<summary><strong>Q20: Computed vs stored properties?</strong></summary>

**Answer**:
- **Stored**: Hold value in memory
- **Computed**: Calculate value on access, no storage
</details>

## Concurrency (21-30)

<details>
<summary><strong>Q21: What is GCD?</strong></summary>

**Answer**: Grand Central Dispatch - low-level API for managing concurrent operations. Uses queues to execute tasks.

**Key**: Abstracts thread management.
</details>

<details>
<summary><strong>Q22: Sync vs async?</strong></summary>

**Answer**:
- **Sync**: Blocks until task completes
- **Async**: Returns immediately, task runs in background
</details>

<details>
<summary><strong>Q23: Serial vs concurrent queues?</strong></summary>

**Answer**:
- **Serial**: One task at a time, in order
- **Concurrent**: Multiple tasks simultaneously
</details>

<details>
<summary><strong>Q24: What is a race condition?</strong></summary>

**Answer**: Multiple threads access shared data simultaneously, causing unpredictable results. Fixed with synchronization (locks, queues, actors).
</details>

<details>
<summary><strong>Q25: What is a deadlock?</strong></summary>

**Answer**: Two or more threads waiting for each other, causing permanent block. Often from nested sync calls on same queue.
</details>

<details>
<summary><strong>Q26: How does DispatchGroup work?</strong></summary>

**Answer**: Groups multiple tasks, notifies when all complete. Use `enter()`/`leave()` or pass to async calls.

**Usage**: Coordinate multiple network calls.
</details>

<details>
<summary><strong>Q27: What is OperationQueue?</strong></summary>

**Answer**: Higher-level abstraction over GCD. Supports dependencies, cancellation, priorities. Uses Operation objects.
</details>

<details>
<summary><strong>Q28: How does async-await work?</strong></summary>

**Answer**: Modern concurrency syntax. `async` marks function as asynchronous, `await` suspends until result ready. Compiler handles continuations.
</details>

<details>
<summary><strong>Q29: What are actors?</strong></summary>

**Answer**: Reference type that protects mutable state from data races. Only one task can access at a time. Automatic synchronization.
</details>

<details>
<summary><strong>Q30: What does MainActor do?</strong></summary>

**Answer**: Global actor representing main thread. Ensures UI updates happen on main thread. Use `@MainActor` annotation.
</details>

## Memory Management (31-40)

<details>
<summary><strong>Q31: How does ARC allocate/free memory?</strong></summary>

**Answer**: Allocates on heap when instance created. Tracks references. Frees when count = 0. Inserts retain/release at compile time.
</details>

<details>
<summary><strong>Q32: What do weak references do?</strong></summary>

**Answer**: Don't increase reference count. Automatically become nil when object deallocated. Always optional. Prevent retain cycles.
</details>

<details>
<summary><strong>Q33: What do unowned references do?</strong></summary>

**Answer**: Don't increase reference count. Non-optional. Assume object always exists. Crash if accessed after deallocation.

**Use when**: Object lifetime guaranteed.
</details>

<details>
<summary><strong>Q34: Strong reference cycles in closures?</strong></summary>

**Answer**: Closure captures self strongly, self holds closure strongly = cycle. Fix with capture list `[weak self]` or `[unowned self]`.
</details>

<details>
<summary><strong>Q35: Capture list usage?</strong></summary>

**Answer**: Define how closure captures values. Syntax: `{ [weak self, unowned obj] in }`. Prevents retain cycles.
</details>

<details>
<summary><strong>Q36: What causes memory leaks?</strong></summary>

**Answer**: Retain cycles, strong delegate references, closures capturing self, timers, observers not removed.
</details>

<details>
<summary><strong>Q37: Detect leaks with Instruments?</strong></summary>

**Answer**: Use Leaks instrument. Shows leaked objects, allocation stack trace. Also use Memory Graph Debugger in Xcode.
</details>

<details>
<summary><strong>Q38: MVVM retain cycle examples?</strong></summary>

**Answer**: ViewModel holds closure, closure captures ViewModel. View holds ViewModel, ViewModel holds View. Fix with weak references.
</details>

<details>
<summary><strong>Q39: Memory warning handling?</strong></summary>

**Answer**: iOS sends warning when low memory. Override `didReceiveMemoryWarning()`. Clear caches, release non-essential resources.
</details>

<details>
<summary><strong>Q40: Reference counting under the hood?</strong></summary>

**Answer**: Each object has reference count field. Retain increments, release decrements. When 0, dealloc called. Atomic operations for thread safety.
</details>

## UIKit & SwiftUI (41-60)

<details>
<summary><strong>Q41: UIViewController lifecycle?</strong></summary>

**Answer**: `init` → `loadView` → `viewDidLoad` → `viewWillAppear` → `viewDidAppear` → `viewWillDisappear` → `viewDidDisappear` → `deinit`
</details>

<details>
<summary><strong>Q42: App lifecycle?</strong></summary>

**Answer**: Not Running → Inactive → Active → Background → Suspended. Use SceneDelegate (iOS 13+) or AppDelegate.
</details>

<details>
<summary><strong>Q43: Frame vs bounds?</strong></summary>

**Answer**:
- **Frame**: Position/size in superview's coordinate system
- **Bounds**: Position/size in own coordinate system (origin usually 0,0)
</details>

<details>
<summary><strong>Q44: Auto Layout basics?</strong></summary>

**Answer**: Constraint-based layout system. Define relationships between views. Adapts to different screen sizes. Uses constraints (equal, greater, less).
</details>

<details>
<summary><strong>Q45: Constraints vs frames?</strong></summary>

**Answer**:
- **Constraints**: Adaptive, relationship-based, works across devices
- **Frames**: Fixed positions, manual calculation, breaks on rotation
</details>

<details>
<summary><strong>Q46: Table view cell reuse?</strong></summary>

**Answer**: Cells dequeued from reuse pool instead of creating new. Improves performance. Must reset cell state in `prepareForReuse()`.
</details>

<details>
<summary><strong>Q47: Diffable data source?</strong></summary>

**Answer**: Modern UITableView/UICollectionView data source. Uses snapshots. Automatic animations. Type-safe. No index path crashes.
</details>

<details>
<summary><strong>Q48: Compositional layout?</strong></summary>

**Answer**: Flexible UICollectionView layout. Compose sections with different layouts. Supports groups, items, sections. Replaces flow layout.
</details>

<details>
<summary><strong>Q49: SwiftUI view lifecycle?</strong></summary>

**Answer**: `init` → `body` → `onAppear` → `onDisappear`. No viewDidLoad equivalent. Use `.task` for async work.
</details>

<details>
<summary><strong>Q50: @State vs @Binding?</strong></summary>

**Answer**:
- **@State**: Source of truth, owned by view
- **@Binding**: Two-way connection to @State, doesn't own data
</details>

<details>
<summary><strong>Q51: @ObservedObject vs @StateObject?</strong></summary>

**Answer**:
- **@StateObject**: Creates and owns object, survives view updates
- **@ObservedObject**: Observes external object, can be recreated
</details>

<details>
<summary><strong>Q52: Environment values?</strong></summary>

**Answer**: Pass data down view hierarchy without explicit parameters. System values (colorScheme) or custom. Use `@Environment`.
</details>

<details>
<summary><strong>Q53: NavigationStack basics?</strong></summary>

**Answer**: Modern navigation (iOS 16+). Programmatic navigation with path. Type-safe. Replaces NavigationView + NavigationLink.
</details>

<details>
<summary><strong>Q54: SwiftUI diff engine?</strong></summary>

**Answer**: Compares old and new view trees. Only updates changed views. Uses view identity and type. Efficient rendering.
</details>

<details>
<summary><strong>Q55: View identity in SwiftUI?</strong></summary>

**Answer**: How SwiftUI tracks views across updates. Based on type, position, and explicit `id()`. Affects state preservation and animations.
</details>

<details>
<summary><strong>Q56: LazyVStack and LazyHStack?</strong></summary>

**Answer**: Load views on-demand as they appear. Better performance for long lists. Unlike VStack/HStack which load all immediately.
</details>

<details>
<summary><strong>Q57: Scroll performance best practices?</strong></summary>

**Answer**: Use lazy stacks, avoid heavy computations in body, cache images, use `.drawingGroup()` for complex views, minimize state changes.
</details>

<details>
<summary><strong>Q58: Rendering pipeline in SwiftUI?</strong></summary>

**Answer**: State change → body called → diff → update → render. Three phases: update, layout, render. Optimized by SwiftUI.
</details>

<details>
<summary><strong>Q59: UIKit vs SwiftUI architecture?</strong></summary>

**Answer**:
- **UIKit**: Imperative, mutable, view controllers, delegates
- **SwiftUI**: Declarative, immutable, views, data flow
</details>

<details>
<summary><strong>Q60: When to mix SwiftUI + UIKit?</strong></summary>

**Answer**: Use UIViewRepresentable/UIViewControllerRepresentable. When: UIKit component not in SwiftUI, legacy code, specific UIKit features needed.
</details>

## Networking (61-70)

<details>
<summary><strong>Q61: URLSession flow?</strong></summary>

**Answer**: Create URLRequest → Create URLSession → Create task (data/download/upload) → Resume task → Handle response/data → Parse.
</details>

<details>
<summary><strong>Q62: DataTask vs DownloadTask?</strong></summary>

**Answer**:
- **DataTask**: Returns data in memory, for small responses
- **DownloadTask**: Saves to file, for large files, supports background
</details>

<details>
<summary><strong>Q63: Decoding JSON with Codable?</strong></summary>

**Answer**: `JSONDecoder().decode(Type.self, from: data)`. Struct must conform to Codable. Use CodingKeys for custom mapping.
</details>

<details>
<summary><strong>Q64: Handling errors in networking?</strong></summary>

**Answer**: Check URLError, HTTP status codes, decoding errors. Use Result type. Provide user-friendly messages. Implement retry logic.
</details>

<details>
<summary><strong>Q65: What is HTTP caching?</strong></summary>

**Answer**: Store responses to avoid repeated requests. URLCache handles automatically. Control with Cache-Control headers. Improves performance.
</details>

<details>
<summary><strong>Q66: What are URLRequests?</strong></summary>

**Answer**: Encapsulates request details: URL, method (GET/POST), headers, body, timeout. Immutable. Use URLComponents for URL building.
</details>

<details>
<summary><strong>Q67: REST vs GraphQL?</strong></summary>

**Answer**:
- **REST**: Multiple endpoints, over/under-fetching, simple
- **GraphQL**: Single endpoint, request exact data, complex
</details>

<details>
<summary><strong>Q68: Handling status codes?</strong></summary>

**Answer**: 2xx = success, 3xx = redirect, 4xx = client error, 5xx = server error. Check `httpResponse.statusCode`. Handle each appropriately.
</details>

<details>
<summary><strong>Q69: Retry mechanism?</strong></summary>

**Answer**: Exponential backoff, max retry count, only retry on specific errors (network, 5xx). Use DispatchQueue.asyncAfter or Task.sleep.
</details>

<details>
<summary><strong>Q70: Debouncing network calls?</strong></summary>

**Answer**: Delay execution until user stops typing. Cancel previous requests. Use Timer, Combine's debounce, or Task cancellation.
</details>

---

## 📚 Study Tips

1. **Review daily**: Go through 10 flashcards per day
2. **Active recall**: Try to answer before revealing
3. **Spaced repetition**: Review difficult cards more often
4. **Practice coding**: Don't just memorize, write code
5. **Teach others**: Best way to solidify understanding

---

[← Back to Course](./introduction.md) | [Take Quizzes →](./quizzes/swift-quiz.md)
