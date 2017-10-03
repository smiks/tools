"""
	Country abbreviation translator
"""
def abb_country_map(country_abb):
	"""
		Maps country abbreviation (alpha-2) to name of country.
	"""

	cabb = {
		'KN': 'Saint Kitts and Nevis', 'AI': 'Anguilla', 'DZ': 'Algeria', 'MA': 'Morocco', 'VU': 'Vanuatu', 
		'JM': 'Jamaica', 'ET': 'Ethiopia', 'UG': 'Uganda', 'CU': 'Cuba', 'TD': 'Chad', 'US': 'United States of America', 
		'DO': 'Dominican Republic', 'SZ': 'Swaziland', 'NU': 'Niue', 'AQ': 'Antarctica', 'LY': 'Libya', 'KW': 'Kuwait', 
		'TN': 'Tunisia', 'NG': 'Nigeria', 'MD': 'Moldova', 'BY': 'Belarus', 'FJ': 'Fiji', 'NI': 'Nicaragua', 
		'SB': 'Solomon Islands', 'DM': 'Dominica', 'RE': 'Réunion', 'IO': 'British Indian Ocean Territory', 'GU': 'Guam', 
		'CV': 'Cape Verde', 'PA': 'Panama', 'GP': 'Guadeloupe', 'AZ': 'Azerbaijan', 'BJ': 'Benin', 'DJ': 'Djibouti', 
		'TZ': 'Tanzania, United Republic of', 'FI': 'Finland', 'AN': 'Netherlands Antilles', 'MY': 'Malaysia', 'NR': 'Nauru', 
		'HN': 'Honduras', 'MO': 'Macao, SAR China', 'RW': 'Rwanda', 'IT': 'Italy', 'MN': 'Mongolia', 'DK': 'Denmark', 
		'GT': 'Guatemala', 'PE': 'Peru', 'MV': 'Maldives', 'KG': 'Kyrgyzstan', 'EC': 'Ecuador', 'AT': 'Austria', 'EG': 'Egypt', 
		'SK': 'Slovakia', 'CM': 'Cameroon', 'SC': 'Seychelles', 'LT': 'Lithuania', 'MQ': 'Martinique', 'CG': 'Congo (Brazzaville)', 
		'AW': 'Aruba', 'UZ': 'Uzbekistan', 'ER': 'Eritrea', 'PT': 'Portugal', 'BT': 'Bhutan', 'EH': 'Western Sahara', 
		'JE': 'Jersey', 'JP': 'Japan', 'GQ': 'Equatorial Guinea', 'MF': 'Saint-Martin (French part)', 'MC': 'Monaco', 'SN': 'Senegal', 
		'BF': 'Burkina Faso', 'NF': 'Norfolk Island', 'GB': 'United Kingdom', 'ML': 'Mali', 'GM': 'Gambia', 'PS': 'Palestinian Territory', 
		'QA': 'Qatar', 'ID': 'Indonesia', 'GG': 'Guernsey', 'MM': 'Myanmar', 'NL': 'Netherlands', 'LA': 'Lao PDR', 'LK': 'Sri Lanka', 
		'PK': 'Pakistan', 'JO': 'Jordan', 'LC': 'Saint Lucia', 'HU': 'Hungary', 'NO': 'Norway', 'MP': 'Northern Mariana Islands', 
		'PF': 'French Polynesia', 'CN': 'China', 'IE': 'Ireland', 'BE': 'Belgium', 'KR': 'Korea (South)', 'BO': 'Bolivia', 
		'MX': 'Mexico', 'FO': 'Faroe Islands', 'UY': 'Uruguay', 'ZM': 'Zambia', 'GD': 'Grenada', 'ZW': 'Zimbabwe', 'NC': 'New Caledonia', 
		'MU': 'Mauritius', 'GE': 'Georgia', 'CF': 'Central African Republic', 'BR': 'Brazil', 'DE': 'Germany', 'MR': 'Mauritania', 
		'TO': 'Tonga', 'ZA': 'South Africa', 'SJ': 'Svalbard and Jan Mayen Islands', 'NE': 'Niger', 'ST': 'Sao Tome and Principe', 
		'NP': 'Nepal', 'KY': 'Cayman Islands', 'VI': 'Virgin Islands, US', 'PM': 'Saint Pierre and Miquelon', 'KP': 'Korea (North)', 
		'GY': 'Guyana', 'BS': 'Bahamas', 'CY': 'Cyprus', 'CX': 'Christmas Island', 'AD': 'Andorra', 'RU': 'Russian Federation', 
		'VN': 'Vietnam', 'EE': 'Estonia', 'AE': 'United Arab Emirates', 'PR': 'Puerto Rico', 'LR': 'Liberia', 'GN': 'Guinea', 
		'SM': 'San Marino', 'GA': 'Gabon', 'UA': 'Ukraine', 'BH': 'Bahrain', 'AM': 'Armenia', 'BW': 'Botswana', 'PN': 'Pitcairn', 
		'AS': 'American Samoa', 'BV': 'Bouvet Island', 'HR': 'Croatia', 'IS': 'Iceland', 'PG': 'Papua New Guinea', 'SO': 'Somalia', 
		'CD': 'Congo, (Kinshasa)', 'TH': 'Thailand', 'CL': 'Chile', 'BD': 'Bangladesh', 'BL': 'Saint-Barthélemy', 
		'VE': 'Venezuela (Bolivarian Republic)', 'BG': 'Bulgaria', 'RS': 'Serbia', 'GS': 'South Georgia and the South Sandwich Islands', 
		'HK': 'Hong Kong, SAR China', 'CC': 'Cocos (Keeling) Islands', 'AU': 'Australia', 'LS': 'Lesotho', 'GL': 'Greenland', 
		'TR': 'Turkey', 'KZ': 'Kazakhstan', 'BN': 'Brunei Darussalam', 'NA': 'Namibia', 'IL': 'Israel', 'TK': 'Tokelau', 
		'BB': 'Barbados', 'SY': 'Syrian Arab Republic (Syria)', 'LI': 'Liechtenstein', 'KH': 'Cambodia', 'HM': 'Heard and Mcdonald Islands', 
		'BZ': 'Belize', 'YT': 'Mayotte', 'CO': 'Colombia', 'IQ': 'Iraq', 'HT': 'Haiti', 'PH': 'Philippines', 'PY': 'Paraguay', 
		'TM': 'Turkmenistan', 'AR': 'Argentina', 'TF': 'French Southern Territories', 'MG': 'Madagascar', 'CR': 'Costa Rica', 
		'GR': 'Greece', 'KM': 'Comoros', 'VG': 'British Virgin Islands', 'ES': 'Spain', 'GI': 'Gibraltar', 'BA': 'Bosnia and Herzegovina', 
		'MZ': 'Mozambique', 'FR': 'France', 'TT': 'Trinidad and Tobago', 'TJ': 'Tajikistan', 'VC': 'Saint Vincent and Grenadines', 
		'FM': 'Micronesia, Federated States of', 'RO': 'Romania', 'AF': 'Afghanistan', 'GH': 'Ghana', 'LB': 'Lebanon', 'NZ': 'New Zealand', 
		'SS': 'South Sudan', 'SE': 'Sweden', 'TV': 'Tuvalu', 'ME': 'Montenegro', 'BI': 'Burundi', 'SI': 'Slovenia', 'Aland Islands': 'ALA', 
		'KI': 'Kiribati', 'SH': 'Saint Helena', 'OM': 'Oman', 'TL': 'Timor-Leste', 'CZ': 'Czech Republic', 'GW': 'Guinea-Bissau', 
		'SD': 'Sudan', 'SV': 'El Salvador', 'TW': 'Taiwan, Republic of China', 'TG': 'Togo', 'BM': 'Bermuda', 'YE': 'Yemen', 
		'TC': 'Turks and Caicos Islands', 'IM': 'Isle of Man', 'KE': 'Kenya', 'MS': 'Montserrat', 'WS': 'Samoa', 'MW': 'Malawi', 
		'SA': 'Saudi Arabia', 'SG': 'Singapore', 'LU': 'Luxembourg', 'MH': 'Marshall Islands', 'UM': 'US Minor Outlying Islands', 
		'IN': 'India', 'AO': 'Angola', 'WF': 'Wallis and Futuna Islands', 'SR': 'Suriname', 'VA': 'Holy See (Vatican City State)', 
		'SL': 'Sierra Leone', 'FK': 'Falkland Islands (Malvinas)', 'MK': 'Macedonia, Republic of', 'PW': 'Palau', 'IR': 'Iran, Islamic Republic of', 
		'CA': 'Canada', 'MT': 'Malta', 'CK': 'Cook Islands', 'CI': "Côte d'Ivoire", 'PL': 'Poland', 'AG': 'Antigua and Barbuda', 
		'CH': 'Switzerland', 'LV': 'Latvia', 'GF': 'French Guiana', 'AL': 'Albania'
	}

	try:
		res = cabb[country_abb]
	except:
		res = country_abb

	return res

