from app1.models import *
from django.contrib.auth.models import User

# exec(open(r'C:\Users\SAMeer\OneDrive\Desktop\Rohini_Python_Program\DjangoProjects\first_project\app1\db_shell.py').read())


# to get all data
# objs = Person.objects.all()
# print(list(objs))

# for person in objs:
#     print(person.__dict__)

# to get first record
# first_record = Person.objects.first()
# print(first_record)

# to get recird by passing id
# obj = Person.objects.get(id = 3) # single record
# print(obj)

# if record doesnot exists
# try:
#     obj = Person.objects.get(id = 4) # single record
#     print(obj)
# except Person.DoesNotExist:  
#     print("Record does not exist")

# to get multiple record by passing filename
# objs = Person.objects.filter(age = 25)
# print(objs)

# objs = Person.objects.filter(age = 25)  # it will print where query
# print(objs.query)
# SELECT "person"."id", "person"."name", "person"."age", "person"."mobile_num", "person"."address" FROM "person" WHERE "person"."age" = 25

# objs = Person.objects.filter(age = 25, address = 'Bangalore')  # , and
# print(objs.query)   
# SELECT "person"."id", "person"."name", "person"."age", "person"."mobile_num", "person"."address" FROM "person" WHERE ("person"."address" = Bangalore AND "person"."age" = 25)

# objs = Person.objects.filter(age = 25, marks = 'Bangalore')  # , and
# print(objs)   

# to get query 
# objs = Person.objects.all()
# print(objs.query)     
# SELECT "person"."id", "person"."name", "person"."age", "person"."mobile_num", "person"."address" FROM "person"

# modify existing data
# p1 = Person.objects.get(id = 1)
# print(p1.__dict__)  # print in dict module
# print(p1.mobile_num) # it will print mobuile number
# p1.mobile_num = 9857777127
# print(p1.__dict__)
# p1.save()

# how to create object 
# 1st way
# p1 = Person(name ="abc", age = 29, mobile_num = 6553451842, address = "Nanded")
# p1.save()
# 2nd way
# Person.objects.create(name ="xyz", age = 32, mobile_num = 8214518472, address = "Akola")

# # print(dir(Person.objects))
# 'aggregate', 'alias', 'all', 'annotate', 'auto_created', 'bulk_create',
# 'bulk_update', 'check', 'complex_filter', 'contribute_to_class', 'count', 'create', 'creation_counter', 
# 'dates', 'datetimes', 'db', 'db_manager', 'deconstruct', 'defer', 'difference', 'distinct', 'earliest', 
# 'exclude', 'exists', 'explain', 'extra', 'filter', 'first', 'from_queryset', 'get', 'get_or_create',
# 'get_queryset', 'in_bulk', 'intersection', 'iterator', 'last', 'latest', 'model', 'name', 'none', 
# 'only','order_by', 'prefetch_related', 'raw', 'reverse', 'select_for_update', 
# 'select_related', 'union', 'update', 'update_or_create', 'use_in_migrations', 'using', 'values', 'values_list'

# bulk_create
# p1 = Person(name = "P", age = 27, mobile_num = 9845761234, address = "Thane")
# p2 = Person(name = "Q", age = 18, mobile_num = 9453185237, address = "Pune")
# p3 = Person(name = "R", age = 37, mobile_num = 9845722222, address = "chennai")
# p4 = Person(name = "S", age = 49, mobile_num = 9845711111, address = "Mumbai")
# Person.objects.bulk_create([p1, p2, p3, p4])

# count records 
# print(Person.objects.count())   # 11

# to delete all records
# Person.objects.all().delete()

# to delete multiple records
# Person.objects.filter(age=25).delete()

# to get names startswith any latter
# print(Person.objects.filter(name__startswith = "A"))

#  to get names endswith any latter
# print(Person.objects.filter(name__endswith = "t"))

# exclude
# print(Person.objects.exclude(name__startswith = "A"))

# exsits - it will print in true false
# print(Person.objects.filter(id=1).exists())
# print(Person.objects.filter(name = "Apurva").exists())
# print(Person.objects.filter(name = "Apurva1").exists())

# order_by
# print(Person.objects.all().order_by("id"))  # only id - it will print in Asscending order
# print(Person.objects.all().order_by("-id")) #  -id - it will print in Descending order

# print(Person.objects.all().order_by("name"))  # only id - it will print in Asscending order
# print(Person.objects.all().order_by("-name"))

# Person.objects.get(id=1).show_details()

# for per_obj in Person.objects.all():
#     per_obj.show_details()

# print(Person.get_data_above_age())


# exec(open(r'C:\Users\SAMeer\OneDrive\Desktop\Rohini_Python_Program\DjangoProjects\first_project\app1\db_shell.py').read())

# 103 session
# print(Person.objects.all())

# contains
# print(Person.objects.filter(name__contains = "K"))

# values
# data = Person.objects.all().values("id", "name", "age")
# print(data)

# # values by using for loop
# data = Person.objects.all().values()
# for i in data:
#     print(i, type(i))

# data = Person.objects.all().values("id", "name", "age")
# names_list = []
# for i in data:
#     names_list.append(i["name"])
# print(names_list)

