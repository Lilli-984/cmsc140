

print("start of script")
def outer_function():
    print("Outer function called")

print("After the function")

for i in range(5):
    for j in range(5):
        print("i =", i, "j =", j)


def file_namer():
    filename_fn = "my_program.py"
    file_reader()
    print(filename_fn)

def file_reader():
    filename_fr = "my_thoughts.pdf"
    print(filename_fr)

file_namer()
file_reader()

