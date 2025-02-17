# -*- coding: utf-8 -*-


class ErrorCodes:

    unidentified_error = ('E0001', '')
    service_name = ('E0002', "A service name can't contain `.`")
    arguments_noservice = ('E0003',
                           'You have defined an argument, but not a service')
    return_outside = ('E0004', '`return` is allowed only inside functions')
    variables_backslash = ('E0005', "A variable name can't contain `/`")
    variables_dash = ('E0006', "A variable name can't contain `-`")
    assignment_incomplete = ('E0007', 'Missing value after `=`')
    function_misspell = ('E0008', 'You have misspelt `function`')
    import_misspell = ('E0009', 'You have misspelt `import`')
    import_misspell_as = ('E0010',
                          'You have misspelt `as` in an import statement')
    import_unquoted_file = ('E0011', 'The imported filename must be in quotes')
    string_opening_quote = ('E0012', 'Missing opening quote for string')
    string_closing_quote = ('E0013', 'Missing closing quote for string')
    list_trailing_comma = ('E0014', 'Trailing comma in list')
    list_opening_bracket = ('E0015', 'Missing opening bracket for list')
    list_closing_bracket = ('E0016', 'Missing closing bracket for list')
    object_opening_bracket = ('E0017', 'Missing opening bracket for object')
    object_closing_bracket = ('E0018', 'Missing closing bracket for object')
    service_argument_colon = ('E0019', 'Missing colon in service argument')
    reserved_keyword = ('E0020', '`{keyword}` is a reserved keyword')
    future_reserved_keyword = ('E0030',
                               '`{keyword}` is reserved for future use')
    arguments_nomutation = (
        'E0039',
        'You have defined a chained mutation, but not a mutation')
    compiler_error_no_operator = (
        'E0040', 'Invalid operator `{operator}` provided.')
    invalid_character = ('E0041', '`{character}` is not allowed here')
    unexpected_token = ('E0043',
                        '`{token}` is not allowed here. Allowed: {allowed}')
    break_outside = ('E0044', '`break` is allowed only inside loops')
    unnecessary_colon = (
        'E0045',
        'There is an unnecessary colon at the end of the line')
    block_expected_before = ('E0046',
                             'An indented block is required to be before here')
    file_not_found = ('E0047',
                      'File `{path}` not found at `{abspath}`')
    function_call_invalid_path = ('E0049',
                                  'Functions can only be called by name')
    function_call_no_inline_expression = (
        'E0050', 'Service output can not be called as a function')
    when_no_output_parent = (
        'E0051', 'No service parent has been found.')
    service_without_command = (
        'E0052', 'Service calls require a command.')
    unexpected_end_of_line = (
        'E0053', 'Unexpected end of line. Expected: {allowed}.')
    arguments_expected = (
        'E0054', 'Arguments need to be declared with `key:value`')
    first_option_more_stories = (
        'E0055',
        'The option `--first`/-`f` can only be used if one story is complied.')
    expected_end_of_line = (
        'E0056', 'Expected end of line instead of `{token}`.')
    string_templates_no_assignment = (
        'E0057', 'Only expressions are allowed inside string templates')
    path_name_internal = (
        'E0058', "Path names can't start with double underscore")
    string_templates_nested = (
        'E0059', "String templates can't be nested")
    string_templates_empty = (
        'E0060', "String templates can't be empty")
    path_name_invalid_char = (
        'E0061', 'Invalid path name: `{path}`. '
        "Path names can't contain `{token}`")
    return_required = ('E0062', 'All paths of a function need to return')
    assignment_inline_expression = (
        'E0063', "Can't assign to inline expressions.")
    foreach_output_required = (
        'E0064', 'Foreach blocks require an output (e.g. `as item`)')
    nested_service_block = ('E0065', 'Nested service blocks are not allowed')
    nested_when_block = ('E0066', 'Nested when blocks are not allowed')
    time_value_inconsistent_week = (
        'E0067', 'Time value inconsistency: `w` must be the first time unit')
    time_value_inconsistent = (
        'E0068',
        'Time value inconsistency: `{current}` must to be before `{prev}`')
    time_value_duplicate = (
        'E0069',
        'Time value duplication: `{time_type}` must only occur once')
    string_templates_unclosed = (
        'E0070', 'Unclosed string template. Did you forget a `}}`?')
    string_templates_unopened = (
        'E0071',
        ('Unopened string template. Did you forget a `{{` or '
         'wanted to escape with `\\}}`?'))
    object_destructoring_invalid_path = (
        'E0072', 'Objects can only be destructored into variable names.')
    object_destructoring_no_variables = (
        'E0073', 'Objects destructoring requires variable names.')
    unicode_decode_error = (
        'E0074', 'Unicode decode error: {reason}.')
    expected_closing_parenthesis = (
        'E0075', 'Expected closing parenthesis: {cp}')
    expected_closing_block = (
        'E0076',
        'Unexpected end of line. Maybe close a `}}` or `]` expression?')
    indentation_error = (
        'E0077', 'Invalid indentation detected.')
    invalid_preview_flag = (
        'E0078',
        'Invalid preview flag. `{flag}` is not a valid preview feature.')
    type_assignment_different = (
        'E0100', "Can't assign `{source}` to `{target}`")
    var_not_defined = (
        'E0101', 'Variable `{name}` has not been defined.')
    return_type_differs = (
        'E0102',
        "`{source}` can't be implicitly converted to expected "
        'return type `{target}`.')
    type_operation_incompatible = (
        'E0103',
        '`{op}` between `{left}` and `{right}` is not supported.'
    )
    type_index_incompatible = (
        'E0104',
        "`{left}` can't be indexed with `{name}` of type `{right}`"
    )
    foreach_output_children = (
        'E0105',
        '`foreach` can only have one or two outputs'
    )
    foreach_iterable_required = (
        'E0106',
        '`foreach` requires an iterable type, but `{target}` is not'
    )
    output_type_only_one = (
        'E0107',
        'Only one output is allowed for `{target}` blocks.'
    )
    output_unique = (
        'E0108', 'Service output `{name}` must be unique. Use `as outputName`')
    service_no_inline_output = (
        'E0109', "Inline service calls can't define an output")
    function_without_output_return = (
        'E0110',
        ('`return` expected. Did you miss to add `returns {return_type}`?'))
    function_redeclaration = (
        'E0111', 'Function `{name}` has already been declared')
    function_not_found = (
        'E0112', 'Function `{name}` has not been declared')
    function_arg_required = (
        'E0113', '{fn_type} `{name}` requires argument `{arg}`')
    function_arg_invalid = (
        'E0114', '{fn_type} `{name}` does not accept argument `{arg}`')
    param_arg_type_mismatch = (
        'E0115',
        '{fn_type} `{name}` requires argument `{arg_name}` to be of '
        '`{target}`, not `{source}`')
    assignment_type_none = (
        'E0116', 'Assignments with the type `None` are not allowed')
    mutation_invalid_name = (
        'E0117', 'Invalid mutation `{name}`')
    arg_name_required = (
        'E0118', '{fn_type} `{name}` requires arguments to be named')
    mutation_output = (
        'E0120', "Mutations can't have outputs.")
    mutation_overload_mismatch = (
        'E0121', 'Multiple mutation overloads for `{name}` found:'
        '{overloads}\n'
        'but none matches.')
    type_operation_boolean_incompatible = (
        'E0122',
        "`{val}` can't be converted to `boolean`"
    )
    type_operation_cmp_incompatible = (
        'E0123',
        "`{left}` can't be compared with `{right}`"
    )
    type_operation_equal_incompatible = (
        'E0124',
        'Equality comparison not supported between `{left}` and `{right}`.'
    )
    type_key_not_hashable = (
        'E0125',
        "`{key}` is not hashable and can't be used as an object key."
    )
    type_operation_cast_incompatible = (
        'E0126',
        'Type casting not supported from `{left}` to `{right}`.'
    )
    readonly_type_assignment = (
        'E0127',
        '`{left}` is readonly and can not be assigned to.'
    )
    return_type_readonly = (
        'E0128',
        '`{source}` is readonly and can not be returned.'
    )
    single_quotes = (
        'E0129',
        'Single quotes are not allowed.'
    )
    if_expression_boolean = (
        'E0130',
        'If expression must evaluate to a `boolean`, but is `{type}`'
    )
    type_dot_incompatible = (
        'E0131',
        "`{left}` can't be dot-accessed with `{name}` of type `{right}`"
    )
    tabs = (
        'E0132',
        'Tabs are not allowed.'
    )
    continue_outside = ('E0133', '`continue` is allowed only inside loops')
    block_expected_after = (
        'E0134',
        'An indented block is required to follow here'
    )
    throw_only_string = (
        'E0135',
        'Only strings can be thrown.'
    )
    catch_no_output = (
        'E0136',
        'Access to the exception object is currently disallowed.'
    )
    scope_join_incompatible = (
        'E0137',
        'Scope variable type mismatch: `{t1name}` of {t1type} is not '
        'compatible with `{t2name}` of {t2type}.'
    )
    output_assignment_existing_var = (
        'E0138',
        'Output must be unique. Can not use existing `{var}`.',
    )
    service_not_found = (
        'E0139', 'Service `{name}` does not exist on the hub.'
    )
    service_action_not_found = (
        'E0140', 'Service `{name}` has no action `{action}`.'
    )
    service_arg_invalid = (
        'E0141',
        '{service} action `{action}` does not accept argument `{arg}`.')
    service_event_not_found = (
        'E0142', 'Event action `{name}` has no event `{event}`.'
    )
    service_arg_required = (
        'E0143', '{service} `{action}` requires argument `{arg}`.')

    event_not_defined = (
        'E0144',
        'No event listener with output `{output}` for event `{event}`.'
    )
    map_type_no_any = (
        'E0145',
        'Map initialization without elements must be typed. Use `as ...`'
    )
    list_type_no_any = (
        'E0146',
        'List initialization without elements must be typed. Use `as ...`'
    )
    service_action_without_output = (
        'E0147',
        'Service object `{object}` only support events, no actions.'
    )
    service_name_not_var = (
        'E0148',
        'Service name expected but existing variable `{var}` found.'
    )
    service_name_not_inline_service = (
        'E0149',
        'Service name expected but inline service expression found.'
    )
    service_output_invalid_prop = (
        'E0150',
        'Service output object `{object}` has no property `{prop}`.'
    )
    object_invalid_prop = (
        'E0151',
        'Object `{object}` has no property `{prop}`.'
    )
    assignment_no_as = (
        'E0152',
        '`as` can not be used in assignments.'
    )
    return_type_no_object = (
        'E0153',
        'Return type cannot be `object`.'
    )
    object_no_as = (
        'E0154',
        'Type cast to `object` is not allowed.'
    )
    object_expect_action = (
        'E0155',
        'Service object expected but existing variable `{var}` found.'
    )
    expression_no_event = (
        'E0156',
        'Event based action `{action}` of service `{service}` cannot be used '
        'in expressions.'
    )

    @staticmethod
    def is_error(error_name):
        """
        Checks whether a given error name is a valid error.
        """
        if isinstance(error_name, str):
            if hasattr(ErrorCodes, error_name):
                return True

    @staticmethod
    def get_error(error_name):
        """
        Retrieve the error object for a valid error name.
        """
        return getattr(ErrorCodes, error_name)
