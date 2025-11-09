from django.db import models
from .Estado import Estado


class AutoConfirmado(Estado):
    """
    Estado concreto AutoConfirmado - Persiste en BD
    Hereda toda la funcionalidad de Estado sin sobreescribir métodos
    """
    
    class Meta:
        app_label = 'core'
        # No es abstracto, se creará una tabla en la BD
    
    def __str__(self):
        return f"Estado AutoConfirmado (ID: {self.id})"
