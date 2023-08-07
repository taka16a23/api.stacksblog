export default class HttpErrorFactory {
  static _cache = {};

  // create HttpError from response
  static createHttpError(response) {
    // 400
    if(response.status === 400) {
      return HttpErrorFactory.createHttp400BadRequestError(response);
    }

    // 401
    if(response.status === 401) {
      return HttpErrorFactory.createHttp401UnauthorizedError(response);
    }
    // 402
    if(response.status === 402) {
      return HttpErrorFactory.createHttp402PaymentRequiredError(response);
    }
    // 403
    if(response.status === 403) {
      return HttpErrorFactory.createHttp403ForbiddenError(response);
    }
    // 404
    if(response.status === 404) {
      return HttpErrorFactory.createHttp404NotFoundError(response);
    }
    // 405
    if(response.status === 405) {
      return HttpErrorFactory.createHttp405MethodNotAllowedError(response);
    }
    // 406
    if(response.status === 406) {
      return HttpErrorFactory.createHttp406NotAcceptableError(response);
    }
    // 407
    if(response.status === 407) {
      return HttpErrorFactory.createHttp407ProxyAuthenticationRequiredError(response);
    }
    // 408
    if(response.status === 408) {
      return HttpErrorFactory.createHttp408RequestTimeoutError(response);
    }
    // 409
    if(response.status === 409) {
      return HttpErrorFactory.createHttp409ConflictError(response);
    }
    // 410
    if(response.status === 410) {
      return HttpErrorFactory.createHttp410GoneError(response);
    }
    // 411
    if(response.status === 411) {
      return HttpErrorFactory.createHttp411LengthRequiredError(response);
    }
    // 412
    if(response.status === 412) {
      return HttpErrorFactory.createHttp412PreconditionFailedError(response);
    }
    // 413
    if(response.status === 413) {
      return HttpErrorFactory.createHttp413PayloadTooLargeError(response);
    }
    // 414
    if(response.status === 414) {
      return HttpErrorFactory.createHttp414URITooLongError(response);
    }
    // 415
    if(response.status === 415) {
      return HttpErrorFactory.createHttp415UnsupportedMediaTypeError(response);
    }
    // 500
    if(response.status === 500) {
      return HttpErrorFactory.createHttp500InternalServerError(response);
    }
    // 500
    if(response.status === 500) {
      return HttpErrorFactory.createHttp500InternalServerError(response);
    }
    // 501
    if(response.status === 501) {
      return HttpErrorFactory.createHttp501NotImplementedError(response);
    }
    // 502
    if(response.status === 502) {
      return HttpErrorFactory.createHttp502BadGatewayError(response);
    }
    // 503
    if(response.status === 503) {
      return HttpErrorFactory.createHttp503ServiceUnavailableError(response);
    }
    // 504
    if(response.status === 504) {
      return HttpErrorFactory.createHttp504GatewayTimeoutError(response);
    }
    // 505
    if(response.status === 505) {
      return HttpErrorFactory.createHttp505HTTPVersionNotSupportedError(response);
    }
    // 506
    if(response.status === 506) {
      return HttpErrorFactory.createHttp506VariantAlsoNegotiatesError(response);
    }
    // 507
    if(response.status === 507) {
      return HttpErrorFactory.createHttp507InsufficientStorageError(response);
    }
    // 508
    if(response.status === 508) {
      return HttpErrorFactory.createHttp508LoopDetectedError(response);
    }
    // 510
    if(response.status === 510) {
      return HttpErrorFactory.createHttp510NotExtendedError(response);
    }
    // 511
    if(response.status === 511) {
      return HttpErrorFactory.createHttp511NetworkAuthenticationRequiredError(response);
    }
    // HttpError
    if(!HttpErrorFactory._cache[response.status]) {
      HttpErrorFactory._cache[response.status] = require('./HttpError.js').default;
    }
    return new HttpErrorFactory._cache[response.status](response);
  }

  // 400
  static async createHttp400BadRequestError(response) {
    if(HttpErrorFactory._cache[400] === undefined) {
      HttpErrorFactory._cache[400] = await require('./Http400BadRequestError.js').default;
    }
    return new HttpErrorFactory._cache[400](response);
  }
  // 401
  static createHttp401UnauthorizedError(response) {
    if(HttpErrorFactory._cache[401] === undefined) {
      HttpErrorFactory._cache[401] = require('./Http401UnauthorizedError.js').default;
    }
    return new HttpErrorFactory._cache[401](response);
  }
  // 402
  static createHttp402PaymentRequiredError(response) {
    if(HttpErrorFactory._cache[402] === undefined) {
      HttpErrorFactory._cache[402] = require('./Http402PaymentRequiredError.js').default;
    }
    return new HttpErrorFactory._cache[402](response);
  }
  // 403
  static createHttp403ForbiddenError(response) {
    if(HttpErrorFactory._cache[403] === undefined) {
      HttpErrorFactory._cache[403] = require('./Http403ForbiddenError.js').default;
    }
    return new HttpErrorFactory._cache[403](response);
  }
  // 404
  static createHttp404NotFoundError(response) {
    if(HttpErrorFactory._cache[404] === undefined) {
      HttpErrorFactory._cache[404] = require('./Http404NotFoundError.js').default;
    }
    return new HttpErrorFactory._cache[404](response);
  }
  // 405
  static createHttp405MethodNotAllowedError(response) {
    if(HttpErrorFactory._cache[405] === undefined) {
      HttpErrorFactory._cache[405] = require('./Http405MethodNotAllowedError.js').default;
    }
    return new HttpErrorFactory._cache[405](response);
  }
  // 406
  static createHttp406NotAcceptableError(response) {
    if(HttpErrorFactory._cache[406] === undefined) {
      HttpErrorFactory._cache[406] = require('./Http406NotAcceptableError.js').default;
    }
    return new HttpErrorFactory._cache[406](response);
  }
  // 407
  static createHttp407ProxyAuthenticationRequiredError(response) {
    if(HttpErrorFactory._cache[407] === undefined) {
      HttpErrorFactory._cache[407] = require('./Http407ProxyAuthenticationRequiredError.js').default;
    }
    return new HttpErrorFactory._cache[407](response);
  }
  // 408
  static createHttp408RequestTimeoutError(response) {
    if(HttpErrorFactory._cache[408] === undefined) {
      HttpErrorFactory._cache[408] = require('./Http408RequestTimeoutError.js').default;
    }
    return new HttpErrorFactory._cache[408](response);
  }
  // 409
  static createHttp409ConflictError(response) {
    if(HttpErrorFactory._cache[409] === undefined) {
      HttpErrorFactory._cache[409] = require('./Http409ConflictError.js').default;
    }
    return new HttpErrorFactory._cache[409](response);
  }
  // 410
  static createHttp410GoneError(response) {
    if(HttpErrorFactory._cache[410] === undefined) {
      HttpErrorFactory._cache[410] = require('./Http410GoneError.js').default;
    }
    return new HttpErrorFactory._cache[410](response);
  }
  // 411
  static createHttp411LengthRequiredError(response) {
    if(HttpErrorFactory._cache[411] === undefined) {
      HttpErrorFactory._cache[411] = require('./Http411LengthRequiredError.js').default;
    }
    return new HttpErrorFactory._cache[411](response);
  }
  // 412
  static createHttp412PreconditionFailedError(response) {
    if(HttpErrorFactory._cache[412] === undefined) {
      HttpErrorFactory._cache[412] = require('./Http412PreconditionFailedError.js').default;
    }
    return new HttpErrorFactory._cache[412](response);
  }
  // 413
  static createHttp413PayloadTooLargeError(response) {
    if(HttpErrorFactory._cache[413] === undefined) {
      HttpErrorFactory._cache[413] = require('./Http413PayloadTooLargeError.js').default;
    }
    return new HttpErrorFactory._cache[413](response);
  }
  // 414
  static createHttp414URITooLongError(response) {
    if(HttpErrorFactory._cache[414] === undefined) {
      HttpErrorFactory._cache[414] = require('./Http414URITooLongError.js').default;
    }
    return new HttpErrorFactory._cache[414](response);
  }
  // 415
  static createHttp415UnsupportedMediaTypeError(response) {
    if(HttpErrorFactory._cache[415] === undefined) {
      HttpErrorFactory._cache[415] = require('./Http415UnsupportedMediaTypeError.js').default;
    }
    return new HttpErrorFactory._cache[415](response);
  }
  // 416
  static createHttp416RangeNotSatisfiableError(response) {
    if(HttpErrorFactory._cache[416] === undefined) {
      HttpErrorFactory._cache[416] = require('./Http416RangeNotSatisfiableError.js').default;
    }
    return new HttpErrorFactory._cache[416](response);
  }
  // 500
  static createHttp500InternalServerError(response) {
    if(HttpErrorFactory._cache[500] === undefined) {
      HttpErrorFactory._cache[500] = require('./Http500InternalServerError.js').default;
    }
    return new HttpErrorFactory._cache[500](response);
  }
  // 501
  static createHttp501NotImplementedError(response) {
    if(HttpErrorFactory._cache[501] === undefined) {
      HttpErrorFactory._cache[501] = require('./Http501NotImplementedError.js').default;
    }
    return new HttpErrorFactory._cache[501](response);
  }
  // 502
  static createHttp502BadGatewayError(response) {
    if(HttpErrorFactory._cache[502] === undefined) {
      HttpErrorFactory._cache[502] = require('./Http502BadGatewayError.js').default;
    }
    return new HttpErrorFactory._cache[502](response);
  }
  // 503
  static createHttp503ServiceUnavailableError(response) {
    if(HttpErrorFactory._cache[503] === undefined) {
      HttpErrorFactory._cache[503] = require('./Http503ServiceUnavailableError.js').default;
    }
    return new HttpErrorFactory._cache[503](response);
  }
  // 504
  static createHttp504GatewayTimeoutError(response) {
    if(HttpErrorFactory._cache[504] === undefined) {
      HttpErrorFactory._cache[504] = require('./Http504GatewayTimeoutError.js').default;
    }
    return new HttpErrorFactory._cache[504](response);
  }
  // 505
  static createHttp505HTTPVersionNotSupportedError(response) {
    if(HttpErrorFactory._cache[505] === undefined) {
      HttpErrorFactory._cache[505] = require('./Http505HTTPVersionNotSupportedError.js').default;
    }
    return new HttpErrorFactory._cache[505](response);
  }
  // 506
  static createHttp506VariantAlsoNegotiatesError(response) {
    if(HttpErrorFactory._cache[506] === undefined) {
      HttpErrorFactory._cache[506] = require('./Http506VariantAlsoNegotiatesError.js').default;
    }
    return new HttpErrorFactory._cache[506](response);
  }
  // 507
  static createHttp507InsufficientStorageError(response) {
    if(HttpErrorFactory._cache[507] === undefined) {
      HttpErrorFactory._cache[507] = require('./Http507InsufficientStorageError.js').default;
    }
    return new HttpErrorFactory._cache[507](response);
  }
  // 508
  static createHttp508LoopDetectedError(response) {
    if(HttpErrorFactory._cache[508] === undefined) {
      HttpErrorFactory._cache[508] = require('./Http508LoopDetectedError.js').default;
    }
    return new HttpErrorFactory._cache[508](response);
  }
  // 510
  static createHttp510NotExtendedError(response) {
    if(HttpErrorFactory._cache[510] === undefined) {
      HttpErrorFactory._cache[510] = require('./Http510NotExtendedError.js').default;
    }
    return new HttpErrorFactory._cache[510](response);
  }
  // 511
  static createHttp511NetworkAuthenticationRequiredError(response) {
    if(HttpErrorFactory._cache[511] === undefined) {
      HttpErrorFactory._cache[511] = require('./Http511NetworkAuthenticationRequiredError.js').default;
    }
    return new HttpErrorFactory._cache[511](response);
  }
}
