import Filter from './Filter';

export default class IncludeFilter extends Filter {

  inspect(aValue) {
    var tValue = this.getValue();
    if(!tValue) {
      return true;
    }
    tValue = String(this.getValue());
    if(!tValue) {
      return true;
    }
    return tValue.includes(tValue);
  }
}
