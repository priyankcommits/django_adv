# cookbook/ingredients/schema.py
from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from web.models import Country


class CountryNode(DjangoObjectType):
    class Meta:
        model = Country
        filter_fields = ["id", 'name', 'population']
        interfaces = (relay.Node, )


class Query(AbstractType):
    country = relay.Node.Field(CountryNode)
    all_countries = DjangoFilterConnectionField(CountryNode)
