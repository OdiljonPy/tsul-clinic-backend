from modeltranslation.translator import translator, TranslationOptions
from .models import DocumentCategory, DocumentType


class DocumentCategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


class DocumentTypeTranslationOptions(TranslationOptions):
    fields = ('document_name',)


translator.register(DocumentCategory, DocumentCategoryTranslationOptions)
translator.register(DocumentType, DocumentTypeTranslationOptions)
