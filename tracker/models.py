from django.db import models

# Create your models here.
class BaseGearModel(models.Model):
    gear_score = models.PositiveSmallIntegerField()


class ClassyGearSet(models.Model):
    CHEST = 'CH'
    MASK = 'MA'
    KNEES = 'KN'
    BACKPACK = 'BP'
    GLOVES = 'GL'
    HOLSTER = 'HO'
    ALPHA_BRIDGE = 'AB'
    BANSHEE = 'BS'
    D3 = 'D3'
    DEADEYE = 'DE'
    FIRECREST = 'FC'
    FINAL_MEASURE = 'FM'
    HUNTERS = 'HF'
    LONESTAR = 'LS'
    NOMAD = 'NO'
    PREDATORS = 'PM'
    RECLAIMER = 'RE'
    SENTRY = 'SC'
    STRIKER = 'ST'
    TACTICIANS = 'TA'
    GEAR_SET_CHOICES = (
        (ALPHA_BRIDGE, 'Alpha Bridge'),
        (BANSHEE, 'Banshee\'s Shadow'),
        (D3, 'D3-FNC'),
        (DEADEYE, 'DeadEYE'),
        (FIRECREST, 'FireCrest'),
        (FINAL_MEASURE, 'Final Measure'),
        (HUNTERS, 'Hunter\'s Faith'),
        (LONESTAR, 'Lone Star'),
        (NOMAD, 'Path of the Nomad'),
        (PREDATORS, 'Predator\'s Mark'),
        (RECLAIMER, 'Reclaimer'),
        (SENTRY, 'Sentry\'s Call'),
        (STRIKER, 'Striker\'s Battlegear'),
        (TACTICIANS, 'Tactician\'s Authority'),
    )
    SLOT_CHOICES = (
        (CHEST, 'Chest'),
        (MASK, 'Mask'),
        (KNEES, 'Knee Pads'),
        (BACKPACK, 'Backpack'),
        (GLOVES, 'Gloves'),
        (HOLSTER, 'Holster'),
    )
    gear_score = models.PositiveSmallIntegerField()
    gear_set = models.CharField(
        max_length=2,
        choices=GEAR_SET_CHOICES
    )
    slot = models.CharField(
        max_length=2,
        choices=SLOT_CHOICES
    )
