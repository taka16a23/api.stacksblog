import APIFactory from 'api/APIFactory';
import { PostModel } from 'models';

export default class PostRepository extends Object {

  constructor() {
    super();
    this.api = APIFactory.createPostAPI();
  }

  get(a_oParams) {
    return new Promise((resolve, reject) => {
      this.api.get(a_oParams).then(data => {
        var tResult = [];
        data.forEach(d => {
          tResult.push(Object.assign(new PostModel(), d));
        })
        resolve(tResult);
      }).catch(err => {
        reject(err);
      });
    });
  }

  getByID(a_sID) {
    return new Promise((resolve, reject) => {
      this.api.get({}, a_sID).then(data => {
        resolve(Object.assign(new PostModel(), data));
      }).catch(err => {
        reject(err);
      });
    });
  }

}
