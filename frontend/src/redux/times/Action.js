import {
  SERVER_TIME_OFFSET,
} from "../constants/";

export const setServerTimeOffset = (payload) => {
    return {
        type: SERVER_TIME_OFFSET,
        payload
    }
}
