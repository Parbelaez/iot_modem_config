cgatt = {
    'title': 'Attach or Dettach from PS',

    'short_name': 'Attach/Dettach',

    'commands': {
        'check': 'AT+CGATT?',
        'set': 'AT+CGATT=',
    },

    'fields_names': [
        "State",
    ],

    'result_fields_values': [
        [
            '0 - Detached',
            '1 - Attached'
        ],
    ],

    'send_parameters': [
        "State",
    ],

    'info_fields_positions': [
        [0, 1],
    ],

    'parameters_fields_positions': [
        [0, 0],
    ]
}
