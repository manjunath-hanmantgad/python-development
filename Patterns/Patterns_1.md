Singleton Pattern:
Ensures a class has only one instance and provides a global point of access to it. This is useful when exactly one object is needed to coordinate actions across the system.

Factory Pattern:
Provides an interface for creating instances of a class, with its subclasses deciding which class to instantiate. It allows the client code to create objects without specifying the exact class of object that will be created.

Decorator Pattern:
Allows behavior to be added to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class. This pattern is useful for extending classes in a flexible and reusable way.

Observer Pattern:
Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. This pattern is widely used in implementing distributed event handling systems.

Strategy Pattern:
Defines a family of algorithms, encapsulates each algorithm, and makes them interchangeable. It allows the client code to choose an algorithm from a family of algorithms at runtime, without altering the code that uses the algorithm.

Iterator Pattern:
Provides a way to access the elements of an aggregate object (like a list) sequentially without exposing its underlying representation. This pattern is useful for traversing collections of objects without exposing the details of the collection's implementation.

Builder Pattern:
Allows for the construction of complex objects step by step. It separates the construction of a complex object from its representation, allowing the same construction process to create various representations.

Adapter Pattern:
Allows incompatible interfaces to work together. It wraps an existing class with a new interface, making it compatible with another class or system without altering its source code.

Composite Pattern:
Allows you to compose objects into tree structures to represent part-whole hierarchies. It lets clients treat individual objects and compositions of objects uniformly.

State Pattern:
Allows an object to alter its behavior when its internal state changes. The object will appear to change its class.

Command Pattern:
Encapsulates a request as an object, allowing for parameterization of clients with queues, requests, and operations. It also allows undoable operations.
