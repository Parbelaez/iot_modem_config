cops = {
    'title': 'Operator Scan and Selection',

    'short_name': 'Operator',

    'commands': {
        'check': 'AT+COPS?',
        'set': 'AT+COPS=',
    },

    'fields_names': [
        "Mode",
        "Format",
        "Operator",
        "Access Technology"
    ],

    'result_fields_values': [
        [
            '0 - Automatic',
            '1 - Manual',
            '2 - Deregistered from Network',
            '3 - Set Only',
            '4 - Manual/Auto',
        ],

        [
            '0 - Long Alpha',
            '1 - Short Alpha',
            '2 - Numeric',
        ],


        'literal',
        
        [
            '0 - GSM',
            '1 - GSM Compact',
            '2 - UTRAN',
            '3 - GSM w/EGPRS',
            '4 - UTRAN w/HSDPA',
            '5 - UTRAN w/HSUPA',
            '6 - UTRAN w/HSDPA and HSUPA',
            '7 - E-UTRAN',
            '8 - LTE-M',
            '9 - NB-IoT',
        ]
    ],

    'send_parameters': [
        "Mode",
        "Format",
        "Operator",
        "Access Technology"
    ],

    'info_fields_positions': [
        [0, 1],
        [0, 2],
        [0, 3],
        [0, 4]
    ],

    'parameters_fields_positions': [
        [0, 1],
        [0, 2],
        [0, 3],
        [0, 4]
    ]
}
