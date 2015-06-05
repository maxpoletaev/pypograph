# Pypograph

> Simple typographic tool for Python/Django.

## Usage

```python
from pypograph import Typograph
from pypograph import rules

typograph = Typograph([rules.QuoteRule, rules.MdashRule])
typograph.typo('- Это "типограф"?') # -> '— Это «типограф»?'
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

## Сustom rules

```python
from pypograph.rules import BaseRule
from pypograph import Typograph


class MyOwnRule(BaseRule):
    config = {
      'from': 'a',
      'to': 'b',
    }

    def process(self, text):
        return text.replace(self.config['from'], self.config['to'])


typograph = Typograph([MyOwnRule])
typograph.typo('abc') # -> 'bbc'
```


## Testing

```
python -m unittest pypograph.tests
```
