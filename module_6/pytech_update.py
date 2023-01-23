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
    
def update_student_last_name(student_id, new_last_name):
    result = db.students.update_one({"student_id": student_id}, {"$set": {"last_name": new_last_name}})
    return result

def find_one(student_id):
    student = db.students.find_one({"student_id": student_id})
    student_id = student.get('student_id')
    first_name = student.get('first_name')
    last_name = student.get('last_name')
    print(f'Student Id: {student_id}\nFirst Name: {first_name}\nLast Name: {last_name}\n\n')
    return student
    

print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")
find()

# update student 1007
update_student_last_name(1007, "Grewal")

print(" -- DISPLAYING STUDENT DOCUMENT 1007 -- ")
find_one(1007)