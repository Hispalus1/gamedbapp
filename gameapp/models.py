from django.db import models


class Firma(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Company name",
                            help_text='Enter a name of Company')
    Sidlo = models.CharField(max_length=100, help_text="Enter Company address", blank=True, null=True)

    class Meta:
        verbose_name = 'Firma'
        verbose_name_plural = 'Firmy'
        ordering = ['-name']

        def __str__(self):
            return self.name

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'zanr'
        verbose_name_plural = 'zanry'
        ordering = ['-name']

        def __str__(self):
            return self.name

    def __str__(self):
        return self.name


class Hodnoceni(models.Model):
    name = models.CharField(max_length=50, unique=True, )

    class Meta:
        verbose_name = 'Hodnoceni'
        verbose_name_plural = 'Hodnoceni'
        ordering = ['-name']

        def __str__(self):
            return self.name

    def __str__(self):
        return self.name


class Game(models.Model):
    HODNOCENI = [
        ("1", "VERY BAD"),
        ("2", "BAD"),
        ("3", "AVERAGE"),
        ("4", "GOOD"),
        ("5", "VERY GOOD"),
    ]

    ZANRY = [
        ("survival", "Survival"),
        ("strategy", "Strategy"),
        ("simulator", "Simulator"),
        ("adventure", "Adventure"),
        ("shooter", "Shooter"),
        ("rogue-like", "Rogue-like"),
        ("rpg", "RPG"),
        ("novel", "Novel"),
        ("moba", "MOBA"),
        ("mmorpg", "MMORPG"),
        ("horror", "Horror"),
        ("fps", "FPS"),
        ("action", "Action"),
        ("3d", "3D"),
        ("2d", "2D"),
    ]

    name = models.CharField(max_length=50, unique=True, verbose_name="Game name",
                            help_text='Enter a name of Game')
    popis = models.TextField(help_text="Enter description of the game", blank=True, null=True)
    zanr = models.ManyToManyField(Genres)
    hodnoceni = models.ManyToManyField(Hodnoceni)
    datum = models.DateField(blank=True, null=True, verbose_name='datum vydání')
    icon = models.ImageField(null=True, blank=True, verbose_name='Obrazek hry',
                             help_text='Nahrejte fotku¨¨')

    class Meta:
        verbose_name = 'Hra'
        verbose_name_plural = 'Hry'
        ordering = ['-name']

        def __str__(self):
            return self.name

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Developer name",
                            help_text='Enter a name of Developer')
    popis = models.TextField(help_text="Enter description of their work", blank=True, null=True)
    games = models.ManyToManyField(Game, null=True)
    icon = models.ImageField(null=True, blank=True, verbose_name='Icona Dev',
                             help_text='Nahrejte fotku')

    class Meta:
        verbose_name = 'Vyvojar'
        verbose_name_plural = 'Vyvojari'
        ordering = ['-name']

        def __str__(self):
            return self.name

    def __str__(self):
        return self.name


class Costumer(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Costumer name",
                            help_text='Enter a name of Costumer')
    profilovka = models.ImageField(upload_to='company', verbose_name='Fotografie')
    hry = models.ManyToManyField(Game)
    email = models.CharField(max_length=50, unique=True, verbose_name="Costumer email",
                             help_text='email', default="it2001@sspu-opava.cz")
    datum = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Zakaznik'
        verbose_name_plural = 'Zakaznici'
        ordering = ['-name']

        def __str__(self):
            return self.name

    def __str__(self):
        return self.name
