import datetime
"""This is a bio about myself, Jeffrey Kimani Wainaina.
I am trying to compose every aspect of my life that I
can gather/remember.

It is also my Python Variables practice lesson.
I hope to be a pythooneer/pythonista very soon!!!
    """

Name = "Jeffrey Kimani Wainaina"
IDNumber = 35698148
BirthDate = datetime.date(1962, 12, 31)
CurrentDate = datetime.date(2021, 1, 27)
Difference = CurrentDate - BirthDate
#Age will be displayed in form of days
AgeInDays = Difference.days
AgeInYears = str(AgeInDays/365) + " years old"
Profession = "Computer Scientist"
DreamJob = "Data Scientist"
Father = "John"
Mother = "Christine"
NumberOfSiblings = 3
NumberOfMaleSiblings = 2
NumberOfFemaleSiblings = 1
NamesofSiblings = "Brian Wainaina, Karen Wainaina, Wayne Wainaina"
Dating = True

#love of my life
NameOfWife = "Gladys Kimani Muendo"

NumberOfChildren = 0


print(Name)
print(IDNumber)
print(AgeInDays)
print(AgeInYears)
print(Profession)
print(DreamJob)
print(Father)
print(Mother)
print(NumberOfSiblings)
print(NumberOfMaleSiblings)
print(NumberOfFemaleSiblings)
print(NamesofSiblings)
print(Dating)
print(NameOfWife)
print(NumberOfChildren)