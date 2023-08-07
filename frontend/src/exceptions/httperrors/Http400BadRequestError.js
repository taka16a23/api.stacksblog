import HttpError from 'exceptions/httperrors/HttpError';

// 400 Bad Request
export default class Http400BadRequestError extends HttpError {
  constructor(response) {
    super(response);
  }
}
