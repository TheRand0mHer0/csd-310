from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.1bsup9t.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

def find():
    all_students = db.students.find({})
    for student in all_students:
        print(f'Student Id: {student.student_id}\nFirst Name: {student.first_name}\nLast Name: {student.last_name}\n\n')
    return all_students
    
def find_one(student_id):
    student = db.students.find_one({"student_id": student_id})
    print(f'Student Id: {student.student_id}\nFirst Name: {student.first_name}\nLast Name: {student.last_name}\n\n')
    return student
    

print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")
find()
print(" -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY -- ")
find_one(1008)
