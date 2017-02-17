from catalog.models import Material


def get_minimum_price(nails, varnish, glass, fabrics, cushions):
    _nails = Material.objects.get(material_name='nails')
    _fabrics = Material.objects.get(material_name='fabrics')
    _cushions = Material.objects.get(material_name='cushions')
    _glass = Material.objects.get(material_name='glass')
    _varnish = Material.objects.get(material_name='varnish')

    nail_price = _nails.per_unit_price * nails
    fabrics_price = _fabrics.per_unit_price * fabrics
    cushions_price = _cushions.per_unit_price * cushions
    glass_price = _glass.per_unit_price * glass
    varnish_price = _varnish.per_unit_price * varnish

    minimum_price = nail_price + fabrics_price + cushions_price + glass_price + varnish_price

    return minimum_price * 1.7
