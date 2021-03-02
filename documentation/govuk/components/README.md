---
---
# GOVUK Components

The GOVUK components from the [GOVUK Design System](https://design-system.service.gov.uk) are written in nunjucks and work well with node.

The [digital land site](https://digital-land.github.io/) and services are built using python, and to get the components working we needed to port them to Jinja.

We did that and created a package ([govuk-jinja-components](https://github.com/digital-land/govuk-jinja-components)) to install in your python projects.

You can install it with `pip`.

    pip install -e git+https://github.com/digital-land/govuk-jinja-components.git#egg=govuk_jinja_components
