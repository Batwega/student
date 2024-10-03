class StudentRegistration:
    def __init__(self):
        # Initialize an empty list to store student registrations
        self.students = []

    def add_student(self, name, reg_number):
        """Add a student's name and registration number to the list."""
        if name and reg_number:  # Ensure both name and reg_number are provided
            self.students.append({'name': name, 'registration_number': reg_number})
        else:
            print("Both name and registration number must be provided.")

    def display_students(self):
        """Display all registered students and their registration numbers."""
        if not self.students:
            print("No students registered.")
        else:
            print("Registered Students:")
            for student in self.students:
                print(f"Name: {student['name']}, Registration Number: {student['registration_number']}")


if __name__ == "__main__":
    registration = StudentRegistration()
    registration.add_student("josephine ayebare", "REG078")
    registration.add_student("humphary made", "REG004")
    registration.display_students()
    
if __name__ == "__main__":
    registration = StudentRegistration()
    registration.add_student("sinead kwagala", "reg065")
    registration.add_student("mebra khauda", "reg011")
    registration.add_student("desire jael", "reg095")
    registration.display_students()
    
    if __name__ == "__main__":
        registration = StudentRegistration()
        registration.add_student("joel junior", "reg055")
        registration.add_student("benji ogwal", "reg097")
        registration.add_student("gideon jeremy","reg045")
        registration.display_students()
            
        
        
    
