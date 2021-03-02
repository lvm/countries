#!/usr/bin/env python3

import abc
from typing import List
from typing import Union
from typing import Literal
from typing import Optional
from dataclasses import field
from dataclasses import dataclass

try:
    from typing import Iterator
except:
    from collections.abc import Iterator

CC_DICT = {
    "AD": {"code": "AD", "name": "Andorra", "year": 1974, "alias": "", "tld": ".ad"},
    "AE": {
        "code": "AE",
        "name": "United Arab Emirates",
        "year": 1974,
        "alias": "",
        "tld": ".ae",
    },
    "AF": {
        "code": "AF",
        "name": "Afghanistan",
        "year": 1974,
        "alias": "",
        "tld": ".af",
    },
    "AG": {
        "code": "AG",
        "name": "Antigua and Barbuda",
        "year": 1974,
        "alias": "",
        "tld": ".ag",
    },
    "AI": {"code": "AI", "name": "Anguilla", "year": 1985, "alias": "", "tld": ".ai"},
    "AL": {"code": "AL", "name": "Albania", "year": 1974, "alias": "", "tld": ".al"},
    "AM": {"code": "AM", "name": "Armenia", "year": 1992, "alias": "", "tld": ".am"},
    "AO": {"code": "AO", "name": "Angola", "year": 1974, "alias": "", "tld": ".ao"},
    "AQ": {"code": "AQ", "name": "Antarctica", "year": 1974, "alias": "", "tld": ".aq"},
    "AR": {"code": "AR", "name": "Argentina", "year": 1974, "alias": "", "tld": ".ar"},
    "AS": {
        "code": "AS",
        "name": "American Samoa",
        "year": 1974,
        "alias": "",
        "tld": ".as",
    },
    "AT": {"code": "AT", "name": "Austria", "year": 1974, "alias": "", "tld": ".at"},
    "AU": {"code": "AU", "name": "Australia", "year": 1974, "alias": "", "tld": ".au"},
    "AW": {"code": "AW", "name": "Aruba", "year": 1986, "alias": "", "tld": ".aw"},
    "AX": {
        "code": "AX",
        "name": "Åland Islands",
        "year": 2004,
        "alias": "",
        "tld": ".ax",
    },
    "AZ": {"code": "AZ", "name": "Azerbaijan", "year": 1992, "alias": "", "tld": ".az"},
    "BA": {
        "code": "BA",
        "name": "Bosnia and Herzegovina",
        "year": 1992,
        "alias": "",
        "tld": ".ba",
    },
    "BB": {"code": "BB", "name": "Barbados", "year": 1974, "alias": "", "tld": ".bb"},
    "BD": {"code": "BD", "name": "Bangladesh", "year": 1974, "alias": "", "tld": ".bd"},
    "BE": {"code": "BE", "name": "Belgium", "year": 1974, "alias": "", "tld": ".be"},
    "BF": {
        "code": "BF",
        "name": "Burkina Faso",
        "year": 1984,
        "alias": "",
        "tld": ".bf",
    },
    "BG": {"code": "BG", "name": "Bulgaria", "year": 1974, "alias": "", "tld": ".bg"},
    "BH": {"code": "BH", "name": "Bahrain", "year": 1974, "alias": "", "tld": ".bh"},
    "BI": {"code": "BI", "name": "Burundi", "year": 1974, "alias": "", "tld": ".bi"},
    "BJ": {"code": "BJ", "name": "Benin", "year": 1977, "alias": "", "tld": ".bj"},
    "BL": {
        "code": "BL",
        "name": "Saint Barthélemy",
        "year": 2007,
        "alias": "",
        "tld": ".bl",
    },
    "BM": {"code": "BM", "name": "Bermuda", "year": 1974, "alias": "", "tld": ".bm"},
    "BN": {
        "code": "BN",
        "name": "Brunei Darussalam",
        "year": 1974,
        "alias": "",
        "tld": ".bn",
    },
    "BO": {
        "code": "BO",
        "name": "Bolivia (Plurinational State of)",
        "year": 1974,
        "alias": "",
        "tld": ".bo",
    },
    "BQ": {
        "code": "BQ",
        "name": "Bonaire, Sint Eustatius and Saba",
        "year": 2010,
        "alias": "",
        "tld": ".bq",
    },
    "BR": {"code": "BR", "name": "Brazil", "year": 1974, "alias": "", "tld": ".br"},
    "BS": {"code": "BS", "name": "Bahamas", "year": 1974, "alias": "", "tld": ".bs"},
    "BT": {"code": "BT", "name": "Bhutan", "year": 1974, "alias": "", "tld": ".bt"},
    "BV": {
        "code": "BV",
        "name": "Bouvet Island",
        "year": 1974,
        "alias": "",
        "tld": ".bv",
    },
    "BW": {"code": "BW", "name": "Botswana", "year": 1974, "alias": "", "tld": ".bw"},
    "BY": {"code": "BY", "name": "Belarus", "year": 1974, "alias": "", "tld": ".by"},
    "BZ": {"code": "BZ", "name": "Belize", "year": 1974, "alias": "", "tld": ".bz"},
    "CA": {"code": "CA", "name": "Canada", "year": 1974, "alias": "", "tld": ".ca"},
    "CC": {
        "code": "CC",
        "name": "Cocos (Keeling) Islands",
        "year": 1974,
        "alias": "",
        "tld": ".cc",
    },
    "CD": {
        "code": "CD",
        "name": "Congo, Democratic Republic of the",
        "year": 1997,
        "alias": "",
        "tld": ".cd",
    },
    "CF": {
        "code": "CF",
        "name": "Central African Republic",
        "year": 1974,
        "alias": "",
        "tld": ".cf",
    },
    "CG": {"code": "CG", "name": "Congo", "year": 1974, "alias": "", "tld": ".cg"},
    "CH": {
        "code": "CH",
        "name": "Switzerland",
        "year": 1974,
        "alias": "",
        "tld": ".ch",
    },
    "CI": {
        "code": "CI",
        "name": "Côte d'Ivoire",
        "year": 1974,
        "alias": "",
        "tld": ".ci",
    },
    "CK": {
        "code": "CK",
        "name": "Cook Islands",
        "year": 1974,
        "alias": "",
        "tld": ".ck",
    },
    "CL": {"code": "CL", "name": "Chile", "year": 1974, "alias": "", "tld": ".cl"},
    "CM": {"code": "CM", "name": "Cameroon", "year": 1974, "alias": "", "tld": ".cm"},
    "CN": {"code": "CN", "name": "China", "year": 1974, "alias": "", "tld": ".cn"},
    "CO": {"code": "CO", "name": "Colombia", "year": 1974, "alias": "", "tld": ".co"},
    "CR": {"code": "CR", "name": "Costa Rica", "year": 1974, "alias": "", "tld": ".cr"},
    "CU": {"code": "CU", "name": "Cuba", "year": 1974, "alias": "", "tld": ".cu"},
    "CV": {"code": "CV", "name": "Cabo Verde", "year": 1974, "alias": "", "tld": ".cv"},
    "CW": {"code": "CW", "name": "Curaçao", "year": 2010, "alias": "", "tld": ".cw"},
    "CX": {
        "code": "CX",
        "name": "Christmas Island",
        "year": 1974,
        "alias": "",
        "tld": ".cx",
    },
    "CY": {"code": "CY", "name": "Cyprus", "year": 1974, "alias": "", "tld": ".cy"},
    "CZ": {"code": "CZ", "name": "Czechia", "year": 1993, "alias": "", "tld": ".cz"},
    "DE": {"code": "DE", "name": "Germany", "year": 1974, "alias": "", "tld": ".de"},
    "DJ": {"code": "DJ", "name": "Djibouti", "year": 1977, "alias": "", "tld": ".dj"},
    "DK": {"code": "DK", "name": "Denmark", "year": 1974, "alias": "", "tld": ".dk"},
    "DM": {"code": "DM", "name": "Dominica", "year": 1974, "alias": "", "tld": ".dm"},
    "DO": {
        "code": "DO",
        "name": "Dominican Republic",
        "year": 1974,
        "alias": "",
        "tld": ".do",
    },
    "DZ": {"code": "DZ", "name": "Algeria", "year": 1974, "alias": "", "tld": ".dz"},
    "EC": {"code": "EC", "name": "Ecuador", "year": 1974, "alias": "", "tld": ".ec"},
    "EE": {"code": "EE", "name": "Estonia", "year": 1992, "alias": "", "tld": ".ee"},
    "EG": {"code": "EG", "name": "Egypt", "year": 1974, "alias": "", "tld": ".eg"},
    "EH": {
        "code": "EH",
        "name": "Western Sahara",
        "year": 1974,
        "alias": "",
        "tld": "",
    },
    "ER": {"code": "ER", "name": "Eritrea", "year": 1993, "alias": "", "tld": ".er"},
    "ES": {"code": "ES", "name": "Spain", "year": 1974, "alias": "", "tld": ".es"},
    "ET": {"code": "ET", "name": "Ethiopia", "year": 1974, "alias": "", "tld": ".et"},
    "FI": {"code": "FI", "name": "Finland", "year": 1974, "alias": "", "tld": ".fi"},
    "FJ": {"code": "FJ", "name": "Fiji", "year": 1974, "alias": "", "tld": ".fj"},
    "FK": {
        "code": "FK",
        "name": "Falkland Islands (Malvinas)",
        "year": 1974,
        "alias": "",
        "tld": ".fk",
    },
    "FM": {
        "code": "FM",
        "name": "Micronesia (Federated States of)",
        "year": 1986,
        "alias": "",
        "tld": ".fm",
    },
    "FO": {
        "code": "FO",
        "name": "Faroe Islands",
        "year": 1974,
        "alias": "",
        "tld": ".fo",
    },
    "FR": {"code": "FR", "name": "France", "year": 1974, "alias": "", "tld": ".fr"},
    "GA": {"code": "GA", "name": "Gabon", "year": 1974, "alias": "", "tld": ".ga"},
    "GB": {
        "code": "GB",
        "name": "United Kingdom of Great Britain and Northern Ireland",
        "year": 1974,
        "alias": "UK",
        "tld": ".gb, .uk",
    },
    "GD": {"code": "GD", "name": "Grenada", "year": 1974, "alias": "", "tld": ".gd"},
    "GE": {"code": "GE", "name": "Georgia", "year": 1992, "alias": "", "tld": ".ge"},
    "GF": {
        "code": "GF",
        "name": "French Guiana",
        "year": 1974,
        "alias": "",
        "tld": ".gf",
    },
    "GG": {"code": "GG", "name": "Guernsey", "year": 2006, "alias": "", "tld": ".gg"},
    "GH": {"code": "GH", "name": "Ghana", "year": 1974, "alias": "", "tld": ".gh"},
    "GI": {"code": "GI", "name": "Gibraltar", "year": 1974, "alias": "", "tld": ".gi"},
    "GL": {"code": "GL", "name": "Greenland", "year": 1974, "alias": "", "tld": ".gl"},
    "GM": {"code": "GM", "name": "Gambia", "year": 1974, "alias": "", "tld": ".gm"},
    "GN": {"code": "GN", "name": "Guinea", "year": 1974, "alias": "", "tld": ".gn"},
    "GP": {"code": "GP", "name": "Guadeloupe", "year": 1974, "alias": "", "tld": ".gp"},
    "GQ": {
        "code": "GQ",
        "name": "Equatorial Guinea",
        "year": 1974,
        "alias": "",
        "tld": ".gq",
    },
    "GR": {"code": "GR", "name": "Greece", "year": 1974, "alias": "EL", "tld": ".gr"},
    "GS": {
        "code": "GS",
        "name": "South Georgia and the South Sandwich Islands",
        "year": 1993,
        "alias": "",
        "tld": ".gs",
    },
    "GT": {"code": "GT", "name": "Guatemala", "year": 1974, "alias": "", "tld": ".gt"},
    "GU": {"code": "GU", "name": "Guam", "year": 1974, "alias": "", "tld": ".gu"},
    "GW": {
        "code": "GW",
        "name": "Guinea-Bissau",
        "year": 1974,
        "alias": "",
        "tld": ".gw",
    },
    "GY": {"code": "GY", "name": "Guyana", "year": 1974, "alias": "", "tld": ".gy"},
    "HK": {"code": "HK", "name": "Hong Kong", "year": 1974, "alias": "", "tld": ".hk"},
    "HM": {
        "code": "HM",
        "name": "Heard Island and McDonald Islands",
        "year": 1974,
        "alias": "",
        "tld": ".hm",
    },
    "HN": {"code": "HN", "name": "Honduras", "year": 1974, "alias": "", "tld": ".hn"},
    "HR": {"code": "HR", "name": "Croatia", "year": 1992, "alias": "", "tld": ".hr"},
    "HT": {"code": "HT", "name": "Haiti", "year": 1974, "alias": "", "tld": ".ht"},
    "HU": {"code": "HU", "name": "Hungary", "year": 1974, "alias": "", "tld": ".hu"},
    "ID": {"code": "ID", "name": "Indonesia", "year": 1974, "alias": "", "tld": ".id"},
    "IE": {"code": "IE", "name": "Ireland", "year": 1974, "alias": "", "tld": ".ie"},
    "IL": {"code": "IL", "name": "Israel", "year": 1974, "alias": "", "tld": ".il"},
    "IM": {
        "code": "IM",
        "name": "Isle of Man",
        "year": 2006,
        "alias": "",
        "tld": ".im",
    },
    "IN": {"code": "IN", "name": "India", "year": 1974, "alias": "", "tld": ".in"},
    "IO": {
        "code": "IO",
        "name": "British Indian Ocean Territory",
        "year": 1974,
        "alias": "",
        "tld": ".io",
    },
    "IQ": {"code": "IQ", "name": "Iraq", "year": 1974, "alias": "", "tld": ".iq"},
    "IR": {
        "code": "IR",
        "name": "Iran (Islamic Republic of)",
        "year": 1974,
        "alias": "",
        "tld": ".ir",
    },
    "IS": {"code": "IS", "name": "Iceland", "year": 1974, "alias": "", "tld": ".is"},
    "IT": {"code": "IT", "name": "Italy", "year": 1974, "alias": "", "tld": ".it"},
    "JE": {"code": "JE", "name": "Jersey", "year": 2006, "alias": "", "tld": ".je"},
    "JM": {"code": "JM", "name": "Jamaica", "year": 1974, "alias": "", "tld": ".jm"},
    "JO": {"code": "JO", "name": "Jordan", "year": 1974, "alias": "", "tld": ".jo"},
    "JP": {"code": "JP", "name": "Japan", "year": 1974, "alias": "", "tld": ".jp"},
    "KE": {"code": "KE", "name": "Kenya", "year": 1974, "alias": "", "tld": ".ke"},
    "KG": {"code": "KG", "name": "Kyrgyzstan", "year": 1992, "alias": "", "tld": ".kg"},
    "KH": {"code": "KH", "name": "Cambodia", "year": 1974, "alias": "", "tld": ".kh"},
    "KI": {"code": "KI", "name": "Kiribati", "year": 1979, "alias": "", "tld": ".ki"},
    "KM": {"code": "KM", "name": "Comoros", "year": 1974, "alias": "", "tld": ".km"},
    "KN": {
        "code": "KN",
        "name": "Saint Kitts and Nevis",
        "year": 1974,
        "alias": "",
        "tld": ".kn",
    },
    "KP": {
        "code": "KP",
        "name": "Korea (Democratic People's Republic of)",
        "year": 1974,
        "alias": "",
        "tld": ".kp",
    },
    "KR": {
        "code": "KR",
        "name": "Korea, Republic of",
        "year": 1974,
        "alias": "",
        "tld": ".kr",
    },
    "KW": {"code": "KW", "name": "Kuwait", "year": 1974, "alias": "", "tld": ".kw"},
    "KY": {
        "code": "KY",
        "name": "Cayman Islands",
        "year": 1974,
        "alias": "",
        "tld": ".ky",
    },
    "KZ": {"code": "KZ", "name": "Kazakhstan", "year": 1992, "alias": "", "tld": ".kz"},
    "LA": {
        "code": "LA",
        "name": "Lao People's Democratic Republic",
        "year": 1974,
        "alias": "",
        "tld": ".la",
    },
    "LB": {"code": "LB", "name": "Lebanon", "year": 1974, "alias": "", "tld": ".lb"},
    "LC": {
        "code": "LC",
        "name": "Saint Lucia",
        "year": 1974,
        "alias": "",
        "tld": ".lc",
    },
    "LI": {
        "code": "LI",
        "name": "Liechtenstein",
        "year": 1974,
        "alias": "",
        "tld": ".li",
    },
    "LK": {"code": "LK", "name": "Sri Lanka", "year": 1974, "alias": "", "tld": ".lk"},
    "LR": {"code": "LR", "name": "Liberia", "year": 1974, "alias": "", "tld": ".lr"},
    "LS": {"code": "LS", "name": "Lesotho", "year": 1974, "alias": "", "tld": ".ls"},
    "LT": {"code": "LT", "name": "Lithuania", "year": 1992, "alias": "", "tld": ".lt"},
    "LU": {"code": "LU", "name": "Luxembourg", "year": 1974, "alias": "", "tld": ".lu"},
    "LV": {"code": "LV", "name": "Latvia", "year": 1992, "alias": "", "tld": ".lv"},
    "LY": {"code": "LY", "name": "Libya", "year": 1974, "alias": "", "tld": ".ly"},
    "MA": {"code": "MA", "name": "Morocco", "year": 1974, "alias": "", "tld": ".ma"},
    "MC": {"code": "MC", "name": "Monaco", "year": 1974, "alias": "", "tld": ".mc"},
    "MD": {
        "code": "MD",
        "name": "Moldova, Republic of",
        "year": 1992,
        "alias": "",
        "tld": ".md",
    },
    "ME": {"code": "ME", "name": "Montenegro", "year": 2006, "alias": "", "tld": ".me"},
    "MF": {
        "code": "MF",
        "name": "Saint Martin (French part)",
        "year": 2007,
        "alias": "",
        "tld": ".mf",
    },
    "MG": {"code": "MG", "name": "Madagascar", "year": 1974, "alias": "", "tld": ".mg"},
    "MH": {
        "code": "MH",
        "name": "Marshall Islands",
        "year": 1986,
        "alias": "",
        "tld": ".mh",
    },
    "MK": {
        "code": "MK",
        "name": "North Macedonia",
        "year": 1993,
        "alias": "",
        "tld": ".mk",
    },
    "ML": {"code": "ML", "name": "Mali", "year": 1974, "alias": "", "tld": ".ml"},
    "MM": {"code": "MM", "name": "Myanmar", "year": 1989, "alias": "", "tld": ".mm"},
    "MN": {"code": "MN", "name": "Mongolia", "year": 1974, "alias": "", "tld": ".mn"},
    "MO": {"code": "MO", "name": "Macao", "year": 1974, "alias": "", "tld": ".mo"},
    "MP": {
        "code": "MP",
        "name": "Northern Mariana Islands",
        "year": 1986,
        "alias": "",
        "tld": ".mp",
    },
    "MQ": {"code": "MQ", "name": "Martinique", "year": 1974, "alias": "", "tld": ".mq"},
    "MR": {"code": "MR", "name": "Mauritania", "year": 1974, "alias": "", "tld": ".mr"},
    "MS": {"code": "MS", "name": "Montserrat", "year": 1974, "alias": "", "tld": ".ms"},
    "MT": {"code": "MT", "name": "Malta", "year": 1974, "alias": "", "tld": ".mt"},
    "MU": {"code": "MU", "name": "Mauritius", "year": 1974, "alias": "", "tld": ".mu"},
    "MV": {"code": "MV", "name": "Maldives", "year": 1974, "alias": "", "tld": ".mv"},
    "MW": {"code": "MW", "name": "Malawi", "year": 1974, "alias": "", "tld": ".mw"},
    "MX": {"code": "MX", "name": "Mexico", "year": 1974, "alias": "", "tld": ".mx"},
    "MY": {"code": "MY", "name": "Malaysia", "year": 1974, "alias": "", "tld": ".my"},
    "MZ": {"code": "MZ", "name": "Mozambique", "year": 1974, "alias": "", "tld": ".mz"},
    "NA": {"code": "NA", "name": "Namibia", "year": 1974, "alias": "", "tld": ".na"},
    "NC": {
        "code": "NC",
        "name": "New Caledonia",
        "year": 1974,
        "alias": "",
        "tld": ".nc",
    },
    "NE": {"code": "NE", "name": "Niger", "year": 1974, "alias": "", "tld": ".ne"},
    "NF": {
        "code": "NF",
        "name": "Norfolk Island",
        "year": 1974,
        "alias": "",
        "tld": ".nf",
    },
    "NG": {"code": "NG", "name": "Nigeria", "year": 1974, "alias": "", "tld": ".ng"},
    "NI": {"code": "NI", "name": "Nicaragua", "year": 1974, "alias": "", "tld": ".ni"},
    "NL": {
        "code": "NL",
        "name": "Netherlands",
        "year": 1974,
        "alias": "",
        "tld": ".nl",
    },
    "NO": {"code": "NO", "name": "Norway", "year": 1974, "alias": "", "tld": ".no"},
    "NP": {"code": "NP", "name": "Nepal", "year": 1974, "alias": "", "tld": ".np"},
    "NR": {"code": "NR", "name": "Nauru", "year": 1974, "alias": "", "tld": ".nr"},
    "NU": {"code": "NU", "name": "Niue", "year": 1974, "alias": "", "tld": ".nu"},
    "NZ": {
        "code": "NZ",
        "name": "New Zealand",
        "year": 1974,
        "alias": "",
        "tld": ".nz",
    },
    "OM": {"code": "OM", "name": "Oman", "year": 1974, "alias": "", "tld": ".om"},
    "PA": {"code": "PA", "name": "Panama", "year": 1974, "alias": "", "tld": ".pa"},
    "PE": {"code": "PE", "name": "Peru", "year": 1974, "alias": "", "tld": ".pe"},
    "PF": {
        "code": "PF",
        "name": "French Polynesia",
        "year": 1974,
        "alias": "",
        "tld": ".pf",
    },
    "PG": {
        "code": "PG",
        "name": "Papua New Guinea",
        "year": 1974,
        "alias": "",
        "tld": ".pg",
    },
    "PH": {
        "code": "PH",
        "name": "Philippines",
        "year": 1974,
        "alias": "",
        "tld": ".ph",
    },
    "PK": {"code": "PK", "name": "Pakistan", "year": 1974, "alias": "", "tld": ".pk"},
    "PL": {"code": "PL", "name": "Poland", "year": 1974, "alias": "", "tld": ".pl"},
    "PM": {
        "code": "PM",
        "name": "Saint Pierre and Miquelon",
        "year": 1974,
        "alias": "",
        "tld": ".pm",
    },
    "PN": {"code": "PN", "name": "Pitcairn", "year": 1974, "alias": "", "tld": ".pn"},
    "PR": {
        "code": "PR",
        "name": "Puerto Rico",
        "year": 1974,
        "alias": "",
        "tld": ".pr",
    },
    "PS": {
        "code": "PS",
        "name": "Palestine, State of",
        "year": 1999,
        "alias": "",
        "tld": ".ps",
    },
    "PT": {"code": "PT", "name": "Portugal", "year": 1974, "alias": "", "tld": ".pt"},
    "PW": {"code": "PW", "name": "Palau", "year": 1986, "alias": "", "tld": ".pw"},
    "PY": {"code": "PY", "name": "Paraguay", "year": 1974, "alias": "", "tld": ".py"},
    "QA": {"code": "QA", "name": "Qatar", "year": 1974, "alias": "", "tld": ".qa"},
    "RE": {
        "code": "RE",
        "name": '<span data-sort-value="Reunion !">Réunion',
        "year": 1974,
        "alias": "",
        "tld": ".re",
    },
    "RO": {"code": "RO", "name": "Romania", "year": 1974, "alias": "", "tld": ".ro"},
    "RS": {"code": "RS", "name": "Serbia", "year": 2006, "alias": "", "tld": ".rs"},
    "RU": {
        "code": "RU",
        "name": "Russian Federation",
        "year": 1992,
        "alias": "",
        "tld": ".ru",
    },
    "RW": {"code": "RW", "name": "Rwanda", "year": 1974, "alias": "", "tld": ".rw"},
    "SA": {
        "code": "SA",
        "name": "Saudi Arabia",
        "year": 1974,
        "alias": "",
        "tld": ".sa",
    },
    "SB": {
        "code": "SB",
        "name": "Solomon Islands",
        "year": 1974,
        "alias": "",
        "tld": ".sb",
    },
    "SC": {"code": "SC", "name": "Seychelles", "year": 1974, "alias": "", "tld": ".sc"},
    "SD": {"code": "SD", "name": "Sudan", "year": 1974, "alias": "", "tld": ".sd"},
    "SE": {"code": "SE", "name": "Sweden", "year": 1974, "alias": "", "tld": ".se"},
    "SG": {"code": "SG", "name": "Singapore", "year": 1974, "alias": "", "tld": ".sg"},
    "SH": {
        "code": "SH",
        "name": "Saint Helena, Ascension and Tristan da Cunha",
        "year": 1974,
        "alias": "",
        "tld": ".sh",
    },
    "SI": {"code": "SI", "name": "Slovenia", "year": 1992, "alias": "", "tld": ".si"},
    "SJ": {
        "code": "SJ",
        "name": "Svalbard and Jan Mayen",
        "year": 1974,
        "alias": "",
        "tld": ".sj",
    },
    "SK": {"code": "SK", "name": "Slovakia", "year": 1993, "alias": "", "tld": ".sk"},
    "SL": {
        "code": "SL",
        "name": "Sierra Leone",
        "year": 1974,
        "alias": "",
        "tld": ".sl",
    },
    "SM": {"code": "SM", "name": "San Marino", "year": 1974, "alias": "", "tld": ".sm"},
    "SN": {"code": "SN", "name": "Senegal", "year": 1974, "alias": "", "tld": ".sn"},
    "SO": {"code": "SO", "name": "Somalia", "year": 1974, "alias": "", "tld": ".so"},
    "SR": {"code": "SR", "name": "Suriname", "year": 1974, "alias": "", "tld": ".sr"},
    "SS": {
        "code": "SS",
        "name": "South Sudan",
        "year": 2011,
        "alias": "",
        "tld": ".ss",
    },
    "ST": {
        "code": "ST",
        "name": "Sao Tome and Principe",
        "year": 1974,
        "alias": "",
        "tld": ".st",
    },
    "SV": {
        "code": "SV",
        "name": "El Salvador",
        "year": 1974,
        "alias": "",
        "tld": ".sv",
    },
    "SX": {
        "code": "SX",
        "name": "Sint Maarten (Dutch part)",
        "year": 2010,
        "alias": "",
        "tld": ".sx",
    },
    "SY": {
        "code": "SY",
        "name": "Syrian Arab Republic",
        "year": 1974,
        "alias": "",
        "tld": ".sy",
    },
    "SZ": {"code": "SZ", "name": "Eswatini", "year": 1974, "alias": "", "tld": ".sz"},
    "TC": {
        "code": "TC",
        "name": "Turks and Caicos Islands",
        "year": 1974,
        "alias": "",
        "tld": ".tc",
    },
    "TD": {"code": "TD", "name": "Chad", "year": 1974, "alias": "", "tld": ".td"},
    "TF": {
        "code": "TF",
        "name": "French Southern Territories",
        "year": 1979,
        "alias": "",
        "tld": ".tf",
    },
    "TG": {"code": "TG", "name": "Togo", "year": 1974, "alias": "", "tld": ".tg"},
    "TH": {"code": "TH", "name": "Thailand", "year": 1974, "alias": "", "tld": ".th"},
    "TJ": {"code": "TJ", "name": "Tajikistan", "year": 1992, "alias": "", "tld": ".tj"},
    "TK": {"code": "TK", "name": "Tokelau", "year": 1974, "alias": "", "tld": ".tk"},
    "TL": {
        "code": "TL",
        "name": "Timor-Leste",
        "year": 2002,
        "alias": "",
        "tld": ".tl",
    },
    "TM": {
        "code": "TM",
        "name": "Turkmenistan",
        "year": 1992,
        "alias": "",
        "tld": ".tm",
    },
    "TN": {"code": "TN", "name": "Tunisia", "year": 1974, "alias": "", "tld": ".tn"},
    "TO": {"code": "TO", "name": "Tonga", "year": 1974, "alias": "", "tld": ".to"},
    "TR": {"code": "TR", "name": "Turkey", "year": 1974, "alias": "", "tld": ".tr"},
    "TT": {
        "code": "TT",
        "name": "Trinidad and Tobago",
        "year": 1974,
        "alias": "",
        "tld": ".tt",
    },
    "TV": {"code": "TV", "name": "Tuvalu", "year": 1977, "alias": "", "tld": ".tv"},
    "TW": {
        "code": "TW",
        "name": "Taiwan, Province of China",
        "year": 1974,
        "alias": "",
        "tld": ".tw",
    },
    "TZ": {
        "code": "TZ",
        "name": "Tanzania, United Republic of",
        "year": 1974,
        "alias": "",
        "tld": ".tz",
    },
    "UA": {"code": "UA", "name": "Ukraine", "year": 1974, "alias": "", "tld": ".ua"},
    "UG": {"code": "UG", "name": "Uganda", "year": 1974, "alias": "", "tld": ".ug"},
    "UM": {
        "code": "UM",
        "name": "United States Minor Outlying Islands",
        "year": 1986,
        "alias": "",
        "tld": "",
    },
    "US": {
        "code": "US",
        "name": "United States of America",
        "year": 1974,
        "alias": "",
        "tld": ".us",
    },
    "UY": {"code": "UY", "name": "Uruguay", "year": 1974, "alias": "", "tld": ".uy"},
    "UZ": {"code": "UZ", "name": "Uzbekistan", "year": 1992, "alias": "", "tld": ".uz"},
    "VA": {"code": "VA", "name": "Holy See", "year": 1974, "alias": "", "tld": ".va"},
    "VC": {
        "code": "VC",
        "name": "Saint Vincent and the Grenadines",
        "year": 1974,
        "alias": "",
        "tld": ".vc",
    },
    "VE": {
        "code": "VE",
        "name": "Venezuela (Bolivarian Republic of)",
        "year": 1974,
        "alias": "",
        "tld": ".ve",
    },
    "VG": {
        "code": "VG",
        "name": "Virgin Islands (British)",
        "year": 1974,
        "alias": "",
        "tld": ".vg",
    },
    "VI": {
        "code": "VI",
        "name": "Virgin Islands (U.S.)",
        "year": 1974,
        "alias": "",
        "tld": ".vi",
    },
    "VN": {"code": "VN", "name": "Viet Nam", "year": 1974, "alias": "", "tld": ".vn"},
    "VU": {"code": "VU", "name": "Vanuatu", "year": 1980, "alias": "", "tld": ".vu"},
    "WF": {
        "code": "WF",
        "name": "Wallis and Futuna",
        "year": 1974,
        "alias": "",
        "tld": ".wf",
    },
    "WS": {"code": "WS", "name": "Samoa", "year": 1974, "alias": "", "tld": ".ws"},
    "YE": {"code": "YE", "name": "Yemen", "year": 1974, "alias": "", "tld": ".ye"},
    "YT": {"code": "YT", "name": "Mayotte", "year": 1993, "alias": "", "tld": ".yt"},
    "ZA": {
        "code": "ZA",
        "name": "South Africa",
        "year": 1974,
        "alias": "",
        "tld": ".za",
    },
    "ZM": {"code": "ZM", "name": "Zambia", "year": 1974, "alias": "", "tld": ".zm"},
    "ZW": {"code": "ZW", "name": "Zimbabwe", "year": 1980, "alias": "", "tld": ".zw"},
}


