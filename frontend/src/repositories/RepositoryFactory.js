export default class RepositoryFactory {
  static _cache = {};

  // Category
  static createCategoryRepository() {
    if(!RepositoryFactory._cache['CategoryRepository']) {
      let klass = require('./Category.repository').default;
      RepositoryFactory._cache['CategoryRepository'] = new klass();
    }
    return RepositoryFactory._cache['CategoryRepository'];
  }

  // Post
  static createPostRepository() {
    if(!RepositoryFactory._cache['PostRepository']) {
      let klass = require('./Post.repository').default;
      RepositoryFactory._cache['PostRepository'] = new klass();
    }
    return RepositoryFactory._cache['PostRepository'];
  }

}
