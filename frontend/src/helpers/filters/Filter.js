export default class Filter extends Object {

  constructor(aValue=null) {
    this.value = aValue;
  }

  inspect(aValue) {
    return this.getValue() === aValue;
  }

  getValue() {
    return this.value;
  }

  setValue(aValue) {
    this.value = aValue;
    return this;
  }
}
