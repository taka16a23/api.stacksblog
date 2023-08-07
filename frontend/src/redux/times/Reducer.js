import {
  SERVER_TIME_OFFSET,
} from "../constants/";

const INIT_STATE = {
  serverTimeOffset: 0,
};

export default (state = INIT_STATE, action) => {
  switch (action.type) {
    case SERVER_TIME_OFFSET:
      return {
        ...state,
        serverTimeOffset: action.payload,
      };
    default:
      return state;
  }
};
