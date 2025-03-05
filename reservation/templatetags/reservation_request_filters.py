from django import template

register = template.Library()

@register.filter
def get_boat_count(req, name):
    return req.reservationboat_set.filter(boat_type_id__boat_type=name).count() 