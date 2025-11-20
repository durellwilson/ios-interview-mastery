# Q28: Async-Await

## 🎯 The Answer

Modern concurrency syntax. async marks functions as asynchronous, await suspends execution until result ready.

## 📖 Deep Dive

```swift
// Async function
func fetchUser() async throws -> User {
    let (data, _) = try await URLSession.shared.data(from: url)
    return try JSONDecoder().decode(User.self, from: data)
}

// Calling async
Task {
    do {
        let user = try await fetchUser()
        print(user.name)
    } catch {
        print(error)
    }
}

// Async let - parallel execution
func loadData() async {
    async let user = fetchUser()
    async let posts = fetchPosts()
    
    let (u, p) = await (user, posts)  // Wait for both
}

// MainActor for UI
@MainActor
func updateUI() {
    label.text = "Updated"  // Guaranteed on main thread
}
```

## ✅ Mastery Checklist

- [ ] Understand async/await
- [ ] Can use Task
- [ ] Know async let

---

**Next**: [Q29: Actors →](./29-actors.md)
