qping = {
    'title': 'PING',

    'type': 'test',

    'short_name': 'PING',

    'commands': {
        'set': 'AT+QPING=',
    },

    'fields_names': [
    ],

    'result_fields_values': [
        'literal',
        'literal',
        'literal',
        'literal',
    ],

    'send_parameters': [
        "Context ID",
        "Host IP/Name",
        "Timeout",
        "Number of Pings"
    ],

    'info_fields_positions': [
    ],

    'parameters_fields_positions': [
        [0, 0],
        [0, 1],
        [0, 2],
        [0, 3]
    ]
}