@dataclass
class Country(object, metaclass=abc.ABCMeta):
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
    alias: List[str] = field(default_factory=list)

    def __getitem__(self, key):
        if isinstance(self, Country) or issubclass(self, Country):
            return getattr(self, key)
        else:
            raise NotImplementedError


@dataclass(frozen=True)
class World:
    """
    A World holds little info:
    * `countries` a list of Countries.
    """

    countries: List[Optional[Country]] = field(default_factory=list)

    def __post_init__(self, *args: list, **kwargs: dict) -> Literal[None]:
        for cc, data in CC_DICT.items():
            name, year, tld, alias = [
                data.get(_) for _ in ["name", "year", "tld", "alias"]
            ]
            tld = [_.strip() for _ in tld.split(",")]
            alias = [_.strip() for _ in alias.split(",")]
            self.countries.append(Country(cc, name, year, tld, alias))

    def __iter__(self, *args: list, **kwargs: dict) -> Iterator[Country]:
        for country in self.countries:
            yield country

    def __find(
        self, attr: str, value: str, strict: bool = False, *args: list, **kwargs: dict
    ) -> Optional[Country]:
        def match(
            current: Union[str, list], value: str, strict: bool = False
        ) -> Optional[Country]:
            if isinstance(current, str):
                return (
                    country
                    if (not strict and value.lower() == current.lower())
                    or (strict and value == current)
                    else None
                )
            elif isinstance(current, list):
                return (
                    country
                    if (not strict and value.lower() in [_.lower() for _ in current])
                    or (strict and value in current)
                    else None
                )

        result = None
        for country in self:
            if match(getattr(country, attr), value, strict):
                result = country
                break

        return result

    def find_by_id(self, value: str, *args: list, **kwargs: dict) -> Country:
        return self.__find("id", value)

    def find_by_name(
        self, value: str, strict: bool = True, *args: list, **kwargs: dict
    ) -> Country:
        return self.__find("name", value, strict)

    def find_by_tld(
        self, value: str, strict: bool = True, *args: list, **kwargs: dict
    ) -> Country:
        return self.__find("tld", value, strict)

    def find_by_alias(
        self, value: str, strict: bool = True, *args: list, **kwargs: dict
    ) -> Country:
        return self.__find("alias", value, strict)

    def find(
        self, value: str, strict: bool = False, *args: list, **kwargs: dict
    ) -> List[Optional[Country]]:
        finders = [
            getattr(self, f"find_by_{name}") for name in ["id", "name", "tld", "alias"]
        ]

        return list(filter(lambda c: c, [finder(value, strict) for finder in finders]))
