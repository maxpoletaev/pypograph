# Pypograph

> Simple typographic tool for Python/Django.

## Usage

```python
from pypograph import Typograph
from pypograph import rules

typograph = Typograph([rules.QuoteRule, rules.MdashRule])
typograph.typo('- Это "типограф"?')
```

## Usage with Django

Add `pypograph` to `INSTALLED_APPS` and try:

```html
{% load typograph %}

<html>
  <body>
    {% typo %}
      <p>- Это "типограф"?</p>
    {% endtypo %}
  </body>
</html>
```

You can configure rules by adding `TYPOGRAPH_RULES` into your `setting.py`:

```python
TYPOGRAPH_RULES = {
    'pypograph.rules.QuoteRule': {'quotes': '“”'},
}
```

## Testing

```
python -m unittest pypograph.tests
```
