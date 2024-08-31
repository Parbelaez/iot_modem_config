creg = {
    'title': 'Network Registration Status',

    'short_name': 'Network Reg.',

    'commands': {
        'check': 'AT+CREG?',
        'set': 'AT+CREG=',
    },

    'fields_names': [
        "Config. (n)",
        "Status",
        "LAC",
        "Cell ID",
        "AcT"
    ],

    'result_fields_values': [
        [
            '0 - Disable net. reg. unsolicited results code reports',
            '1 - Enable net. reg. unsolicited results code reports',
            '2 - Enable net. reg. and location information unsolicited result code reports',
            '3 - Enable net. reg., location info and network name unsolicited result code reports',
            '4 - Enable net. reg., location info, net. name and net. time zone unsolicited result code reports',
            '5 - Enable net. reg., location info, net. name, net. time zone and operator name unsolicited result code reports'
        ],

        [
            '0 - Not registered, not searching for a new operator to register to',
            '1 - Registered, home network',
            '2 - Not registered, but searching for a new operator to register to',
            '3 - Registration denied',
            '4 - Unknown',
            '5 - Registered, roaming'
        ],

        'literal',

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
        ],



    ],

    'send_parameters': [
        "Config. (n)"
    ],

    'info_fields_positions': [
        [0, 1],
        [0, 2],
        [1, 2],
        [0, 3],
        [1, 3]
    ],

    'parameters_fields_positions': [
        [0, 1]
    ]
}
