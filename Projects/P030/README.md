# Design Patterns

Implement the following patterns in the language of your choice: 

## Creational Patterns

### Factory

- also known as "Concrete Factory"
- mentioned as a byproduct of the "Abstract Factory" in [Gamma1995]

### Abstract Factory

- [Gamma1995], p. 89:
  - Normally a single instance of a ConcreteFactory class is created at run-time. This concrete factory creates product objects having a particular implementation. To create different product objects, clients should use a different concrete factory.
  - AbstractFactory defers creation of product objects to its ConcreteFactory subclass.

### Builder

- [Gamma1995], p. 99:
  - The client creates the Director object and configures it with the desired Builder object.
  - Director notifies the builder whenever a part of the product should be built.
  - Builder handles requ4ests from the director and adds parts to the product.
  - The client retrieves the product from the builder.

### Factory Method

- [Gamma1995], p. 109:
  - Creator relies on its subclasses to define the factory method so that it returns an instance of the appropriate ConcreteProduct

### Prototype

- [Gamma1995], p. 119:
  - A client asks a prototype to clone itself

### Singleton

- [Gamma1995], p. 128:
  - Clients access a Singleton instance solely through Singleton's Instance operation.

## Structural Patterns

### Adapter

- [Gamma1995], p. 141:
  - Clients call operations on an Adapter instance. In turn, the adapter calls Adaptee operations that carry out the request.

### Bridge

- [Gamma1995], p. 154:
  - Abstraction forwards client requests to its Implementor object

