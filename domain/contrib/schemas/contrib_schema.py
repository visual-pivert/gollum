from apiflask import Schema
from apiflask.fields import String, List, Nested, Integer


class ContribInputSchema(Schema):
    username = String(required=True)


class ContribOutputSchema(Schema):
    username = String()
    status_code = Integer()


class ContribListSchema(Schema):
    contributors = List(Nested(ContribOutputSchema))
    status_code = Integer()