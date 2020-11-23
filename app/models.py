from django.db import models


class CommonMixin(models.Model):
    src = models.CharField(max_length=255)
    date = models.DateField()
    country_or_region = models.CharField(max_length=255, blank=True)
    province_or_state = models.CharField(max_length=255, blank=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=6)
    longitude = models.DecimalField(max_digits=15, decimal_places=6)
    active = models.IntegerField(null=True)
    confirmed = models.IntegerField(null=True)
    deaths = models.IntegerField(null=True)
    recovered = models.IntegerField(null=True)
    timestamp = models.DateTimeField(null=True, editable=False)
    inserted_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    class Meta:
        abstract = True


class DailyData(CommonMixin):
    county = models.CharField(max_length=127)
    incidence_rate = models.DecimalField(max_digits=15, decimal_places=6)
    case_fatality_ratio = models.DecimalField(max_digits=15, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'daily_data'


class DailyUSData(CommonMixin):
    uid = models.CharField(max_length=255)
    people_tested = models.IntegerField(null=True)
    people_hospitalized = models.IntegerField(null=True)
    incident_rate = models.DecimalField(max_digits=15, decimal_places=6)
    testing_rate = models.DecimalField(max_digits=15, decimal_places=6)
    hospitalization_rate = models.DecimalField(max_digits=15, decimal_places=6)
    mortality_rate = models.DecimalField(max_digits=15, decimal_places=6)
    total_test_results = models.DecimalField(max_digits=15, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'daily_data_us'
