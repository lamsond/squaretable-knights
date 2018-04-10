'''
initial models.py for wcts_app
originally created by Thomas Sperduto
on Feb 23rd 2018
'''

from django.db import models
from django.core.validators import RegexValidator

'''
regex written by Andrew Flyte. Gives user the option of entering
numbers in any of the following formats:
1-908-123-4567
908-123-4567
19081234567
9081234567
'''
phone_regex = RegexValidator(
 regex=r'^\d{0,1}[\-]?\d{3}[\-]?\d{3}[\-]?\d{4}$',
 message="Phone number should be between 10 and 11 digits")

'''
date validation code written by Garrett Maurer 3/19/18
captures days per month and leap year logic
'''
def checkLeap(year):
    if(year % 4 == 0):
        return True

def dateValid(day, month, year):
    thirtyOneMonths = [1, 3, 5, 7, 9, 11]
    thirtyMonths = [4, 6, 8, 10, 12]
    if month in thirtyMonths:
        if(day < 31 and day > 0):
            return True
        else:
            return False
    elif month in thirtyOneMonths:
        if(day < 32 and day > 0):
            return True
        else:
            return False
    elif(month == 2):
        if(checkLeap(year)):
            return True
        else:
            return False
#career major options compiled by Thomas Sperduto
MAJORS = (
 ("AT","Automotive Technology"),
 ("BT","Building Technology"),
 ("BM","Business Management"),
 ("CD","Child Development"),
 ("CVP","Cinematography Video Production"),
 ("CP","Computer Programming"),
 ("C","Cosmetology"),
 ("ERC","Electrician Residential Commercial"),
 ("ET","Electronics Technology"),
 ("GAPM","Graphic Arts Printing Management"),
 ("GE","General Engineering"),
 ("HS","Health Science"),
 ("HMCA","Hospitality Management Culinary Arts"),
 ("LPSS","Law Public Safety Security"),
 )

#middle school options compiled by Ally McDonald and Thomas Sperduto on 3/2/18
SCHOOLS = (
 ("ATS","Allamuchy Township School"),
 ("AS","Alpha School"),
 ("OSES","Oxford Street Elementary School"),
 ("NWRHS","North Warren Regional High School"),
 ("WHRMS","Warren Hills Regional Middle School"),
 ("SS","Stewarstville School"),
 ("HMS","Hackettstown Middle School"),
 ("HTES","Harmony Township Elementary School"),
 ("HTS","Hope Township School"),
 ("GMRMS","Great Meadows Regional Middle School"),
 ("LTMS","Lopatcong Township Middle School"),
 ("PMS","Phillipsburg Middle School"),
 ("PALS","Phillipsburg Alternative Learning School"),
 ("WTCS","White Township Consolidated School"),
 ("RVCS","Ridge and Valley Charter School"),
 ("WCSSSD","Warren County Special Services School District"),
 ("O","Other")
 )

#warren county townships compiled by Ally McDonald and Thomas Sperduto on 3/15/18
TOWNSHIPS = (
  ("AT","Allamuchy Township"),
  ("AB","Alpha Borough"),
  ("TOB","Town of Belvidere"),
  ("BT","Blairstown Township"),
  ("FT_1","Franklin Township"),
  ("FT_2","Frelinghuysen Township"),
  ("GT","Greenwich Township"),
  ("H","Hackettstown"),
  ("HT_1","Hardwick Township"),
  ("HT_2","Harmony Township"),
  ("HT_3","Hope Township"),
  ("IT","Independence Township"),
  ("KT","Knowlton Township"),
  ("LT_1","Liberty Township"),
  ("LT_2","Lopatcong Township"),
  ("MT","Mansfield Township"),
  ("OT","Oxford Township"),
  ("TOP","Town of Phillipsburg"),
  ("PT","Pohatcong Township"),
  ("WB","Washington Borough"),
  ("WT_1","Washington Township"),
  ("WT_2","White Township"),
  ("O","Other"),
 )
 
#warren county cities and zips compiled by Ally McDonald
ZIPS = ("07820","07823","07825","07829","07831","07832","07833",
    "07838","07840","07844","07846","07863","07865","07880",
    "07882","08802","08808","08865","08886","Others")

CITIES = (
	("AL","Allamuchy"),
	("ALP","Alpha"),
	("AS","Asbury"),
	("BEL","Belvidere"),
	("BL","Blairstown"),
	("BR","Broadway"),
	("BU","Buttzville"),
	("CH","Changewater"),
	("CO","Columbia"),
	("DE","Delaware"),
	("GM","Great Meadows"),
	("HAC","Hackettstown"),
	("HAR","Hardwick"),
	("HO","Hope"),
	("JO","Johnsonburg"),
	("OX","Oxford"),
	("PH","Phillipsburg"),
	("PM","Port Murray"),
	("ST","Stewartsville"),
	("VI","Vienna"),
	("WA","Washington"),
	("O","Others")
)


