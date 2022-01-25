from django.db import models

from core.models.base import BaseModel


class CweModel(BaseModel):
    cwe_id = models.CharField(max_length=16, blank=False, db_index=True)
    name = models.CharField(max_length=256)
    description = models.TextField()

    class Meta:
        db_table = "opencve_cwes"

    @property
    def short_id(self):
        if not self.cwe_id.startswith("CWE-"):
            return None
        return self.cwe_id.split("CWE-")[1]

    def __str__(self):
        return "<Cwe {}>".format(self.cwe_id)
