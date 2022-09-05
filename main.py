from jinja2 import Environment, FileSystemLoader

lookup = {}
for n in range(255):
  lookup[n] = chr(n)
stack = {}
for n in range(32):
  stack[n] = 0
cursor = len(stack)/2
code = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
cl = len(code)
l = [0] 

environment = Environment(loader=FileSystemLoader("./"))
template = environment.get_template("jinja.txt")

print(template.render(stack=stack, cursor=cursor, code=code, cl=cl, l=l, lookup=lookup))