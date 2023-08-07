import axios from "axios";
import HttpError from "exceptions/httperrors/HttpError";


export default class API {

  constructor(baseURL, path) {
    this.baseURL = baseURL;
    this.path = path;
    this.URL = this.baseURL + path;
  }

  getData() {
    return {};
  }

  getFormData() {
    return new FormData();
  }

  getURL(id) {
    if(id === undefined) {
      return this.URL;
    }
    return this.URL + id + '/';
  }

  get(data, id) {
    if(data === undefined) {
      data = {};
    }
    return new Promise((resolve, reject) => {
      axios.get(this.getURL(id), data)
        .then((response) => {
          // 200 OK
          if(response.status === 200) {
            resolve(response.data);
            return;
          }
          // 201 Created
          if(response.status === 201) {
            reject(new HttpError(response));
            return;
          }
          // 204 No Content
          if(response.status === 204) {
            resolve(response.data);
            return;
          }
          reject(new HttpError(response));
        }
      ).catch(err => {
        reject(err);
      });
    });
  }

  post(data) {
    if(data === undefined) {
      data = {};
    }
    return new Promise((resolve, reject) => {
      axios.post(this.getURL(), data)
        .then(response => {
          if(!response) {
            return;
          }
          // 200 OK
          if(response.status === 200) {
            resolve(response.data);
            return;
          }
          // 201 Created
          if(response.status === 201) {
            resolve(response.data);
            return;
          }
          // 204 No Content
          if(response.status === 204) {
            resolve(response.data);
            return;
          }
          reject(new HttpError(response));
        }).catch(err => {
          reject(err);
        });
    });
  }

  patch(id, data) {
    if(data === undefined) {
      data = {};
    }
    return new Promise((resolve, reject) => {
      axios.patch(this.getURL(id), data)
        .then(response => {
          if(!response) {
            return;
          }
          // 200 Created
          if(response.status === 200) {
            resolve(response.data);
            return;
          }
          // 201 Created
          if(response.status === 201) {
            resolve(response.data);
            return;
          }
          // 202 Accepted
          if(response.status === 202) {
            resolve(response.data);
            return;
          }
          // 204 No Content
          if(response.status === 204) {
            resolve(response.data);
            return;
          }
          reject(new HttpError(response));
        }).catch(err => {
          reject(err);
        });
    });
  }

  delete(id, data) {
    if(data === undefined) {
      data = {};
    }
    return new Promise((resolve, reject) => {
      axios.delete(this.getURL(id), data)
        .then(response => {
          if(!response) {
            return;
          }
          // 200 Created
          if(response.status === 200) {
            resolve(response.data);
            return;
          }
          // 201 Created
          if(response.status === 201) {
            resolve(response.data);
            return;
          }
          // 202 Accepted
          if(response.status === 202) {
            resolve(response.data);
            return;
          }
          // 204 No Content
          if(response.status === 204) {
            resolve(response.data);
            return;
          }
          reject(new HttpError(response));
        }).catch(err => {
          reject(err);
        });
    });
  }

  put(id, data) {
    if(data === undefined) {
      data = {};
    }
    return new Promise((resolve, reject) => {
      axios.put(this.getURL(id), data)
        .then(response => {
          if(!response) {
            return;
          }
          // 200 Created
          if(response.status === 200) {
            resolve(response.data);
            return;
          }
          // 201 Created
          if(response.status === 201) {
            resolve(response.data);
            return;
          }
          // 202 Accepted
          if(response.status === 202) {
            resolve(response.data);
            return;
          }
          // 204 No Content
          if(response.status === 204) {
            resolve(response.data);
            return;
          }
          reject(new HttpError(response));
        }).catch(err => {
          reject(err);
        });
    });
  }
}
