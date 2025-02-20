# Introduction to Fast & Slow Pointers Pattern
## The Fast & Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two pointers which move through the array (or sequence/LinkedList) at different speeds. By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are bound to meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.

## 1. What is the Fast & Slow Pointers Pattern?

## The Fast & Slow Pointers pattern involves using two pointers (or iterators) that move through a data structure at different speeds—commonly, the “fast” pointer moves two steps at a time, while the “slow” pointer moves one step at a time. This technique is usually applied to linked lists (though it can be used in arrays or other sequential data structures) and is a clever way to detect conditions like cycles or find a specific position (e.g., the middle).

## Example Scenario

## Imagine two friends walking around a circular track:

## One friend (the “slow” pointer) walks one lap per hour.
## Another friend (the “fast” pointer) runs two laps per hour. If there is a cycle (the track is circular), the fast pointer will eventually “lap” or catch up to the slow pointer. This concept directly translates to data structures where pointers traverse nodes.
## 2. Why Use Fast & Slow Pointers?

## Cycle Detection: The pattern helps in detecting cycles without extra space. You don’t need additional data structures like hash sets to keep track of visited nodes.
## Efficiency: By traversing the structure in a single pass, you reduce time complexity. You only use constant extra space—just two pointers!
## Finding Critical Positions: Using different movement speeds allows you to pinpoint interesting locations, such as the middle of a list or the start of a cycle.
3. Key Scenarios Where This Pattern Shines

## Linked List Cycle Detection: Whenever a problem states, “Given a linked list, determine if it has a cycle,” you should think about the Fast & Slow Pointers pattern.
## Middle of a Linked List: If you need to find the middle node of a list in one pass, the Fast & Slow Pointers approach is perfect.
## Length of a Cycle: After detecting a cycle, you can continue with the fast pointer to measure the cycle length.
## Reorder or Split Linked List: When partitioning or rearranging a linked list, finding the middle node is often crucial.
## 4. How the Fast & Slow Pointers Work

## Step-by-Step Movement

## Initialization: Set both pointers to the head of the list.
## Movement: In each iteration:
## The slow pointer (let’s call it slow) moves by 1 node.
## The fast pointer (let’s call it fast) moves by 2 nodes.
## Check Condition:
## If fast (or fast.next) becomes null, it means there’s no cycle (you’ve reached the end).
## If slow meets fast, there is a cycle or a special condition we’re looking for.
Visual:

Linked List: A -> B -> C -> D -> E -> F -> G -> ...
slow = A
fast = A

Iteration 1:
  slow -> B
  fast -> C

Iteration 2:
  slow -> C
  fast -> E

...
## You continue until fast is null (no cycle) or slow == fast (cycle detected or specific position reached).

## Let’s jump onto this problem to see Fast & Slow pattern in action.