from storyscript.compiler.semantics.types.Casting import implicit_type_cast
from storyscript.compiler.semantics.types.Types import BaseType


class BaseFunction:
    """
    An individual function.
    """
    def __init__(self, fn_type, name, args, output):
        assert fn_type == 'function' or fn_type == 'mutation'
        self.fn_type = fn_type.capitalize()
        self._name = name
        self._args = args
        self._arg_names = set(args.keys())
        assert isinstance(output, BaseType)
        self._output = output

    def check_call(self, tree, args):
        """
        Checks call arguments for their conformity with this function's
        arguments. This means
         (1) checking for required or invalid argument names.
         (2) checking the argument type of each argument
        :param tree: AST node for error messages
        :param args: argument to be checked
        :return: None
        """
        self._check_arg_names(tree, args)
        self._check_arg_types(tree, args)

    def _check_arg_names(self, tree, args):
        """
        Checks that all argument names occur in arg (required) and that no
        unknown argument names are used (invalid).
        """
        arg_names = set(args.keys())
        name_difference = self._arg_names.symmetric_difference(arg_names)
        # check arg names for differences
        for d in sorted(name_difference):
            if d in self._arg_names:
                tree.expect(0, 'function_arg_required', fn_type=self.fn_type,
                            name=self._name, arg=d)
            else:
                tree.expect(0, 'function_arg_invalid', fn_type=self.fn_type,
                            name=self._name, arg=d)

    def _check_arg_types(self, tree, args):
        """
        Checks that for each argument its type can be implicitly converted to
        the respective function argument.
        """
        for k, (sym, arg_node) in args.items():
            target = self._args[k].type()
            t = sym.type()
            implicit_type_cast(tree, t, target,
                               self.fn_type, self._name, k, arg_node)

    def output(self):
        return self._output

    def pretty(self):
        """
        Returns a pretty-printed representation of the function
        """
        args = ''
        if self._args:
            args_arr = []
            for k, v in sorted(self._args.items()):
                args_arr.append(f'{k}:`{v.type()}`')
            args = ' '.join(args_arr)
            if self.fn_type == 'Mutation':
                args = f' {args}'
        if self.fn_type == 'Function':
            args = f'({args})'
        return f'{self._name}{args}'

    def __str__(self):
        return f'{self.fn_type}({self._name})'


class Function(BaseFunction):
    """
    Representation of a Storyscript function.
    """
    def __init__(self, name, args, output):
        super().__init__('function', name, args, output)


class MutationFunction(BaseFunction):
    """
    Representation of a instantiated Storyscript mutation.
    """
    def __init__(self, name, args, output):
        super().__init__('mutation', name, args, output)
