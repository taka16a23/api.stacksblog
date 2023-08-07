import Filter from './Filter';


class FilterManager extends Object {

  constructor() {
    this.filters = [];
  }

  addFilter(aFilter) {
    if(!(aFilter instanceof Filter)) {
      throw new TypeError("Invalid type of aFilter. Must be Filter instance.");
    }
    this.filters.push(aFilter);
    return this;
  }

  removeFilter(aFilter) {
    for(var i = 0; i < this.filters.length; i++) {
      if (this.filters[i] === aFilter) {
        this.filters.splice(i, 1);
        i--;
      }
    }
    return this;
  }

  clearFilters() {
    this.filters = [];
    return this;
  }

  handleFilter(aValue) {
    for(var i = 0; i < this.filters.length; i++) {
      if(this.filters[i].determine(aValue) === true) {
        return true;
      }
    }
    return false;
  }
}
