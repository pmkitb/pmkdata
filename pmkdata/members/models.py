from django.db import models
from django.contrib.auth import get_user_model
from pmkdata.members import constants


User = get_user_model()


class Department(models.Model):
    code = models.CharField('singkatan', max_length=7)
    name = models.CharField('nama', max_length=255)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "fakultas"
        verbose_name_plural = "fakultas"


class Major(models.Model):
    department = models.ForeignKey(verbose_name='fakultas', to=Department,
                                   related_name='majors', on_delete=models.PROTECT)
    code = models.CharField('singkatan', max_length=7)
    name = models.CharField('nama', max_length=255)
    nim_prefix = models.IntegerField('awalan NIM')
    is_tpb = models.BooleanField('program TPB', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "program studi"
        verbose_name_plural = "program studi"


class Member(models.Model):
    user = models.OneToOneField(verbose_name='akun', to=User,
                                related_name='member', on_delete=models.CASCADE)
    nim = models.IntegerField('NIM')
    tpb_nim = models.IntegerField('NIM TPB', null=True)
    name = models.CharField('nama lengkap', max_length=255)
    nickname = models.CharField('nama panggilan', max_length=255)
    gender = models.CharField('jenis kelamin', max_length=7, choices=constants.GENDER_CHOICES)
    birth_date = models.DateField('tanggal lahir', null=True)
    major = models.ForeignKey(verbose_name='program studi', to=Major,
                              related_name='members', on_delete=models.PROTECT)
    year = models.IntegerField('angkatan')
    line = models.CharField('ID LINE', max_length=31, blank=True)
    phone = models.CharField('nomor telepon', max_length=31, blank=True)
    email = models.EmailField('email', blank=True)
    current_address = models.CharField('tempat tinggal di Bandung', max_length=1023, blank=True)
    origin_province = models.CharField('provinsi asal', max_length=255, blank=True)
    origin_address = models.CharField('kota/daerah asal', max_length=1023, blank=True)
    origin_school = models.CharField('sekolah asal', max_length=255, blank=True)
    current_church = models.CharField('gereja di Bandung', max_length=255, blank=True)
    origin_church = models.CharField('gereja asal', max_length=255, blank=True)
    status = models.CharField('status mahasiswa', max_length=31, choices=constants.MEMBER_STATUS_CHOICES, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "anggota"
        verbose_name_plural = "anggota"
