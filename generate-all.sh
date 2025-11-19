#!/bin/bash

# Q4: Strong, Weak, Unowned
cat > src/swift/04-reference-types.md << 'EOF'
# Q4: Strong, Weak, Unowned

## 🎯 The Answer

**Strong** (default): Increases reference count, keeps object alive
**Weak**: Doesn't increase count, becomes nil when deallocated (optional)
**Unowned**: Doesn't increase count, crashes if accessed after deallocation (non-optional)

## 📖 Deep Dive

```swift
class Person {
    let name: String
    weak var friend: Person?        // weak
    unowned let parent: Person      // unowned
    var pet: Pet?                   // strong (default)
    
    init(name: String, parent: Person) {
        self.name = name
        self.parent = parent
    }
}
```

## ⚠️ Common Pitfalls

**Pitfall**: Using unowned when object might be deallocated
```swift
class ViewController {
    unowned let delegate: Delegate  // ❌ Crashes if delegate deallocated
}
```

## 🎤 Interview Tips

"Strong references increase the reference count and keep objects alive. Weak references don't increase the count and automatically become nil when the object is deallocated - use for optional relationships. Unowned is like weak but non-optional - use when you're certain the object will outlive the reference."

## 🏋️ Practice Challenge

Create Parent/Child classes where child has weak reference to parent.

## ✅ Mastery Checklist

- [ ] Know when to use each type
- [ ] Understand reference counting impact
- [ ] Can prevent retain cycles

---

**Next**: [Q5: Retain Cycles →](./05-retain-cycles.md)
EOF

# Continue for all other questions...
echo "Generated Q4"

