export default class CategoryModel extends Object {
  constructor() {
    super();
    this.category_id = null;
    this.name = "";
    this.created_at = null;
    this.modified_at = null;
    this.created_by = null;
    this.modified_by = null;
  }

  /*
   * Getter Setter method
   */
  getID() {
    return this.category_id;
  }

  setID(a_iID) {
    this.category_id = a_iID;
    return this;
  }

  getName() {
    return this.name;
  }

  setName(a_sValue) {
    this.name = a_sValue;
    return this;
  }

  getCreatedBy() {
    return this.created_by;
  }

  setCreatedBy(a_iCreatedUserID) {
    this.created_by = a_iCreatedUserID;
    return this;
  }

  getModifiedBy() {
    return this.modified_by;
  }

  setModifiedBy(a_iModifiedUserID) {
    this.modified_by = a_iModifiedUserID;
    return this;
  }

  /* End Getter Setter method */

}
