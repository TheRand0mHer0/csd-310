from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.1bsup9t.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

def insert_one(student_obj):
    student_obj_id = db.students.insert_one(student_obj).inserted_id
    print(f'Inserted student {student_obj.first_name} {student_obj.last_name} into students collection with document_id {student_obj_id}');
    return 


student_one = { "student_id": 1008, "first_name": 'ant', "last_name": 'tony' }
student_two = { "student_id": 1007, "first_name": 'yo', "last_name": 'lo' }
student_three = { "student_id": 1009, "first_name": 'test', "last_name": 'test' }

print("-- INSERT STATEMENTS --")
insert_one(student_one)
insert_one(student_two)
insert_one(student_three)