# average of age
# data = Person.objects.all().values("id", "name", "age")
# lst = (list(map(lambda x : x['age'], list(data))))
# print(sum(lst)//len(lst))

# values_list - its a list of tuple containing values only
# data = Person.objects.all().values_list("name")
# print(list(data))

# database change to mysql
# create user
# User.objects.create_user(username = "Poonam" , password ="python@123") # always user create_user for creating new user

# Task
# PostgreSQL -- yt -- python connect -- psycopg2---
# UI -- pgAdmin4 --

# print(Person.objects.all())
# delete  - soft delete, hard delete

# update
# data = Person.objects.filter(id__in=[3, 5]).update(is_active = False)
# print(data)

# p1 = Person.objects.get(id=3)
# p1.is_active= False
# p1.save()



# for i in data:
#     i.is_active = False()
#     i.save()


# print(Person.activep.all())
# print(Person.inactivep.all())

# print(Person.all_data.all())

# exec(open(r'C:\Users\SAMeer\OneDrive\Desktop\Rohini_Python_Program\DjangoProjects\first_project\app1\db_shell.py').read())
# 104 , 105
# clgs = College.objects.all() 
# prnc = Principal.objects.all()
# depts = Department.objects.all()
# studs = Student.objects.all()
# subjs = Subject.objects.all()

# print(clgs)
# print(prnc)
# print(depts)
# print(studs)
# print(subjs)

# depts = Department.objects.all()
# for dept in depts:
#     print(dept.__dict__)
    
# studs = Student.objects.all()
# for stud in studs:
#     print(stud.__dict__)
    
# subjs = Subject.objects.all()
# for subj in subjs:
#     print(subj.__dict__)

# clgs = College.objects.all() 
# clg = clgs[0]
# print(clg)
         
# clgs = College.objects.all() 
# clg = clgs[0]
# print(clg.principal.__dict__)       

# savita_obj = Principal.objects.first() 
# print(savita_obj.College)

# clgs = College.objects.all() 
# clg = clgs[0]
# print(clg.department_set.all())

# depts = Department.objects.first()
# print(depts.College)


# get all studs dept wise
# all_depts = Department.objects.all()
# d = {}
# for depts in all_depts:
#     print(f"Departament Name:- {depts.name}, Studs:- {list(depts.student_set.all())}")
    

# all_depts = Department.objects.all()
# d = {}
# for depts in all_depts:
#     d[depts.name] = list(depts.student_set.all())
# print(d)

# s1 = Student.objects.first()
# print(s1.dept)

# s1 = Student.objects.get(id = 6)
# print(s1.dept)

# get department from student
# studs = Student.objects.all()
# for stud in studs:
#     print(stud)

# get stud_department dict
# studs = Student.objects.all()
# stud_dept_dict = {}
# for stud in studs:
#     stud_dept_dict[stud.name] = stud.dept.name
# print(stud_dept_dict)    
# {'Mohini': 'EE', 'Mosami': 'EE', 'Rashid': 'EE', 'Rohit': 'IT', 'Priyanka': 'IT', 'Prajkta': 'IT', 'Sayali': 'Civil', 'Seema': 'Civil', 'Samyak': 'Civil'}


# clg = College.objects.get(id = 1)
# print(clg.princi)

# clg = College.objects.get(id = 1)
# print(clg.depts.all())


# depts = Department.objects.get(id = 1)
# print(depts.subjs.all())

# depts = Department.objects.get(id = 2)
# print(depts.subjs.all())

# depts = Department.objects.get(id = 3)
# print(depts.subjs.all())

# depts = Department.objects.all()
# for dept in depts:
#     print(dept.subjs.all())

# by using list comphrehension 
# depts = Department.objects.all()
# for dept in depts:
#     print(dept.subjs.all())
# print([list(dept.subjs.all() for depts in Department.objects.all())])

# collage se diect IT vale student nikalne k liye
# clg = College.objects.get(id = 1)
# print(clg.depts.all()[1].studs.all())   # IT students

# clg = College.objects.get(id = 1)
# print(clg.depts.all()[0].studs.all())   # EE Students

# clg = College.objects.get(id = 1)
# print(clg.depts.all()[2].studs.all())   # Civil Students

# # if you want all students then - 1st way
# clg = College.objects.get(id = 1)
# stude_list = []
# for dept in clg.depts.all():
#     stude_list.extend(dept.studs.all())
# print(stude_list)

# 2nd way
# stude_list = []
# for dept in College.objects.get(id = 1).depts.all():
#     stude_list.extend(dept.studs.all())
# print(stude_list)


# students se clg ka name nikalne k liye
# stud = Student.objects.get(id = 5)
# print(stud.dept.College.est_date)

# Addition 

# College.objects.create(name = "MIT", adr = "Kothrud")

# 1st way
# c1 = College.objects.get(id = 3)
# p1 = Principal.objects.create(name="ABC" , exp = 15, qual="PHD", College = c1)  # as it is pass object to clg
# p1.save()

