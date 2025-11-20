# Q18: Inout

## 🎯 The Answer

inout allows functions to modify parameter values, passing by reference instead of by value. Creates copy-in, copy-out behavior.

## 📖 Deep Dive

```swift
func increment(_ value: inout Int) {
    value += 1
}

var number = 5
increment(&number)  // Must use &
print(number)  // 6

// Swap function
func swap<T>(_ a: inout T, _ b: inout T) {
    let temp = a
    a = b
    b = temp
}

var x = 1, y = 2
swap(&x, &y)
print(x, y)  // 2, 1

// Can't pass constants or literals
// increment(&5)  // ❌ Error
let constant = 10
// increment(&constant)  // ❌ Error
```

## ✅ Mastery Checklist

- [ ] Understand inout keyword
- [ ] Know & syntax
- [ ] Can modify parameters

---

**Next**: [Q19: Optional Chaining →](./19-optional-chaining.md)
