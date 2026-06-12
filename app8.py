from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "James",
        "age": 20,
        "college": "ABC College",
        "branch": "Computer Science"
    },
    {
        "id": 2,
        "name": "John",
        "age": 21,
        "college": "XYZ College",
        "branch": "Mechanical"
    },
    {
        "id": 3,
        "name": "Sara",
        "age": 19,
        "college": "ABC College",
        "branch": "Computer Science"
    }
]

# Get all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# Update Student
@app.route('/update-student/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()

    for student in students:
        if student["id"] == id:
            student["name"] = data.get("name", student["name"])
            student["age"] = data.get("age", student["age"])
            student["college"] = data.get("college", student["college"])
            student["branch"] = data.get("branch", student["branch"])

            return jsonify({
                "message": "Student updated successfully",
                "student": student
            })

    return jsonify({"message": "Student not found"}), 404

# Student Count
@app.route('/student-count', methods=['GET'])
def student_count():
    return jsonify({
        "total_students": len(students)
    })

# Student Branch Filter
@app.route('/students/branch/<branch>', methods=['GET'])
def students_by_branch(branch):
    filtered_students = [
        student for student in students
        if student["branch"].lower() == branch.lower()
    ]

    return jsonify(filtered_students)

if __name__ == '__main__':
    app.run(debug=True)