cgdcont = {
    'title': 'PDP Context Definition',

    'short_name': 'PDP Context',

    'commands': {
        'check': 'AT+CGDCONT?',
        'set': 'AT+CGDCONT=',
    },

    'fields_names': [
        "Cell ID",
        "PDP Type",
        "APN",
        "PDP Address",
        "Data Compression",
        "Header Compression"
    ],

    'result_fields_values': [
        'literal',          # Cell ID

        [                   # PDP Type (IP, PPP, IPV6, IPV4V6)
            'IP',
            'PPP',
            'IPV6',
            'IPV4V6'
        ],

        'literal',          # APN

        'literal',          # PDP Address

        [                   # Data Compression (V.42bis, V.44)
            
            '0 - Off',
            '1 - On'
            '2 - V.42bis',
            '3 - V.44',
        ],

        [                   # Header Compression (Off, On, RFC1144, RFC2507, RFC3095)
            '0 - Off',
            '1 - On',
            '2 - RFC1144',
            '3 - RFC2507',
            '4 - RFC3095',
        ]
    ],

    'send_parameters': [
        "Cell ID",
        "PDP Type",
        "APN",
        "PDP Address",
        "Data Compression",
        "Header Compression"
    ],

    'info_fields_positions': [
        [0, 1],
        [0, 2],
        [0, 3],
        [0, 4],
        [0, 5],
        [0, 6]
    ],

    'parameters_fields_positions': [
        [0, 0],
        [0, 1],
        [0, 2],
        [0, 3],
        [0, 4],
        [0, 5]
    ]
}