# 2nd way
# p1 = Principal(name="ABC" , exp = 20, qual="PHD", College_id= 3)  # pass college id, collage_id
# p1.save()


# make sure collage id is paresnt in table
# c1 = College.objects.get(id = 3)
# Department.objects.create(name = "Production", dept_str = 80, College = c1) # collage ka instance(collage) pass karo ya phir collage_id 

# c1 = College.objects.get(id = 1)
# Department.objects.create(name = "Petrochemical", dept_str = 80, College = c1) # collage ka instance(collage) pass karo ya phir collage_id 


# depart k anada students bana ne hai so first create your student
# Student.objects.create(name = "A", marks = 44, age = 18)
# Student.objects.create(name = "B", marks = 97, age = 17)
# Student.objects.create(name = "C", marks = 49, age = 19)

# s1, s2, s3 = Student.objects.filter(id__gt = 9)
# print(s1, s2, s3)


# creating student relation department
# s1, s2, s3 = Student.objects.filter(id__gt = 9)
# prod_dept = Department.objects.get(id = 4)
# # print(dir(prod_dept))
# prod_dept.studs.add(s1, s2, s3) # one to many  -  add students in one to many

# college - MIT -- id 3
# Department - Production -- id 4
# Students -- A-- 10, B -- 11, C -- 12

# exec(open(r'C:\Users\SAMeer\OneDrive\Desktop\Rohini_Python_Program\DjangoProjects\first_project\app1\db_shell.py').read())

# 106 
# prod_dept = Department.objects.get(id = 4)
# print(dir(prod_dept.studs))

# select related
# studs = Student.objects.select_related("dept")
# for stud in studs:
#     print(stud.dept)
    
# studs = Student.objects.select_related("dept")
# for stud in studs:
#     print(stud.dept.name)    

# Many to Many
# create car models
# c180 = CarModel.objects.create(name="C180")
# c200 = CarModel.objects.create(name="C200")
# print(CarModel.objects.all())

# gas = FuelType.objects.create(name="Gas")
# diesel = FuelType.objects.create(name="Diesel")
# hybrid = FuelType.objects.create(name="Hybrid")
# print(FuelType.objects.all())

# get car models
# c180 = CarModel.objects.get(name="C180")
# c200 = CarModel.objects.get(name="C200")

# get fuel types
# gas = FuelType.objects.get(name="Gas")
# diesel = FuelType.objects.get(name="Diesel")
# hybrid = FuelType.objects.get(name="Hybrid")

# add fuel types
# c180.fueltype.add(gas)
# c180.fueltype.add(diesel, hybrid)

# fetch all fuel type
# c180.fueltype.all()

# add fuel types
# c200. fueltype.add(gas, diesel, hybrid)

# create new fule type 
# c200.fueltype.create(name = "Bio diesel") # create and assign to c200

# fetch all data for both the models
# print(c200.fueltype.all())
# print(c180.fueltype.all())

# associate the fueltype with car model
# print(gas.carmodel_set.all())
# print(diesel.carmodel_set.all())
# print(hybrid.carmodel_set.all())

# print(gas.carmodels.all())



# filter carmodel record
# print(CarModel.objects.filter(fueltype__name__startswith="G"))

# fetch fuetype
# print(FuelType.objects.filter(carmodels__name="c180"))
# print(FuelType.objects.filter(carmodels__name="c200"))

#  use of distinct
# print(FuelType.objects.filter(carmodels__name__startswith="C").distinct())

# print(c180.fueltype.clear())

# 107
# exec(open(r'C:\Users\SAMeer\OneDrive\Desktop\Rohini_Python_Program\DjangoProjects\first_project\app1\db_shell.py').read())


# Raw AQL Databse
# 1st way 
# from django.db import connection
# cursor = connection.cursor()
# cursor.execute('''SELECT * FROM b8_db.student''')
# data = cursor.fetchall()
# print(data)

# cursor = connection.cursor()
# cursor.execute('''SELECT * FROM b8_db.student''')
# data = cursor.fetchmany(3)
# print(data)

# 2nd way 
# data = Student.objects.raw('SELECT * FROM Student')
# for i in data:
#     print(i)


# Multiple Databse
# MySQL, SQLite3

# data = Student.objects.all()
# print(data)

# SECOND_DATABASE = "second_db"
# data = Student.objects.using(SECOND_DATABASE).all()
# print(data)

# to create database
# databse = Student.objects.using(SECOND_DATABASE).create()

# c1 = College.objects.using(SECOND_DATABASE).create(name = "COEP", adr = "Pune")
# d1 = Department.objects.using(SECOND_DATABASE).create(name = "ENTC", dept_str = 60, College = c1)
# s1 = Student.objects.using(SECOND_DATABASE).create(name = "XYZ", marks = 89, age = 25, dept = d1)
# s1 = Student.objects.using(SECOND_DATABASE).create(name = "PQR", marks = 98, age = 26, dept = d1)
# d1 = Department.objects.get(id = 1)
# Subject.objects.create(name = "Data Signal", is_practical = True, dept = d1)

# to fecth all data in second_db
# studs = Student.objects.using(SECOND_DATABASE).all()
# print(studs)



