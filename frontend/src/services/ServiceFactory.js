export default class ServiceFactory {
  static _cache = {};

  // Blog
  static createBlogService() {
    if(!ServiceFactory._cache['BlogService']) {
      let klass = require('./Blog.service.js').default;
      ServiceFactory._cache['BlogService'] = new klass();
    }
    return ServiceFactory._cache['BlogService'];
  }

}
