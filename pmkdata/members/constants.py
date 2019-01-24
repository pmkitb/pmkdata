MALE = 'male'
FEMALE = 'female'

GENDER_CHOICES = (
    (MALE, 'Laki-laki'),
    (FEMALE, 'Perempuan'),
)

MEMBER_ACTIVE = 'active'
MEMBER_GRADUATED = 'graduated'
MEMBER_DROPPED_OUT = 'dropped_out'
MEMBER_ON_LEAVE = 'on_leave'
MEMBER_TRANSFERRED = 'transferred'
MEMBER_DECEASED = 'deceased'

MEMBER_STATUS_CHOICES = (
    (MEMBER_ACTIVE, 'Aktif'),
    (MEMBER_GRADUATED, 'Lulus'),
    (MEMBER_DROPPED_OUT, 'DO'),
    (MEMBER_ON_LEAVE, 'Cuti'),
    (MEMBER_TRANSFERRED, 'Pindah'),
    (MEMBER_DECEASED, 'Meninggal'),
)
