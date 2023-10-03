What is inheritance?
Inheritance is an important aspect of the object-oriented paradigm. Inheritance provides code reusability to the program because we can use an existing class to create a new class instead of creating it from scratch.

In inheritance, the child class acquires the properties and can access all the data members and functions defined in the parent class. A child class can also provide its specific implementation to the functions of the parent class. 

Base Class
  ^
  |
  |
Derived Class

Types of inheritance in python?
1. Multi-level --->> The Derived class is inherite from another Derived class, there is no limit on the number of levels up to which
 class 1
   ^
   |
   |
 class 2
   ^
   |
   |
 class N

2. Multiple -->> In this type of inheritance, the one derived class can inherite multiple classes
  or in other word the multiple base class in the child class

  Base A    Base B   Base C

         
          Derived class

3. single inheritance
  where one derived class inherite from the  base class


4. Hierarchical Inheritance:
  Hierarchical inhertance involves multiple derived classed from one base class

5. Hybrid Inheritance:
  Hybrid inheritance is a combination of multiple types of inheritance. It can involve single, multiple, multilevel, or hierarchical inheritance in a single program.