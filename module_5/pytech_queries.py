from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.1bsup9t.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

def find():
    all_students = db.students.find({})
    return all_students
    
def find_one(student_id):
    student = db.students.find_one({"student_id": student_id})
    return student