#!/usr/bin/env python3

from typing import List
from typing import Optional
from dataclasses import field
from dataclasses import dataclass


CC_DICT = {
    "AD": {"code": "AD", "name": "Andorra", "year": 1974, "tld": ".ad"},
    "AE": {"code": "AE", "name": "United Arab Emirates", "year": 1974, "tld": ".ae"},
    "AF": {"code": "AF", "name": "Afghanistan", "year": 1974, "tld": ".af"},
    "AG": {"code": "AG", "name": "Antigua and Barbuda", "year": 1974, "tld": ".ag"},
    "AI": {"code": "AI", "name": "Anguilla", "year": 1985, "tld": ".ai"},
    "AL": {"code": "AL", "name": "Albania", "year": 1974, "tld": ".al"},
    "AM": {"code": "AM", "name": "Armenia", "year": 1992, "tld": ".am"},
    "AO": {"code": "AO", "name": "Angola", "year": 1974, "tld": ".ao"},
    "AQ": {"code": "AQ", "name": "Antarctica", "year": 1974, "tld": ".aq"},
    "AR": {"code": "AR", "name": "Argentina", "year": 1974, "tld": ".ar"},
    "AS": {"code": "AS", "name": "American Samoa", "year": 1974, "tld": ".as"},
    "AT": {"code": "AT", "name": "Austria", "year": 1974, "tld": ".at"},
    "AU": {"code": "AU", "name": "Australia", "year": 1974, "tld": ".au"},
    "AW": {"code": "AW", "name": "Aruba", "year": 1986, "tld": ".aw"},
    "AX": {
        "code": "AX",
        "name": "Åland Islands",
        "year": 2004,
        "tld": ".ax",
    },
    "AZ": {"code": "AZ", "name": "Azerbaijan", "year": 1992, "tld": ".az"},
    "BA": {"code": "BA", "name": "Bosnia and Herzegovina", "year": 1992, "tld": ".ba"},
    "BB": {"code": "BB", "name": "Barbados", "year": 1974, "tld": ".bb"},
    "BD": {"code": "BD", "name": "Bangladesh", "year": 1974, "tld": ".bd"},
    "BE": {"code": "BE", "name": "Belgium", "year": 1974, "tld": ".be"},
    "BF": {"code": "BF", "name": "Burkina Faso", "year": 1984, "tld": ".bf"},
    "BG": {"code": "BG", "name": "Bulgaria", "year": 1974, "tld": ".bg"},
    "BH": {"code": "BH", "name": "Bahrain", "year": 1974, "tld": ".bh"},
    "BI": {"code": "BI", "name": "Burundi", "year": 1974, "tld": ".bi"},
    "BJ": {"code": "BJ", "name": "Benin", "year": 1977, "tld": ".bj"},
    "BL": {"code": "BL", "name": "Saint Barthélemy", "year": 2007, "tld": ".bl"},
    "BM": {"code": "BM", "name": "Bermuda", "year": 1974, "tld": ".bm"},
    "BN": {"code": "BN", "name": "Brunei Darussalam", "year": 1974, "tld": ".bn"},
    "BO": {
        "code": "BO",
        "name": "Bolivia (Plurinational State of)",
        "year": 1974,
        "tld": ".bo",
    },
    "BQ": {
        "code": "BQ",
        "name": "Bonaire, Sint Eustatius and Saba",
        "year": 2010,
        "tld": ".bq",
    },
    "BR": {"code": "BR", "name": "Brazil", "year": 1974, "tld": ".br"},
    "BS": {"code": "BS", "name": "Bahamas", "year": 1974, "tld": ".bs"},
    "BT": {"code": "BT", "name": "Bhutan", "year": 1974, "tld": ".bt"},
    "BV": {"code": "BV", "name": "Bouvet Island", "year": 1974, "tld": ".bv"},
    "BW": {"code": "BW", "name": "Botswana", "year": 1974, "tld": ".bw"},
    "BY": {"code": "BY", "name": "Belarus", "year": 1974, "tld": ".by"},
    "BZ": {"code": "BZ", "name": "Belize", "year": 1974, "tld": ".bz"},
    "CA": {"code": "CA", "name": "Canada", "year": 1974, "tld": ".ca"},
    "CC": {"code": "CC", "name": "Cocos (Keeling) Islands", "year": 1974, "tld": ".cc"},
    "CD": {
        "code": "CD",
        "name": "Congo, Democratic Republic of the",
        "year": 1997,
        "tld": ".cd",
    },
    "CF": {
        "code": "CF",
        "name": "Central African Republic",
        "year": 1974,
        "tld": ".cf",
    },
    "CG": {"code": "CG", "name": "Congo", "year": 1974, "tld": ".cg"},
    "CH": {"code": "CH", "name": "Switzerland", "year": 1974, "tld": ".ch"},
    "CI": {
        "code": "CI",
        "name": "Côte d'Ivoire",
        "year": 1974,
        "tld": ".ci",
    },
    "CK": {"code": "CK", "name": "Cook Islands", "year": 1974, "tld": ".ck"},
    "CL": {"code": "CL", "name": "Chile", "year": 1974, "tld": ".cl"},
    "CM": {"code": "CM", "name": "Cameroon", "year": 1974, "tld": ".cm"},
    "CN": {"code": "CN", "name": "China", "year": 1974, "tld": ".cn"},
    "CO": {"code": "CO", "name": "Colombia", "year": 1974, "tld": ".co"},
    "CR": {"code": "CR", "name": "Costa Rica", "year": 1974, "tld": ".cr"},
    "CU": {"code": "CU", "name": "Cuba", "year": 1974, "tld": ".cu"},
    "CV": {"code": "CV", "name": "Cabo Verde", "year": 1974, "tld": ".cv"},
    "CW": {"code": "CW", "name": "Curaçao", "year": 2010, "tld": ".cw"},
    "CX": {"code": "CX", "name": "Christmas Island", "year": 1974, "tld": ".cx"},
    "CY": {"code": "CY", "name": "Cyprus", "year": 1974, "tld": ".cy"},
    "CZ": {"code": "CZ", "name": "Czechia", "year": 1993, "tld": ".cz"},
    "DE": {"code": "DE", "name": "Germany", "year": 1974, "tld": ".de"},
    "DJ": {"code": "DJ", "name": "Djibouti", "year": 1977, "tld": ".dj"},
    "DK": {"code": "DK", "name": "Denmark", "year": 1974, "tld": ".dk"},
    "DM": {"code": "DM", "name": "Dominica", "year": 1974, "tld": ".dm"},
    "DO": {"code": "DO", "name": "Dominican Republic", "year": 1974, "tld": ".do"},
    "DZ": {"code": "DZ", "name": "Algeria", "year": 1974, "tld": ".dz"},
    "EC": {"code": "EC", "name": "Ecuador", "year": 1974, "tld": ".ec"},
    "EE": {"code": "EE", "name": "Estonia", "year": 1992, "tld": ".ee"},
    "EG": {"code": "EG", "name": "Egypt", "year": 1974, "tld": ".eg"},
    "EH": {"code": "EH", "name": "Western Sahara", "year": 1974, "tld": ""},
    "ER": {"code": "ER", "name": "Eritrea", "year": 1993, "tld": ".er"},
    "ES": {"code": "ES", "name": "Spain", "year": 1974, "tld": ".es"},
    "ET": {"code": "ET", "name": "Ethiopia", "year": 1974, "tld": ".et"},
    "FI": {"code": "FI", "name": "Finland", "year": 1974, "tld": ".fi"},
    "FJ": {"code": "FJ", "name": "Fiji", "year": 1974, "tld": ".fj"},
    "FK": {
        "code": "FK",
        "name": "Falkland Islands (Malvinas)",
        "year": 1974,
        "tld": ".fk",
    },
    "FM": {
        "code": "FM",
        "name": "Micronesia (Federated States of)",
        "year": 1986,
        "tld": ".fm",
    },
    "FO": {"code": "FO", "name": "Faroe Islands", "year": 1974, "tld": ".fo"},
    "FR": {"code": "FR", "name": "France", "year": 1974, "tld": ".fr"},
    "GA": {"code": "GA", "name": "Gabon", "year": 1974, "tld": ".ga"},
    "GB": {
        "code": "GB",
        "name": "United Kingdom of Great Britain and Northern Ireland",
        "year": 1974,
        "tld": ".gb, .uk",
    },
    "GD": {"code": "GD", "name": "Grenada", "year": 1974, "tld": ".gd"},
    "GE": {"code": "GE", "name": "Georgia", "year": 1992, "tld": ".ge"},
    "GF": {"code": "GF", "name": "French Guiana", "year": 1974, "tld": ".gf"},
    "GG": {"code": "GG", "name": "Guernsey", "year": 2006, "tld": ".gg"},
    "GH": {"code": "GH", "name": "Ghana", "year": 1974, "tld": ".gh"},
    "GI": {"code": "GI", "name": "Gibraltar", "year": 1974, "tld": ".gi"},
    "GL": {"code": "GL", "name": "Greenland", "year": 1974, "tld": ".gl"},
    "GM": {"code": "GM", "name": "Gambia", "year": 1974, "tld": ".gm"},
    "GN": {"code": "GN", "name": "Guinea", "year": 1974, "tld": ".gn"},
    "GP": {"code": "GP", "name": "Guadeloupe", "year": 1974, "tld": ".gp"},
    "GQ": {"code": "GQ", "name": "Equatorial Guinea", "year": 1974, "tld": ".gq"},
    "GR": {"code": "GR", "name": "Greece", "year": 1974, "tld": ".gr"},
    "GS": {
        "code": "GS",
        "name": "South Georgia and the South Sandwich Islands",
        "year": 1993,
        "tld": ".gs",
    },
    "GT": {"code": "GT", "name": "Guatemala", "year": 1974, "tld": ".gt"},
    "GU": {"code": "GU", "name": "Guam", "year": 1974, "tld": ".gu"},
    "GW": {"code": "GW", "name": "Guinea-Bissau", "year": 1974, "tld": ".gw"},
    "GY": {"code": "GY", "name": "Guyana", "year": 1974, "tld": ".gy"},
    "HK": {"code": "HK", "name": "Hong Kong", "year": 1974, "tld": ".hk"},
    "HM": {
        "code": "HM",
        "name": "Heard Island and McDonald Islands",
        "year": 1974,
        "tld": ".hm",
    },
    "HN": {"code": "HN", "name": "Honduras", "year": 1974, "tld": ".hn"},
    "HR": {"code": "HR", "name": "Croatia", "year": 1992, "tld": ".hr"},
    "HT": {"code": "HT", "name": "Haiti", "year": 1974, "tld": ".ht"},
    "HU": {"code": "HU", "name": "Hungary", "year": 1974, "tld": ".hu"},
    "ID": {"code": "ID", "name": "Indonesia", "year": 1974, "tld": ".id"},
    "IE": {"code": "IE", "name": "Ireland", "year": 1974, "tld": ".ie"},
    "IL": {"code": "IL", "name": "Israel", "year": 1974, "tld": ".il"},
    "IM": {"code": "IM", "name": "Isle of Man", "year": 2006, "tld": ".im"},
    "IN": {"code": "IN", "name": "India", "year": 1974, "tld": ".in"},
    "IO": {
        "code": "IO",
        "name": "British Indian Ocean Territory",
        "year": 1974,
        "tld": ".io",
    },
    "IQ": {"code": "IQ", "name": "Iraq", "year": 1974, "tld": ".iq"},
    "IR": {
        "code": "IR",
        "name": "Iran (Islamic Republic of)",
        "year": 1974,
        "tld": ".ir",
    },
    "IS": {"code": "IS", "name": "Iceland", "year": 1974, "tld": ".is"},
    "IT": {"code": "IT", "name": "Italy", "year": 1974, "tld": ".it"},
    "JE": {"code": "JE", "name": "Jersey", "year": 2006, "tld": ".je"},
    "JM": {"code": "JM", "name": "Jamaica", "year": 1974, "tld": ".jm"},
    "JO": {"code": "JO", "name": "Jordan", "year": 1974, "tld": ".jo"},
    "JP": {"code": "JP", "name": "Japan", "year": 1974, "tld": ".jp"},
    "KE": {"code": "KE", "name": "Kenya", "year": 1974, "tld": ".ke"},
    "KG": {"code": "KG", "name": "Kyrgyzstan", "year": 1992, "tld": ".kg"},
    "KH": {"code": "KH", "name": "Cambodia", "year": 1974, "tld": ".kh"},
    "KI": {"code": "KI", "name": "Kiribati", "year": 1979, "tld": ".ki"},
    "KM": {"code": "KM", "name": "Comoros", "year": 1974, "tld": ".km"},
    "KN": {"code": "KN", "name": "Saint Kitts and Nevis", "year": 1974, "tld": ".kn"},
    "KP": {
        "code": "KP",
        "name": "Korea (Democratic People's Republic of)",
        "year": 1974,
        "tld": ".kp",
    },
    "KR": {"code": "KR", "name": "Korea, Republic of", "year": 1974, "tld": ".kr"},
    "KW": {"code": "KW", "name": "Kuwait", "year": 1974, "tld": ".kw"},
    "KY": {"code": "KY", "name": "Cayman Islands", "year": 1974, "tld": ".ky"},
    "KZ": {"code": "KZ", "name": "Kazakhstan", "year": 1992, "tld": ".kz"},
    "LA": {
        "code": "LA",
        "name": "Lao People's Democratic Republic",
        "year": 1974,
        "tld": ".la",
    },
    "LB": {"code": "LB", "name": "Lebanon", "year": 1974, "tld": ".lb"},
    "LC": {"code": "LC", "name": "Saint Lucia", "year": 1974, "tld": ".lc"},
    "LI": {"code": "LI", "name": "Liechtenstein", "year": 1974, "tld": ".li"},
    "LK": {"code": "LK", "name": "Sri Lanka", "year": 1974, "tld": ".lk"},
    "LR": {"code": "LR", "name": "Liberia", "year": 1974, "tld": ".lr"},
    "LS": {"code": "LS", "name": "Lesotho", "year": 1974, "tld": ".ls"},
    "LT": {"code": "LT", "name": "Lithuania", "year": 1992, "tld": ".lt"},
    "LU": {"code": "LU", "name": "Luxembourg", "year": 1974, "tld": ".lu"},
    "LV": {"code": "LV", "name": "Latvia", "year": 1992, "tld": ".lv"},
    "LY": {"code": "LY", "name": "Libya", "year": 1974, "tld": ".ly"},
    "MA": {"code": "MA", "name": "Morocco", "year": 1974, "tld": ".ma"},
    "MC": {"code": "MC", "name": "Monaco", "year": 1974, "tld": ".mc"},
    "MD": {"code": "MD", "name": "Moldova, Republic of", "year": 1992, "tld": ".md"},
    "ME": {"code": "ME", "name": "Montenegro", "year": 2006, "tld": ".me"},
    "MF": {
        "code": "MF",
        "name": "Saint Martin (French part)",
        "year": 2007,
        "tld": ".mf",
    },
    "MG": {"code": "MG", "name": "Madagascar", "year": 1974, "tld": ".mg"},
    "MH": {"code": "MH", "name": "Marshall Islands", "year": 1986, "tld": ".mh"},
    "MK": {"code": "MK", "name": "North Macedonia", "year": 1993, "tld": ".mk"},
    "ML": {"code": "ML", "name": "Mali", "year": 1974, "tld": ".ml"},
    "MM": {"code": "MM", "name": "Myanmar", "year": 1989, "tld": ".mm"},
    "MN": {"code": "MN", "name": "Mongolia", "year": 1974, "tld": ".mn"},
    "MO": {"code": "MO", "name": "Macao", "year": 1974, "tld": ".mo"},
    "MP": {
        "code": "MP",
        "name": "Northern Mariana Islands",
        "year": 1986,
        "tld": ".mp",
    },
    "MQ": {"code": "MQ", "name": "Martinique", "year": 1974, "tld": ".mq"},
    "MR": {"code": "MR", "name": "Mauritania", "year": 1974, "tld": ".mr"},
    "MS": {"code": "MS", "name": "Montserrat", "year": 1974, "tld": ".ms"},
    "MT": {"code": "MT", "name": "Malta", "year": 1974, "tld": ".mt"},
    "MU": {"code": "MU", "name": "Mauritius", "year": 1974, "tld": ".mu"},
    "MV": {"code": "MV", "name": "Maldives", "year": 1974, "tld": ".mv"},
    "MW": {"code": "MW", "name": "Malawi", "year": 1974, "tld": ".mw"},
    "MX": {"code": "MX", "name": "Mexico", "year": 1974, "tld": ".mx"},
    "MY": {"code": "MY", "name": "Malaysia", "year": 1974, "tld": ".my"},
    "MZ": {"code": "MZ", "name": "Mozambique", "year": 1974, "tld": ".mz"},
    "NA": {"code": "NA", "name": "Namibia", "year": 1974, "tld": ".na"},
    "NC": {"code": "NC", "name": "New Caledonia", "year": 1974, "tld": ".nc"},
    "NE": {"code": "NE", "name": "Niger", "year": 1974, "tld": ".ne"},
    "NF": {"code": "NF", "name": "Norfolk Island", "year": 1974, "tld": ".nf"},
    "NG": {"code": "NG", "name": "Nigeria", "year": 1974, "tld": ".ng"},
    "NI": {"code": "NI", "name": "Nicaragua", "year": 1974, "tld": ".ni"},
    "NL": {"code": "NL", "name": "Netherlands", "year": 1974, "tld": ".nl"},
    "NO": {"code": "NO", "name": "Norway", "year": 1974, "tld": ".no"},
    "NP": {"code": "NP", "name": "Nepal", "year": 1974, "tld": ".np"},
    "NR": {"code": "NR", "name": "Nauru", "year": 1974, "tld": ".nr"},
    "NU": {"code": "NU", "name": "Niue", "year": 1974, "tld": ".nu"},
    "NZ": {"code": "NZ", "name": "New Zealand", "year": 1974, "tld": ".nz"},
    "OM": {"code": "OM", "name": "Oman", "year": 1974, "tld": ".om"},
    "PA": {"code": "PA", "name": "Panama", "year": 1974, "tld": ".pa"},
    "PE": {"code": "PE", "name": "Peru", "year": 1974, "tld": ".pe"},
    "PF": {"code": "PF", "name": "French Polynesia", "year": 1974, "tld": ".pf"},
    "PG": {"code": "PG", "name": "Papua New Guinea", "year": 1974, "tld": ".pg"},
    "PH": {"code": "PH", "name": "Philippines", "year": 1974, "tld": ".ph"},
    "PK": {"code": "PK", "name": "Pakistan", "year": 1974, "tld": ".pk"},
    "PL": {"code": "PL", "name": "Poland", "year": 1974, "tld": ".pl"},
    "PM": {
        "code": "PM",
        "name": "Saint Pierre and Miquelon",
        "year": 1974,
        "tld": ".pm",
    },
    "PN": {"code": "PN", "name": "Pitcairn", "year": 1974, "tld": ".pn"},
    "PR": {"code": "PR", "name": "Puerto Rico", "year": 1974, "tld": ".pr"},
    "PS": {"code": "PS", "name": "Palestine, State of", "year": 1999, "tld": ".ps"},
    "PT": {"code": "PT", "name": "Portugal", "year": 1974, "tld": ".pt"},
    "PW": {"code": "PW", "name": "Palau", "year": 1986, "tld": ".pw"},
    "PY": {"code": "PY", "name": "Paraguay", "year": 1974, "tld": ".py"},
    "QA": {"code": "QA", "name": "Qatar", "year": 1974, "tld": ".qa"},
    "RE": {
        "code": "RE",
        "name": '<span data-sort-value="Reunion !">Réunion',
        "year": 1974,
        "tld": ".re",
    },
    "RO": {"code": "RO", "name": "Romania", "year": 1974, "tld": ".ro"},
    "RS": {"code": "RS", "name": "Serbia", "year": 2006, "tld": ".rs"},
    "RU": {"code": "RU", "name": "Russian Federation", "year": 1992, "tld": ".ru"},
    "RW": {"code": "RW", "name": "Rwanda", "year": 1974, "tld": ".rw"},
    "SA": {"code": "SA", "name": "Saudi Arabia", "year": 1974, "tld": ".sa"},
    "SB": {"code": "SB", "name": "Solomon Islands", "year": 1974, "tld": ".sb"},
    "SC": {"code": "SC", "name": "Seychelles", "year": 1974, "tld": ".sc"},
    "SD": {"code": "SD", "name": "Sudan", "year": 1974, "tld": ".sd"},
    "SE": {"code": "SE", "name": "Sweden", "year": 1974, "tld": ".se"},
    "SG": {"code": "SG", "name": "Singapore", "year": 1974, "tld": ".sg"},
    "SH": {
        "code": "SH",
        "name": "Saint Helena, Ascension and Tristan da Cunha",
        "year": 1974,
        "tld": ".sh",
    },
    "SI": {"code": "SI", "name": "Slovenia", "year": 1992, "tld": ".si"},
    "SJ": {"code": "SJ", "name": "Svalbard and Jan Mayen", "year": 1974, "tld": ".sj"},
    "SK": {"code": "SK", "name": "Slovakia", "year": 1993, "tld": ".sk"},
    "SL": {"code": "SL", "name": "Sierra Leone", "year": 1974, "tld": ".sl"},
    "SM": {"code": "SM", "name": "San Marino", "year": 1974, "tld": ".sm"},
    "SN": {"code": "SN", "name": "Senegal", "year": 1974, "tld": ".sn"},
    "SO": {"code": "SO", "name": "Somalia", "year": 1974, "tld": ".so"},
    "SR": {"code": "SR", "name": "Suriname", "year": 1974, "tld": ".sr"},
    "SS": {"code": "SS", "name": "South Sudan", "year": 2011, "tld": ".ss"},
    "ST": {"code": "ST", "name": "Sao Tome and Principe", "year": 1974, "tld": ".st"},
    "SV": {"code": "SV", "name": "El Salvador", "year": 1974, "tld": ".sv"},
    "SX": {
        "code": "SX",
        "name": "Sint Maarten (Dutch part)",
        "year": 2010,
        "tld": ".sx",
    },
    "SY": {"code": "SY", "name": "Syrian Arab Republic", "year": 1974, "tld": ".sy"},
    "SZ": {"code": "SZ", "name": "Eswatini", "year": 1974, "tld": ".sz"},
    "TC": {
        "code": "TC",
        "name": "Turks and Caicos Islands",
        "year": 1974,
        "tld": ".tc",
    },
    "TD": {"code": "TD", "name": "Chad", "year": 1974, "tld": ".td"},
    "TF": {
        "code": "TF",
        "name": "French Southern Territories",
        "year": 1979,
        "tld": ".tf",
    },
    "TG": {"code": "TG", "name": "Togo", "year": 1974, "tld": ".tg"},
    "TH": {"code": "TH", "name": "Thailand", "year": 1974, "tld": ".th"},
    "TJ": {"code": "TJ", "name": "Tajikistan", "year": 1992, "tld": ".tj"},
    "TK": {"code": "TK", "name": "Tokelau", "year": 1974, "tld": ".tk"},
    "TL": {"code": "TL", "name": "Timor-Leste", "year": 2002, "tld": ".tl"},
    "TM": {"code": "TM", "name": "Turkmenistan", "year": 1992, "tld": ".tm"},
    "TN": {"code": "TN", "name": "Tunisia", "year": 1974, "tld": ".tn"},
    "TO": {"code": "TO", "name": "Tonga", "year": 1974, "tld": ".to"},
    "TR": {"code": "TR", "name": "Turkey", "year": 1974, "tld": ".tr"},
    "TT": {"code": "TT", "name": "Trinidad and Tobago", "year": 1974, "tld": ".tt"},
    "TV": {"code": "TV", "name": "Tuvalu", "year": 1977, "tld": ".tv"},
    "TW": {
        "code": "TW",
        "name": "Taiwan, Province of China",
        "year": 1974,
        "tld": ".tw",
    },
    "TZ": {
        "code": "TZ",
        "name": "Tanzania, United Republic of",
        "year": 1974,
        "tld": ".tz",
    },
    "UA": {"code": "UA", "name": "Ukraine", "year": 1974, "tld": ".ua"},
    "UG": {"code": "UG", "name": "Uganda", "year": 1974, "tld": ".ug"},
    "UM": {
        "code": "UM",
        "name": "United States Minor Outlying Islands",
        "year": 1986,
        "tld": "",
    },
    "US": {
        "code": "US",
        "name": "United States of America",
        "year": 1974,
        "tld": ".us",
    },
    "UY": {"code": "UY", "name": "Uruguay", "year": 1974, "tld": ".uy"},
    "UZ": {"code": "UZ", "name": "Uzbekistan", "year": 1992, "tld": ".uz"},
    "VA": {"code": "VA", "name": "Holy See", "year": 1974, "tld": ".va"},
    "VC": {
        "code": "VC",
        "name": "Saint Vincent and the Grenadines",
        "year": 1974,
        "tld": ".vc",
    },
    "VE": {
        "code": "VE",
        "name": "Venezuela (Bolivarian Republic of)",
        "year": 1974,
        "tld": ".ve",
    },
    "VG": {
        "code": "VG",
        "name": "Virgin Islands (British)",
        "year": 1974,
        "tld": ".vg",
    },
    "VI": {"code": "VI", "name": "Virgin Islands (U.S.)", "year": 1974, "tld": ".vi"},
    "VN": {"code": "VN", "name": "Viet Nam", "year": 1974, "tld": ".vn"},
    "VU": {"code": "VU", "name": "Vanuatu", "year": 1980, "tld": ".vu"},
    "WF": {"code": "WF", "name": "Wallis and Futuna", "year": 1974, "tld": ".wf"},
    "WS": {"code": "WS", "name": "Samoa", "year": 1974, "tld": ".ws"},
    "YE": {"code": "YE", "name": "Yemen", "year": 1974, "tld": ".ye"},
    "YT": {"code": "YT", "name": "Mayotte", "year": 1993, "tld": ".yt"},
    "ZA": {"code": "ZA", "name": "South Africa", "year": 1974, "tld": ".za"},
    "ZM": {"code": "ZM", "name": "Zambia", "year": 1974, "tld": ".zm"},
    "ZW": {"code": "ZW", "name": "Zimbabwe", "year": 1980, "tld": ".zw"},
}


@dataclass
class Country:
    """
    A Country holds:
    * `id` 2-Letter Country Code.
    * `name` the verbose name in standard-english.
    * `year` the year the alpha-2 code was officialized
    * `tld` Top Level Domain.
    """

    id: str
    name: str
    year: int
    tld: List[str]


@dataclass(frozen=True)
class World:
    """
    A World holds little info:
    * `countries` a list of Countries.
    """

    countries: List[Optional[Country]] = field(default_factory=list)

    def __post_init__(self):
        for cc, data in CC_DICT.items():
            name, year, tld = [data.get(_) for _ in ["name", "year", "tld"]]
            tld = [_.strip() for _ in tld.split(",")]
            self.countries.append(Country(cc, name, year, tld))

    def __iter__(self):
        for country in self.countries:
            yield country

    def __find(self, key, value, strict=False):
        if key == "id":
            for country in self:
                if country.id == value:
                    return country
        if key == "name":
            for country in self:
                if (not strict and value.lower() in country.name.lower()) or (
                    strict and country.name == value
                ):
                    return country

    def find_by_id(self, value):
        return self.__find("id", value)

    def find_by_name(self, value, strict=True):
        return self.__find("name", value, strict)
