import { APIFactory } from 'api';
import { RepositoryFactory } from 'repositories';

export default class BlogService extends Object {

  constructor() {
    super();
    this.category_repository = RepositoryFactory.createCategoryRepository();
    this._categories_cache = {};
    this.post_repository = RepositoryFactory.createPostRepository();
    this._posts_cache = {};
  }

  listCategories(a_oParams={}) {
    return new Promise((resolve, reject) => {
      var tData = {'params': a_oParams};
      this.category_repository.get(tData).then(models => {
        let result = models.map(model => {
          if(this._categories_cache[model.category_id] === undefined) {
            this._categories_cache[model.category_id] = model;
          }
          Object.assign(this._categories_cache[model.category_id], model);
          return this._categories_cache[model.category_id];
        })
        resolve(result);
      }).catch(err => {
        reject(err);
      });
    });
  }

  listPosts(a_oParams={}) {
    return new Promise((resolve, reject) => {
      var tData = {'params': a_oParams};
      this.post_repository.get(tData).then(models => {
        let result = models.map(model => {
          if(this._posts_cache[model.post_id] === undefined) {
            this._posts_cache[model.post_id] = model;
          }
          Object.assign(this._posts_cache[model.post_id], model);
          return this._posts_cache[model.post_id];
        })
        resolve(result);
      }).catch(err => {
        reject(err);
      });
    });
  }

  listPostIds(a_oParams={}) {
    return new Promise((resolve, reject) => {
      var tData = {'params': a_oParams};
      let api = APIFactory.createPostIdsAPI();
      api.get(tData).then(data => {
        resolve(data);
      }).catch(err => {
        reject(err);
      });
    });
  }

  getPost(a_sSlug) {
    // TODO: (Atami) [2023/08/07]
    // use cache
    return new Promise((resolve, reject) => {
      var tData = {'params': {'slug': a_sSlug}};
      this.post_repository.get(tData).then(models => {
        let result = models.map(model => {
          if(this._posts_cache[model.post_id] === undefined) {
            this._posts_cache[model.post_id] = model;
          }
          Object.assign(this._posts_cache[model.post_id], model);
          return this._posts_cache[model.post_id];
        })
        resolve(result);
      }).catch(err => {
        reject(err);
      });
    });
  }
  getPostByID(a_sID) {
    return new Promise((resolve, reject) => {
      this.post_repository.getByID(a_sID).then(model => {
        resolve(model);
      }).catch(err => {
        reject(err);
      });
    });
  }
}
