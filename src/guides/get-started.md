# Getting started with digital land frontend

Use this getting started guide to find out how to:

* install Digital Land Frontend
* set up a test page to check your installation is working

You can see live examples of Digital Land Frontend components, GOVUK components we've ported to jinja, and guidance on when to use them, in this design system.

[Contact](mailto:DigitalLand@communities.gov.uk) us if you have any questions or feedback.

## Install

[Install digital land frontend with pip](https://github.com/digital-land/frontend).

    pip install -e git+https://github.com/digital-land/frontend.git#egg=digital_land_frontend
    pip install -e git+https://github.com/digital-land/govuk-jinja-components.git#egg=govuk_jinja_components

## Register templates with Jinja

Installing `govuk-jinja-components` and digital land's `frontend` makes a number of templates available. You will need to register this with Jinja to be able to use them.

Where you initialise jinja include the following:

    import jinja2

    # where you set up jinja add this
    multi_loader = jinja2.ChoiceLoader([
        jinja2.FileSystemLoader(searchpath="<<path to your templates>>"),
        jinja2.PrefixLoader({
            'govuk-jinja-components': jinja2.PackageLoader('govuk_jinja_components'),
            'digital-land-frontend': jinja2.PackageLoader('digital_land_frontend')
        })
    ])
    jinja2.Environment(loader=multi_loader)

## Create a page

Create a page in your application.

To extend the digital land base template start with the line

    % extends "digital-land-frontend/dlf-base.html" %

To use `govuk-jinja-components` import the ones you need. E.g. import the `govukButton` component with

    % from 'govuk-jinja-components/components/button/macro.jinja' import govukButton  %

You can paste the HTML or jinja from the [govukButton documentation page](/design-system/govuk-components/button) into you page, paste it between the **content** block

    % block content %
    <!-- paste here -->
    % endblock %

Take the same approach to use the `digital-land-frontend` components. E.g.

    {% from 'digital-land-frontend/components/feedback-panel/macro.html' import dlFeedbackPanel %}
    % block content %
    <!-- paste dlFeedbackPanel here -->
    % endblock %

Paste [dlFeedbackPanel example](/design-system/components/feedback-panel) from the documentation page.

## Using the CSS and JS assets

The **CSS** is already included if extending the `dlf-base.html` template.

The *JS** is also included if extending the `dlf-base.html` template. To initialise one of the JS modules use:

    % block bodyEnd %
    { super() }
    <script>
        const $inputCopyElements = document.querySelectorAll('[data-module*="input-copy"]')
        $inputCopyElements.forEach(function ($input) {
            new window.DLFrontend.InputCopy($input).init()
        })
    </script>
    % endblock %
