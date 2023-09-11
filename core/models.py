from django.db import models
from stdimage import StdImageField


class Base(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Cliente(Base):
    nome = models.CharField(max_length=70)
    endereco = models.CharField(max_length=150)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)

    class Meta:
        verbose_name= 'Cliente'
        verbose_name_plural= 'Clientes'

    def __str__(self):
        return self.nome


class Especie(Base):
    descricao = models.CharField(max_length=30)

    class Meta:
        verbose_name= 'Espécie'
        verbose_name_plural= 'Espécies'

    def __str__(self):
        return self.descricao


class Animal(Base):
    nome = models.CharField(max_length=70)
    idade = models.IntegerField(max_length=150)
    sexo = models.CharField(max_length=9, choices=[("M", "Masculino"),("F", "Feminino"),])
    foto = StdImageField(upload_to='animais',
                         variations={'thumb': {'width' : 600, 'height': 600, 'crop':True}})
    idEspecie = models.ForeignKey(Especie, models.SET_NULL, null=True, blank=True, verbose_name="Espécie")
    idCliente = models.ForeignKey(Cliente, models.SET_NULL, null=True, blank=True, verbose_name="Cliente")

    class Meta:
        verbose_name= 'Animal'
        verbose_name_plural= 'Animais'

    def __str__(self):
        return self.nome