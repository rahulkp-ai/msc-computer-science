class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,val):
        """Helper to construct a standard list."""
        new_node    =   ListNode(val)
        if not self.head:
            self.head = new_node
            return new_node
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        
        return new_node
    
    def create_cycle(self, pos: int):
            """Creates a cycle where the tail node points to node at index `pos` (0-indexed)."""
            if pos < 0:
                return

            cycle_node = None
            curr = self.head
            index = 0

            while curr.next:
                if index == pos:
                    cycle_node = curr
                curr = curr.next
                index += 1

            if index == pos:
                cycle_node = curr

            # Point tail to the cycle_node
            if curr and cycle_node:
                curr.next = cycle_node

    def detect_and_remove_cycle(self) -> bool:
        """
        Uses Tortoise and Hare algorithm (LeetCode 141 style)
        to detect a cycle, then extends it to break the cycle (LeetCode 142 extension).
        """
        if not self.head or not self.head.next:
            return False
        
        slow     = self.head
        fast     = self.head
        has_cycle   = False

        # --- Detection ------
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                has_cycle = True
                break
        
        if not has_cycle:
            return False
        
        # --- Removal ---
        
        slow = self.head

        while slow.next != fast.next:
            slow    = slow.next
            fast    = fast.next
        
        fast.next   = None
        return True
    
    def print_list(self, limit=15):
        """Prints list elements; stops if infinite loop is detected beyond limit."""
        curr = self.head
        elems = []
        count = 0

        while curr and count < limit:
            elems.append(str(curr.val))
            curr = curr.next
            count += 1

        if count >= limit:
            elems.append("... (infinite cycle detected)")
            print(" -> ".join(elems))
        else:
            print(" -> ".join(elems) + " -> None")
        

if __name__ == "__main__":
    ll = LinkedList()
    
    # 1. Build a list: 3 -> 2 -> 0 -> -4
    ll.append(3)
    ll.append(2)
    ll.append(0)
    ll.append(-4)

    # 2. Point -4 back to node index 1 (value 2)
    ll.create_cycle(pos=1)

    print("--- Before Removal ---")
    ll.print_list()  # Shows cycle print limit

    # 3. Detect and remove the cycle
    cycle_found = ll.detect_and_remove_cycle()

    print("\n--- Cycle Removal ---")
    print(f"Cycle Detected and Removed: {cycle_found}")

    print("\n--- After Removal ---")
    ll.print_list()  # Standard linear traverse