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
    
def insert_one(student_obj):
    student_obj_id = db.students.insert_one(student_obj).inserted_id
    print(f'Inserted student record into students collection with document_id {student_obj_id}');
    return 

def delete_one(student_id):
    result = db.students.delete_one({"student_id": student_id})
    return

print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")
find()

new_student = { "student_id": 1010, "first_name": 'Newton', "last_name": 'Nonoe' }
print('-- INSERT STATEMENTS -- ')
insert_one(new_student)

print(" -- DISPLAYING STUDENT TEST DOC -- ")
find_one(1010)

# delete student 1010
delete_one(1010)
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")
find()