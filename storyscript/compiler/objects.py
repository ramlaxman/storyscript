# -*- coding: utf-8 -*-
import re

from lark.lexer import Token

from ..parser import Tree


class Objects:

    @staticmethod
    def path(tree):
        paths = [tree.child(0).value]
        for fragment in tree.children[1:]:
            paths.append(fragment.child(0).value)
        return {'$OBJECT': 'path', 'paths': paths}

    @classmethod
    def mutation(cls, tree):
        """
        Compiles a mutation tree.
        """
        arguments = []
        if tree.arguments:
            arguments = cls.arguments(tree.arguments)
        return {'$OBJECT': 'mutation', 'mutation': tree.child(0).value,
                'arguments': arguments}

    @staticmethod
    def number(tree):
        return int(tree.child(0).value)

    @staticmethod
    def replace_placeholders(string, matches):
        """
        Replaces placeholder values with '{}'
        """
        for match in matches:
            placeholder = '{}{}{}'.format('{', match, '}')
            string = string.replace(placeholder, '{}')
        return string

    @classmethod
    def placeholders_values(cls, matches):
        values = []
        for match in matches:
            values.append(cls.path(Tree('path', [Token('WORD', match)])))
        return values

    @classmethod
    def string(cls, tree):
        """
        Compiles a string tree. If the string has templated values, they
        are processed and compiled.
        """
        item = {'$OBJECT': 'string', 'string': tree.child(0).value[1:-1]}
        matches = re.findall(r'{([^}]*)}', item['string'])
        if matches == []:
            return item
        item['values'] = cls.placeholders_values(matches)
        item['string'] = cls.replace_placeholders(item['string'], matches)
        return item

    @staticmethod
    def boolean(tree):
        if tree.child(0).value == 'true':
            return True
        return False

    @staticmethod
    def file(token):
        return {'$OBJECT': 'file', 'string': token.value[1:-1]}

    @classmethod
    def list(cls, tree):
        items = []
        for value in tree.children:
            items.append(cls.values(value))
        return {'$OBJECT': 'list', 'items': items}

    @classmethod
    def objects(cls, tree):
        items = []
        for item in tree.children:
            key = cls.string(item.node('string'))
            value = cls.values(item.child(1))
            items.append([key, value])
        return {'$OBJECT': 'dict', 'items': items}

    @staticmethod
    def types(tree):
        return {'$OBJECT': 'type', 'type': tree.child(0).value}

    @classmethod
    def method(cls, tree):
        """
        Produces a method object. This is used when it's not possible to
        compile something that would normally be a line as a line.
        For example, in `x = alpine echo` the `alpine echo` bit would be
        compiled as method object.
        """
        service = tree.child(0).child(0).value
        args = cls.arguments(tree.node('service_fragment'))
        object = {'$OBJECT': 'method', 'method': 'execute', 'service': service,
                  'output': None, 'args': args}
        command = tree.node('service_fragment.command')
        if command:
            object['command'] = command.child(0).value
        return object

    @classmethod
    def values(cls, tree):
        """
        Parses a values subtree
        """
        subtree = tree.child(0)
        if hasattr(subtree, 'data'):
            if subtree.data == 'string':
                return cls.string(subtree)
            elif subtree.data == 'boolean':
                return cls.boolean(subtree)
            elif subtree.data == 'list':
                return cls.list(subtree)
            elif subtree.data == 'number':
                return cls.number(subtree)
            elif subtree.data == 'objects':
                return cls.objects(subtree)
            elif subtree.data == 'types':
                return cls.types(subtree)
            elif subtree.data == 'path':
                # NOTE(vesuvium): path trees are sent to Objects.values only
                # when they are in a service tree. Objects.method however takes
                # the whole tree.
                return cls.method(tree)
        if subtree.type == 'FILEPATH':
            return cls.file(subtree)
        elif subtree.type == 'NAME':
            return cls.path(tree)

    @classmethod
    def argument(cls, tree):
        """
        Compiles an argument tree to the corresponding object.
        """
        name = tree.child(0).value
        value = cls.values(tree.child(1))
        return {'$OBJECT': 'argument', 'name': name, 'argument': value}

    @classmethod
    def arguments(cls, tree):
        """
        Parses a group of arguments rules
        """
        arguments = []
        for argument in list(tree.find_data('arguments')):
            arguments.append(cls.argument(argument))
        return arguments

    @classmethod
    def typed_argument(cls, tree):
        subtree = tree.node('typed_argument')
        name = subtree.child(0).value
        value = cls.values(Tree('anon', [subtree.child(1)]))
        return {'$OBJECT': 'argument', 'name': name, 'argument': value}

    @classmethod
    def function_arguments(cls, tree):
        arguments = []
        for argument in list(tree.find_data('function_argument')):
            arguments.append(cls.typed_argument(argument))
        return arguments

    @staticmethod
    def fill_expression(left_handside, operator, right_handside):
        """
        Compiles the expression template
        """
        return '{} {} {}'.format(left_handside, operator, right_handside)

    @classmethod
    def expression(cls, tree):
        """
        Compiles an expression object with the given tree.
        """
        if tree.values:
            operator = tree.operator.child(0).value
            expression = Objects.fill_expression('{}', operator, '{}')
            values = [cls.values(tree.values), cls.values(tree.child(2))]
            return [{'$OBJECT': 'expression', 'expression': expression,
                     'values': values}]
        left_handside = cls.values(tree.path_value.child(0))
        comparison = tree.child(1)
        if comparison is None:
            return [left_handside]
        right_handside = cls.values(tree.child(2).child(0))
        expression = Objects.fill_expression('{}', comparison.child(0), '{}')
        return [{'$OBJECT': 'expression', 'expression': expression,
                'values': [left_handside, right_handside]}]
