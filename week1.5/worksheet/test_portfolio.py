from rect import Rectangle
from person import Person
from datetime import date

#Test Rectangle
print("=== RECTANGLE TESTS ===")

r1 = Rectangle(4, 5)
print("Area:", r1.area())
print("Perimeter:", r1.perimeter())
print("Is square:", r1.is_square())

r2 = Rectangle(4, 4)
print("Square area:", r2.area())
print("Square perimeter:", r2.perimeter())
print("Is square:", r2.is_square())

#Test Person
print("=== PERSON TESTS ===")

p1 = Person("Alan John Smith", date(2000, 5, 10))
print("Initials:", p1.initials())
print("Is birthday:", p1.is_birthday())

today = date.today()
p2 = Person("Sara Ahmed", today)
print("Today's initials:", p2.initials())
print("Is birthday today:", p2.is_birthday())


# Test Invalid Inputs

print("=== ERROR TESTS ===")

try:
    Rectangle(4.5, 5)
except TypeError:
    print("PASS: Rectangle rejects float width")

try:
    Rectangle(4, "5")
except TypeError:
    print("PASS: Rectangle rejects string height")

try:
    Rectangle(0, 5)
except ValueError:
    print("PASS: Rectangle rejects zero width")

try:
    Rectangle(4, -2)
except ValueError:
    print("PASS: Rectangle rejects negative height")

try:
    Person(123, date(2000, 5, 10))
except TypeError:
    print("PASS: Person rejects non-string name")

try:
    Person("", date(2000, 5, 10))
except ValueError:
    print("PASS: Person rejects empty name")

try:
    Person("Sara", "2000-05-10")
except TypeError:
    print("PASS: Person rejects non-date birth")