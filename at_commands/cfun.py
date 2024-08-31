cfun = {
    'title': 'Modem Functionality',

    'short_name': 'Modem Functionality',

    'commands': {
        'check': 'AT+CFUN?',
        'set': 'AT+CFUN=',
    },

    'fields_names': [
        "Func. Type"
    ],

    'result_fields_values': [
        [                                   # Func. Type
            '0 - Minimum functionality',
            '1 - Full functionality',
            '4 - Disable phone activity'
        ]

        , [                                   # Reset
            '0 - Do not reset the modem',
            '1 - Reset the modem',
        ]
    ],

    'send_parameters': [
        "Func. Type",
        "Reset"
    ],

    'parameters_fields_values': [
        [   
            'Reset',
            [                                   # Reset
            '0 - Do not reset the modem',
            '1 - Reset the modem',
            ]
        ]
    ],

    'info_fields_positions': [
        [0, 1]
    ],

    'parameters_fields_positions': [
        [1, 1],
        [1, 2]
    ]
}
