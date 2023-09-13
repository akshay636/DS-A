class Node {
  constructor(value, next) {
    this.value = value
    this.next = next
  }
}

class LinkedList {
  constructor() {
    this.head = null
  }

  append(value) {
    const newNode = new Node(value)
    if (!this.head) {
      this.head = newNode
    } else {
      let current = this.head
      while (current.next) {
        current = current.next
      }
      current.next = newNode

    }
  }
  display() {
    let current = this.head
    while (current) {
      console.log(current.value)
      current = current.next
    }
  }
}
const LL = new LinkedList()
LL.append(10)
LL.append(30)
LL.append(30)
LL.append(30)
LL.display()