def country_abb_map(country):
	"""
		Maps country name to country abbreviation (alpha-2).
	"""

	cabb = {
		'Libya': 'LY', 'Morocco': 'MA', 'Indonesia': 'ID', "Côte d'Ivoire": 'CI', 'Cape Verde': 'CV', 'Kazakhstan': 'KZ', 
		'Anguilla': 'AI', 'American Samoa': 'AS', 'Brunei Darussalam': 'BN', 'British Indian Ocean Territory': 'IO', 'Comoros': 
		'KM', 'Eritrea': 'ER', 'Netherlands': 'NL', 'United Arab Emirates': 'AE', 'Austria': 'AT', 'Taiwan, Republic of China': 
		'TW', 'Western Sahara': 'EH', 'Togo': 'TG', 'Cambodia': 'KH', 'Norfolk Island': 'NF', 'Mauritania': 'MR', 
		'Marshall Islands': 'MH', 'Zimbabwe': 'ZW', 'Bangladesh': 'BD', 'Cyprus': 'CY', 'Moldova': 'MD', 'Denmark': 'DK', 
		'Northern Mariana Islands': 'MP', 'Norway': 'NO', 'Tuvalu': 'TV', 'Costa Rica': 'CR', 'Sri Lanka': 'LK', 'Ireland': 'IE', 
		'Monaco': 'MC', 'Iceland': 'IS', 'Belize': 'BZ', 'Guernsey': 'GG', 'Czech Republic': 'CZ', 'Tokelau': 'TK', 'Slovakia': 'SK', 
		'France': 'FR', 'Slovenia': 'SI', 'Paraguay': 'PY', 'British Virgin Islands': 'VG', 'Kuwait': 'KW', 'Luxembourg': 'LU', 
		'Dominican Republic': 'DO', 'Bosnia and Herzegovina': 'BA', 'Malawi': 'MW', 'Latvia': 'LV', 'Sao Tome and Principe': 'ST', 
		'Belgium': 'BE', 'Italy': 'IT', 'Angola': 'AO', 'Cocos (Keeling) Islands': 'CC', 'Andorra': 'AD', 'Namibia': 'NA', 
		'French Southern Territories': 'TF', 'Spain': 'ES', 'Syrian Arab Republic (Syria)': 'SY', 'Venezuela (Bolivarian Republic)': 'VE', 
		'Lao PDR': 'LA', 'US Minor Outlying Islands': 'UM', 'Algeria': 'DZ', 'Saint-Martin (French part)': 'MF', 'Kyrgyzstan': 'KG', 
		'Tonga': 'TO', 'Somalia': 'SO', 'Guam': 'GU', 'French Polynesia': 'PF', 'Korea (South)': 'KR', 'Lithuania': 'LT', 'Croatia': 'HR', 
		'Jersey': 'JE', 'United Kingdom': 'GB', 'Armenia': 'AM', 'Tajikistan': 'TJ', 'Tunisia': 'TN', 'Grenada': 'GD', 'Panama': 'PA', 
		'Guatemala': 'GT', 'Haiti': 'HT', 'Jordan': 'JO', 'Greenland': 'GL', 'Isle of Man': 'IM', 'New Caledonia': 'NC', 'Dominica': 'DM', 
		'Iran, Islamic Republic of': 'IR', 'Canada': 'CA', 'El Salvador': 'SV', 'Hungary': 'HU', 'Azerbaijan': 'AZ', 'Kiribati': 'KI', 
		'Faroe Islands': 'FO', 'Burkina Faso': 'BF', 'Russian Federation': 'RU', 'Liberia': 'LR', 'Congo (Brazzaville)': 'CG', 
		'Equatorial Guinea': 'GQ', 'Israel': 'IL', 'Germany': 'DE', 'Lebanon': 'LB', 'Kenya': 'KE', 'Benin': 'BJ', 'Thailand': 'TH', 
		'Switzerland': 'CH', 'Ecuador': 'EC', 'Pitcairn': 'PN', 'South Sudan': 'SS', 'Nepal': 'NP', 'Christmas Island': 'CX', 
		'Martinique': 'MQ', 'Macao, SAR China': 'MO', 'Vietnam': 'VN', 'Solomon Islands': 'SB', 'Nauru': 'NR', 'Bulgaria': 'BG', 
		'Myanmar': 'MM', 'Saint-Barthélemy': 'BL', 'Niue': 'NU', 'Saudi Arabia': 'SA', 'Singapore': 'SG', 
		'South Georgia and the South Sandwich Islands': 'GS', 'Oman': 'OM', 'Antigua and Barbuda': 'AG', 'Nigeria': 'NG', 
		'Holy See (Vatican City State)': 'VA', 'Belarus': 'BY', 'Guyana': 'GY', 'Zambia': 'ZM', 'Swaziland': 'SZ', 'Serbia': 'RS', 
		'Pakistan': 'PK', 'Poland': 'PL', 'Montserrat': 'MS', 'Falkland Islands (Malvinas)': 'FK', 'Liechtenstein': 'LI', 
		'Ukraine': 'UA', 'Finland': 'FI', 'Saint Helena': 'SH', 'Bhutan': 'BT', 'Timor-Leste': 'TL', 'Barbados': 'BB', 
		'Afghanistan': 'AF', 'Brazil': 'BR', 'Hong Kong, SAR China': 'HK', 'Micronesia, Federated States of': 'FM', 'Ghana': 'GH', 
		'Central African Republic': 'CF', 'Iraq': 'IQ', 'Trinidad and Tobago': 'TT', 'Suriname': 'SR', 'Albania': 'AL', 'Japan': 'JP', 
		'Estonia': 'EE', 'Uganda': 'UG', 'Cuba': 'CU', 'Samoa': 'WS', 'Peru': 'PE', 'Philippines': 'PH', 'Mongolia': 'MN', 
		'Portugal': 'PT', 'Honduras': 'HN', 'Montenegro': 'ME', 'Korea (North)': 'KP', 'Gambia': 'GM', 'Qatar': 'QA', 
		'Uruguay': 'UY', 'Madagascar': 'MG', 'Puerto Rico': 'PR', 'Palau': 'PW', 'Palestinian Territory': 'PS', 'Malta': 'MT', 
		'Uzbekistan': 'UZ', 'Georgia': 'GE', 'Lesotho': 'LS', 'Congo, (Kinshasa)': 'CD', 'Saint Pierre and Miquelon': 'PM', 'Gabon': 'GA', 
		'Guinea': 'GN', 'Rwanda': 'RW', 'Cayman Islands': 'KY', 'Netherlands Antilles': 'AN', 'Heard and Mcdonald Islands': 'HM', 
		'Sweden': 'SE', 'Sudan': 'SD', 'ALA': 'Aland Islands', 'United States of America': 'US', 'India': 'IN', 'Bahamas': 'BS', 
		'New Zealand': 'NZ', 'Malaysia': 'MY', 'Saint Kitts and Nevis': 'KN', 'South Africa': 'ZA', 'Mayotte': 'YT', 'Mauritius': 'MU', 
		'Argentina': 'AR', 'Egypt': 'EG', 'Djibouti': 'DJ', 'San Marino': 'SM', 'Turks and Caicos Islands': 'TC', 'Chad': 'TD', 
		'Burundi': 'BI', 'Ethiopia': 'ET', 'Mozambique': 'MZ', 'Gibraltar': 'GI', 'Seychelles': 'SC', 'Senegal': 'SN', 'Australia': 'AU', 
		'Mexico': 'MX', 'Niger': 'NE', 'Antarctica': 'AQ', 'Maldives': 'MV', 'Greece': 'GR', 'China': 'CN', 'Tanzania, United Republic of': 'TZ', 
		'Saint Vincent and Grenadines': 'VC', 'Jamaica': 'JM', 'Aruba': 'AW', 'Turkey': 'TR', 'Botswana': 'BW', 'Guadeloupe': 'GP', 
		'Svalbard and Jan Mayen Islands': 'SJ', 'Wallis and Futuna Islands': 'WF', 'Virgin Islands, US': 'VI', 'Bolivia': 'BO', 
		'Yemen': 'YE', 'Vanuatu': 'VU', 'French Guiana': 'GF', 'Colombia': 'CO', 'Nicaragua': 'NI', 'Bahrain': 'BH', 
		'Macedonia, Republic of': 'MK', 'Cameroon': 'CM', 'Sierra Leone': 'SL', 'Romania': 'RO', 'Fiji': 'FJ', 'Cook Islands': 'CK', 
		'Bouvet Island': 'BV', 'Turkmenistan': 'TM', 'Papua New Guinea': 'PG', 'Saint Lucia': 'LC', 'Mali': 'ML', 'Chile': 'CL', 
		'Guinea-Bissau': 'GW', 'Bermuda': 'BM', 'Réunion': 'RE'
	}

	try:
		res = cabb[country]
	except:
		res = country

	return res

