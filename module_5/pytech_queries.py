from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.1bsup9t.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

def find():
    all_students = db.students.find({})
    for student in all_students:
        student_id = student.get('student_id')
        first_name = student.get('first_name')
        last_name = student.get('last_name')
        print(f'Student Id: {student_id}\nFirst Name: {first_name}\nLast Name: {last_name}\n\n')
    return all_students

def find_one(student_id):
    student = db.students.find_one({"student_id": student_id})
    student_id = student.get('student_id')
    first_name = student.get('first_name')
    last_name = student.get('last_name')
    print(f'Student Id: {student_id}\nFirst Name: {first_name}\nLast Name: {last_name}\n\n')
    return student
    

print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")
find()
print(" -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY -- ")
find_one(1008)
