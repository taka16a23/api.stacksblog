export function focusInput(a_sName) {
  var arrInputs = document.querySelectorAll('input[name="' + a_sName + '"]');
  if(arrInputs) {
    arrInputs[arrInputs.length -1].focus();
  };
}
