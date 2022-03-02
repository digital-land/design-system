
// Similar approach to huffduffer
// if input has readonly content make it easy to copy
function InputCopy ($module) {
  this.$module = $module
}

InputCopy.prototype.init = function (params) {
  this.$module.addEventListener('click', function (ev) {
    var target = ev.target
    if (target.hasAttribute('readonly')) {
      target.focus()
      target.select()
    }
  })
}

export default InputCopy
