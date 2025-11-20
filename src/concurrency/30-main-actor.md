# Q30: MainActor

## 🎯 The Answer

MainActor is a global actor representing the main thread. Ensures UI updates happen on main thread.

## 📖 Deep Dive

```swift
// Mark class
@MainActor
class ViewModel: ObservableObject {
    @Published var data: [String] = []
    
    func loadData() {
        // All methods run on main thread
    }
}

// Mark function
@MainActor
func updateUI() {
    label.text = "Updated"
}

// Switch to main
func fetchData() async {
    let data = await downloadData()
    
    await MainActor.run {
        self.updateUI(with: data)
    }
}

// SwiftUI views are @MainActor by default
struct ContentView: View {
    var body: some View {
        Text("Hello")  // Always on main thread
    }
}
```

## ✅ Mastery Checklist

- [ ] Know MainActor purpose
- [ ] Can annotate types/functions
- [ ] Understand UI thread safety

---

**Congratulations!** Completed Concurrency (Q21-Q30)

**Next Section**: [Q31: Memory Management →](../memory/31-arc-allocation.md)
