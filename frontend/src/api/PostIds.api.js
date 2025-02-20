import API from "./API";
import AliasRoutes from 'routes/AliasRoutes';


export default class PostIdsAPI extends API {

  static PATH = AliasRoutes.APIBlogPostIds;

  constructor() {
    super(process.env.REACT_APP_API_URL, PostIdsAPI.PATH);
  }
}
