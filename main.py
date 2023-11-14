from teacher_crud import TeacherCRUD

crud = TeacherCRUD()

crud.create('Chris Lima', 1956, '189.052.396-66')
result = crud.read('Chris Lima')
print("Query Result:", result)

crud.update('Chris Lima', '162.052.777-77')

crud.db.close()