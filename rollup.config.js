module.exports = [
  {
    input: 'src/javascripts/application-design-system.js',
    output: {
      file: 'docs/static/javascripts/application-design-system.js',
      format: 'umd',
      name: "DLStyleguide"
    },
    context: "window",
  }
]
