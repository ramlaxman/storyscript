# -*- coding: utf-8 -*-
from storyscript.exceptions import StorySyntaxError


class Lines:
    """
    Holds compiled lines and provides methods for operation on lines.
    """
    def __init__(self, story):
        self.story = story
        self.lines = {}
        self._lines = []  # sorted line nr (by insertion)
        self.variables = []
        self.services = []
        self.functions = {}
        self.output_scopes = []
        self.scopes = []
        self.previous_scope = None
        self.finished_scopes = []

    def entrypoint(self):
        """
        Returns the first line number or None
        """
        # empty files are allowed
        if len(self._lines) == 0:
            return None
        return self._lines[0]

    def first(self):
        """
        Gets the first line.
        """
        if len(self._lines) == 0:
            return None
        return self.lines[self._lines[0]]

    def last(self):
        """
        Gets the last line
        """
        if len(self._lines) == 0:
            return None
        return self.lines[self._lines[-1]]

    def set_name(self, name):
        """
        Sets the name of the previous line
        """
        previous_line = self.last()
        if previous_line is not None:
            previous_line['name'] = name

        self.variables.append(name)

    def set_next(self, line_number):
        """
        Finds the previous line, and set the current as its next line
        """
        previous_line = self.last()
        if previous_line is None:
            return

        if self.previous_scope is not None:
            # if a scope had only one line (NO_NEXT) ignore it
            if self.previous_scope != 'NO_NEXT':
                self.lines[self.previous_scope]['next'] = line_number

            self.previous_scope = None
            return

        previous_line['next'] = line_number

    def set_scope(self, line, parent, output):
        """
        Keeps track of output scopes so that defined outputs are recognized for
        nested children.
        """
        self.scopes.append(line)
        # initially a new scope starts without a next reference
        self.previous_scope = 'NO_NEXT'
        self.output_scopes.append({line: {'parent': parent, 'output': output}})

    def finish_scope(self, line):
        """
        Finishes an output scope and prepares 'exit' adjustment for the scope
        when the next line gets added.
        """
        self.previous_scope = self.scopes.pop()
        self.finished_scopes.append(self.previous_scope)
        self.output_scopes.pop()

    def is_output(self, parent, service):
        """
        Checks whether a service has been defined as output for this block
        or for its parents.
        """
        for output_scope in self.output_scopes:
            if parent in output_scope:
                scope = output_scope[parent]
                if service in scope['output']:
                    return True
                if scope['parent']:
                    assert scope['parent'] != parent
                    return self.is_output(scope['parent'], service)
        return False

    def make(self, method, position, name=None, args=None, service=None,
             command=None, function=None, output=None, enter=None, exit=None,
             parent=None):
        """
        Creates the base dictionary for a given line.
        """
        assert position.line not in self.lines, \
            f'Line {position.line} is not unique'
        col_start = self._as_none(position.column)
        col_end = self._as_none(position.end_column)
        raw_line = self.story.line(position.line)
        self.lines[position.line] = {
            'method': method,
            'ln': position.line,
            'col_start': col_start,
            'col_end': col_end,
            'output': output,
            'name': name,
            'service': service,
            'command': command,
            'function': function,
            'args': args,
            'enter': enter,
            'exit': exit,
            'parent': parent,
            'src': raw_line,
        }
        # save insertion order
        self._lines.append(position.line)

    def check_service_name(self, service, line):
        """
        Checks whether a service name is valid
        """
        if '.' in service:
            raise StorySyntaxError('service_name')

    def append(self, method, position, **kwargs):
        for scope in self.finished_scopes:
            self.lines[scope]['exit'] = position.line
        self.finished_scopes = []
        if 'service' in kwargs:
            self.check_service_name(kwargs['service'], position.line)

        if method == 'function':
            self.functions[kwargs['function']] = position.line
        elif method == 'execute':
            if self.is_output(kwargs['parent'], kwargs['service']) is False:
                self.services.append(kwargs['service'])
        self.set_next(position.line)
        self.make(method, position, **kwargs)

    def execute(self, position, service, command, arguments, output, enter,
                parent):
        kwargs = {'service': service, 'command': command, 'args': arguments,
                  'output': output, 'enter': enter, 'parent': parent}
        self.append('execute', position, **kwargs)

    def get_services(self):
        """
        Get the services and remove duplicates.
        """
        return list(sorted(set(self.services)))

    def is_variable_defined(self, variable_name):
        """
        Checks whether a variable has been defined so far
        """
        for vs in self.variables:
            if variable_name in vs:
                return True
        return False

    def _as_none(self, value):
        return value if value != 'None' else None
