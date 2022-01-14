from oop_review import *

snape = Professor("Snape")
harry = Student("Harry", snape)

harry.visit_office_hours(snape) 

harry.visit_office_hours(Professor("Hagrid")) 

harry.understanding 
