# Step 1: Create the Student Class
class Student:
    def __init__(self, name, scores):
        
        self.name = name
        self.scores = scores

    def calculate_average(self):
        
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=50):
        
        return all(score >= passing_score for score in self.scores)


# Step 2: Create the PerformanceTracker Class
class PerformanceTracker:
    def __init__(self):
        
        self.students:list = {}

    def add_student(self, name, scores):
        
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        
        if not self.students:
            return 0
        total_scores = sum(student.calculate_average() for student in self.students.values())
        return total_scores / len(self.students)

    def display_student_performance(self):
        
        print("\nStudent Performance:")
        for student in self.students.values():
            avg_score = student.calculate_average()
            status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"Name: {student.name}, Average: {avg_score:.2f}, Status: {status}")


# Step 3 and Step 4: Handle User Input and Display Results
def main():
    
    tracker = PerformanceTracker()

    print("Welcome to the Student Performance Tracker!")
    while True:
        
        try:
            name = input("Enter the student's name (or type 'done' to finish): ")
            if name.lower() == 'done':
                break
            if name.isdigit():
                print("Invalid input. Please enter a valid name (not a number).")
                continue

            scores:list = []
            subjects:list=["math", "science", "english"]
            for i in subjects:  # Assume 3 subjects
                score = float(input(f"Enter score for subject {i}: "))
                scores.append(score)

            tracker.add_student(name, scores)
        except ValueError:
            print("Invalid input. Please enter numeric values for scores.")

    # Display results
    if tracker.students:
        tracker.display_student_performance()
        class_avg = tracker.calculate_class_average()
        print(f"\nClass Average: {class_avg:.2f}")
    else:
        print("No student data entered.")

if __name__ == "__main__":
    main()
