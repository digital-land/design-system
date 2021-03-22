---
contains_map: False
---
# Feedback

Use these components when you want the user to provide feedback on the page / content.

## Inline feedback

For inline feedback use the `feedback-panel` component.

Use the feedback panel component when you want to ask the user to provide feedback on a page or section of a page.

{{ designSystemExample({
"iframe": {
    "title": "An example of the feedback panel component",
    "url": "example.html",
    "size": "s"
},
"example": {
    "path": "digital-land/components/feedback"
}
}) }}

It works well when included at the bottom of the page, after the main content. Putting it after the main content means it won't distract the user from the content before they have had chance to read it.

## Feedback prompt

Use the `dlf-feedback-prompt` component to place a prompt for feedback. The component includes options to add content to the panel and an `action` in the form of a button.

By default the component will be 100% width.

### Feedback with button

Using a button in the prompt helps the user know they can interact with the prompt.

{{ designSystemExample({
"iframe": {
    "title": "An example of the feedback prompt that uses a button as the action",
    "url": "example-feedback.html",
    "size": "s"
},
"example": {
    "path": "digital-land/components/feedback"
}
}) }}

### Feedback without button

You don't always need to include a button. A link can be used instead.

{{ designSystemExample({
"iframe": {
    "title": "An example of the feedback prompt that uses a link as the action",
    "url": "example-feedback-no-action.html",
    "size": "s"
},
"example": {
    "path": "digital-land/components/feedback"
}
}) }}

### Feedback when pinned to footer

Often if makes sense to ask for feedback about the whole page.

When doing this it makes sense to place the feedback prompt at the bottom of the page.

The [dlf-base template](../../template/dlf-base) has a `feedbackPrompt` block that can be used to place the component at the end of the page.

This takes the feeback component out of the main `content` block on the page and uses the `feedbackPrompt` block. This will wrap the component in div with the `.dlf-feedback__wrapper`. This class limits the width of the component to the maximum page width.

{{ designSystemExample({
"iframe": {
    "title": "An example of the feedback panel component",
    "url": "example-feedback-pinned.html",
    "size": "xl"
},
"example": {
    "path": "digital-land/components/feedback"
}
}) }}


### Stacked feedback

You can use the feedback prompt component in a narrower layout - for example, in a `govuk-grid-column-one-third` parent.

Add the class `dlf-feedback--stacked` to get the desired effect.

{{ designSystemExample({
"iframe": {
    "title": "An example of the feedback panel component stacked in a narrow layout",
    "url": "example-feedback-stacked.html",
    "size": "m"
},
"example": {
    "path": "digital-land/components/feedback"
}
}) }}
