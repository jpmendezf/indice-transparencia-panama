from django.db import models
from autoslug import AutoSlugField


class Party(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Nombre")
    initials = models.CharField(max_length=255, verbose_name=u"Iniciales")
    slug = AutoSlugField(populate_from='name', null=True)

    def __str__(self):
        return self.initials


class EducationalRecord(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Nombre Programa")
    institution = models.CharField(max_length=255, verbose_name=u"Institución")
    start = models.CharField(max_length=255, verbose_name=u"Fecha de ingreso")
    end = models.CharField(max_length=255, verbose_name=u"Fecha de término")
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name="educational_records", null=True)


class WorkRecord(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Cargo")
    institution = models.CharField(max_length=255, verbose_name=u"Institución")
    start = models.CharField(max_length=255, verbose_name=u"Fecha de ingreso")
    end = models.CharField(max_length=255, verbose_name=u"Fecha de término")
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name="work_records", null=True)
    

class JudiciaryProcessRecord(models.Model):
    number = models.CharField(max_length=255, verbose_name=u"Número")
    date = models.DateField(max_length=255, verbose_name=u"Fecha")
    kind = models.CharField(max_length=255, verbose_name=u"Tipo")
    result = models.TextField(max_length=255, verbose_name=u"Fallo")
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name="judiciary_records", null=True)


class Benefit(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre del beneficio')

    def __str__(self):
        return self.name


TYPES_OF_PERSON = (('parlamentario', 'Parlamentario'), ('candidato', 'Candidato'), )


class Person(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Nombre Completo")
    specific_type = models.CharField(max_length=255,
                                     choices=TYPES_OF_PERSON,
                                     verbose_name=u"Tipo de persona",
                                     help_text=u"Parlamentario o candidato")
    birth_date = models.DateField(verbose_name=u"Fecha de nacimiento", null=True, blank=True)
    email = models.EmailField(verbose_name=u"Correo electrónico de contacto", null=True, blank=True)
    web = models.URLField(max_length=512, verbose_name=u"Link al sitio web personal (o cuenta oficial en redes sociales)", null=True, blank=True)
    declared_intention_to_transparent = models.BooleanField(default=False, verbose_name=u"¿Desea Ud. transparentar su información política general?", blank=True)
    party = models.ForeignKey(Party, null=True, on_delete=models.SET_NULL, related_name="persons", blank=True)
    circuit = models.CharField(max_length=255, verbose_name=u"Circuito al que representa o busca representar", null=True, blank=True)
    period = models.CharField(max_length=255, verbose_name=u"¿En qué período legislativo se encuentra actualmente?", null=True, blank=True)
    previous_parties = models.ManyToManyField(Party, related_name="ex_members", verbose_name=u"¿Ha pertenecido ud. a otros partidos o movimientos políticos?", blank=True)
    reelection = models.BooleanField(default=False, verbose_name=u"¿Va a reelección?", null=True, blank=True)

    extra_education = models.TextField(max_length=512,
                                       null=True,
                                       verbose_name=u"¿Desea transparentar alguna otra experiencia relevante de formación? Puede escribirlas a continuación", blank=True)
    intention_to_transparent_work_plan = models.BooleanField(default=False, verbose_name=u"¿Desea Ud. transparentar su plan de trabajo de diputado(a) o candidato(a)?", blank=True)

    work_plan_link = models.URLField(null=True, max_length=255, verbose_name=u"Si respondió 'sí', indique en qué link se puede acceder a su programa de trabajo", blank=True)
    work_plan_doc = models.FileField(upload_to='work_plans/%Y/%m/%d/',
                                     null=True,
                                     verbose_name=u"Si respondió 'sí' pero no tiene su plan de trabajo online, acá tiene la posibilidad de adjuntar el archivo", blank=True)
    intention_to_transparent_patrimony = models.BooleanField(default=False, null=True, verbose_name=u"¿Desea Ud. transparentar sus declaraciones de Patrimonio e Intereses", blank=True)
    patrimony_link = models.URLField(null=True,
                                     verbose_name=u"Si respondió 'sí' por favor indique a continuación el link para acceder a su declaración de patrimonio", blank=True)
    patrimony_doc = models.FileField(upload_to='patrimony/%Y/%m/%d/',
                                     null=True,
                                     verbose_name=u"Si respondió 'sí' pero no tiene su declaración de patrimonio publicada online, acá tiene la oportunidad de adjuntar el archivo", blank=True)

    existing_interests_declaration = models.BooleanField(default=False, null=True, verbose_name=u"¿Cuenta ud. con una declaración de intereses actualizada?", blank=True)
    interests_link = models.CharField(max_length=255, null=True,
                                      verbose_name=u"Si respondió 'sí' por favor indique a continuación el link para acceder a su declaración de Intereses", blank=True)
    interests_doc = models.FileField(upload_to='patrimony/%Y/%m/%d/',
                                     null=True,
                                     verbose_name=u"Si respondió 'sí' pero no tiene su declaración de intereses publicada online, acá tiene la oportunidad de adjuntar el archivo", blank=True)
    judiciary_declaration = models.BooleanField(default=False,
                                                verbose_name=u"¿Desea Ud. transparentar información sobre los procesos judiciales en los que ha estado involucrado(a)?", blank=True)

    extra_judiciary_declaration = models.TextField(max_length=255,null=True, verbose_name=u"¿Se ha visto involucrado en más procesos judiciales?", blank=True)
    judiciary_link = models.URLField(null=True, verbose_name=u"Si respondió 'sí', por favor indique dónde se puede acceder a esta información (facilite un link u otro recurso)", blank=True)
    judiciary_description = models.TextField(null=True, verbose_name=u"¿Desea agregar comentarios o notas aclaratorias sobre uno o más de los procesos judiciales declarados?", blank=True)
    reelection = models.BooleanField(default=False, verbose_name=u"¿Eres actualmente diputado/a?", blank=True)
    benefits = models.ManyToManyField(Benefit, blank=True)

    benefits_link = models.CharField(max_length=512,
                                     verbose_name=u"Por favor, indique dónde es posible acceder al detalle sobre los valores asociados al uso de beneficios (se le sugiere indicar un link donde esté publicado el detalle)",
                                     null=True, blank=True)

    eth_080_link = models.URLField(verbose_name=u"Indique en qué link es posible acceder al detalle de su planilla 080",
                                   help_text=u"Link a la planilla 080", null=True, blank=True)
    eth_172_link = models.URLField(verbose_name=u"Indique en qué link es posible acceder al detalle de su planilla 172",
                                   help_text=u"Link a la planilla 172", null=True, blank=True)
    eth_080_doc = models.FileField(upload_to='patrimony/%Y/%m/%d/',
                                  verbose_name=u"Si su planilla 080 no se encuentra publicada online, puede subir el archivo a continuación",
                                  help_text=u"Link a la planilla 080", null=True, blank=True)
    eth_172_doc = models.FileField(upload_to='patrimony/%Y/%m/%d/',
                                  verbose_name=u"Si su planilla 172 no se encuentra publicada online, puede subir el archivo a continuación",
                                  help_text=u"Link a la planilla 172", null=True, blank=True)

    def __str__(self):
        return self.name + " " + self.specific_type
