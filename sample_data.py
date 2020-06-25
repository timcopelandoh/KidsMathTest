import sqlite3
import names
import numpy as np
from add_record import add_student, add_class, add_score



students = 200
tests = 5
subjects = 3
class_size = 25

count = 0
student_id = 1

while count < students:

	first_name = names.get_first_name()
	last_name = names.get_last_name()
	email = first_name + last_name + '@ccs.edu'

	add_student(student_id, email, first_name, last_name, 12122013)

	add_class(student_id // class_size + 1, 2020, student_id)

	test_count = 0

	while test_count < tests:

		subject_count = 0

		while subject_count < subjects:

			add_score(student_id, subject_count+1, str(test_count+1) + '012020', np.random.randint(0,100))

			subject_count += 1

		test_count += 1

	student_id += 1
	count += 1


