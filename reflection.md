# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Users should be able to add pets, schedule tasks and keep track of the tasks they completed
  -Design includes an Owner class that stores the data of the user, this class uses the Pet class which stores the data of the Owner's pets. The CareTask class can be assigned to a pet storing information about the tasks for this pet. Finally, the DailyPlan class uses both the Owner and pet classes to schedule the CareTasks.

**b. Design changes**

- Changes include Owner having a list of pets and Pet having a list of tasks with DailyPlan building a plan from those objects.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- The scheduler is lightweight but it only detects exact time conflicts,which makes it easy to use and fast but can miss real problems with overlapping duration.

---

## 3. AI Collaboration

**a. How you used AI**

- - I used the VScode Copilot to help me build the framework and give me certain instructions but to also review my code and provide me with an alternate perspective. The most useful prompts that I used were more focused on explaining different chunks of code or ways to implement ideas.

**b. Judgment and verification**

- Alot of the ideas the AI suggested were alternate to or completely against the instructions, some were interesting but didn't implement the idea of the app in the way I invisioned. This mainly occurred with the first diagram for the skeleton of the class structure,where the entire program was dependent on the DailyPlan class.

---

## 4. Testing and Verification

**a. What you tested**


I tested the core scheduling behaviors, including owner-pet relationships, task priority and feasibility along with filetering, plan generation and more. These tests were important becuase they verified that the scheduler makes sense and handles edge cases.
**b. Confidence**
confidence level: 4

- I am considerable confident that this program works although next time I would like to continue to use the AI to explain the different pieces of code it generates but also spend more time verfiying the code created.

---

## 5. Reflection

**a. What went well**

-I am most satisfied with the structure of the objects and how they work together.

**b. What you would improve**

- In another iteration I would improve readability by alot. 

**c. Key takeaway**

- One important thing that I learned about is the importance of having comprehensive tests. 
