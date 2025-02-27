export default class PostModel extends Object {
  constructor() {
    super();
    this.post_id = null;
    this.title = "";
    this.excerpt = "";
    this.slug = "";
    this.image = null;
    this.content = "";
    this.category = {};
    this.publish_date = null;
    this.next = null;
    this.prev = null;
    this.created_at = null;
    this.modified_at = null;
    this.created_by = null;
    this.modified_by = null;
  }

  /*
   * Getter Setter method
   */
  getID() {
    return this.post_id;
  }

  setID(a_iID) {
    this.post_id = a_iID;
    return this;
  }

  getTitle() {
    return this.title;
  }

  setTitle(a_sValue) {
    this.title = a_sValue;
    return this;
  }

  getExcerpt() {
    return this.excerpt;
  }

  setExcerpt(a_sValue) {
    this.excerpt = a_sValue;
    return this;
  }

  getSlug() {
    return this.slug;
  }

  setSlug(a_sValue) {
    this.slug = a_sValue;
    return this;
  }

  getImage() {
    return this.image;
  }

  setImage(a_sValue) {
    this.image = a_sValue;
    return this;
  }

  getContent() {
    return this.content;
  }

  setContent(a_sValue) {
    this.content = a_sValue;
    return this;
  }

  getCategories() {
    return this.category;
  }

  setCategories(a_oValue) {
    this.category = a_oValue;
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
