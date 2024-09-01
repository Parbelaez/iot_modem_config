qiact = {
    'title': 'Activate a PDP Context',

    'short_name': 'PDP Act.',

    'commands': {
        'check': 'AT+QIACT?',
        'set': 'AT+QIACT=',
    },

    'fields_names': [
        "ID",
        "State",
        "Type",
        "IP Address",
    ],

    'result_fields_values': [
        'literal',

        [
            '0 - Deactivated',
            '1 - Activated'
        ],

        [
            '1 - IP',
            '2 - IPv6'
        ],

        'literal'
    ],

    'send_parameters': [
        "ID",
        "State"
    ],

    'info_fields_positions': [
        [0, 1],
        [0, 2],
        [0, 3],
        [0, 4]
    ],

    'parameters_fields_positions': [
        [0, 0],
        [0, 1]
    ]
}
