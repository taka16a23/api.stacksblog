import API from "./API";
import AliasRoutes from 'routes/AliasRoutes';


export default class PostAPI extends API {

  static PATH = AliasRoutes.APIBlogPost;

  constructor() {
    super(process.env.REACT_APP_API_URL, PostAPI.PATH);
  }
}
