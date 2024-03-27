from django.contrib import admin
from flashcard.models import Flashcard, Categoria, FlashcardDesafio, Desafio

admin.site.register(Categoria)
admin.site.register(Flashcard)
admin.site.register(FlashcardDesafio)
admin.site.register(Desafio)
