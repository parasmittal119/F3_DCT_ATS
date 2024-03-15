from jinja2 import Template

t = Template("HELLO {{ something }}")
print(t.render(something="World!"))

t = Template("for loop o/p : {% for n in range(1,11) %}{{n}}"" {%endfor%}")
print(t.render())