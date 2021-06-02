import peewee_validates as pv


class PeeWeeShopValidator(pv.Validator):
    name = pv.StringField(validators=[pv.validate_required(),
                                      pv.validate_not_empty(),
                                      pv.validate_length(low=1, high=255)])
    street = pv.IntegerField(validators=[pv.validate_required(), pv.validate_not_empty()])
    city = pv.IntegerField(validators=[pv.validate_required(), pv.validate_not_empty()])
    building = pv.StringField(validators=[pv.validate_required(),
                                          pv.validate_not_empty(),
                                          pv.validate_length(low=1, high=10)])
    opens = pv.TimeField(validators=[pv.validate_required(), pv.validate_not_empty()])
    closes = pv.TimeField(validators=[pv.validate_required(), pv.validate_not_empty()])