def abb_country_map_3(country_abb):
	"""
		Maps country abbreviation (alpha-3) to name of country.
	"""

	cabb = {
		'SJM': 'Svalbard and Jan Mayen Islands', 'AFG': 'Afghanistan', 'DMA': 'Dominica', 
		'BLR': 'Belarus', 'GIB': 'Gibraltar', 'GHA': 'Ghana', 'MHL': 'Marshall Islands', 'MCO': 'Monaco', 
		'GEO': 'Georgia', 'BHS': 'Bahamas', 'COG': 'Congo (Brazzaville)', 'MMR': 'Myanmar', 'BFA': 'Burkina Faso', 
		'CRI': 'Costa Rica', 'TUR': 'Turkey', 'GAB': 'Gabon', 'SHN': 'Saint Helena', 'BDI': 'Burundi', 
		'PRT': 'Portugal', 'FRA': 'France', 'BMU': 'Bermuda', 'SGS': 'South Georgia and the South Sandwich Islands', 
		'PNG': 'Papua New Guinea', 'IRL': 'Ireland', 'CHN': 'China', 'UGA': 'Uganda', 'USA': 'United States of America', 
		'MDA': 'Moldova', 'KEN': 'Kenya', 'ISL': 'Iceland', 'PRI': 'Puerto Rico', 'SAU': 'Saudi Arabia', 'COM': 'Comoros', 
		'GRL': 'Greenland', 'AUT': 'Austria', 'MAC': 'Macao, SAR China', 'BEL': 'Belgium', 'CUB': 'Cuba', 
		'CAF': 'Central African Republic', 'ARE': 'United Arab Emirates', 'DNK': 'Denmark', 'BWA': 'Botswana', 
		'NOR': 'Norway', 'FJI': 'Fiji', 'KHM': 'Cambodia', 'ATG': 'Antigua and Barbuda', 'ECU': 'Ecuador', 'TTO': 'Trinidad and Tobago', 
		'AIA': 'Anguilla', 'RUS': 'Russian Federation', 'NIU': 'Niue', 'KAZ': 'Kazakhstan', 'GNQ': 'Equatorial Guinea', 
		'ARG': 'Argentina', 'SLV': 'El Salvador', 'VUT': 'Vanuatu', 'LKA': 'Sri Lanka', 'CIV': "Côte d'Ivoire", 'BGR': 'Bulgaria', 
		'VEN': 'Venezuela (Bolivarian Republic)', 'GRC': 'Greece', 'BRN': 'Brunei Darussalam', 'CAN': 'Canada', 
		'THA': 'Thailand', 'PSE': 'Palestinian Territory', 'COL': 'Colombia', 'TKM': 'Turkmenistan', 'NLD': 'Netherlands', 
		'LSO': 'Lesotho', 'KIR': 'Kiribati', 'LBY': 'Libya', 'ARM': 'Armenia', 'GRD': 'Grenada', 'HMD': 'Heard and Mcdonald Islands', 
		'DJI': 'Djibouti', 'LAO': 'Lao PDR', 'PCN': 'Pitcairn', 'BIH': 'Bosnia and Herzegovina', 'SUR': 'Suriname', 'FRO': 'Faroe Islands', 
		'TLS': 'Timor-Leste', 'JEY': 'Jersey', 'BEN': 'Benin', 'LUX': 'Luxembourg', 'KWT': 'Kuwait', 'ATA': 'Antarctica', 
		'SLE': 'Sierra Leone', 'ROU': 'Romania', 'SSD': 'South Sudan', 'PHL': 'Philippines', 'CHL': 'Chile', 'PRK': 'Korea (North)', 
		'ISR': 'Israel', 'GUM': 'Guam', 'MEX': 'Mexico', 'BGD': 'Bangladesh', 'TCD': 'Chad', 'AND': 'Andorra', 'SVK': 'Slovakia', 
		'MRT': 'Mauritania', 'GNB': 'Guinea-Bissau', 'JOR': 'Jordan', 'SDN': 'Sudan', 'MNE': 'Montenegro', 'LVA': 'Latvia', 
		'NCL': 'New Caledonia', 'HND': 'Honduras', 'EGY': 'Egypt', 'NGA': 'Nigeria', 'POL': 'Poland', 'GTM': 'Guatemala', 'REU': 'Réunion', 
		'CCK': 'Cocos (Keeling) Islands', 'HKG': 'Hong Kong, SAR China', 'UMI': 'US Minor Outlying Islands', 'ZAF': 'South Africa', 
		'CPV': 'Cape Verde', 'PLW': 'Palau', 'IRQ': 'Iraq', 'UZB': 'Uzbekistan', 'MLT': 'Malta', 'KGZ': 'Kyrgyzstan', 'IDN': 'Indonesia', 
		'SWE': 'Sweden', 'NAM': 'Namibia', 'AZE': 'Azerbaijan', 'BHR': 'Bahrain', 'SWZ': 'Swaziland', 'BTN': 'Bhutan', 'GIN': 'Guinea', 
		'MNG': 'Mongolia', 'MNP': 'Northern Mariana Islands', 'CMR': 'Cameroon', 'MDG': 'Madagascar', 'MLI': 'Mali', 'PAN': 'Panama', 
		'TUN': 'Tunisia', 'MWI': 'Malawi', 'NZL': 'New Zealand', 'VAT': 'Holy See (Vatican City State)', 'GMB': 'Gambia', 'ESP': 'Spain', 
		'ETH': 'Ethiopia', 'LIE': 'Liechtenstein', 'IOT': 'British Indian Ocean Territory', 'AX': 'ALA', 'SYR': 'Syrian Arab Republic (Syria)', 
		'IMN': 'Isle of Man', 'HTI': 'Haiti', 'COK': 'Cook Islands', 'URY': 'Uruguay', 'YEM': 'Yemen', 'LBN': 'Lebanon', 'RWA': 'Rwanda', 
		'MYT': 'Mayotte', 'BVT': 'Bouvet Island', 'IRN': 'Iran, Islamic Republic of', 'VCT': 'Saint Vincent and Grenadines', 
		'ZWE': 'Zimbabwe', 'TKL': 'Tokelau', 'KOR': 'Korea (South)', 'AUS': 'Australia', 'AGO': 'Angola', 'ASM': 'American Samoa', 
		'DOM': 'Dominican Republic', 'DZA': 'Algeria', 'MKD': 'Macedonia, Republic of', 'LTU': 'Lithuania', 'ZMB': 'Zambia', 
		'NPL': 'Nepal', 'LCA': 'Saint Lucia', 'SPM': 'Saint Pierre and Miquelon', 'ABW': 'Aruba', 'ERI': 'Eritrea', 'BRA': 'Brazil', 
		'MAR': 'Morocco', 'NIC': 'Nicaragua', 'HRV': 'Croatia', 'FIN': 'Finland', 'OMN': 'Oman', 'PRY': 'Paraguay', 'MTQ': 'Martinique', 
		'GLP': 'Guadeloupe', 'TON': 'Tonga', 'TWN': 'Taiwan, Republic of China', 'DEU': 'Germany', 'SGP': 'Singapore', 'PYF': 'French Polynesia', 
		'MOZ': 'Mozambique', 'JPN': 'Japan', 'GBR': 'United Kingdom', 'BLM': 'Saint-Barthélemy', 'JAM': 'Jamaica', 'HUN': 'Hungary', 
		'ANT': 'Netherlands Antilles', 'CXR': 'Christmas Island', 'UKR': 'Ukraine', 'SOM': 'Somalia', 'BOL': 'Bolivia', 'GUY': 'Guyana', 
		'SYC': 'Seychelles', 'NFK': 'Norfolk Island', 'GUF': 'French Guiana', 'ESH': 'Western Sahara', 'GGY': 'Guernsey', 
		'TZA': 'Tanzania, United Republic of', 'VNM': 'Vietnam', 'PER': 'Peru', 'SMR': 'San Marino', 'EST': 'Estonia', 'NRU': 'Nauru', 
		'MYS': 'Malaysia', 'LBR': 'Liberia', 'MDV': 'Maldives', 'VIR': 'Virgin Islands, US', 'QAT': 'Qatar', 'PAK': 'Pakistan', 
		'BRB': 'Barbados', 'SEN': 'Senegal', 'CYM': 'Cayman Islands', 'TGO': 'Togo', 'TCA': 'Turks and Caicos Islands', 'IND': 'India', 
		'FLK': 'Falkland Islands (Malvinas)', 'BLZ': 'Belize', 'VGB': 'British Virgin Islands', 'WSM': 'Samoa', 'MAF': 'Saint-Martin (French part)', 
		'KNA': 'Saint Kitts and Nevis', 'MSR': 'Montserrat', 'NER': 'Niger', 'MUS': 'Mauritius', 'TUV': 'Tuvalu', 
		'ATF': 'French Southern Territories', 'ALB': 'Albania', 'ITA': 'Italy', 'CZE': 'Czech Republic', 'SRB': 'Serbia', 
		'FSM': 'Micronesia, Federated States of', 'SLB': 'Solomon Islands', 'WLF': 'Wallis and Futuna Islands', 'STP': 'Sao Tome and Principe', 
		'CYP': 'Cyprus', 'COD': 'Congo, (Kinshasa)', 'CHE': 'Switzerland', 'SVN': 'Slovenia', 'TJK': 'Tajikistan'
	}

	try:
		res = cabb[country_abb]
	except:
		res = country_abb

	return res