#compiled by Omar Mohammed
STATES = (
    ('AK', 'Alaska'),
    ('AL', 'Alabama'),
    ('AR', 'Arkansas'),
    ('AS', 'American Samo'),
    ('AZ', 'Arizona'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DC', 'District of Columbia'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('GU', 'Guam'),
    ('HI', 'Hawaii'),
    ('IA', 'Iowa'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('MA', 'Massachusetts'),
    ('MD', 'Maryland'),
    ('ME', 'Maine'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MO', 'Missouri'),
    ('MP', 'Northern Mariana Islands'),
    ('MS', 'Mississippi'),
    ('MT', 'Montana'),
    ('NA', 'National'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('NE', 'Nebraska'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NV', 'Nevada'),
    ('NY', 'New York'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('PR', 'Puerto Rico'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VA', 'Virginia'),
    ('VI', 'Virgin Islands'),
    ('VT', 'Vermont'),
    ('WA', 'Washington'),
    ('WI', 'Wisconsin'),
    ('WV', 'West Virginia'),
    ('WY', 'Wyoming')
)
#Omar
MONTHS = (
    (1, "January"),
    (2, "February"),
    (3, "March"),
    (4, "April"),
    (5, "May"),
    (6, "June"),
    (7, "July"),
    (8, "August"),
    (9, "September"),
    (10, "October"),
    (11, "November"),
    (12, "December"),
)
#Omar
YEARS = (
   (2000, "2000"),
   (2001, "2001"),
   (2002, "2002"),
   (2003, "2003"),
   (2004, "2004"),
   (2005, "2005"),
)

class Applicant(models.Model):
    first_name = models.CharField(max_length = 100)
    middle_letter = models.CharField(max_length = 1, blank = True)#OM removed null=True to fix ValueError
    last_name = models.CharField(max_length = 100)
    birth_month = models.IntegerField(choices = MONTHS) #add choices
    birth_date = models.IntegerField()
    birth_year = models.IntegerField(choices = YEARS, default = "2004")
    mailing_address = models.CharField(max_length = 100)
    apartment_number = models.CharField(max_length = 5, blank = True)
    city = models.CharField(max_length = 100, choices = CITIES)
    state = models.CharField(max_length = 30, default='NJ', choices = STATES)#OM added default 3/5
    zip_code = models.CharField(max_length = 5)
    student_home_phone = models.CharField(validators=[phone_regex,], max_length = 100)
    township_municipality = models.CharField(max_length = 100, choices = TOWNSHIPS)
    parent_name_1 = models.CharField(max_length = 100)
    parent_cell_1 = models.CharField(validators=[phone_regex,],max_length = 11)
    parent_work_1 = models.CharField(validators=[phone_regex,],max_length = 11, blank = True)#OM removed null=True to fix ValueError
    parent_1_email = models.EmailField(max_length = 100)
    parent_name_2 = models.CharField(max_length = 100, blank = True)#JG
    parent_cell_2 = models.CharField(validators=[phone_regex,], max_length = 11, blank = True)
    parent_work_2 = models.CharField(validators=[phone_regex,], max_length = 11, blank = True)#OM removed null=True to fix ValueError
    parent_2_email = models.EmailField(max_length = 100, blank = True)
    parent_2_address = models.CharField(max_length = 100, blank = True)#OM removed null=True to fix ValueError
    parent_2_apartment_number = models.CharField(max_length = 5, blank = True)
    parent_2_city = models.CharField(max_length = 100, blank = True, choices = CITIES)
    parent_2_state = models.CharField(max_length = 100, blank = True, choices = STATES)
    parent_2_zip = models.CharField(max_length = 5, blank = True)
    school_presently_attending = models.CharField(max_length = 100, choices = SCHOOLS)
    guidance_counselor = models.CharField(max_length = 100)
    counselor_phone = models.CharField(validators=[phone_regex,] ,max_length = 11)
    choice_1 = models.CharField(max_length = 100, choices = MAJORS)
    choice_2 = models.CharField(max_length = 100, choices = MAJORS)
    choice_3 = models.CharField(max_length = 100, choices = MAJORS)

    def __str__(self):
  #Joey Greenleaf and Ian Dorman added logic to correctly format name without a middle initial 3/2/18
        if self.middle_letter == "":
            return self.first_name + " " + self.last_name

        elif self.middle_letter != "":
            return self.first_name + " " + self.middle_letter + ". " + self.last_name
            
#Parent model created by Thomas Sperduto 3/26/18
class Parent(models.Model):
    parent_name_1 = models.CharField(max_length = 100)
    parent_cell_1 = models.CharField(validators=[phone_regex,],max_length = 11)
    parent_work_1 = models.CharField(validators=[phone_regex,],max_length = 11, blank = True)#OM removed null=True to fix ValueError
    parent_1_email = models.EmailField(max_length = 100)
    parent_name_2 = models.CharField(max_length = 100, blank = True)#JG
    parent_cell_2 = models.CharField(validators=[phone_regex,], max_length = 11, blank = True)
    parent_work_2 = models.CharField(validators=[phone_regex,], max_length = 11, blank = True)#OM removed null=True to fix ValueError
    parent_2_email = models.EmailField(max_length = 100, blank = True)
    parent_2_address = models.CharField(max_length = 100, blank = True)#OM removed null=True to fix ValueError
    parent_2_apartment_number = models.CharField(max_length = 5, blank = True)
    parent_2_city = models.CharField(max_length = 100, blank = True, choices = CITIES)
    parent_2_state = models.CharField(max_length = 100, blank = True, choices = STATES)
    parent_2_zip = models.CharField(max_length = 5, blank = True)

