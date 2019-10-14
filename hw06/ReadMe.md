Isaac Austin
ECE434 - HW06

*What Every Driver Developer Should Know about RT*
1) National Instruments
2) PREEMPT_RT is a Linux kernel patch that allows the OS to run in real-time 
3) When an embedded system runs two or more different types of tasks that need to communicate, some of which may be time critical
4) Cyclictest is a function that uses sleep to determine the delta time
5) Delta is the delay between an event occurring and the relevant task executing
6) 
7) Figure 2 is a histogram of response delays, comparing preempt and preempt_rt
8) Dispatch is the amount of time it takes for the scheduler to be aware of the event, and scheduling is the amount of time it takes the releveant task to execute
9) Mainline is a model that shows tasks being executed with interrupts 
10) The non-critical interrupt is preventing the CPU from addressing the event
11) A further interrupt tells the CPU that a more critical event should be handled first