def country_abb_map_3(country):
	"""
		Maps country name to country abbreviation (alpha-3).
	"""

	cabb = {
		'US Minor Outlying Islands': 'UMI', 'British Indian Ocean Territory': 'IOT', 'Timor-Leste': 'TLS', 
		'Armenia': 'ARM', 'Bosnia and Herzegovina': 'BIH', 'Azerbaijan': 'AZE', 'Bouvet Island': 'BVT', 
		'Wallis and Futuna Islands': 'WLF', 'Cuba': 'CUB', 'Georgia': 'GEO', 'Bulgaria': 'BGR', 'Bhutan': 'BTN', 
		'Russian Federation': 'RUS', 'Jamaica': 'JAM', 'Benin': 'BEN', 'Senegal': 'SEN', 'Peru': 'PER', 'Liberia': 'LBR', 
		'Saint Kitts and Nevis': 'KNA', 'Eritrea': 'ERI', 'Congo (Brazzaville)': 'COG', 'Denmark': 'DNK', 'Lebanon': 'LBN', 
		'Spain': 'ESP', 'Bermuda': 'BMU', 'Algeria': 'DZA', 'Ethiopia': 'ETH', 'Guadeloupe': 'GLP', 'Antarctica': 'ATA', 
		'Réunion': 'REU', 'Yemen': 'YEM', 'Jordan': 'JOR', 'Zimbabwe': 'ZWE', 'Hong Kong, SAR China': 'HKG', 'Uzbekistan': 'UZB', 
		'Serbia': 'SRB', 'Holy See (Vatican City State)': 'VAT', 'Austria': 'AUT', 'Iceland': 'ISL', 'Germany': 'DEU', 
		'Papua New Guinea': 'PNG', 'Libya': 'LBY', 'Liechtenstein': 'LIE', 'Nepal': 'NPL', 'San Marino': 'SMR', 'Nicaragua': 'NIC', 
		'Bahrain': 'BHR', 'Czech Republic': 'CZE', 'Jersey': 'JEY', 'Korea (North)': 'PRK', 'Saint-Martin (French part)': 'MAF', 
		'Slovenia': 'SVN', 'Saudi Arabia': 'SAU', 'Guernsey': 'GGY', 'Netherlands': 'NLD', 'India': 'IND', 'Central African Republic': 
		'CAF', 'Fiji': 'FJI', 'Ukraine': 'UKR', 'Tokelau': 'TKL', 'Sri Lanka': 'LKA', 'Ireland': 'IRL', 'Malawi': 'MWI', 
		'Thailand': 'THA', 'Vanuatu': 'VUT', 'Dominica': 'DMA', 'American Samoa': 'ASM', 'French Southern Territories': 'ATF', 
		'Heard and Mcdonald Islands': 'HMD', 'Trinidad and Tobago': 'TTO', 'Chad': 'TCD', 'Montenegro': 'MNE', 'Finland': 'FIN', 
		'Ecuador': 'ECU', 'Mexico': 'MEX', 'Philippines': 'PHL', 'Mongolia': 'MNG', 'Portugal': 'PRT', 'Mayotte': 'MYT', 'Afghanistan': 'AFG', 
		'Falkland Islands (Malvinas)': 'FLK', 'Montserrat': 'MSR', 'Lao PDR': 'LAO', 'Kenya': 'KEN', 'Cyprus': 'CYP', 
		'Macao, SAR China': 'MAC', 'Tajikistan': 'TJK', 'Qatar': 'QAT', 'Niger': 'NER', 'Italy': 'ITA', 'New Zealand': 'NZL', 
		'Guatemala': 'GTM', 'Uruguay': 'URY', 'Mauritius': 'MUS', 'Guinea': 'GIN', 'Puerto Rico': 'PRI', 'French Polynesia': 'PYF', 
		'Pakistan': 'PAK', 'Sierra Leone': 'SLE', 'Samoa': 'WSM', 'Mali': 'MLI', 'Tanzania, United Republic of': 'TZA', 
		'Saint Pierre and Miquelon': 'SPM', 'Mauritania': 'MRT', 'Lithuania': 'LTU', 'Costa Rica': 'CRI', 'Angola': 'AGO', 
		'Greenland': 'GRL', 'Panama': 'PAN', 'Maldives': 'MDV', 'Palestinian Territory': 'PSE', 'Tunisia': 'TUN', 'Poland': 'POL', 
		'Togo': 'TGO', 'Romania': 'ROU', 'Nigeria': 'NGA', 'Tonga': 'TON', 'Botswana': 'BWA', 'Singapore': 'SGP', 'Antigua and Barbuda': 'ATG', 
		'Gabon': 'GAB', 'Seychelles': 'SYC', 'Brazil': 'BRA', 'Korea (South)': 'KOR', 'Gambia': 'GMB', 'Paraguay': 'PRY', 
		'Vietnam': 'VNM', 'Saint Vincent and Grenadines': 'VCT', 'Brunei Darussalam': 'BRN', 'Svalbard and Jan Mayen Islands': 'SJM', 
		'Chile': 'CHL', 'Belarus': 'BLR', 'Colombia': 'COL', 'British Virgin Islands': 'VGB', 'South Africa': 'ZAF', 'Andorra': 'AND', 
		'Monaco': 'MCO', 'Haiti': 'HTI', 'Sweden': 'SWE', 'Cambodia': 'KHM', 'Faroe Islands': 'FRO', 'Swaziland': 'SWZ', 'Belize': 'BLZ', 
		'ALA': 'AX', 'Luxembourg': 'LUX', 'Guam': 'GUM', 'Pitcairn': 'PCN', 'Rwanda': 'RWA', 'Ghana': 'GHA', 'Canada': 'CAN', 
		'Sudan': 'SDN', 'Cape Verde': 'CPV', 'Kiribati': 'KIR', 'Syrian Arab Republic (Syria)': 'SYR', 'Congo, (Kinshasa)': 'COD', 
		'Indonesia': 'IDN', 'Micronesia, Federated States of': 'FSM', 'Iraq': 'IRQ', 'Djibouti': 'DJI', 'Virgin Islands, US': 'VIR', 
		'Norfolk Island': 'NFK', 'Comoros': 'COM', 'Venezuela (Bolivarian Republic)': 'VEN', 'Tuvalu': 'TUV', 'Cayman Islands': 'CYM', 
		'Uganda': 'UGA', 'Kyrgyzstan': 'KGZ', 'Japan': 'JPN', 'Christmas Island': 'CXR', 'Switzerland': 'CHE', 'Isle of Man': 'IMN', 
		'Barbados': 'BRB', 'Saint-Barthélemy': 'BLM', 'Nauru': 'NRU', 'Oman': 'OMN', 'South Georgia and the South Sandwich Islands': 'SGS', 
		'Croatia': 'HRV', 'Zambia': 'ZMB', 'Australia': 'AUS', 'United Arab Emirates': 'ARE', 'Turkey': 'TUR', 'Myanmar': 'MMR', 
		'Netherlands Antilles': 'ANT', 'Malaysia': 'MYS', 'United Kingdom': 'GBR', 'Belgium': 'BEL', 'French Guiana': 'GUF', 'Albania': 
		'ALB', 'Western Sahara': 'ESH', 'Morocco': 'MAR', 'Bolivia': 'BOL', 'Turkmenistan': 'TKM', 'Latvia': 'LVA', 'Cook Islands': 'COK', 
		'Slovakia': 'SVK', 'Burundi': 'BDI', 'Bahamas': 'BHS', 'Grenada': 'GRD', 'Kazakhstan': 'KAZ', 'Hungary': 'HUN', 'Niue': 'NIU', 
		'Sao Tome and Principe': 'STP', 'Bangladesh': 'BGD', 'Burkina Faso': 'BFA', 'Mozambique': 'MOZ', 'United States of America': 'USA', 
		'Macedonia, Republic of': 'MKD', 'Malta': 'MLT', 'El Salvador': 'SLV', "Côte d'Ivoire": 'CIV', 'Estonia': 'EST', 'Lesotho': 'LSO', 
		'Solomon Islands': 'SLB', 'Taiwan, Republic of China': 'TWN', 'Palau': 'PLW', 'Equatorial Guinea': 'GNQ', 'China': 'CHN', 
		'Somalia': 'SOM', 'Saint Lucia': 'LCA', 'Aruba': 'ABW', 'Saint Helena': 'SHN', 'Norway': 'NOR', 'Kuwait': 'KWT', 'Argentina': 'ARG', 
		'Greece': 'GRC', 'New Caledonia': 'NCL', 'Honduras': 'HND', 'Marshall Islands': 'MHL', 'Gibraltar': 'GIB', 'Martinique': 'MTQ', 
		'France': 'FRA', 'Israel': 'ISR', 'Moldova': 'MDA', 'Northern Mariana Islands': 'MNP', 'Egypt': 'EGY', 'Namibia': 'NAM', 
		'Guinea-Bissau': 'GNB', 'Iran, Islamic Republic of': 'IRN', 'Cameroon': 'CMR', 'Suriname': 'SUR', 'South Sudan': 'SSD', 
		'Anguilla': 'AIA', 'Dominican Republic': 'DOM', 'Madagascar': 'MDG', 'Cocos (Keeling) Islands': 'CCK', 'Guyana': 'GUY', 
		'Turks and Caicos Islands': 'TCA'
	}


	try:
		res = cabb[country]
	except:
		res = country

	return res