- [Video](https://www.youtube.com/watch?v=9jIgSsIfh_8)
  - Progressivly adding functionality while separating out major differences into separate classes

### Composite

- [Gamma1995], p. 165:
  - Clients use the Component class interface to interact with objects in the composite structure. If the recipient is a Leaf, then the request is handled directly. If the recipient is a Composite, then it usually forwards requests to its child components, possibly performing additional operations before and/or after forwarding.

### Decorator

- [Gamma1995], p. 178:
  - Decorator forwards requests to its Component object. It may optionally perform additional operations before and after forwarding the request.

### Facade 

- [Gamma1995], p. 187:
  - Clients communicate with the subsystem by sending requests to Facade, which forwards them to the appropriate subsystem object(s). Although the subsystem objects perform the actual work, the facade may have to do work of its own to translate its interface to subsystem interfaces.
  - Clients that use the facade don't have to access its subsystem objects directly.

### Flyweight

- [Gamma1995], p. 199:
  - State that a flyweight needs to function must be characterized as either intrinsic or extrinsic. Intrinsic state is stored in the ConcreteFlyweight object; extrinsic state is stored or computed by Client objects. Clients pass this state to the flyweight when they invoke its operations.
  - Clients should not instantiate ConcreteFlyweights directly. Clients must obtain ConcreteFlyweight objects exclusivly from the FlyweightFactory object to ensure they are shared properly.

### Proxy

- [Gamma1995], p. 210:
  - Proxy forwards requests to RealSubject when appropriate, depending on the kind of proxy.

## Behavioral Patterns

### Chain of Responsibility

- [Gamma1995], p. 226:
  - When a client issues a request, the request propagates along the chain until a ConcreteHandler object takes responsibility for handling it.

### Command

- [Gamma1995], p. 237:
  - The client creates a ConcreteCommand object and specifies its receiver.
  - An Invoker object stores the ConcreteCommand object.
  - The invoker issues a request by calling Execute on the command. When commands are undoable, ConcreteCommand stores state for undoing the command prior to invoking Execute.
  - The ConcreteCommand object invokes operations on its receiver to carry out the request.

https://www.youtube.com/watch?v=zRbHlDeon3E

### Interpreter

- [Gamma1995], p. 246:
  - The client builds (or is given) the sentence as an abstract syntax tree of NonterminalExpression and TerminalExpression instances. Then the client initializes the context and invokes the Interpret operation.
  - Each Nonterminal Expression node defines Interpret in terms of Interpret on each subexpression. The Interpret operation of each TerminalExpression defines the base case in the recursion.
  - The Interpret operations at each node use the context to store and access the state of the interpreter.

### Iterator

- [Gamma1995], p. 260:
  - A ConcreteIterator keeps track of the current object in the aggregate and can compute the succeeding object in the traversal.

### Mediator

- [Gamma1995], p. 277:
  - Colleagues send and receive requests from a Mediator object. The mediator implements the cooperative behavior by routing requests between the appropriate colleague(s).

### Memento

- [Gamma1995], p. 286:
  - A caretaker requests a memento from an originator, holds it for a time, and passes it back to the originator [...]. Sometimes the caretaker won't pass the memento back to the originator, because the originator might never need to revert to an earlier state.
  - Mementos are passive. Only the originator that created a memento will assign or retrieve its state.

### Observer

- [Gamma1995], p. 295:
  - ConcreteSubject notifies its observers whenever a change occurs that could make its observers' state inconsistent with its own.
  - After being informed of a change in the concrete subject, a ConcreteObserver objectmay query the subject for information. ConcreteObjserver uses this information to reconsile its state with that of the subject. [...]

### State

- [Gamma1995], p. 307:
  - Context delegates state-specific requests to the current ConcreteState object.
  - A context may pass itself as an argument to the State object handling the request. This lets the State object access the context if necessary. 
  - Contect is the primary interface for clients. Clients can configure a context with State objects. Once a context is configured, its clients don't have to deal with the State objects directly.
  Either Context or the ConcreteState subclasses can decide which state succeeds another and under what circumstances.

### Strategy

- [Gamma1995], p. 317:
  - Strategy and Context interact to implement the chosen algorithm. A context may pass all data required by the algorithm to the stategy when the algorithm is called. Alternativly, the context can pass itself as an argument to Strategy operations. That lets the strategy call back on the context as required.
  - A context forwards requests from its clients to its strategy. Clients usually create and pass a ConcreteStrategy object to the context; thereafter, clients interact with the context exclusively. There is often a family of ConcreteStrategy classes for a client to choose from.

### Template Method

- [Gamma1995], p. 327:
  - ConcreteClass relies on AbstractClass to implement the invariant steps of the algorithm.

### Visitor

- [Gamma1995], p. 335:
  - A client that uses the Visitor pattern must create a ConcreteVisitor object and then traverse the object structure, visiting each element with the visitor.
  - When an element is visited, it calls the Visitor operation that corresponds to its class. The element supplies itself as an argument to this operation to let the visitor access its state, if necessary. [...]


----

## Literature

- [X] [Gamma1995](https://www.amazon.de/Patterns-Elements-Reusable-Object-Oriented-Software/dp/0201633612/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=169HFZV3RS1XT&keywords=Design+Patterns&qid=1645804329&sprefix=design+patterns+%2Caps%2C94&sr=8-1) Design Patterns - Elements of Reuseable Object-Oriented Software
- [ ] [Geirhos2015](https://www.amazon.de/Entwurfsmuster-umfassende-Handbuch-Matthias-Geirhos/dp/3836227622/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=JFWOZ44IY034&keywords=Entwurfsmuster+-+das+umfassende+Buch&qid=1645804344&sprefix=entwurfsmuster+-+das+umfassende+buch%2Caps%2C73&sr=8-3) Entwurfsmuster - das umfassende Buch
- [ ] [Freeman2020](https://www.amazon.de/Head-First-Design-Patterns-Object-Oriented/dp/149207800X/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=33FBW8Q5AO3LZ&keywords=Building+Extensible+%26+Maintainable+Object-Oriented+Software&qid=1645804370&sprefix=building+extensible+%26+maintainable+object-oriented+software%2Caps%2C63&sr=8-1) Head First, Design Patterns - Building Extensible & Maintainable Object-Oriented Software, Second Edition
