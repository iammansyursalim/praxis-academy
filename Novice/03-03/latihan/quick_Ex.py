from jinja2 import Template

t = Template("Hello {{ something }}!")
t.render(something="world")

t = Template("my favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")
t.render()