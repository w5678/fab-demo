from flask import Markup, url_for, g
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Table, Column,Enum ,Integer, String, ForeignKey, Date, Float, Text,text,TIMESTAMP,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from flask_appbuilder.models.decorators import renders
from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqualFunction

from datetime import datetime
#学院
class College(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

#部门
class Department(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

#专业
class Major(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

#班级
class MClass(Model):
    __tablename__ = 'mclass'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

#教师
class Teacher(Model):
    id = Column(Integer, primary_key=True)
    work_num = Column(String(30), unique=True, nullable=False)  #工号
    name = Column(String(50), nullable=False)
    college_id = Column(Integer, ForeignKey('college.id'), nullable=False)  #学院
    college = relationship("College")
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)    #部门
    department = relationship("Department")
    tel_num = Column(String(30), unique=True, nullable=False)   #电话号
    birthday = Column(Date)

    def __repr__(self):
        return self.name

assoc_teacher_student = Table('teacher_student', Model.metadata,
                                      Column('id', Integer, primary_key=True),
                                      Column('teacher_id', Integer, ForeignKey('teacher.id')),
                                      Column('student_id', Integer, ForeignKey('student.id'))
)

# 学生
class Student(Model):
    id = Column(Integer, primary_key=True)
    stu_num = Column(String(30), unique=True, nullable=False)  #学号
    name = Column(String(50), nullable=False)
    college_id = Column(Integer, ForeignKey('college.id'), nullable=False)
    college = relationship("College")
    major_id = Column(Integer, ForeignKey('major.id'), nullable=False)
    major = relationship("Major")
    mclass_id = Column(Integer, ForeignKey('mclass.id'), nullable=False)
    mclass = relationship("MClass")
    teachers = relationship('Teacher', secondary=assoc_teacher_student, backref='student')
    tel_num = Column(String(30), unique=True, nullable=False)   #电话号
    birthday = Column(Date)

    def __repr__(self):
        return self.name




class Baseimage(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    version = Column(String(64), nullable=False)
    pxeversion = Column(String(64), nullable=False)
    test_status = Column(Enum("QA","Public","Private"), nullable=False)
    status = Column(Enum("QA","Public","Private"), nullable=False)
    owner = Column(String(32), nullable=False)
    changelog = Column(Text(512), nullable=False)
    ctime = Column(DateTime,nullable=False)
    utime = Column(TIMESTAMP, nullable=False)


    def __repr__(self):
        return self.name


