export default class APIFactory {

  static _cache = {};

  // Category
  static createCategoryAPI() {
    if(!APIFactory._cache['CategoryAPI']) {
      let klass = require('./Category.api.js').default;
      APIFactory._cache['CategoryAPI'] = new klass();
    }
    return APIFactory._cache['CategoryAPI'];
  }

  // Post
  static createPostAPI() {
    if(!APIFactory._cache['PostAPI']) {
      let klass = require('./Post.api.js').default;
      APIFactory._cache['PostAPI'] = new klass();
    }
    return APIFactory._cache['PostAPI'];
  }
}
