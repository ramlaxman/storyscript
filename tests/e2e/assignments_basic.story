t = true
f = false
_null = null
zero = 0
_int = +3
_float = 3.14
_string = "cake"
_list = [1, 2]
list_empty = [] as List[any]
list_multiline = [
    1,
    2
]
obj = {"x": 1, "y": 3}
obj_empty = {} as Map[any,any]
obj_multiline = {
    "x": 1,
    "y": 3
}
regexp = /^foo/
regexp_flags = /^foo/g
sum = 3 + 2
mul = 3 * 2
my_service = yaml parse data:"foobar"
service_inline = (yaml format data: my_service)
