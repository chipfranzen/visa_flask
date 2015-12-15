from wtforms.fields import SelectField
import string


class YesNoField(SelectField):
    def __init__(self, *args, **kwargs):
        super(YesNoField, self).__init__(*args, **kwargs)
        self.choices = [(1, 'Yes'), (0, 'No')]
        self.default = 0


class EducationField(SelectField):
    def __init__(self, *args, **kwargs):
        super(EducationField, self).__init__(*args, **kwargs)
        eds = ['Doctorate', 'Master\'s', 'Bachelor\'s', 'Associate\'s',
               'High School', 'None', 'Other']
        self.choices = [(name, name) for name in eds]


class CountryField(SelectField):
    def __init__(self, *args, **kwargs):
        super(CountryField, self).__init__(*args, **kwargs)
        countries = ['AFGHANISTAN', 'ALBANIA', 'ALGERIA', 'ANGOLA',
                     'ANTIGUA AND BARBUDA', 'ARGENTINA', 'ARMENIA',
                     'AUSTRALIA', 'AUSTRIA', 'AZERBAIJAN', 'BAHAMAS',
                     'BAHRAIN', 'BANGLADESH', 'BARBADOS', 'BELARUS', 'BELGIUM',
                     'BELIZE', 'BENIN', 'BERMUDA', 'BHUTAN', 'BOLIVIA',
                     'BOSNIA AND HERZEGOVINA', 'BOTSWANA', 'BRAZIL',
                     'BRITISH VIRGIN ISLANDS', 'BULGARIA', 'BURKINA FASO',
                     'BURMA (MYANMAR)', 'BURUNDI', 'CAMBODIA', 'CAMEROON',
                     'CANADA', 'CHILE', 'CHINA', 'COLOMBIA', 'COSTA RICA',
                     "COTE d'IVOIRE", 'CROATIA', 'CUBA', 'CYPRUS',
                     'CZECH REPUBLIC', 'DEMOCRATIC REPUBLIC OF CONGO',
                     'DENMARK', 'DOMINICA', 'DOMINICAN REPUBLIC', 'ECUADOR',
                     'EGYPT', 'EL SALVADOR', 'EQUATORIAL GUINEA', 'ERITREA',
                     'ESTONIA', 'ETHIOPIA', 'FIJI', 'FINLAND', 'FRANCE',
                     'GABON', 'GAMBIA', 'GEORGIA', 'GERMANY', 'GHANA',
                     'GREECE', 'GRENADA', 'GUATEMALA', 'GUINEA',
                     'GUINEA-BISSAU', 'GUYANA', 'HAITI', 'HONDURAS',
                     'HONG KONG', 'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA',
                     'IRAN', 'IRAQ', 'IRELAND', 'ISRAEL', 'ITALY',
                     'IVORY COAST', 'JAMAICA', 'JAPAN', 'JORDAN', 'KAZAKHSTAN',
                     'KENYA', 'KIRIBATI', 'KOSOVO', 'KUWAIT', 'KYRGYZSTAN',
                     'LAOS', 'LATVIA', 'LEBANON', 'LIBYA', 'LIECHTENSTEIN',
                     'LITHUANIA', 'LUXEMBOURG', 'MACAU', 'MACEDONIA',
                     'MADAGASCAR', 'MALAWI', 'MALAYSIA', 'MALDIVES', 'MALI',
                     'MARSHALL ISLANDS', 'MAURITANIA', 'MAURITIUS', 'MEXICO',
                     'MOLDOVA', 'MONGOLIA', 'MONTENEGRO', 'MOROCCO', 'NAMIBIA',
                     'NEPAL', 'NETHERLANDS', 'NETHERLANDS ANTILLES',
                     'NEW ZEALAND', 'NICARAGUA', 'NIGER', 'NIGERIA', 'NORWAY',
                     'PAKISTAN', 'PALESTINE', 'PALESTINIAN TERRITORIES',
                     'PANAMA', 'PARAGUAY', 'PERU', 'PHILIPPINES', 'POLAND',
                     'PORTUGAL', 'REPUBLIC OF CONGO', 'ROMANIA', 'RUSSIA',
                     'RWANDA', 'SAINT VINCENT AND THE GRENADINES', 'SAMOA',
                     'SAO TOME AND PRINCIPE', 'SAUDI ARABIA', 'SENEGAL',
                     'SERBIA', 'SERBIA AND MONTENEGRO', 'SEYCHELLES',
                     'SIERRA LEONE', 'SINGAPORE', 'SLOVAKIA', 'SLOVENIA',
                     'SOMALIA', 'SOUTH AFRICA', 'SOUTH KOREA', 'SOUTH SUDAN',
                     'SPAIN', 'SRI LANKA', 'ST KITTS AND NEVIS', 'ST LUCIA',
                     'ST VINCENT', 'SUDAN', 'SURINAME', 'SWEDEN',
                     'SWITZERLAND', 'SYRIA', 'TAIWAN', 'TAJIKISTAN',
                     'TANZANIA', 'THAILAND', 'TOGO', 'TRINIDAD AND TOBAGO',
                     'TUNISIA', 'TURKEY', 'TURKMENISTAN', 'UGANDA', 'UKRAINE',
                     'UNITED ARAB EMIRATES', 'UNITED KINGDOM',
                     'UNITED STATES OF AMERICA', 'URUGUAY', 'UZBEKISTAN',
                     'VENEZUELA', 'VIETNAM', 'YEMEN', 'YUGOSLAVIA', 'ZAMBIA',
                     'ZIMBABWE']
        self.choices = [(name, string.capwords(name)) for name in countries]


class VisaField(SelectField):
    def __init__(self, *args, **kwargs):
        super(VisaField, self).__init__(*args, **kwargs)
        visas = ['A-3', 'A1/A2', 'B-1', 'B-2', 'C-1', 'C-3', 'D-1', 'E-1',
                 'E-2', 'E-3', 'EWI', 'F-1', 'F-2', 'G-1', 'G-4', 'G-5',
                 'H-1A', 'H-1B', 'H-1B1', 'H-2A', 'H-2B', 'H-3', 'H-4', 'I',
                 'J-1', 'J-2', 'K-1', 'L-1', 'L-2', 'M-1', 'N', 'Not in USA',
                 'O-1', 'O-2', 'O-3', 'P-1', 'P-3', 'P-4', 'Parolee', 'Q',
                 'R-1', 'R-2', 'TD', 'TN', 'TPS', 'V-2', 'VWB', 'VWT']
        self.choices = [(name, name) for name in visas]







