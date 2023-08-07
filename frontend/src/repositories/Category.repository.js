import APIFactory from 'api/APIFactory';
import { CategoryModel } from 'models';

export default class CategoryRepository extends Object {

  constructor() {
    super();
    this.api = APIFactory.createCategoryAPI();
  }

  get(a_oParams) {
    return new Promise((resolve, reject) => {
      this.api.get(a_oParams).then(data => {
        var tResult = [];
        data.forEach(d => {
          tResult.push(Object.assign(new CategoryModel(), d));
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
        resolve(Object.assign(new CategoryModel(), data));
      }).catch(err => {
        reject(err);
      });
    });
  }

}
