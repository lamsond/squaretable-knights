from django.db import models

#career majors
class Major(models.Model):
    shop_name = models.CharField(max_length = 50)
    applicants = models.IntegerField(default = 0)

    def __str__(self):
        return self.shop_name

#student
class Student(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    middle_init = models.CharField(max_length = 1, blank=True)
    email = models.EmailField(max_length = 254)
    choice_one = models.ForeignKey(Major, on_delete=models.CASCADE)

    STATUS_CHOICES = (
            ('NS', 'Not Submitted'),
            ('RV', 'Under Review'),
            ('MI', 'Missing Information'),
            ('AA', 'Applicant Accepted'),
            ('AD', 'Applicant Declined'),
            )

    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='NS')
    def __str__(self):
        if self.middle_init != '':
            return self.first_name + " " + self.middle_init + ". " + self.last_name
        else:
            return self.first_name + " " + self.last_name
