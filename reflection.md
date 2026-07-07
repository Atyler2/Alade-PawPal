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

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
