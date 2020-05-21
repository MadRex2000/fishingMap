from django.db import models
from django.utils.translation import gettext_lazy as _

#setup models and can migrate to sqlite database 

class city(models.Model):
    CITY_CHOICES = (
        (_('KEL'), _('Keelung')),
        (_('NTPC'), _('New Taipei City')),
        (_('TPE'), _('Taipei')),
        (_('TYN'), _('Taoyuan')),
        (_('HSZ'), _('Hsinchu')),
        (_('ZMI'), _('Miaoli')),
        (_('TXG'), _('Taichung')),
        (_('CHW'), _('Changhua')),
        (_('NTC'), _('Nantou')),
        (_('YUN'), _('Yunlin')),
        (_('CYI'), _('Chiayi')),
        (_('TNN'), _('Tainan')),
        (_('KHH'), _('Kaohsiung')),
        (_('PIF'), _('Pingtung')),
        (_('ILA'), _('Yilan')),
        (_('HUN'), _('Hualien')),
        (_('TTT'), _('Taitung')),
        (_('PEH'), _('Penghu')),
        (_('GNI'), _('Green Island')),
        (_('KYD'), _('Orchid Island')),
        (_('KNH'), _('Kinmen')),
        (_('MFK'), _('Matsu')),
        (_('LNN'), _('Lienchiang'))
    )
    city = models.CharField(max_length = 4, verbose_name = 'City', choices = CITY_CHOICES)

    def __str__(self):
        return str(self.city)



class monthChoices(models.Model):
    MONTH_CHOICES = (
        (_('Jan'), _('January')),
        (_('Feb'), _('February')),
        (_('Mar'), _('March')),
        (_('Apr'), _('April')),
        (_('May'), _('May')),
        (_('Jun'), _('June')),
        (_('Jul'), _('July')),
        (_('Aug'), _('August')),
        (_('Sep'), _('September')),
        (_('Oct'), _('October')),
        (_('Nov'), _('November')),
        (_('Dec'), _('December'))
    )
    month = models.CharField(max_length = 3, verbose_name = 'Month', choices = MONTH_CHOICES)

    def __str__(self):
        return str(self.month)


class area(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(blank = True, max_length = 100)
    lat = models.FloatField(verbose_name = 'Latitude')
    lon = models.FloatField(verbose_name = 'Longitude')
    city = models.ForeignKey('city', related_name = 'area_city', verbose_name = '縣市', on_delete=models.CASCADE)
    district = models.CharField(blank = True, max_length = 100, verbose_name = '行政區')

    def __str__(self):
        return str(self.location)

class branches(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100, verbose_name = '科名')
    city = models.ManyToManyField('city', related_name = 'branches_city', verbose_name = '區域')
    month = models.ManyToManyField('monthChoices', verbose_name = '月份')

    def __str__(self):
        return str(self.name)

class fingerling(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100, verbose_name = '名稱')
    nickname = models.CharField(max_length = 100, verbose_name = '俗名')
    branch = models.ForeignKey('branches', related_name = 'fingerling_branch', verbose_name = '科別', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
