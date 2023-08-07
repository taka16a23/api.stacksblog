import {
  ROUTES,
} from "../constants/";

const INIT_STATE = {
  routes: [],
};

export default (state = INIT_STATE, action) => {
  switch (action.type) {
    case ROUTES:
      return {
        ...state,
        routes: action.payload,
      };
    default:
      return state;
  }
};
