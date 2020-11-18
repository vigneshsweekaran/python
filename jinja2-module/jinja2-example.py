from jinja2 import Template,escape

# Reference : http://zetcode.com/python/jinja/
########################## Data passed as string ################################
# t = Template("Hello {{ something }}")
# output = t.render(something="world")
# print(output)


########################### Data passed as variable ###############################
# name="vignesh"
# skill="python"
# t = Template("My name is {{ name }} and my programming skill is {{ skill }} ")
# output = t.render(name=name, skill=skill)
# print(output)


########################### Data passed as object ##################################
# class Person:
#     def __init__(self, name, skill):
#         self.name = name
#         self.skill = skill
#
#     def getName(self):
#         return self.name
#
#     def getSkill(self):
#         return self.skill
#
#
# person = Person('vignesh', 'python')
#
# t = Template("My name is {{ person.getName() }} and my programming skill is {{ person.getSkill() }} ")
# output = t.render(person=person)
# print(output)


############################# Data passed as dictionary #########################################
# #Jinja allows a convenient dot notation to access data in Python dictionaries.
# person = { 'name': 'Person', 'age': 34 }
#
# tm = Template("My name is {{ per.name }} and I am {{ per.age }}")
# # tm = Template("My name is {{ per['name'] }} and I am {{ per['age'] }}")
# msg = tm.render(per=person)
# print(msg)


############################# Jinja raw data ###################################################
## We can use raw, endraw markers to escape Jinja delimiters.
# data = '''
# {% raw %}
# His name is {{ name }}
# {% endraw %}
# '''
#
# tm = Template(data)
# msg = tm.render(name='Peter')
# print(msg)


################################ Jinja escape data ################################################
# data = '<a>Today is a sunny day</a>'
#
# tm = Template("{{ data | e }}")
# msg = tm.render(data=data)
# print(msg)
# print(escape(data))
