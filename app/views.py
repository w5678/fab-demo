# 导入相关的包和模块

from flask import render_template, flash
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, MultipleView, MasterDetailView
from app import appbuilder, db
from flask_appbuilder import AppBuilder, expose, BaseView, has_access, SimpleFormView
from flask_babel import lazy_gettext as _
from flask_appbuilder.charts.views import DirectByChartView

from wtforms import Form, StringField
from wtforms.validators import DataRequired
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm

from flask_appbuilder.widgets import ListThumbnail
from .models import College, Department, Major, MClass, Teacher, Student
from .models import Baseimage
from flask_appbuilder.actions import action
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget, Select2Widget

# 这里定义了学院、部门、专业、班级、教师和学生的相关视图。
# 代码比较简单，直接关联我们定义好的模型就可以了，代码如下：

class CollegeView(ModelView):
    datamodel = SQLAInterface(College)
    list_columns=["name"]

class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    list_columns=["name"]

class MajorView(ModelView):
    datamodel = SQLAInterface(Major)
    list_columns=["name"]

class MClassView(ModelView):
    datamodel = SQLAInterface(MClass)
    list_columns=["name"]

class TeacherView(ModelView):
    datamodel = SQLAInterface(Teacher)
    list_columns=["name"]

class StudentView(ModelView):
    datamodel = SQLAInterface(Student)
    list_columns=["name"]

class BaseimageView(ModelView):
    datamodel = SQLAInterface(Baseimage)
    list_columns=["name"]

#db.drop_all()
db.create_all()

# 这里将6个视图作为子菜单添加到了`School Manage`菜单中：

appbuilder.add_view(CollegeView, "College", icon="fa-apple", category='School Manage',)
appbuilder.add_view(DepartmentView, "Department", icon="fa-android",category='School Manage')
appbuilder.add_view(MajorView, "Major", icon="fa-chrome", category='School Manage')
appbuilder.add_view(MClassView, "MClass", icon="fa-github", category='School Manage')
appbuilder.add_view(TeacherView, "Teacher", icon="fa-edge",category='School Manage')
appbuilder.add_view(StudentView, "Student", icon="fa-linux",category='School Manage')

# baseimage 
appbuilder.add_view(BaseimageView, "Baseimage", icon="fa-weixin",category='OSaaS Baseimage')



