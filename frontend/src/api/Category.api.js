import API from "./API";
import AliasRoutes from 'routes/AliasRoutes';


export default class CategoryAPI extends API {

  static PATH = AliasRoutes.APIBlogCategory;

  constructor() {
    super(process.env.REACT_APP_API_URL, CategoryAPI.PATH);
  }
}
