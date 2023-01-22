from django.contrib.auth import get_user_model
from django.db.models import Model, CharField, TextField, IntegerField, ImageField, ForeignKey, DateField, CASCADE
from parler.models import TranslatableModel, TranslatedFields

from django.utils.translation import gettext_lazy as _


User = get_user_model()
class BaseModel(Model):
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)

    class Meta:
        abstract = True


class Blog(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        tag=CharField(_("Tag"), max_length=56),
        title=CharField(_("Title"), max_length=128),
        decription=TextField(_("Description")),
        author=ForeignKey(User, on_delete=CASCADE)
    )
    likes = IntegerField(default=33)
    photo = ImageField(verbose_name= "Photo", upload_to="blogs/")

    class Meta:
        db_table = "blog"


class Service(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        title=CharField(_("Title"), max_length=200),
        description=TextField(_("Description")),
        price=IntegerField(_("Price")),
        domain=CharField(_("Domain"), max_length=56),
        disk=CharField(_("Disk Space"), max_length=56),
        email=CharField(_("Email"), max_length=56),
        monthly=CharField(_("Monthly"), max_length=56),
        admin_panel=CharField(_("Admin Panel"), max_length=56),
    )

    class Meta:
        db_table = "service"
