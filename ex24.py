print("Let's practice everything.")
print('You\' need to know\' bout escapes with \\ that do:')
print('\n newlines and \t tabs.')
pome = """\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""
print("-"*12)
print(pome)
print("-"*12)

five = 10-2+3-6
print(f"This should be five:{five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans,jars,crates

start_point = 10000
beans,jars,crates = secret_formula(start_point)
#使用f“{}”的形式输出
print("With a starting point of:{}".format(start_point))
print(f"We'd have {beans} benans,{jars} jars,{crates} crates.")
start_point = start_point / 10
print("We can also do that this way:")
formula = secret_formula(start_point)
#使用.format加*变量的方式输出
print("We'd have {} beans, {}jars, {}crates.".format(*formula))
