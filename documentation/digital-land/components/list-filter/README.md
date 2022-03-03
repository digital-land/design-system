---
contains_map: False
---
{{ govukTag({
  "text": "candidate"
}) }}

# List filter

Allow a user to search or filter a list. This is an progressive enhancement.

## When to use

When you have a list of values that is cumbersome to scan. Roughly 20+ items.

When a user needs to find an item quickly and knows an attribute of the item to help find it. For example, this could be a name or reference number.

## How to use

It is a modules in `dl-frontend.js`. This script is loaded on all digital land pages.

To use it:

* markup the list correctly
* instantiate the JS module

### Markup the list

Add `data-filter="list"` to the element that contains the list.

Add `data-filter="item"` to every item in the list. Elements with the `data-filter="item"` attribute will be elements shown and hidden depending on the search term.

Add `data-filter="match-content"` on any element contained in a `data-filter="item"` element where you want the content to be searchable. This is optional. If you do not include a `data-filter="match-content"` the module will look for any `<a>` element within the `data-filter="item"` element.

Use `data-filter="match-content"` if you want more than one term to be searchable. For example, make the an id and the name of an item searchable:

    <tr data-filter="item">
        <td><a class="govuk-link" href="./dev-plan-buc-bmwlp" data-filter="match-content">dev-plan-buc-bmwlp</a></td>
        <td><p class="govuk-body" data-filter="match-content">Buckinghamshire Minerals and Waste Local Plan 2016-2036</p>
        </td>
    </tr>

Insert the form with

    <form class="filter-organisations-list__form" data-filter="form">
        <label class="filter-list__label govuk-label govuk-!-font-weight-bold" for="filter-organisations-list">I'm looking for</label>
        <input class="filter-list__input govuk-input" type="text" id="filter-organisations-list" placeholder="{{ filterInputPlaceholder|default('For example, Harrogate Borough Council') }}">
    </form>

In a jinja template you can set the placeholder text but setting `filterInputPlaceholder`. E.g:

    {% set filterInputPlaceholder = "For example, E04007372 or Knaresborough" %}

The filter module will update a count if you provide pointers to it. The count element consists of a count element with the class `.js-list-count` and a matching count element for accessibility, with the class `.js-accessible-list-count"`.

The count element might look like:

    <div class="count-wrapper">
        <p class="govuk-body" aria-hidden="true">Showing <span class="js-list-count">{{ count }}</span> records.</p>
        <p class="govuk-visually-hidden">There are
            <span class="js-accessible-list-count">{{ count }}</span>
        records listed.</p>
    </div>

### Instantiate JS

Grab the form element first. Then run `FilterList.init()`. The `init` function accepts some options. E.g:

    <script>
        const $form = document.querySelector('[data-filter="form"]');
        new window.DLFrontend.FilterList($form).init({
            list_section_selector: '.index-list-wrapper',
            count_wrapper_selector: '.count-wrapper'
        })
    </script>

`list_section_selector` - the element that contains the list
`count_wrapper_selector` - the element that contains the count(s)
